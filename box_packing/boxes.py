box_sizes = {
    'kcup': {'length': 12, 'width': 12, 'height': 10},
    'xsmall': {'length': 21, 'width': 16, 'height': 15},
    'small': {'length': 17, 'width': 11, 'height': 11},
    'medium': {'length': 21, 'width': 16, 'height': 15},
    'xlarge': {'length': 21, 'width': 24, 'height': 20},
}


default_boxes = [
    {
        "name": "Computers",
        "size": "medium",
        "length": 21,
        "width": 16,
        "height": 15,
        "weight_class": 3,
        "fragile": True,
        "liquid": False,
        "valuable": True,
        "weather_resistant": False,
        "can_freeze": False,
        "essential": False
    },
    {
        "name": "Food Staples",
        "size": "medium",
        "length": 21,
        "width": 16,
        "height": 15,
        "weight_class": 2,
        "fragile": False,
        "liquid": False,
        "valuable": False,
        "weather_resistant": False,
        "can_freeze": False,
        "essential": False
    },
]
