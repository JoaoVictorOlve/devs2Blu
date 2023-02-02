from typing import Optional
from pydantic import BaseModel

class Aluno(BaseModel):
    id : Optional[int] = None
    nome : str
    idade : int
    email : str

alunos = [
    Aluno(id=1, nome="João", idade=17, email="joao@gmail.com"),
    Aluno(id=1, nome="Victor", idade=18, email="victor@gmail.com")
]