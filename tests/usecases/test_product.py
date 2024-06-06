from typing import List
import pytest
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase as usecase
from store.core.exceptions import NotFoundException


async def test_usecases_create_success(product_in):
    result = await usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "test"


async def test_usecases_get_succes(product_inserted):
    result = await usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "test"


async def test_usecases_get_not_found():
    with pytest.raises(NotFoundException) as err:
        await usecase.get(id="d5c57627-2152-424a-900f-1e6a9c5fe04c")
    assert err.value.message == (
        "Product not found with filter "
        + ('{"id": "d5c57627-2152-424a-900f-1e6a9c5fe04c"}')
    )


async def test_usecases_query_success(product_inserted):
    result = await usecase.query()

    assert result[0].name == "test"
    assert isinstance(result, List)


async def test_usecases_update_success(product_inserted, product_up):
    result = await usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)
    assert result.name == "updated_name"
    assert result.quantity == 12
