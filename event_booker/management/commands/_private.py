# from event_booker import models
from faker import Faker
import datetime

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
    print('success')
    print(dates_)
    return dates_


# def create_events():
#     models.Event.objects.create(name='Python Basics', date='20')
#     pass

if __name__ == '__main__':
    print(dates())
