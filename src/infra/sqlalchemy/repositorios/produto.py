from sqlalchemy import select 
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models



class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome,tamanho=produto.tamanho,preço=produto.preço,quantidade=produto.quantidade,categoria=produto.categoria)


        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter_estoque_por_produto(self, nome_produto: str):
        stmt = select(models.Produto).filter_by(nome=nome_produto)
        produtos = self.db.execute(stmt).scalars().all()

        estoque = []

        for produto in produtos:
            estoque.append({
                "tamanho": produto.tamanho,
                "quantidade": produto.quantidade
            })

        return {
            "produto": nome_produto,
            "estoque": estoque
        }
    
    def deletar(self, nome_produto: str, tamanho_produto: str):
        stmt = select(models.Produto).filter_by(nome=nome_produto, tamanho = tamanho_produto)
        produto = self.db.execute(stmt).scalars().first()

        if produto:
            self.db.delete(produto)
            self.db.commit()    