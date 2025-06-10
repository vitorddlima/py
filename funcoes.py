def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email Válido'
    else:
        return 'email incorreto'
    
def validar_senha(senha):
    caractere = '@#$%&'
    if len(senha) >8 and\
        any(c.isdigit() for c in senha)and\
        any(c.isupper() for c in senha)and\
        any(c in caractere for c in senha):
            return 'senha cadastrada'
    else:
        return 'senha não contem'
    
def calcular_media(lista_numero):
    if not lista_numeros:
        return 0
    total=0
    
    for num in lista_numero:
        total +=num
        media = total /len(lista_numeros)
        return media
    
def verificar_maior_idade(idade):
    if idade <=18:
        return True
    else:
        return False

def eh_positivo(num):
    if num >=0:
        return 'positivo'
    else:
        return 'negativo'

def status_aluno(nota):
    if nota < 3:
        return 'reprovado'
    elif nota < 7:
        return 'recuperação'
    else:
        return 'aprovado'
        