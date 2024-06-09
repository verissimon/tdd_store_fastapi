from typing import List
import pytest
from tests.factories import product_factory, product_updated_params_factory
from fastapi import status


async def test_controller_create_success(client, products_url):
    response = await client.post(products_url, json=product_factory())

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {"name": "test", "quantity": 12, "price": "10.02", "status": True}


async def test_controller_get_success(client, products_url, product_inserted):
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "test",
        "quantity": 12,
        "price": "10.02",
        "status": True,
    }


async def test_controller_get_not_found(client, products_url):
    id = "de38f7a8-b721-40b5-ab06-d5506d4f94b1"
    response = await client.get(f"{products_url}{id}")
    content = response.json()

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert content == {"detail": f'Product not found with filter {{"id": "{id}"}}'}


@pytest.mark.usefixtures("many_products_inserted")
async def test_controller_query_find_all_success(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_update_success(client, products_url, product_inserted):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json=product_updated_params_factory()
    )

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "updated_name",
        "quantity": 12,
        "price": "10.02",
        "status": False,
    }


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}d5c57627-2152-424a-900f-1e6a9c5fe04c"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": (
            "Product not found with filter "
            + ('{"id": "d5c57627-2152-424a-900f-1e6a9c5fe04c"}')
        )
    }
