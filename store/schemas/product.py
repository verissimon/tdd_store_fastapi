from typing import Optional
from pydantic import BaseModel, Field, UUID4
from store.schemas.base import BaseSchemaMixin
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(
        ..., description="Product name", max_length=255
    )  # ... indica campo obrigatorio
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(BaseSchemaMixin, ProductBase):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


class ProductUpdate(ProductBase):
    name: Optional[str] = Field(
        None, description="Product name", max_length=255
    )  # ... indica campo obrigatorio
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[float] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate):
    ...
