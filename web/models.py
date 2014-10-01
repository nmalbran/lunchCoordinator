from django.db import models
from django_extensions.db.fields import UUIDField

class Place(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    mail = models.EmailField()


    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __unicode__(self):
        return self.name


class Quorum(models.Model):
    person = models.ForeignKey('Person')
    uuid = UUIDField(unique=True)
    lunch = models.IntegerField(choices=[(0,'n/a'), (1,'yes'), (2,'no')], default=0)

    class Meta:
        verbose_name = 'Quorum'
        verbose_name_plural = 'Quorums'

    def __unicode__(self):
        return self.person.name
