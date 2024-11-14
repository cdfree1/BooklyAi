# builtin

# extern
from pydantic import BaseModel

# internal

class BookInfo(BaseModel):
    book_title: str
    book_genre: str
    book_author: str
    book_description: str