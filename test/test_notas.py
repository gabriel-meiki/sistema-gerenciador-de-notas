import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './')))

from notas import calcular_media, verificar_situacao, validar_entradas


def test_calcular_media():
    """Testa o cálculo de média"""

    # Preparar
    nota1 = 10
    nota2 = 8

    # Agir
    resultado = calcular_media(nota1, nota2)

    # Verificar
    assert resultado == 9.0

def test_verificar_situacao():
    """Testa a verificação da situação da média do estudante"""

    # Preparar
    media_final = 7

    # Agir
    resultado = verificar_situacao(media_final)

    # Verificar
    assert resultado == "Estudante aprovado"

def test_validar_entradas():
    """Testa a validação das entradas de valores para se ter a média"""

    # Preparar
    primeira_nota = -7
    segunda_nota = 11

    # Agir
    resultado = validar_entradas(primeira_nota, segunda_nota)

    # Verificar
    assert resultado == False
    


# Comando para executar o código de teste pelo terminal
# Precisa baixar o pytest
# Não precisa baixar os, sys, porque já vem baixado no python


### python -m pytest -v
