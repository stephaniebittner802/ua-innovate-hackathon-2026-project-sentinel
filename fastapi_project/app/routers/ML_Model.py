from fastapi import APIRouter, Depends, status, HTTPException, Form
from sqlmodel import Session, select
from app.services.database.session import get_session

from app.services.ml_model_service import time_to_zero

router = APIRouter(prefix="/time-to-zero", tags=["time-to-zero"])

@router.get("/", response_model=float, status_code=status.HTTP_201_CREATED)
def getTimetoZero(location: str, resource: str, session: Session = Depends(get_session)):
    hours = time_to_zero(resource_type=resource,location=location, session=session)

    return hours