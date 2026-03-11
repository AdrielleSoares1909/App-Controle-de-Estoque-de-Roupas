

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db,criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto




criar_bd()

app = FastAPI()

@app.post('/produtos')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado



@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.get('/produtos/estoque/{nome}')
def obter_estoque(nome: str, db: Session = Depends(get_db)):
   repositorio = RepositorioProduto(db)
   estoque = repositorio.obter_estoque_por_produto(nome)
   return estoque


@app.delete('/produtos/{nome}/{tamanho}')
def deletar_estoque(nome: str, tamanho: str, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    repositorio.deletar(nome, tamanho)
    return {"Removido "}