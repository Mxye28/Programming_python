# Una función es un grupo de sentencias con un nombre que realiza una computación
# Primero uno define una función y luego se "llama" o se "ejecuta" la función

# Python viene con muchas funciones listas para usar
# Solo hay que llamarla o ejecutarlas
print("Hola mundo")

# La mayoria de las funciones entregan un valor, es decir la mayoria devuelven
# el resultado. Ejemplo:

str_num = '32' # Esto es un string que parece numero
real_num = int(str_num)
print(type(real_num)) # Esta función transforma a entero
print(type(real_num))

float_num = 3.9999
int_num = int(float_num) # No aproxima, corta la parte decimal
print(int_num)

# La siguiente linea es un error
# int("Hola inmundo")

print(float('32')) # Esta función entrega un float
print(str(3.1415)) # Esta función entrega un str

# Composición de funciones: Anidar funciones

print(str(3.1415))