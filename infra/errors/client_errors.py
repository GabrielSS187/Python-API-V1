# -*- coding: utf-8 -*-

import re
from pydantic import BaseModel, validator
from .custom_error import CustomError
           

email_pattern = re.compile(r'^\S+@\S+\.\S+$')

class ClientValidator(BaseModel):
    name: str
    email: str
    password: str
    
    @validator('name')
    def validate_name(cls, name):
        if len(name) < 3:
            raise CustomError('The name must be at least 3 characters long.', 406)
        if len(name) > 35:
            raise CustomError('The name must be a maximum of 35 characters.', 406)
        return name   
    
    @validator('email') 
    def validate_email(cls, email):
        if not email_pattern.match(email):
            raise CustomError('This email format is not correct.', 406)
        return email
        
    @validator('password')
    def validate_password(cls, password):
        if len(password) < 6:
            raise CustomError('The password must contain at least 6 characters.', 406)
        return password

