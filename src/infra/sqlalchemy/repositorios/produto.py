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
    
    
    def atualizar(self):
        pass

    def quantidade(self):
        pass

    def deletar(self):
        pass     