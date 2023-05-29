from django.shortcuts import render, redirect
from .models import Type, Food
from  .forms import TypeForm, FoodForm

# Create your views here.
def list_food (request):
    types = Type.objects.all()
    return render(request, 'food_types/list_type.html', { 'types': types })

def charge_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_food')
    else:
        form = TypeForm()
    return render(request, 'food_types/type_charge.html', {'form': form})

def edit_type (request, type_id):
    type = Type.objects.get(id=type_id)
    if request.method == "POST":
        form = TypeForm(request.POST, request.FILES, instance=type)
        if form.is_valid():
            form.save()
            return redirect(list_food)
    else:
        form = TypeForm(instance=type)
    return render(request, "food_types/edit_type.html", {"form": form})

def delete_type (request, type_id):
    type = Type.objects.get(id=type_id)
    if request.method == "POST":
        type.delete()
        return redirect(list_food)
    else:
        return render(request, "food_types/delete_type.html", {"type": type})
    
def description_types (request, type_id):
    type = Type.objects.get(id=type_id)
    foods = Food.objects.filter(type_by = type_id)
    return render(request, 'foods/list_foods.html', { 'foods': foods, 'type': type})

def charge_food (request, type_id):
    type = Type.objects.get(id=type_id)
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)

            type_instance = Type.objects.get(id=type_id)
            temp_form.type_by = type_instance
            temp_form.save()

            type_id = temp_form.type_by.id
            return redirect('description_types', type_id = type_id)
    else:
        form = FoodForm()
    return render(request, 'foods/food_charge.html', {'form': form, 'type': type})

def delete_food (request, food_id, type_id):
    food = Food.objects.get(id=food_id)
    type = Type.objects.get(id=type_id)
    if request.method == "POST":
        food.delete()
        return redirect('description_types', type_id = type_id)
    else:
        return render(request, "foods/delete_food.html", {'food': food, 'type': type})
 
def edit_food(request, food_id, type_id):
    food = Food.objects.get(id=food_id)
    type = Type.objects.get(id=type_id)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.type_by = type
            temp_form.save()

            type_id = temp_form.type_by.id
            return redirect(description_types, type_id = type_id)
    else:
        form = FoodForm(instance=food)
    return render(request, "foods/edit_food.html", {"form": form, "type": type})
