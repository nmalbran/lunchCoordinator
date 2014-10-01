from web.models import Person, Quorum, Place
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

import random

BASE_URL = 'http://localhost:8000'

SUBJECT = "Almuerzas hoy?"
MESSAGE = """
Hola %(name)s:
Almuerzas en la oficina hoy?
Check In: %(url)s
Bye!
"""
FROM_EMAIL = 'lunchCoordinator@lunch.cl'

def check_quorum():
    people = Person.objects.all()
    Quorum.objects.all().delete()
    for p in people:
        q = Quorum.objects.create(person=p)

        data = {
            'name': p.name,
            'url': BASE_URL + reverse('checkin', kwargs={'pk': q.uuid}),
        }
        print data['url']
        try:
            send_mail(SUBJECT, MESSAGE % data, FROM_EMAIL, [p.mail], fail_silently=False)
        except Exception as e:
            print "Fail to send mail to: %s (%s)" % (p.name, p.mail)


def notify_lunchers():
    quorum = Quorum.objects.filter(lunch='yes')
    names = [q.person.name for q in quorum]

    places = Place.objects.all()
    choice = random.choice([p.name for p in places])

    print q, choice
