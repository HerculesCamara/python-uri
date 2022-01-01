dBol = int(input("Diametro da bola"))
vBox = input("Dimencoes da caixa (separe os valores com espacos)")
map(int, vBox.split())

for i in range(len(vBox)):
    a = vBox[i] % dBol
    if (a != 0):
        break
        b = "N"
    else:
        b = "S"

print(b)