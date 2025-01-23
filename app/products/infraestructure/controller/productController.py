from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.products.infraestructure.db import database
from app.products.application.dtos.createProductDto import CreateProductDto
from app.products.application.dtos.updateProductDto import UpdateProductDto
from app.products.application.services.createProduct import CreateProductService
from app.products.infraestructure.repository.productRepository import ProductRepository
from app.products.infraestructure.mappers.domain_to_dto import domain_to_dto

router = APIRouter(
    tags=["Products"]
)

@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product_dto: CreateProductDto, session: AsyncSession = Depends(database.get_session)):
    repo = ProductRepository(session)
    product_service = CreateProductService(repo) 
    try:
        product_aggregate = await product_service.create_product(product_dto)
        product_dto = domain_to_dto(product_aggregate)
        return {"message": "Product created successfully", "product": product_dto}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))