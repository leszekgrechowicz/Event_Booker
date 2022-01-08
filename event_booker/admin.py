from django.contrib import admin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse

from .models import Customer, Event, EventImage


def sent_invitation_email(self, request, queryset):
    """Sending invitation email to selected customers"""

    for customer in queryset:
        domain = get_current_site(request).domain
        link = reverse('event_booker:confirm-booking', kwargs={'uuid_': customer.uuid})
        link = 'http://' + domain + link
        email_subject = f' {customer.event.name} booking  confirmation.'
        email_send_from = 'no-reply@eventer.com'
        email_body = f'Dear {customer.name} {customer.surname},\n \n\tPlease kindly confirm your attendance to an Event ' \
                     f'"{customer.event.name}" \non {customer.event.date} by following the link below: \n' \
                     f'{link} .\n\n' \
                     f'Kind Regards, \n' \
                     f'Admin - EvEnter'

        send_mail(email_subject,
                  email_body,
                  email_send_from,
                  [customer.email],
                  fail_silently=False)
        customer.invited = True
        customer.save()


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    actions = [sent_invitation_email, ]


admin.site.register(Event)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(EventImage)
