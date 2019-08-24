from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here



class ImageTestClass(TestCase):

    def setUp(self):
        self.Maasai_Mara = Location.objects.create(name='Maasai_Mara')
        self.nature = Category.objects.create(name='nature')

        self.wild_animals = Image.objects.create(
            name ='wild_animals',upload_date="26/08/2019",description='Cat Family Photos',location = self.Maasai_Mara,)

        self.wild_animals.category.add(self.nature)

    def test_instance(self):
        self.wild_animals.save()
        self.assertTrue(isinstance(self.wild_animals, Image))

    def test_save_image(self):
        self.wild_animals.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    
    def test_delete_image(self):
        self.wild_animals.save_image()
        self.wild_animals.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)
    
    def test_update_image(self):
        self.wild_animals.save_image()
        self.wild_animals.name = 'wild_animals'
        self.assertTrue(self.wild_animals.name == 'wild_animals')

    def test_get_image_by_id(self):
        pass
    
    def test_search_image(category):
        pass

    def test_filter_by_location(location):
        pass

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