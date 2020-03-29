from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image
import json

# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_images_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data),2)

    def test_verify_first_from_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'],"nuevo")

    def test_add_user(self):
        response=self.client.post('/gallery/addUser/',json.dumps({"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5", "email": "test@test.com"}), content_type='application/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'],'testUser')

    def test_add_image(self):
        user_model = User.objects.create_user(username='admin', password='12345678', first_name='administrador',
                                              last_name='administrador', email='administrador@hotmail.com')
        image = {'name': 'zapatos',
                 'url': 'No',
                 'description': 'zapatosImage',
                 'type': 'jpg',
                 'userId': user_model.id}

        response = self.client.post('/gallery/', json.dumps(image), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data['quantity'], 1)
        self.assertEqual(current_data['image']['url'], 'No')
        self.assertEqual(current_data['image']['description'], 'zapatosImage')
        self.assertEqual(current_data['image']['type'], 'jpg')
        self.assertEqual(current_data['image']['name'], 'zapatos')
