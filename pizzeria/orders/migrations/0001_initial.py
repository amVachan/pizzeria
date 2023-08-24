# Generated by Django 4.2.4 on 2023-08-24 05:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(choices=[('Thin Crust', 'Thin Crust'), ('Normal', 'Normal'), ('Cheese Burst', 'Cheese Burst')], max_length=20)),
                ('cheese', models.CharField(choices=[('Mozzarella', 'Mozzarella'), ('Cheddar', 'Cheddar'), ('Parmesan', 'Parmesan')], max_length=20)),
                ('toppings', multiselectfield.db.fields.MultiSelectField(choices=[('Pepperoni', 'Pepperoni'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Sausage', 'Sausage'), ('Peppers', 'Peppers'), ('Olives', 'Olives'), ('Extra Cheese', 'Extra Cheese')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Accepted', max_length=20)),
                ('pizzas', models.ManyToManyField(to='orders.pizza')),
            ],
        ),
    ]
