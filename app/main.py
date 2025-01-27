from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.clients.infraestructure.controller.clientController import router as client_router
from app.products.infraestructure.controller.productController import router as product_router
from app.deliver.infraestructure.controller.deliverController import router as deliver_router
from app.common.infraestructure.database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(client_router)
app.include_router(product_router)
app.include_router(deliver_router)

@app.on_event("startup")
async def on_startup():
    await init_db()

app.get("/")
def root():
    return {"message": "Hello World"}