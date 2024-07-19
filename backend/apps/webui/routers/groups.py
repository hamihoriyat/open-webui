from fastapi import Depends, Request, HTTPException, status
from typing import List, Union, Optional
from utils.utils import get_verified_user, get_admin_user
from fastapi import APIRouter
from pydantic import BaseModel
import json
import logging


from apps.webui.models.users import Users
from apps.webui.models.groups import (
Group,
GroupModel,
GroupResponse,
GroupForm,
Groups
)




from constants import ERROR_MESSAGES

from config import SRC_LOG_LEVELS, ENABLE_ADMIN_EXPORT

log = logging.getLogger(__name__)
# log.setLevel(SRC_LOG_LEVELS["GROUPS"])

router = APIRouter()


############################
# CreateNewGroup
############################


@router.post("/", response_model=Optional[GroupResponse])
async def create_new_group(group_body: GroupForm, user=Depends(get_verified_user)):
    
    try:
        group = Groups.insert_group(
            name=group_body.name,
            input_limit=group_body.input_limit,
            output_limit=group_body.output_limit,
            models_limit=group_body.models_limit
        )
        return GroupResponse(**{**group.model_dump()})
    except Exception as e:
        print(e)
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ERROR_MESSAGES.DEFAULT()
        )
    
@router.get("/")
async def getTest(request: Request):
    
    print("miad inja aslan?")
    return {"Hello":"hami"}

