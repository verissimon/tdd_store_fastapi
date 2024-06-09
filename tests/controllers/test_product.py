from tests.factories import product_factory
from fastapi import status


async def test_controller_create_success(client, products_url):
    response = await client.post(products_url, json=product_factory())

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {"name": "test", "quantity": 12, "price": 10.020, "status": True}
