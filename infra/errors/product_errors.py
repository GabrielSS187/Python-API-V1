# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel, validator, Field
from .custom_error import CustomError
           

class PoductValidatorOptional(BaseModel):
    name: Optional[str]
    value: Optional[float]
    type: Optional[str]
    
    @validator('name', pre=True, always=True)
    def validate_name(cls, name):
        if name is None:
            return name
        if not isinstance(name, str):
            raise CustomError('The name must be a string.', 406)
        if not name.strip():
            raise CustomError('The name cannot be empty.', 406)
        if len(name) < 3:
            raise CustomError('The name must be at least 3 characters long.', 406)
        if len(name) > 35:
            raise CustomError('The name must be a maximum of 35 characters.', 406)
        return name
    
    
    @validator('value', pre=True, always=True) 
    def validate_value(cls, value):
        if value is None:
            return value
        if value <= 0:
            raise CustomError('The value must be greater than 0.', 406)
        return value
        
    @validator('type', pre=True, always=True)
    def validate_product_type(cls, type):
        if type is None:
            return type
        if not isinstance(type, str):
            raise CustomError('The type must be a string.', 406)
        if not type.strip():
            raise CustomError('The type cannot be empty.', 406)
        if type != 'Avulso' and type != 'Recorrente':
            raise CustomError("The product type must be 'Avulso' or 'Recorrente'", 406)
        return type


class PoductValidator(PoductValidatorOptional):
    name: str = Field(...)
    value: float = Field(...)
    type: str = Field(...)