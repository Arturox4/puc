# modulo hecho por los ayudantes para la q5

pokemons = {
    'Bulbasaur': 'Planta',
    'Ivysaur': 'Planta',
    'Venusaur': 'Planta',
    'Charmander': 'Fuego',
    'Charmeleon': 'Fuego',
    'Charizard': 'Fuego',
    'Squirtle': 'Agua',
    'Wartortle': 'Agua',
    'Blastoise': 'Agua'
}


# TODO: Revisar siempre los inputs de las funciones
# (son alumnos, preparate para un 'xd' de input)
def mostrar_ganador(winner):
    print('-----------------------')
    print('y el ganador es.....')
    print(f'** {winner:16.16s}! **')
    print('-----------------------')

# perdon por print tan feo, la imaginacion con pokemons no llego uwu


def obtener_tipo_pokemon(poke_name):
    if poke_name in pokemons:
        return pokemons[poke_name]

    return 'El nombre del pokemon ingresado no existe'


def calcular_dmg(poke1_atk, poke1_type, poke2_def, poke2_type):
    dmg = poke1_atk - round(0.2 * poke2_def)
    if dmg < 0:
        dmg = 0

    if poke1_type == 'Fuego' and poke2_type == 'Agua':
        return int((dmg * 0.3) // 1)

    elif poke1_type == 'Fuego' and poke2_type == 'Planta':
        return int((dmg * 2) // 1)

    elif poke1_type == 'Fuego' and poke2_type == 'Fuego':
        return int((dmg * 0.5) // 1)

    elif poke1_type == 'Planta' and poke2_type == 'Fuego':
        return int((dmg * 0.3) // 1)

    elif poke1_type == 'Planta' and poke2_type == 'Agua':
        return int((dmg * 2) // 1)

    elif poke1_type == 'Planta' and poke2_type == 'Planta':
        return int((dmg * 0.5) // 1)

    elif poke1_type == 'Agua' and poke2_type == 'Planta':
        return int((dmg * 0.3) // 1)

    elif poke1_type == 'Agua' and poke2_type == 'Fuego':
        return int((dmg * 2) // 1)

    elif poke1_type == 'Agua' and poke2_type == 'Agua':
        return int((dmg * 0.5) // 1)

    return 'Alguno de los tipos de pokemon ingresados no existe'


def quien_parte(poke1_name, poke2_name):
    return sorted([poke1_name, poke2_name])[1]