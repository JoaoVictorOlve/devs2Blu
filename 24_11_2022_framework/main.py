from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"get": "pegar"}

@app.post("/enviar/")
def read_root():
    return {"Post" : "Enviar"}

@app.get("/items/{id}")
def read_item(id: int, nome: Union[str, None] = None):
    return{"Item_id": id, "nome":nome}

@app.get("/put/")
def read_root():
    return{"Put": "Colocar"}

@app.get("/delete/")
def read_root():
    return{"Delete": "Excluir"}

@app.get("/items/{item_id}/{item_nome}")
def read_item(item_id: int, item_nome: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": item_nome}