from django.db import migrations

DISHES = [
    {"id": 1, "name": "Маргарита", "price": 180, "description": "Томатний соус, моцарела, свіжий базилік."},
    {"id": 2, "name": "Пепероні", "price": 210, "description": "Томатний соус, моцарела, гостра салямі пепероні."},
    {"id": 3, "name": "Чотири сири", "price": 240, "description": "Моцарела, горгонзола, пармезан, фонтіна."},
    {"id": 4, "name": "Карбонара", "price": 220, "description": "Вершковий соус, бекон, яйце, пармезан."},
]

def populate_dishes(apps, schema_editor):
    Dish = apps.get_model('menu', 'Dish')

    if not Dish.objects.exists():
        for dish in DISHES:
            Dish.objects.create(
                name=dish["name"],
                price=dish["price"],
                description=dish["description"]
            )

class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0001_initial'),  # Посилання на створення таблиці, а не на саму себе!
    ]

    operations = [
        migrations.RunPython(populate_dishes),
    ]