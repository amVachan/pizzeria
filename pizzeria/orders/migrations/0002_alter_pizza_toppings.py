# Generated by Django 4.2.4 on 2023-08-24 09:11

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pepperoni', 'Pepperoni'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Sausage', 'Sausage'), ('Peppers', 'Peppers'), ('Olives', 'Olives'), ('Extra Cheese', 'Extra Cheese')], max_length=250),
        ),
    ]
