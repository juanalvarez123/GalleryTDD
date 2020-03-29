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


@csrf_exempt
def manage_user(request, user_id):
    if request.method == 'PUT':
        json_user = json.loads(request.body)
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        email = json_user['email']

        user_model = User.objects.filter(id=user_id)

        if len(user_model) == 1:
            user_model[0].first_name = first_name
            user_model[0].last_name = last_name
            user_model[0].email = email
            user_model[0].save()
            return HttpResponse(serializers.serialize("json", user_model))
        else:
            return HttpResponseNotFound('<h1>User not found</h1>')


@csrf_exempt
def manage_portafolio(request, username, image_id):
    if request.method == 'PUT':
        json_image = json.loads(request.body)
        public = json_image['public']
        user = User.objects.filter(username=username)[0]

        image_model = Image.objects.filter(id=image_id, user=user)

        if len(image_model) == 1:
            image_model[0].public = public
            image_model[0].save()
            return HttpResponse(serializers.serialize("json", image_model))
        else:
            return HttpResponseNotFound('<h1>Image not found</h1>')


@csrf_exempt
def index(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
        return HttpResponse(serializers.serialize("json", [user_model]))
