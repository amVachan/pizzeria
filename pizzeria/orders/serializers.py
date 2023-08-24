from rest_framework import serializers, fields
from .models import Pizza, Order, TOPPINGS_CHOICES


class PizzaSerializer(serializers.Serializer):
    base = serializers.CharField(max_length=20)
    cheese = serializers.CharField(max_length=20)
    toppings = fields.MultipleChoiceField(choices=TOPPINGS_CHOICES)
    price = fields.DecimalField(max_digits=5, decimal_places=2)
    
class OrderSerializer(serializers.Serializer):
    pizzas = PizzaSerializer(many=True)
    status = serializers.CharField(max_length=100)

    def create(self, validated_data):
        pizzas_data = validated_data.pop('pizzas')
        print(validated_data)
        order = Order.objects.create(**validated_data)

        for pizza_data in pizzas_data:
            try:
                pizza = Pizza.objects.create( **pizza_data)
                order.pizzas.add(pizza)
            except Exception as e:
                print(e)


        return order