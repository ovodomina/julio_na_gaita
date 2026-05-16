import pytest
from src.validador import validar_email, eh_maior_de_idade
def test_validar_email_correto():
    assert validar_email("contato@fatec.edu.br") is True
def test_validar_email_incorreto():
    assert validar_email("email-invalido.com") is False
def test_maioridade_sucesso():
    assert eh_maior_de_idade(20) is True
    assert eh_maior_de_idade(18) is True
def test_menoridade():
    assert eh_maior_de_idade(17) is False
def test_idade_negativa():
    with pytest.raises(ValueError):
        eh_maior_de_idade(-5)
        
# --- TESTES COM ERRO PROPOSITAL PARA QUEBRAR O PYTEST ---
#def test_validar_email_erro_proposital():
    
# Este e-mail não possui '@', mas o assert espera True (Vai quebrar!)
#    assert validar_email("fatec@araras.edu.br") is True
#def test_maioridade_erro_proposital():
    
# 18 anos DEVERIA ser True, mas o assert espera False (Vai quebrar!)
#    assert eh_maior_de_idade(18) is False
