from django.test import TestCase
from .models import Material
from django.core.files.uploadedfile import SimpleUploadedFile
import os



class ProjectTests(TestCase):

    def setUp(self):

        video = open('media/4.jpg', 'r')

        self.material_1 = Material.objects.create(material_text="M1", status="in process")
      #  self.media_1 = self.material_1.media_set.create(name="picture", file=video)
        Material.objects.create(material_text="M2", status="in process")

    # finally:
    #         temp.close()

    def test_animals_can_speak(self):
        M1 = Material.objects.get(material_text="M1")
        M2 = Material.objects.get(material_text="M2")
        self.assertEqual(M1.status, 'in process')
        self.assertEqual(M2.status, 'in process')

    def test_homepage_qc(self):
        response = self.client.get('/QC/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get('/QC/1/')
        response = self.client.get('/QC/2/')
        self.assertEqual(response.status_code, 200)

    def test_process_accept(self):
        decision = "accepted"
        material = Material.objects.get(pk=1)
        material.status = decision
        material.save()
        self.assertEqual(material.status, 'accepted')
        response = self.client.post('/QC/1/process/')
        self.assertEqual(response.status_code, 302)

    def test_mateial_model(self):
        self.assertEqual
        (self.material_1.__str__(), self.material_1.material_text)
        self.assertEqual
      #  (self.media_1.__str__(), self.media_1.name)
