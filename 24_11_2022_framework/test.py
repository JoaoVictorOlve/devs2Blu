from typing import Union 
from fastapi import FastAPI

app = FastAPI()

@app.get("/pegar/")
def read_root():
    return{"Get":"Pegar"}

@app.post("/enviar/")
def read_root():
    return{"Post":"Enviar"}

@app.put("/items/{itm_id}")
def reat_item(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q": q}

@app.put("/put/")
def read_root():
    return{"Put": "Colocar"}

@app.delete("/delete/")
def read_root():
    return{"Delete": "Excluir"}
