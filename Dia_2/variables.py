#Dia 2: 30 dias de programacion en Python

nombre = 'Adrian'
apellido = 'Sanchez'
nombre_completo = 'Adrian Sanchez'
pais = 'Ecuador'
ciudad = 'Quito'
edad = 21
año = 2025
is_married = True
is_true = True
is_light_on = True
bienvenida, saludo, conversacion, despedida = 'Bienvenido', 'Hola', 'Como te ha ido?', 'Adios'

type(nombre)
type(apellido)
type(nombre_completo)
type(pais)
type(ciudad)
type(edad)
type(año)
type(is_married)
type(is_true)
type(is_light_on)
type(bienvenida)

len(nombre)

len(apellido)

num_1 = 5
num_2 = 4

total_sum = num_1 + num_2

total_rest = num_2 - num_1

total_mult = num_2 * num_1

total_div = num_1 / num_2

total_modulo = num_2 // num_1

total_potencia = num_1 ** num_2

total_modulo2 = num_1 // num_2

radio = 30
radio_cuadrado = radio * radio
pi = 3.1416
area_de_circulo = pi * radio_cuadrado

circunferencia_de_circulo = 2 * pi * radio

radio_usuario = float(input('Ingrese el valor del radio'))
radio_usuario_cuadrado = radio_usuario * radio_usuario
area_circulo_usuario = pi * radio_usuario_cuadrado
print(f"El area de tu circulo es de: {area_circulo_usuario}")

nombre = input(str('Nombre:'))
apellido = input(str('Apellido'))
pais = input(str('País'))
edad = int(input('Edad'))
print(f'Nombre: {nombre}')
print(f"Apellido: {apellido}")
print(f"País: {pais}")
print(f"Edad: {edad}")
