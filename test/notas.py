def calcular_media(primeira_nota, segunda_nota):
    return (primeira_nota + segunda_nota)/2

def verificar_situacao(media_final):
    if (media_final >= 7):
        return "Estudante aprovado"
    elif (media_final >= 5):
        return "Estudante de recuperação"
    else:
        return "Estudante reprovado"
    
def validar_entradas(primeira_nota, segunda_nota):
    if (primeira_nota < 0 or segunda_nota < 0):
        return False
    elif (primeira_nota > 10 or segunda_nota > 10):
        return False
    else:
        return True
    
# def tudoFuncionando():
#     nota1 = float(input("Digite a primeira nota: "))

#     nota2 = float(input("Digite a segunda nota: "))

#     validacao = validar_entradas(nota1, nota2)

#     while(validacao == False):
#         nota1 = float(input("Digite a primeira nota: "))

#         nota2 = float(input("Digite a segunda nota: "))

#         validacao = validar_entradas(nota1, nota2)



#     media = calcular_media(nota1, nota2)

#     print(f'Essa é a média {media}')

#     situacao = verificar_situacao(media)

#     print(situacao)

# tudoFuncionando()






