# builtin

# external
from fastapi import APIRouter, Request

# internal
from src.api.classification.io import ClassificationClassifyBookOutput, ClassificationClassifyBookInput
from src.modules.classifier import ClassifierModule

classification_router: APIRouter = APIRouter(prefix="/classification", tags=["classification"])



@classification_router.post("/classify-book", response_model=ClassificationClassifyBookOutput)
async def classify_book(input: ClassificationClassifyBookInput, request: Request) -> ClassificationClassifyBookOutput:
    classifier_module: ClassifierModule = request.app.state.classifier_module
    response_model: ClassificationClassifyBookOutput = await classifier_module.classify_book(book_image=input.image_path)
    return response_model