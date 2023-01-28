from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Aluno

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
    return aluno

# @app.get("/alunos/{aluno_name}")
# async def get_aluno_by_name(aluno_name:str):
#     try:
#         for aluno in alunos.values():
#             if aluno["Nome"] == aluno_name:
#                 print(aluno["Nome"])
#                 return aluno

#     except KeyError:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado"
#         )




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True
    )