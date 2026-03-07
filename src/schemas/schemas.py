from fastapi import FastAPI
from pydantic import BaseModel



class Produto(BaseModel):
    nome: str
    tamanho: int
    preco: float
    quantidade: int
    categoria: str