# builtin

# external
from openai import AsyncOpenAI

# internal
from src.models.book import BookInfo


class ClassifierModule:
    def __init__(self, openai_client: AsyncOpenAI):
        self.openai_client = openai_client

    async def pass_book(self, book_image: str) -> BookInfo:
        response = await self.openai_client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Give me information about the book in this picture, if part of the title seems to be missing, use your intuition from other knowledge of the book to fill in the gap but do not make giant leeps if you find yourself guessing too much fill things with unknown instead, if you see no book fill all output entries with unknown"},
                        {"type": "image_url", "image_url": {"url": book_image}},
                    ],
                }
            ],
            response_format=BookInfo,
            max_tokens=300,
        )
        return response.choices[0].message.parsed
                