from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

PIZZA_BASE_CHOICES = [
    ('Thin Crust', 'Thin Crust'),
    ('Normal', 'Normal'),
    ('Cheese Burst', 'Cheese Burst'),
]

CHEESE_CHOICES = [
    ('Mozzarella', 'Mozzarella'),
    ('Cheddar', 'Cheddar'),
    ('Parmesan', 'Parmesan'),
]

TOPPINGS_CHOICES = (
    ('Pepperoni', 'Pepperoni'),
    ('Mushrooms', 'Mushrooms'),
    ('Onions', 'Onions'),
    ('Sausage', 'Sausage'),
    ('Peppers', 'Peppers'),
    ('Olives', 'Olives'),
    ('Extra Cheese', 'Extra Cheese'),
)


class Pizza(models.Model):
    base = models.CharField(max_length=20, choices=PIZZA_BASE_CHOICES)
    cheese = models.CharField(max_length=20, choices=CHEESE_CHOICES)
    toppings = MultiSelectField(choices=TOPPINGS_CHOICES,
                                 max_choices=5,
                                 max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.base} Pizza with {self.cheese} Cheese and Toppings"
    
class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    ordered_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default='Accepted')
    
    