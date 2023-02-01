from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Aluno
from fastapi import Path
from fastapi import Response

app = FastAPI()

@app.get('/')
async def raiz():
    return  {"mensagem":"Seja bem vindo ao more devs"}

alunos = {
    1: {"Nome" : "Lirinha", "Idade" : "195", "E-mail" : "lirinha@gmail.com"},
    2: {"Nome" : "João", "Idade" : "15", "E-mail" : "joaosportclub@outlook.com"},
    3: {"Nome" : "Vander", "Idade" : "27", "E-mail" : "fiodovander@microsoft.com"}, 
    4: {"Nome" : "Thiago", "Idade" : "33", "E-mail" : "thiagogta4@hotmail.com"}
}

@app.get('/alunos')
async def get_alunos():
    return alunos

#Informa o último ID consultado
@app.get("/alunos/{aluno_id}")
async def get_aluno(aluno_id:int):
    try:
        aluno = alunos[aluno_id]
        alunos.update({"id" : aluno_id})
        return aluno
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado"
        )

@app.post("/alunos", status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) + 1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

@app.get("/alunos/{aluno_name}")
async def get_aluno_by_name(aluno_name:str):
    for aluno in alunos.values():
        if aluno["Nome"] == aluno_name:
            print(aluno["Nome"])
            return aluno

@app.put("/alunos/{aluno_id}")
async def put_aluno (aluno_id:int, aluno:Aluno):
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado"
        )

@app.get("/calc/")
async def calc (valor_um:int = 0 , valor_dois:int = 0, valor_tres:int = 0):
    valor_final = valor_um + valor_dois + valor_tres
    raise HTTPException(
        status_code = status.HTTP_200_OK, detail=f"Resultado de {valor_um}, {valor_dois} e {valor_tres} é {valor_final}"
    )

@app.delete("/alunos/{aluno_id}")
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