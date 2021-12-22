from django.shortcuts import render
from django.views import View
import uuid

test = uuid.uuid4()


# # recommended, uuid guarantees uniqueness.
#
# >>> import uuid
# >>> print(uuid.uuid4().hex)
# '772d4c80-3668-4980-a014-aae59e34b9b9'
#
# # others way, some sort of salt combination
#
# >>> import secrets, hashlib
# >>> first_name = user.first_name  # pull user first name, a salt.
# >>> salt = secrets.token_hex(8) + first_name
# >>> hashlib.sha256(salt.encode('utf-8')).hexdigest()
# 'f8b2e14fe3496de336017687089fb3c49bcab889ac80545fc087289c5b1a3850'

class ShowEventsView(View):
    def get(self, request):
        return render(request, 'event_booker/index.html', {'title': 'Home', 'data': 'Leszek'})
