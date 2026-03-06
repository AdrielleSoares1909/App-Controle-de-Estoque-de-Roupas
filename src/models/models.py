from sqlalchemy import Column,Integer,String,Float
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):

    __tablename__ = 'produto'

    nome = Column(String)
    tamanho = Column(String)
    preço = Column(Float)
    quantidade = Column(Integer) 
    categoria = Column(String)