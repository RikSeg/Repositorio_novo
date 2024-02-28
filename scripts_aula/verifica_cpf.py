def validar_cpf(cpf):
    # Removendo caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma * 10) % 11
    if digito_1 == 10:
        digito_1 = 0

    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma * 10) % 11
    if digito_2 == 10:
        digito_2 = 0

    # Verificando se os dígitos calculados são iguais aos dígitos informados
    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        return True
    else:
        return False

# Exemplo de uso
cpf = input("Digite o CPF (somente números): ")
if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
