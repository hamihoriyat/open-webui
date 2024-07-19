import uuid
from pydantic import BaseModel, ConfigDict, parse_obj_as
from typing import List, Union, Optional
import time

from sqlalchemy import String, Column, BigInteger, Text, Integer

from utils.misc import get_gravatar_url

from apps.webui.internal.db import Base, JSONField, Session, get_db
from apps.webui.models.chats import Chats

####################
# Groups DB Schema
####################

class Group(Base):
    __tablename__ = "group"
    id= Column(String, primary_key=True)
    name= Column(String,unique=True)
    input_limit= Column(Integer)
    output_limit= Column(Integer,nullable=True)
    models_limit= Column(String)

class GroupModel(BaseModel):
    id: str
    name: str="basic"
    input_limit: int=5000
    output_limit: int
    models_limit: str="['GPT-4o-mini','llama3:8b','phi3:3.8b']"   

####################
# Forms
####################
class GroupForm(BaseModel):
    name: str
    input_limit: int
    output_limit: int
    models_limit: str   

class GroupResponse(BaseModel):
    id: str
    name: str
   

class GroupTable:
    def insert_group(self,name:str,input_limit:int,output_limit:int,models_limit:str)-> Optional[GroupModel]: 
        with get_db() as db:
            id=str(uuid.uuid4())
            group= GroupModel(**{
                "id":id,
                "name": name,
                "input_limit": input_limit,
                "output_limit": output_limit,
                "models_limit": models_limit
            })
            result = Group(**group.model_dump())
            db.add(result)
            db.commit()
            db.refresh(result)
            if result:
                return group
            else:
                return None


Groups=GroupTable()
    