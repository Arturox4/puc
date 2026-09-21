import crimen as cr

def identificador(altura, pelo, ojos):

    crimen = cr.registro_crimen(altura, pelo)

    if crimen == "INOCENTE":
        print(f"Persona de ojos {ojos} y pelo {pelo}")
    else:
        print(f"ALERTA: es un {crimen}")
        







