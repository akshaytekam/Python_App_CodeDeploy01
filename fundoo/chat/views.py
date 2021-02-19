from django.shortcuts import render, HttpResponse, redirect
import json
from django.utils.safestring import mark_safe


def chatting(request):
    return render(request, 'chat.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def logout_u(request):
    return render(request, 'login.html', {})
