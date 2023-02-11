from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.professor_model import ProfessorModel
from core.dep import get_session

from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()

@router.get('/', response_model=List[ProfessorModel])
async def get_professores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel)

        result= await session.execute(query)

        professores: List[ProfessorModel]= result.scalars().all()

        return professores