def read_file(file_name):
    file = open("file_handling/" + file_name, "r", encoding="UTF-8")
    for line in file:
        print(line)
print("1 Boolean\n")
print("2 Microsystem\n")
print("3 Google\n")
user_option = input("Selecciona cuál es tu empresa\n")
if user_option == "1":
    read_file("boolean.txt")
elif user_option == "2":
    read_file("microsystem.txt")
elif user_option == "3":
    read_file("google.txt")
else:
    print("opción incorrecta")