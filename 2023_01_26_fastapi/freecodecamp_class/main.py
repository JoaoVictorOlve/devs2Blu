from fastapi import FastAPI
from fastapi import HTTPException, Query, Path, Header
from fastapi import status
from models import Aluno, alunos
from fastapi import Path
from fastapi import Response, Depends
from typing import Optional, Any
from time import sleep


@app.get("/")
def root():
    return {"Message" : "Hello"}

