import json
from datetime import datetime

from django.http import HttpResponse


def hello_world(request):
    now = datetime.now().strftime('%H:%M hrs - %dth %b, %Y')
    return HttpResponse(f'Hello World, the time is {now}')


def numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successful',
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def hi(request, name, age):
    """Return a greeting"""

    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, welcome to Platzigram!'

    data = {
        'status': 'ok',
        'message': message,
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
