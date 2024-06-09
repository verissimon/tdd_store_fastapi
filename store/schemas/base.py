from decimal import Decimal
from bson import Decimal128
from pydantic import UUID4, BaseModel, ConfigDict, Field, model_validator
from datetime import datetime


class BaseSchemaMixin(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class Valid:
    @model_validator(mode="before")
    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data


class UpdateValidator:
    @model_validator(mode="after")
    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal):
                data[key] = str(value)

        return data


class ValidOutSchemaMixin(Valid):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
