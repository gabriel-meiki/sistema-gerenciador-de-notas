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
    
def tudo_funcionando(nota1, nota2):
    this_primeira_nota = nota1

    this_segunda_nota = nota2

    validacao = validar_entradas(this_primeira_nota, this_segunda_nota)

    if(validacao != True):  
        mensagem = "Execute a função com valores positivos maiores que zero e menores ou igual a 10"
        print(mensagem)
        return

    media = calcular_media(this_primeira_nota, this_segunda_nota)

    print(f'Essa é a média {media}')

    situacao = verificar_situacao(media)

    print(situacao)

    return situacao

tudo_funcionando(8, 10)






