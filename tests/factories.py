def product_factory():
    return {"name": "test", "quantity": 12, "price": 10.020, "status": True}


def product_updated_params_factory():
    return {"name": "updated_name", "status": False, "price": 10.02}


def product_many_factory():
    return [
        {"name": "test0", "quantity": 12, "price": "10.0", "status": True},
        {"name": "test1", "quantity": 10, "price": "11.1", "status": True},
        {"name": "test2", "quantity": 11, "price": "12.2", "status": False},
        {"name": "test3", "quantity": 13, "price": "13.3", "status": True},
    ]
