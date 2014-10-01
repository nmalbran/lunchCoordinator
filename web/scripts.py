from web.models import Person, Quorum


def send_mails():
    people = Person.objects.all()
    Quorum.objects.all().delete()
    for p in people:
        q = Quorum.objects.create(person=p)
        print q.uuid