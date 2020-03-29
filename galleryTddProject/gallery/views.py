import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Image, Object


@csrf_exempt
def index(request):
    if request.method == 'GET':
        images_list = Image.objects.all()
        return HttpResponse(serializers.serialize("json", images_list))
    elif request.method == 'POST':
        json_image = json.loads(request.body)
        name = json_image['name']
        url = json_image['url']
        description = json_image['description']
        type_image = json_image['type']
        user_id = json_image['userId']

        user = User.objects.filter(id=user_id)[0]

        Image.objects.create(name=name, url=url, description=description, type=type_image, user=user)

        image_response = Object()
        image_response.quantity = len(Image.objects.filter(user=user))
        image_response.image = Object()
        image_response.image.name = name
        image_response.image.url = url
        image_response.image.description = description
        image_response.image.type = type_image
        return HttpResponse(image_response.to_json())
