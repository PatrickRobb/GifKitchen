from django.db import models
from django.urls import reverse

class Recipe(models.Model):

    name = models.CharField(max_length=60, help_text='Enter Name')
    vote_count = models.IntegerField(null=True)
    difficulty = models.CharField(max_length=60)
    ingredients = models.CharField(max_length=1000, null = True, help_text='Enter Ingredients')
    instructions = models.CharField(max_length=2000, null = True, help_text='Enter Written Instructions')
    picture = models.ImageField('recipe picture', upload_to = 'media/', max_length = 255, null = True) 
    breakfast = models.BooleanField(default=False) 
    lunch = models.BooleanField(default=False)  
    dinner = models.BooleanField(default=False)
    dessert = models.BooleanField(default=False)  
    vegan = models.BooleanField(default=False) 

    def get_absolute_url(self):
        
        return reverse('recipe-detail', args=[str(self.id)])
    




# Create your models here.
