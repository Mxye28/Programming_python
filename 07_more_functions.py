# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def" y el cuerpo 
# La función debe ir indentado (sangrado)

def chuchuwa(inst):
    print("chuchuwa chuchuwa chuchuwa wa wa")
    print("chuchuwa chuchuwa chuchuwa wa wa")
    print("Atención!, Compañia")
    print(inst)

print(chuchuwa)
print(type(chuchuwa))

# El llamado de la función

chuchuwa("Mano hacia el frente")
chuchuwa("Hombro hacia atrás")

# Las funciones deben llamarse o ejecutarse con los mismo parametros que se definió
chuchuwa("lengua afuera")
