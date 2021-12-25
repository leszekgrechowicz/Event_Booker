import random

from event_booker import models
from faker import Faker
from lorem_text import lorem
import datetime
from sys import stderr

fake = Faker()


def dates():
    dates_ = []
    while len(dates_) < 1:
        start_date = datetime.date(year=2022, month=1, day=1)
        date1 = fake.date_between(start_date=start_date, end_date='+2y')
        date2 = fake.date_between(start_date=start_date, end_date='+2y')
        if date1 < date2:
            date3 = date2
            date3 += datetime.timedelta(days=1)
            dates_.append((date1, date2, date3))
    print('Success - Date created')
    return dates_[0]


EVENTS = ['Python Basics',
          'Python Intermediate',
          'Python Advanced',
          'Java Script Basics',
          'Java Script Intermediate',
          'Java Script Advanced',
          'SQL Advanced',
          ]


def create_events():
    for event in EVENTS:
        start_date, end_date, date = dates()
        stderr.write(f'Dates for {event} created !')
        models.Event.objects.create(name=event,
                                    date=date,
                                    start_date=start_date,
                                    end_date=end_date,
                                    places=random.randint(10, 50),
                                    description=lorem.words(random.randint(15, 40)),
                                    age_restriction=random.choice([True, False])
                                    )
        stderr.write(f'Event {event} crated !')


