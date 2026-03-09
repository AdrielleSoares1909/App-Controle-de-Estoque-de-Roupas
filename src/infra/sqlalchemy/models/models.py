"""

    Sistema de Controle de Estoque para Loja de Roupas


    Funcionalidades obrigatórias:

    ✅ Cadastrar peça

        -nome?

        -tamanho?

        -preço?

        -quantidade?

        -categoria? (blusa, calça, vestido…)

    ✅ Listar peças

    ✅ Atualizar quantidade por tamanho da peça

    ✅ Deletar peça

    ✅ Controlar quantidade/estoque baixo

    Arquitetura e Ferramentas:

    * Python + FastAPI(pydantic)
    * Sera uma API REST
    * Banco de Dados: Postgres e/ou MongoDB
    * Docker para Postgres
    * MVC
    * Domain Drive Design e Arquitetura Limpa(Clear ARCH.)

"""



from sqlalchemy import Column,Integer,String,Float
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):

    __tablename__ = "produto"

        
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tamanho = Column(String)
    preço = Column(Float)
    quantidade = Column(Integer) 
    categoria = Column(String)

    