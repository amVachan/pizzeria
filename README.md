# pizzeria

# Pizza Ordering System API

This repository contains the documentation for the Pizza Ordering System API, which allows users to create and track pizza orders.

## API Endpoints

### Create Order API

**Endpoint:** `http://127.0.0.1:8000/api/create_order/`
**Method:** POST

#### Sample Request Body

```json
{
    "pizzas": [
        {
            "base": "Thin Crust",
            "cheese": "Mozzarella",
            "toppings": [
                "Pepperoni",
                "Mushrooms",
                "Onions",
                "Olives"
            ],
            "price": 10.99
        }
    ],
    "status": "Accepted"
}
```
#### Sample Response Body
```json
{
    "pizzas": [
        {
            "base": "Thin Crust",
            "cheese": "Mozzarella",
            "toppings": [
                "Onions",
                "Olives",
                "Pepperoni",
                "Mushrooms"
            ],
            "price": "10.99"
        }
    ],
    "status": "Accepted"
}
```


### Track Order API

**Endpoint:** http://127.0.0.1:8000/api/track_order/1/
**Method:** GET

####Sample Response

```json
{
    "pizzas": [
        {
            "base": "Thin Crust",
            "cheese": "Mozzarella",
            "toppings": [
                "Onions",
                "Olives",
                "Pepperoni",
                "Mushrooms"
            ],
            "price": "10.99"
        }
    ],
    "status": "Accepted"
}
```
