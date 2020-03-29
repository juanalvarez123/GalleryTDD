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

    def test_user_login(self):
        User.objects.create_user(username='angie.eraso', email='angie.eraso@uniandes.edu.co', password='12345')

        user_login = {
            'username': 'angie.eraso',
            'password': '12345'
        }
        response = self.client.post('/user/login/', data=json.dumps(user_login), content_type='application/json')
        json_response = json.loads(response.content)

        self.assertEquals(json_response[0]['fields']['username'], 'angie.eraso')
        self.assertEquals(json_response[0]['fields']['email'], 'angie.eraso@uniandes.edu.co')

    def test_another_user_login(self):
        User.objects.create_user(username='js.alvareze', email='js.alvareze@uniandes.edu.co', password='12345')

        user_login = {
            'username': 'js.alvareze',
            'password': '12345'
        }
        response = self.client.post('/user/login/', data=json.dumps(user_login), content_type='application/json')
        json_response = json.loads(response.content)

        self.assertEquals(json_response[0]['fields']['username'], 'js.alvareze')
        self.assertEquals(json_response[0]['fields']['email'], 'js.alvareze@uniandes.edu.co')

    def test_update_user(self):
        user_created = User.objects.create_user(username='konan', email='konan@gmail.com', password='12345')
        user_update = {
            'first_name': 'mauricio',
            'last_name': 'gutierrez',
            'email': 'f@hotmail.com'
        }
        response = self.client.put('/user/' + str(user_created.id), data=json.dumps(user_update),
                                   content_type='application/json')
        json_response = json.loads(response.content)

        self.assertEquals(json_response[0]['fields']['first_name'], 'mauricio')
        self.assertEquals(json_response[0]['fields']['last_name'], 'gutierrez')
        self.assertEquals(json_response[0]['fields']['email'], 'f@hotmail.com')

    def test_update_gallery(self):
        new_user = User.objects.create_user(username='js.alvareze', password='12345',
                                            email='js.alvareze@uniandes.edu.co', first_name='Juan Sebastian')

        Image.objects.create(name='Portafolio 1', url='No', description='Descripción para portafolio 1',
                             type='jpg', user=new_user, public=False)

        image2 = Image.objects.create(name='Portafolio 2', url='No', description='Descripción para portafolio 2',
                                      type='png', user=new_user, public=True)

        params = {
            'public': False
        }
        response = self.client.put('/user/js.alvareze/gallery/' + str(image2.id), data=params,
                                   content_type='application/json')
        json_response = json.loads(response.content)

        self.assertEquals(len(json_response), 1)

        self.assertEquals(json_response[0]['fields']['name'], 'Portafolio 2')
        self.assertFalse(json_response[0]['fields']['public'])
