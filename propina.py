print("ingresa el costo de comida")
cosotocomida = int(input("> "))

print("ingresa el porcentaje de propina a pagar")
propina = float(input("> "))

if propina < 0:
    propina *= -1

print("ingrese el total de personas que pagaran")
personas = int(input("> "))

if propina < 0:
    propina *= -1

totalapagar = cosotocomida + ((propina / 100) * cosotocomida)

totalapagarindividual = totalapagar / personas

print(f"cada persona debe pagar: {totalapagarindividual}")

print(f"""
precio total comida : ${totalapagar}
porcentaje de propina : {propina}%
personas para Dividir la cuenta: {personas}
cada uno debe pagar: {totalapagarindividual}
""")
