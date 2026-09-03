import combate_pokemon

pokemon1 = input()
vida1 = int(input())
atk1 = int(input())
def1  = int(input())

pokemon2 = input()
vida2 = int(input())
atk2 = int(input())
def2  = int(input())

tipo_pokemon1 = combate_pokemon.obtener_tipo_pokemon(pokemon1)
tipo_pokemon2 = combate_pokemon.obtener_tipo_pokemon(pokemon2)

turno1 = combate_pokemon.quien_parte(pokemon1, pokemon2)

print(f"Comienza el combate entre {pokemon1} de tipo {tipo_pokemon1} y {pokemon2} de tipo {tipo_pokemon2}")



    
if turno1 == pokemon2:
    pokemon1, pokemon2 = pokemon2, pokemon1
    vida1, vida2 = vida2, vida1
    atk1, atk2 = atk2, atk1
    def1, def2 = def2, def1
    tipo_pokemon1, tipo_pokemon2 = tipo_pokemon2, tipo_pokemon1








while vida1 > 0 and vida2 > 0:
    daño = combate_pokemon.calcular_dmg(atk1, tipo_pokemon1, def2, tipo_pokemon2)

    if daño >= vida2:
        daño = vida2
        ganador = pokemon1
        perdedor = pokemon2
        
    vida2 -= daño
    print(f"{pokemon1} ha atacado a {pokemon2} provocando {daño} puntos de damage")
    daño = 0

    if vida1 <= 0 or vida2 <= 0:
        break


    daño = combate_pokemon.calcular_dmg(atk2, tipo_pokemon2, def1, tipo_pokemon1)
    if daño >= vida1:
        daño = vida1
        ganador = pokemon2
        perdedor = pokemon1
    vida1 -= daño
    print(f"{pokemon2} ha atacado a {pokemon1} provocando {daño} puntos de damage")
    daño = 0


print(f"{perdedor} no puede continuar...")
combate_pokemon.mostrar_ganador(ganador)