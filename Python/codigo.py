# função que recebe o valor da velocidade do vento e retorna a classficação na escala de Beaufort

def beaufort(velocidade):
    if velocidade < 1:
        return "Calmaria"
    elif velocidade < 6:
        return "Brisa"
    elif velocidade < 12:
        return "Ventania"
    elif velocidade < 20:
        return "Vendaval"
    elif velocidade < 29:
        return "Temporal"
    elif velocidade < 39:
        return "Furacão"
    elif velocidade < 50:
        return "Tufão"
    else:
        return "Super Tufão"
    
# Teste
print(beaufort(0)) # Calmaria
print(beaufort(5)) # Brisa
print(beaufort(10)) # Ventania
print(beaufort(15)) # Vendaval
print(beaufort(25)) # Temporal
print(beaufort(35)) # Furacão
print(beaufort(45)) # Tufão
print(beaufort(55)) # Super Tufão
