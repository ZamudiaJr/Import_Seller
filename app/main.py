from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.clients.infraestructure.controller.clientController import router as client_router
from app.clients.infraestructure.db.database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(client_router)

@app.on_event("startup")
async def on_startup():
    await init_db()

app.get("/")
def root():
    return {"message": "Hello World"}