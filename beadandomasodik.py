lista = []
file = open("be.txt", "r")
for i in file:
    lista.append(i.strip("\n"))
    for i in range(len(lista)):
        try:
            exec(lista[i])
            print("True")
        except:
            print("False")
file.close()
