import os
import random
from web.models import Person, Quorum, Place
from django.core.mail import send_mail, get_connection, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.conf import settings


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

Quejas o QQ a lunch@devnull.com, le responderemos ASAP.

Nos vemos!
"""

def _get_html_message(temp=''):
    here = os.path.abspath(os.path.dirname(__file__))
    temp = 'templates/%s.html' % temp
    f = open(os.path.join(here,temp), 'r')
    msg = f.read()
    f.close()
    return msg

def check_quorum():
    people = Person.objects.filter(active=True)
    Quorum.objects.all().delete()
    conn = get_connection()
    for p in people:
        q = Quorum.objects.create(person=p)

        data = {
            'name': p.name,
            'url_y': settings.BASE_URL + reverse('rsvp', kwargs={'pk': q.uuid, 'rsvp': 1}),
            'url_n': settings.BASE_URL + reverse('rsvp', kwargs={'pk': q.uuid, 'rsvp': 0}),
            'blacklist': p.blacklist,
        }

        msg = EmailMultiAlternatives(QUORUM_SUBJECT, QUORUM_MESSAGE % data, settings.DEFAULT_FROM_EMAIL, [p.mail], connection=conn)
        msg.attach_alternative(_get_html_message('quorum_mail') % data, "text/html")

        try:
            msg.send()
        except Exception as e:
            print "Fail to send quorum mail to %s" % p.mail
            print e

def notify_lunchers():
    quorum = Quorum.objects.filter(lunch='yes')
    names = [q.person.name for q in quorum]
    mail_list = [q.person.mail for q in quorum]

    all_places = Place.objects.filter(active=True)
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
        send_mail(RESULT_SUBJECT, RESULT_MESSAGE % data, settings.DEFAULT_FROM_EMAIL, mail_list, fail_silently=False)
    except Exception as e:
        print "Fail to send result mail."
        print e
