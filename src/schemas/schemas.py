from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    nome: str
    tamanho: str
    preço: float
    quantidade: int
    categoria: str

    

    class Config: # consegui atraves do modelo criar um schema
        from_attributes = True

        