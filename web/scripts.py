from web.models import Person, Quorum, Place
from django.core.mail import send_mail, send_mass_mail
from django.core.urlresolvers import reverse

import random

BASE_URL = 'http://localhost:8000'

FROM_EMAIL = 'nicolas_malbran@mcafee.com'

QUORUM_SUBJECT = "Almuerzas hoy?"
QUORUM_MESSAGE = """Hola %(name)s:
Almuerzas en la oficina hoy?
Si: %(url_y)s
No: %(url_n)s
Bye!
"""

RESULT_SUBJECT = "Resultado del almuerzo"
RESULT_MESSAGE = """Holas,
El lugar elegido es: %(place)s
y los comensales son: %(names)s.

Los lugares disponibles eran: %(valid_places)s.

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
            'url_y': BASE_URL + reverse('rsvp', kwargs={'pk': q.uuid, 'rsvp': 1}),
            'url_n': BASE_URL + reverse('rsvp', kwargs={'pk': q.uuid, 'rsvp': 0}),
        }
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

    all_places = Place.objects.all()
    valid_places = set([p.name for p in all_places])

    for q in quorum:
        valid_places -= set(q.person.get_blacklist())

    choice = random.choice(list(valid_places))

    data = {
        'place': choice,
        'names': ', '.join(names),
        'valid_places': ', '.join(valid_places)
    }

    try:
        send_mail(RESULT_SUBJECT, RESULT_MESSAGE % data, FROM_EMAIL, mail_list, fail_silently=False)
    except Exception as e:
        print "Fail to send result mail."
        print e
