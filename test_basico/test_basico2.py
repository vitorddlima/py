def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email Válido'
    else:
        return 'email incorreto'
     
def text_verificar_email():
    assert verifica_email('vitordranka@gmail.com') =='email Válido'
    assert verifica_email('vitordranka@gmail') =='email incorreto'
    assert verifica_email('vitordranka.com') == 'email incorreto'
    assert verifica_email('vitordranka@outlook.com') == 'email Válido'
