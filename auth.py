from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from config import SECRET_KEY

from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from models import AdminModel
from api.auth.admin_auth import oauth2_bearer, for_user_exception, get_user_exceptions

from db import get_db

router = APIRouter()

@router.post('')
async def get_current_admin(token: str = Depends(oauth2_bearer),
                            db: Session = Depends(get_db)):
    try:
        pyload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Update token")

    gmail: str = pyload.get("username")
    user_id: int = pyload.get("id")
    try:
        res = db.query(AdminModel).filter(AdminModel.gmail == gmail).first()

        is_super = res.is_superuser
        if res is None:
            raise for_user_exception()

        if is_super == False:
            raise for_user_exception()

        if gmail is None or user_id is None:
            raise get_user_exceptions()
    except AttributeError:
        raise for_user_exception()

    return {"sub": gmail, "user_id": user_id}


