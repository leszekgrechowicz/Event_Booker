from event_booker import models

def create_events():
    models.Event.objects.create(name='Python Basics', date='20')
    pass