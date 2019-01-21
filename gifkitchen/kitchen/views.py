from django.shortcuts import render, redirect
from kitchen.forms import RecipeForm
from django.views import generic
from kitchen.models import Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

def home(request):

	context = {}

	return render(request, "home.html", context=context)

def submit(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

# class RecipeListView(generic.ListView):
#     model = Recipe
#     template_name = 'recipe_list.html'

def RecipeList(request):

    All = request.GET.get('All', None)
    Breakfast = request.GET.get('Breakfast', None)
    Lunch = request.GET.get('Lunch', None)
    Dinner = request.GET.get('Dinner', None)
    Dessert = request.GET.get('Dessert', None)
    Vegan = request.GET.get('Vegan', None)
    
    recipes = False 

    if((not All and not Breakfast and not Lunch and not Dinner and not Dessert and not Vegan) or All):
        recipes = Recipe.objects.all()
        
    else:
        if(Breakfast):
            recipes = Recipe.objects.all().filter(breakfast = True)
        if(Lunch):
            recipes = Recipe.objects.all().filter(lunch = True)
        if(Dinner):
            recipes = Recipe.objects.all().filter(dinner = True)
        if(Dessert):
            recipes = Recipe.objects.all().filter(dessert = True)
        if(Vegan):
            recipes = Recipe.objects.all().filter(vegan = True)
                
    

    context = {
                "recipe_list": recipes,
                }

    return render(request, "recipe_list.html", context=context)

# Create your views here.
