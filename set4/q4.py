import pikachu

oscuridad = pikachu.percibir_oscuridad()

print(f"Pika-pika-pika (La oscuridad inicial de la cueva es de {oscuridad} )")

if oscuridad_inicial >= 95:
    print(f"Pi-ka-chu... (Es demasiado oscuro para avanzar - Nivel de oscuridad: {oscuridad} )")

print("Pikachu revisemos si podemos entrar al tunel...")

if pikachu.avanzar() == False:
    valor_a_restar = pikachu.usar_destello(oscuridad)

    
