from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return  {"mensagem":"Seja bem vindo ao more devs"}

alunos = {
    1: "Lirinha1",
    2: "Lirinha2",
    3: "Lirinha3", 
    4: "Lirinha4"
}

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get("/alunos/{aluno_id}/")
async def pegaAlunoId(aluno_id:int):
    return alunos[aluno_id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True
    )