from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.deliver.applicaction.services.createDeliver import CreateDeliverService
from app.deliver.applicaction.dtos.createDeliverDto import CreateDeliverDto
from app.deliver.applicaction.dtos.updateDeliverDto import UpdateDeliverDto

from app.clients.application.services.getClientByDni import GetClientByDNIService
from app.deliver.applicaction.services.getDeliverByClientId import GetDeliverByClientIdService
from app.deliver.applicaction.services.getDeliverById import GetDeliverById

from app.deliver.infraestructure.repository.deliverRepository import DeliverRepository
from app.clients.infraestructure.repository.clientRepository import ClientRepository

from app.deliver.infraestructure.mappers.domain_to_dto import domain_to_dto
from app.deliver.infraestructure.db import database

router = APIRouter(
    tags=["Deliver"]
)

@router.post("/deliver", status_code=status.HTTP_201_CREATED)
async def create_deliver(deliver_dto: CreateDeliverDto, session: AsyncSession = Depends(database.get_session)):
    client_repo = ClientRepository(session)
    client_service = GetClientByDNIService(client_repo)
    deliver_repo = DeliverRepository(session)
    deliver_service = CreateDeliverService(deliver_repo)
    print(deliver_dto.agency)
    try:
        client_aggregate = await client_service.get_client_by_dni(deliver_dto.client_dni)
        #return {"message": "Client_aggregate", "deliver": client_aggregate.client.id.get()}
        deliver_aggregate = await deliver_service.create_deliver(deliver_dto, client_aggregate)
        deliver_dto = domain_to_dto(deliver_aggregate)
        return {"message": "Deliver created successfully", "deliver": deliver_dto}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/deliver/all/{client_id}", status_code=status.HTTP_200_OK)
async def get_delivers_by_client_id(client_id: str, session: AsyncSession = Depends(database.get_session)):
    deliver_repo = DeliverRepository(session)
    deliver_service = GetDeliverByClientIdService(deliver_repo)
    deliver_aggregates = await deliver_service.get_deliver_by_client_id(client_id)
    delivers = [domain_to_dto(deliver_aggregate) for deliver_aggregate in deliver_aggregates]
    return {"message": "Delivers found", "delivers": delivers}

@router.get("/deliver/{deliver_id}", status_code=status.HTTP_200_OK)
async def get_deliver_by_id(deliver_id: str, session: AsyncSession = Depends(database.get_session)):
    deliver_repo = DeliverRepository(session)
    deliver_service = GetDeliverById(deliver_repo)
    deliver_aggregate = await deliver_service.get_deliver_by_id(deliver_id)
    deliver = domain_to_dto(deliver_aggregate)
    return {"message": "Deliver found", "deliver": deliver}