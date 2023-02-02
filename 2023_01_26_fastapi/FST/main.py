from fastapi import FastAPI
from fastapi import HTTPException, Query, Path, Header
from fastapi import status
from models import Aluno
from fastapi import Path
from fastapi import Response, Depends
from typing import Optional, Any
from time import sleep

app = FastAPI(
    title='MoreDevs2Blu',
    version='0.6.7',
    description='Desenvolvido pela turma da história'
)

def db():
    try:
        print('conexao com banco')
        sleep(1)
    finally:
        print('conexao com banco')
        sleep(1)

@app.get('/')
async def raiz():
    return  {"mensagem":"Seja bem vindo ao more devs"}

alunos = {
    1: {"Nome" : "Lirinha", "Idade" : "195", "E-mail" : "lirinha@gmail.com"},
    2: {"Nome" : "João", "Idade" : "15", "E-mail" : "joaosportclub@outlook.com"},
    3: {"Nome" : "Vander", "Idade" : "27", "E-mail" : "fiodovander@microsoft.com"}, 
    4: {"Nome" : "Thiago", "Idade" : "33", "E-mail" : "thiagogta4@hotmail.com"}
}

@app.get('/alunos', description='lista de todos os alunos', summary='retorno substantivo', response_description='Lista alunos cadastrados')
async def get_alunos():
    return alunos

#Informa o último ID consultado
@app.get("/alunos/{aluno_id}", description='Informa aluno pelo ID', summary='retorno individuo', response_description='Aluno cadastrado por ID')
async def get_aluno(aluno_id: int = Path(default=None, title='ID Aluno', description='deve ser entre 1 ou 2', gt=0, lt=3), db :Any =Depends(db)):
    try:
        aluno = alunos[aluno_id]
        return aluno
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado"
        )


@app.post("/alunos", status_code=status.HTTP_201_CREATED, description='Cria novo aluno', summary='retorno individuo', response_description='Aluno criado')
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) + 1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

@app.get("/alunos/{aluno_name}", description='Informa aluno pelo nome', summary='retorno individuo', response_description='Aluno cadastrado por nome')
async def get_aluno_by_name(aluno_name:str):
    for aluno in alunos.values():
        if aluno["Nome"] == aluno_name:
            print(aluno["Nome"])
            return aluno

@app.put("/alunos/{aluno_id}", description='Atualiza aluno na lista de alunos', summary='retorno individuo', response_description='Aluno atualizado')
async def put_aluno (aluno_id:int, aluno:Aluno):
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado"
        )

@app.get("/calc/", description='Efetua cálculos de acordo com a URL de requisição', summary='retorno substantivo', response_description='Resultado do cálculo')
async def calc(valor_um:int = Query(default=None, gt=5), valor_dois:int = Query(default=None, gt=5), xdevs: str = Header(default=None), valor_tres: Optional[int] = None):
    if valor_tres:
        valor_final = valor_um + valor_dois + valor_tres
    else:
        valor_final = valor_um + valor_dois
    print(f'devs: {xdevs}')
    return valor_final
    #raise HTTPException(
    #    status_code = status.HTTP_200_OK, detail=f"Resultado de {valor_um}, {valor_dois} e {valor_tres} é {valor_final}"
    #)

@app.delete("/alunos/{aluno_id}", description='Remove aluno pelo ID', summary='retorno individuo', response_description='Aluno deletado')
async def delete_aluno (aluno_id:int):
    if aluno_id in alunos:
        del alunos[aluno_id]
        raise HTTPException(
            status_code = status.HTTP_200_OK, detail="Aluno deletado com sucesso"
        )

    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado"
        )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True
    )