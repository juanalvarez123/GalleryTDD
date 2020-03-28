import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from gallery.models import Image


@csrf_exempt
def get_portafolio(request, username):
    # Get parameters
    public = request.GET.get('public')
    user = User.objects.filter(username=username)[0]

    images_list = Image.objects.filter(public=public, user=user)
    return HttpResponse(serializers.serialize('json', images_list))


@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        password = json_user['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            user_list = User.objects.filter(username=username)
            return HttpResponse(serializers.serialize("json", user_list))
        else:
            return HttpResponseNotFound('<h1>User not found</h1>')
