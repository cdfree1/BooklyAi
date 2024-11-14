# builtin

# external
from pydantic import BaseModel

# internal

class ClassificationClassifyBookInput(BaseModel):
    image_path: str

class ClassificationClassifyBookOutput(BaseModel):
    book_title: str
    book_genre: str
    book_author: str
    book_description: str

