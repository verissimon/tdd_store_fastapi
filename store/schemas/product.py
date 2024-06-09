from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from store.schemas.base import BaseSchemaMixin, ValidOutSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name", max_length=255)
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(BaseSchemaMixin, ProductBase):
    ...


class ProductOut(ProductIn, ValidOutSchemaMixin):
    ...


class ProductUpdate(ProductBase):
    name: Optional[str] = Field(None, description="Product name", max_length=255)
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate, ValidOutSchemaMixin):
    ...
