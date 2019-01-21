from django import forms
from kitchen.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'difficulty', 'ingredients', 'instructions', 'picture', 'breakfast', 'lunch', 'dinner', 'dessert', 'vegan',)