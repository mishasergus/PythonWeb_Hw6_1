from django.shortcuts import render, redirect
from .models import Dish
from django.contrib import messages


def home(request):
    return render(request, 'menu/home.html')

def menu_list(request):
    dishes = Dish.objects.all()
    q = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if q:
        dishes = dishes.filter(name__contains=q)
    if min_price:
        dishes = dishes.filter(price__gte=min_price)
    if max_price:
        dishes = dishes.filter(price__lte=max_price)

    return render(request, 'menu/menu_list.html', {"dishes":dishes})

def dish_detail(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    return render(request, 'menu/dish_detail.html', {"dish":dish})

def dish_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price_str = request.POST.get('price')
        description = request.POST.get('description')

        try:
            price = int(price_str)
        except (TypeError, ValueError):
            price = 0

        if price < 0:
            return render(request, 'menu/dish_form.html', {'error': 'Ціна не може бути від’ємною'})
        Dish.objects.create(
            name=name,
            price=price,
            description=description
        )
        messages.success(request, "Dish created sucessfuly")
        return redirect('menu:menu_list')
    return render(request, 'menu/dish_form.html')

def dish_update(request):
    dish_id = request.GET.get('id')
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_price_str = request.POST.get('price')
        new_description = request.POST.get('description')

        try:
            new_price = int(new_price_str)
        except (TypeError, ValueError):
            new_price = 0
        if not Dish.objects.filter(id=dish_id).exists():
            return render(request, 'menu/dish_form.html', {'error': 'Неіснуюче id'})
        if new_price < 0:
            return render(request, 'menu/dish_form.html', {'error': 'Ціна не може бути від’ємною'})
        current = Dish.objects.get(id=dish_id)
        current.price = new_price
        current.description = new_description
        current.name = new_name
        current.save()

        return redirect('menu:menu_list')
    dish = None
    if dish_id:
        dish = Dish.objects.filter(id=dish_id).first()

    return render(request, 'menu/dish_form.html', {'object': dish})


def dish_delete(request):
    if request.method == 'POST':
        dish_id = request.POST.get('id')
        if dish_id:
            Dish.objects.filter(id=dish_id).delete()
            messages.success(request, "Dish deleted sucessfuly")
    return redirect('menu:menu_list')


