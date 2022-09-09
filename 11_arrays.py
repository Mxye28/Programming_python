# Los arreglos (listas) son una estructura de datos fundamental
# Que permite agrupar valores, separados por coma 

first_array = ['Sacar la basura','peinsarse','dormir','Secar la ropa']

# En python el primer elmento de un arreglo tiene posición (indice) 0
print(first_array[0])

print(first_array[1])
print(first_array[2])
print(first_array[3])
# No existe el elemento con índice 4 y python da un error
# print(first_array[4])

# Podemos saber el largo de un arreglo o lista con la función pre definida len()
print(len(first_array))

# Además, podemos agregar elementos al arreglo con el método appende
first_array.append('Comer')
first_array.append('Dormir')

# Podemos indicar la posición del nuevo elemento a agregar insert
first_array.insert(0,'Levantarse')

# Podemos imprimir la lista completa
print(first_array)