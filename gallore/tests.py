from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here



# class ImageTestClass(TestCase):

#     def setUp(self):
#         self.Maasai_Mara=Location.objects.Create(name="Maasai_Mara")
#         self.Animals=Category.objects.Create(name="Animals")
#         self.image=Image(name="Nature",description="Wildlife photography",Category=self.Animals,location=self.Maasai_Mara,upload_date="27/08/2019",image="https://www.google.com")

#     def test__instance(self):
#         self.assertEquals(self.image.name,"Nature")


class LocationTestClass(TestCase):
    def setUp(self):
        self.Maasai_Mara = Location(name='Maasai_Mara')

    def test_instance(self):
        self.Maasai_Mara.save()
        self.assertTrue(isinstance(self.Maasai_Mara, Location))

class CategoryTestClass(TestCase):

    def setUp(self):
        self.nature = Category(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))