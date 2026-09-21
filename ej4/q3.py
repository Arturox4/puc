def empanada(amasar, relleno):
    
    for i in range(min(amasar, 5)):
        print("Amasandooo!!!")
    calidad = str("Regular")

    if amasar > 5:
        amasar = amasar - 5
        calidad = str("Super")
        for i in range(amasar):
            print("Amasando cansadooo...")


    if relleno == "pino":
        print(f"{calidad} empanada tipica")
    else:
        print(f"{calidad} empanada de {relleno}")
    

amasar = int(input())
relleno = input()

empanada(amasar, relleno)