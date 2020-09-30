def main():
    # criptorgafar texto:
    # 1º: somente letras maiusculas e minusculas devem se mover 3 posições para a direita (tabela ASCII)
    # 2º: Texto do 1º deve ser invertido
    # 3º: Texto do 2º, da metade em diante, deve se mover 1 casa para a esquerda (tabela ASCII) 

    mensagem = input('Digite um texto: ')

    mensagem_criptografada = criptografia(mensagem)

    print(f'Mensagem encriptada: {mensagem_criptografada}')


def criptografia(mensagem):
    texto_encriptado = ''
    for caractere in mensagem:
        if eh_letra(caractere):
            novo_caractere = mover_direita(caractere)
            texto_encriptado += novo_caractere
        else:
            texto_encriptado += caractere

    return texto_encriptado [::-1]


def mover_direita(c):
    codigo = ord(c)
    
    if eh_letra_maiuscula(c) or eh_letra_minuscula(c):
        novo_codigo = codigo + 3

    novo_caractere = chr(novo_codigo)
    return novo_caractere


def eh_letra_maiuscula(c):
    return ord(c) >= 65 and ord(c) <= 90


def eh_letra_minuscula(c):
    return ord(c) >= 97 and ord(c) <= 122


def eh_letra(c):
    
    if eh_letra_maiuscula(c) or eh_letra_minuscula(c):
        return True
    else:
        return False
 

def mover_metade():
    novo_caractere

main()
