#builtin
from contextlib import asynccontextmanager

#external
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import AsyncOpenAI

#internal
from src.globals.environment import Environment
from src.modules.classifier import ClassifierModule
from src.api.classification.routes import classification_router

def setup_clients(app: FastAPI):
    environment: Environment = app.state.environment
    open_AI_client = AsyncOpenAI(api_key=environment.OPENAPI_KEY)
    app.state.open_AI_client = open_AI_client

def setup_globals(app: FastAPI):
    environment: Environment = Environment()
    app.state.environment = environment

def setup_modules(app: FastAPI):
    classifier_module: ClassifierModule = ClassifierModule(openai_client=app.state.open_AI_client)
    app.state.classifier_module = classifier_module

    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup
    setup_globals(app=app)
    setup_clients(app=app)
    setup_modules(app=app)
    yield
    # teardown


app: FastAPI = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(classification_router)