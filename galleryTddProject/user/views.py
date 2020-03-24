from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from gallery.models import Image


@csrf_exempt
def get_portafolio(request, username):
    # Get parameters
    public = request.GET.get('public')
    user = User.objects.filter(username=username)[0]

    images_list = Image.objects.filter(public=public, user=user)
    return HttpResponse(serializers.serialize('json', images_list))

