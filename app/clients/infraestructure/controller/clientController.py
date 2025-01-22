from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.clients.application.services.createClient import CreateClientService
from app.clients.application.services.getClientById import GetClientByIdService
from app.clients.application.dtos.createClientDto import CreateClientDto
from app.clients.infraestructure.mappers.domain_to_dto import domain_to_dto
from app.clients.infraestructure.repository.clientRepository import ClientRepository
from app.clients.infraestructure.db import database

router = APIRouter(
    tags=["clients"]
)

@router.post("/clients", status_code=status.HTTP_201_CREATED)
async def create_client(client: CreateClientDto, session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_service = CreateClientService(repo)
    try:
        client_aggregate = await client_service.create_client(client)
        client_dto = domain_to_dto(client_aggregate)
        return {"message": "Client created successfully", "client": client_dto}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/clients/{client_id}", status_code=status.HTTP_200_OK)
async def get_client(client_id: str, session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_service = GetClientByIdService(repo)
    try:
        client_aggregate = await client_service.get_client_by_id(client_id)
        client_dto = domain_to_dto(client_aggregate)
        return {"message": "Client found", "client": client_dto}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))