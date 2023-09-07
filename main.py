from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from db import Base, engine
from user_router import router as user_router
from comment_router import router as comment_router
from image_router import router as image_router


app = FastAPI()
app.include_router(comment_router,tags=['Comment'])
app.include_router(user_router,tags=['User'])
app.include_router(image_router,tags=['Image'])

Base.metadata.create_all(engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

