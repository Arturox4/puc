import evento as ev

def dcchupalla(hora, actividad):
    if actividad == "comida":
        return ev.cantidad_comida(hora)

    if actividad == "baile":
        return ev.cancion(hora)

qty_eventos = int(input())

for i in range(qty_eventos):
    hora = int(input())
    actividad = input()
    
    if actividad == "comida":
        for i in range(dcchupalla(hora, actividad)):
            print(f"Que rico mi {i+1} pedazo!")

    if actividad == "baile":
        print(f"A bailar una cuequita con", dcchupalla(hora, actividad))

    if actividad == "foto": 
        print(f"Me saque una foto a las {hora}")

