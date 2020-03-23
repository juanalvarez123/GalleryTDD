import json

from django.contrib.auth.models import User
from django.test import TestCase
from gallery.models import Image


class UserTestCase(TestCase):

    def test_get_public_gallery(self):
        new_user = User.objects.create_user(username='js.alvareze', password='12345',
                                            email='js.alvareze@uniandes.edu.co', first_name='Juan Sebastian')

        Image.objects.create(name='Portafolio 1', url='No', description='Descripción para portafolio 1',
                             type='jpg', user=new_user, public=False)

        Image.objects.create(name='Portafolio 2', url='No', description='Descripción para portafolio 2',
                             type='png', user=new_user, public=True)

        params = {
            'public': True
        }
        response = self.client.get('/user/js.alvareze/gallery/', data=params, content_type='application/json')
        json_response = json.loads(response.content)

        self.assertEquals(len(json_response), 1)

        self.assertEquals(json_response[0]['fields']['name'], 'Portafolio 2')
        self.assertTrue(json_response[0]['fields']['public'])
