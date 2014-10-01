from web.models import Person, Quorum, Place
from django.core.mail import send_mail, send_mass_mail
from django.core.urlresolvers import reverse

import random

BASE_URL = 'http://localhost:8000'

FROM_EMAIL = 'nicolas_malbran@mcafee.com'

QUORUM_SUBJECT = "Almuerzas hoy?"
QUORUM_MESSAGE = """Hola %(name)s:
Almuerzas en la oficina hoy?
Check In: %(url)s
Bye!
"""

RESULT_SUBJECT = "Resultado del almuerzo"
RESULT_MESSAGE = """Holas,
El lugar elegido es: %(place)s
y los comensales son: %(names)s.

Nos vemos!
"""

def check_quorum():
    people = Person.objects.all()
    Quorum.objects.all().delete()
    messages = []
    for p in people:
        q = Quorum.objects.create(person=p)

        data = {
            'name': p.name,
            'url': BASE_URL + reverse('checkin', kwargs={'pk': q.uuid}),
        }
        print data['url']
        m = (QUORUM_SUBJECT, QUORUM_MESSAGE % data, FROM_EMAIL, [p.mail])

        messages.append(m)

    try:
        send_mass_mail(tuple(messages), fail_silently=False)
    except Exception as e:
        print "Fail to send quorum mail."
        print e


def notify_lunchers():
    quorum = Quorum.objects.filter(lunch='yes')
    names = [q.person.name for q in quorum]
    mail_list = [q.person.mail for q in quorum]

    places = Place.objects.all()
    choice = random.choice([p.name for p in places])

    data = {
        'place': choice,
        'names': ', '.join(names),
    }

    try:
        send_mail(RESULT_SUBJECT, RESULT_MESSAGE % data, FROM_EMAIL, mail_list, fail_silently=False)
    except Exception as e:
        print "Fail to send result mail."
        print e
