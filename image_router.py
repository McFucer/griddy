from fastapi import Depends, HTTPException, APIRouter, UploadFile, File
import os
import uuid
import shutil

from db import get_db
from models import Comment_Image, Comment, User

router = APIRouter()

@router.post('/sw')
async def post_image(image: UploadFile = File(...)):
    # Создаем уникальное имя файла с помощью модуля uuid
    unique_filename = str(uuid.uuid4())
    file_extension = os.path.splitext(image.filename)[-1].lower()  # Получаем расширение файла
    saved_filename = unique_filename + file_extension

    # Сохраняем файл в директорию
    save_directory = 'C:\Users\usera\Image_SAVER'
    file_path = os.path.join(save_directory, saved_filename)
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Сохраняем информацию о файле в базе данных
    db_comment = Comment(comment="New Comment")
    db_image_comment = Comment_Image(file_name=saved_filename, file_path=file_path)
    db_comment.image_comments.append(db_image_comment)
    db = next(get_db())
    db.add(db_comment)
    db.commit()
    db.refresh(db_image_comment)

    return {'file_name': saved_filename}