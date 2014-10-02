from django.db import models
from django_extensions.db.fields import UUIDField

class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
        ordering = ['-active', 'name']

    def __unicode__(self):
        return self.name

    @property
    def blacklisted_by(self):
        return ', '.join([p.person.name for p in self.blacklist_set.all()])


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mail = models.EmailField()
    active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['name']

    def __unicode__(self):
        return "%s (BL: %s)" % (self.name, self.blacklist)

    def get_blacklist(self):
        return [p.place.name for p in self.blacklist_set.all()]

    @property
    def blacklist(self):
        return ', '.join(self.get_blacklist())


class Quorum(models.Model):
    uuid = UUIDField(primary_key=True)
    person = models.ForeignKey('Person', unique=True)
    lunch = models.CharField('Almuerza hoy?', max_length=5, choices=[('n/a','n/a'), ('yes','yes'), ('no','no')], default='n/a')

    class Meta:
        verbose_name = 'Quorum'
        verbose_name_plural = 'Quorums'
        ordering = ['-lunch', 'person']

    def __unicode__(self):
        return self.person.name


class BlackList(models.Model):
    person = models.ForeignKey('Person')
    place = models.ForeignKey('Place')

    class Meta:
        verbose_name = 'BlackList'
        verbose_name_plural = 'BlackLists'
        unique_together = ('person', 'place')

    def __unicode__(self):
        return "%s:%s" % (self.person.name, self.place.name)
