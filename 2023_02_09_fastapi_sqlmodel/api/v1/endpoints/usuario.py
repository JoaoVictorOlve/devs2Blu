from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.usuario_model import UsuarioModel
from core.dep import get_session

from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()

@router.get('/', response_model=List[UsuarioModel])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)

        result= await session.execute(query)

        usuarios: List[UsuarioModel]= result.scalars().all()

        return usuarios

@router.get('/{usuario_id}', status_code=status.HTTP_200_OK, response_model=UsuarioModel)
async def get_usuario(usuario_id : int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result= await session.execute(query)
        usuario : UsuarioModel = result.scalar_one_or_none()

        if usuario:
            return usuario
        else:
            raise HTTPException(detail='Usuário nao encontrado', status_code=status.HTTP_404_NOT_FOUND)
