from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.clients.application.services.createClient import CreateClientService
from app.clients.application.services.getClientById import GetClientByIdService
from app.clients.application.services.getClientByDni import GetClientByDNIService
from app.clients.application.services.deleteClient import DeleteClientService
from app.clients.application.services.getClients import GetClientsService
from app.clients.application.services.updateClient import UpdateClientService
from app.clients.application.dtos.createClientDto import CreateClientDto
from app.clients.application.dtos.updateClientDto import UpdateClientDto
from app.clients.infraestructure.mappers.domain_to_dto import domain_to_dto
from app.clients.infraestructure.repository.clientRepository import ClientRepository
from app.clients.infraestructure.db import database

router = APIRouter(
    tags=["Clients"]
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
async def get_client_by_id(client_id: str, session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_service = GetClientByIdService(repo)
    try:
        client_aggregate = await client_service.get_client_by_id(client_id)
        client_dto = domain_to_dto(client_aggregate)
        return {"message": "Client found", "client": client_dto}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/clients/dni/{client_dni}", status_code=status.HTTP_200_OK)
async def get_client_by_dni(client_dni: str, session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_service = GetClientByDNIService(repo)
    try:
        client_aggregate = await client_service.get_client_by_dni(client_dni)
        client_dto = domain_to_dto(client_aggregate)
        return {"message": "Client found", "client": client_dto}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/clients/delete/{client_id}", status_code=status.HTTP_200_OK)
async def delete_client(client_id: str, session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_service = DeleteClientService(repo)
    try:
        await client_service.delete_client(client_id)
        return {"message": "Client deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/clients/all/created/db", status_code=status.HTTP_200_OK)
async def get_clients(session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_services = GetClientsService(repo)
    clients_aggregates = await client_services.get_clients()
    clients = [domain_to_dto(client) for client in clients_aggregates]
    return {"message": "Clients found", "clients": clients}

@router.patch("/clients/update/{client_id}", status_code=status.HTTP_200_OK)
async def update_client(client_id: str, client: UpdateClientDto, session: AsyncSession = Depends(database.get_session)):
    repo = ClientRepository(session)
    client_service = UpdateClientService(repo)
    try:
        success = await client_service.update_client(client_id, client)
        if success:
            return {"message": "Client updated successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))