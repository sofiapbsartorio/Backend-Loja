from pydantic import BaseModel, field_validator

from util.validators import *


class InserirProdutoDto(BaseModel):
    nome: str
    preco: float    
    descricao: str
    estoque: int

    @field_validator("nome")
    def validar_nome(cls, v):
        msg = is_size_between(v, "Nome", 2, 128)
        if msg: raise ValueError(msg)
        return v

    @field_validator("preco")
    def validar_preco(cls, v):
        msg = is_in_range(v, "Preço", 0.0, 100000.0)
        if msg: raise ValueError(msg)
        return v

    @field_validator("descricao")
    def validar_descricao(cls, v):
        msg = is_not_empty(v, "Descrição")
        msg = msg or is_size_between(v, "Descrição", 16, 1024)
        if msg: raise ValueError(msg)
        return v

    @field_validator("estoque")
    def validar_estoque(cls, v):
        msg = is_in_range(v, "Estoque", 0, 1000)
        if msg: raise ValueError(msg)
        return v