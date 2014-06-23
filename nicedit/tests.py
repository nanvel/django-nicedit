import os

from StringIO import StringIO

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson

from .models import NicEditImage


class ImageUploadTestCase(TestCase):

    def test_image_upload(self):
        self.assertFalse(NicEditImage.objects.exists())
        imagefile = StringIO('GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00'
            '\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
        imagefile.name = 'test_image.gif'
        response = self.client.post(reverse('nicedit_upload'), {})
        self.assertEqual(response.status_code, 200)
        data = simplejson.loads(response.content)
        self.assertEqual(data['success'], False)
        # unauthenticated
        response = self.client.post(
            reverse('nicedit_upload'), {'image': imagefile})
        self.assertEqual(response.status_code, 200)
        data = simplejson.loads(response.content)
        self.assertEqual(data['success'], False)
        # authentication
        user = User.objects.create_user(
            username='yoko', password='yoko', email='yoko@mail.com')
        result = self.client.login(
            username=user.username, password=user.username)
        self.assertTrue(result)
        imagefile.seek(0)
        response = self.client.post(
            reverse('nicedit_upload'), {'image': imagefile})
        self.assertEqual(response.status_code, 200)
        data = simplejson.loads(response.content)
        self.assertEqual(data['success'], True)
        self.assertIn(imagefile.name, data['upload']['links']['original'])
        self.assertEqual(NicEditImage.objects.count(), 1)
        image = NicEditImage.objects.latest('id')
        self.assertTrue(os.path.exists(image.image.path))
        os.remove(image.image.path)
