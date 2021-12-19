from django.shortcuts import render
from django.views import View


class ShowEventsView(View):
    def get(self, request):
        return render(request, 'event_booker/index.html', {'title': 'Home', 'data': 'Leszek'})