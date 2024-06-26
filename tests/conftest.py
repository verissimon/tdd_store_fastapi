import asyncio

import pytest
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from tests.factories import (
    product_many_factory,
    product_updated_params_factory,
    product_factory,
)
from httpx import AsyncClient
from uuid import UUID
from store.usecases.product import product_usecase as usecase


@pytest.fixture
async def client():
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collection_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_id():
    return UUID("c5c57627-2152-424a-900f-1e6a9c5fe04b")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_factory(), id=product_id)


@pytest.fixture
async def product_inserted(product_in):
    return await usecase.create(body=product_in)


@pytest.fixture
def many_products_in():
    return [ProductIn(**product) for product in product_many_factory()]


@pytest.fixture
async def many_products_inserted(many_products_in):
    return [await usecase.create(body=product_in) for product_in in many_products_in]


@pytest.fixture
async def product_up(product_inserted):
    return ProductUpdate(**product_updated_params_factory(), id=product_inserted.id)
