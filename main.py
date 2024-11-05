# Pedir al usuario que ingrese 5 voltajes
voltaje1 = float(input("indroduce el primer voltaje: "))  # Primera voltaje
voltaje2 = float(input("introduce el primer voltaje: "))  # Segunda voltaje
voltaje3 = float(input("introduce el tercer voltaje: "))   # Tercera voltaje
voltaje4 = float(input("introduce el cuarto voltaje: "))    # Cuarta voltaje
voltaje5 = float(input("introduce el quinto voltaje: "))     # Quinto voltaje

# Calcular el promedio
promedio = (voltaje1 + voltaje2 + voltaje3 + voltaje4 + voltaje5) / 5  # Sumar las notas y dividir entre 5

# Verificar el promedio del voltaje

if promedio  >= 220:
    print("Alto voltaje")
else:
    print("Voltaje Correcto")