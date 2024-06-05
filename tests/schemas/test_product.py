from uuid import UUID

from pydantic import ValidationError
from store.schemas.product import ProductIn
import pytest

from tests.factories import product_factory


def test_schemas_return_success():
    data = product_factory()
    product = ProductIn.model_validate(data)

    assert product.name == "test"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate({})

    assert err.value.errors().__len__() == 4
    for error in err.value.errors():
        assert error.get("msg") == "Field required"
