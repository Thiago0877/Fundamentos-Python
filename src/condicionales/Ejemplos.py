#Declaración if en Python
'''
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
    
    temperatura = 30
if temperatura > 25:
    print("Hace calor hoy.")
    
    hora = 10
if hora >= 6 and hora < 12:
    print("Buenos días.")

#Declaración if-else en Python

edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")
    
    contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")
    
    numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
    saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")
    '''
#Declaración if-elif-else en Python

numero = 0

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    
    nota = 87

if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")

    edad = 45

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")
    
    color = "azul"

if color == "rojo":
    print("El color es rojo.")
elif color == "verde":
    print("El color es verde.")
elif color == "azul":
    print("El color es azul.")