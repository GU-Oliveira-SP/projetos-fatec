# Define os caracteres válidos para cada base
digitos_validos = {
    2: '01',
    3: '012',
    4: '0123',
    5: '01234',
    6: '012345',
    7: '0123456',
    8: '01234567',
    9: '012345678',
    10: '0123456789',
    11: '0123456789Aa',
    12: '0123456789ABab',
    13: '0123456789ABCabc',
    14: '0123456789ABCDabcd',
    15: '0123456789ABCDEabcde',
    16: '0123456789ABCDEFabcdef'
}

# Definir a base de entrada
while True :
    try:
        base_entrada = int(input("Digite a base de entrada (2  a 16): "))
        if base_entrada in digitos_validos:
            break
        else:
            print(" \n Base inválida. Por favor, digite um número entre 2 e 16.")
    except ValueError:
        print(" \n Entrada inválida. Por favor, digite um número inteiro entre 2 e 16.")

# Definir número a ser convertido
while True:
        v_num = input("Digite um número inteiro e positivo a ser convertido: ")
        if v_num.startswith('-'):
            print(" \n Por favor, digite um número positivo.")
        elif v_num == '':
            print(" \n Entrada vazia. Por favor, digite um número válido.")
        elif not all(char in digitos_validos[base_entrada] for char in v_num):
            print(f" \n O valor não é válido para a base {base_entrada}. Por favor, digite novamente.")
        else:
            break

# Definir a base de saída
while True:
    try:
        base_saida = int(input("Digite a base de saída (2 a 16): "))
        if base_saida in digitos_validos:
            break
        else:
            print(" \n Base inválida. Por favor, digite um número entre 2 e 16.")
    except ValueError:
        print(" \n Entrada inválida. Por favor, digite um número inteiro entre 2 e 16.")

# Conversão para base decimal
def para_dec(v_num, base_entrada):
    decimal = 0
    casas_num = len(v_num) # Conta o número de dígitos
    for posicao, digito in enumerate(v_num): # Percorre cada dígito
        if digito.isdigit(): 
            valor = int(digito) # Se for dígito numérico Converte para inteiro
        else:
            valor = ord(digito.upper()) - ord('A') + 10 # Converte letras A-F para valores 10-15
        decimal += valor * (base_entrada ** (casas_num - posicao - 1)) 
    return decimal

# Conversão de decimal para outra base
def de_decimal(v_num, base_saida):
    if v_num == 0:
        return "0"
    convertido = ""
    while v_num > 0: # Enquanto o número for maior que zero
        resto = v_num % base_saida # Calcula o resto da divisão
        if resto < 10:
            convertido = str(resto) + convertido # Concatena o dígito ao resultado
        else:
            convertido = chr(ord('A') + resto - 10) + convertido # Concatena letras A-F
        v_num //= base_saida # Atualiza o número dividindo pela base
    return convertido

# Lógica principal
if base_entrada == 10:
    resultado = de_decimal(int(v_num), base_saida) # Converte de decimal para a base desejada
elif base_saida == 10:
    resultado = para_dec(v_num, base_entrada) # Converte da base de entrada para decimal
else:
    decimal_intermediario = para_dec(v_num, base_entrada) # Converte para decimal primeiro
    resultado = de_decimal(decimal_intermediario, base_saida) # Depois converte para a base desejada

# Exibir o resultado
print(f" \n O número {v_num} na base {base_entrada} é: \n {resultado} na base {base_saida}.")



