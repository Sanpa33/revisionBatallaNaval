from typing import Any
from biblioteca import *

## EJERCICIO 1

def tamaños_barcos_en_grilla(barcos: list[BarcoEnGrilla]) -> list[Barco]:

    """
    Toma los barcos en la grilla y devuelve una lista con sus respectivos tamaños.

    PRE: True
    Args:
        barcos (list[BarcoEnGrilla]): Barcos ubicados en la grilla.
    Returns:
        list[int]: Una lista donde cada elemento es el tamaño correspondiente a cada barco en la grilla.
    """

    tamañosPorAhora: list[int] = []

    for barcoActual in barcos:
        tamañosPorAhora.append(tamañoDelBarco(barcoActual))

    return tamañosPorAhora


def tamañoDelBarco(barco: BarcoEnGrilla) -> Barco: 

    """
    Devuelve el tamaño de un barco

    PRE: True
    Args:
        barco (BarcoEnGrilla): Barco a medir
    Returns:
        Barco: El tamaño del barco 
    """        


    tamañoPorAhora: int = 0

    for posicionActual in barco:
        tamañoPorAhora += 1
            
    return tamañoPorAhora


def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    
    """
    Calcula la cantidad de barcos de un tamaño específico.

    PRE: barcos son barcos válidos
    Args:
        barcos (list[BarcoEnGrilla]): Barcos en la grilla
        tamaño (int): El tamaño buscado
    Returns:
        int: La cantidad de barcos que tienen el tamaño deseado.
    """
    cantidadDeBarcosPorAhora:int = 0


    for barcoActual in barcos:
        cantidadDeBarcosPorAhora += unoSiCeroSiNo(tamañoDelBarco(barcoActual) == tamaño)


    return cantidadDeBarcosPorAhora


## EJERCICIO 2

def grillaVacía(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla: 

    """
    Crea una grilla vacía del tamaño que se le pasa.

    PRE: True
    Args:
        cantidadDeFilas (int): Número de filas de la grilla a crear.
        cantidadDeColumnas (int): Número de columnas de la grilla a crear
    Returns:
        Grilla: La grilla vacía.
    """

    grillaPorAhora: Grilla = []

    for i in range (cantidadDeFilas):

        grillaPorAhora.append([VACÍO] * cantidadDeColumnas)
    
    return grillaPorAhora


def tableroInicial(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:

    """
    Genera un nuevo tablero para un jugador, compuesto por dos grillas vacías
    
    PRE: True
    Args:
        cantidadDeFilas (int): El número de filas del tablero
        cantidadDeColumnas (int): El número de columnas del tablero
    Returns:
        Tablero: El tablero de uno de los jugadores
    """

    return (grillaVacía(cantidadDeFilas, cantidadDeColumnas), grillaVacía(cantidadDeFilas, cantidadDeColumnas))


def nuevoJuego(cantidadDeFilas: int, cantidadDeColumnas: int, barcosDisponibles: list[Barco]) -> EstadoJuego:
        
    """
    Crea e inicializa un nuevo estado de juego (EstadoJuego)
    Define las dimensiones, los barcos disponibles, los tableros vacíos 
    para ambos jugadores y asigna el turno inicial al Jugador UNO

    PRE: True
    Args:
        cantidadDeFilas (int): El número de filas del tablero.
        cantidadDeColumnas (int): El número de columnas del tablero.
        barcosDisponibles (list[Barco]): La cantidad de barcos que tengo (cada uno, representado por su respectivo tamaño)
    Returns:
        EstadoJuego: El estado inicial del juego: (dimensiones, barcos, turno, tablero_jugador, tablero_oponente).
    """
    
    return ((cantidadDeFilas, cantidadDeColumnas), barcosDisponibles,[UNO], tableroInicial(cantidadDeFilas, cantidadDeColumnas), tableroInicial(cantidadDeFilas, cantidadDeColumnas))


## EJERCICIO 3

def dimension_valida(dimension_tablero: tuple[int, int]) -> bool:

    """
    Verifica si las dimensiones de un tablero son válidas

    PRE: True
    Args:
        dimension_tablero (tuple[int, int]): Las dimensiones (filas, columnas) a validar
    Returns:
        bool: True si las dimensiones son válidas, False en caso contrario
    """

    return (0 < dimension_tablero[0] <= 26)  and (dimension_tablero[1] > 0)


def grilla_valida_en_juego(grilla: Grilla, dimension: tuple[int, int]) -> bool:

    """
    Comprueba si una grilla existente coincide con las dimensiones de juego 
    esperadas.

    PRE: True
    Args:
        grilla (Grilla): La grilla a comprobar si es valida.
        dimension (tuple[int, int]): Las dimensiones del juego
    Returns:
        bool: True si las dimensiones de la grilla coinciden con las dimensiones esperadas, False en caso contrario.
    """

    if not esMatrizVálida(grilla):

        return False

    if len(grilla) == 0:
         # Si está vacía, sus dimensiones son (0, 0)
         # Ojo que es importante este caso, sino cuando se haga mas abajo esto ancho_real = len(grilla[0])  # Python intenta buscar el elemento 0 de una lista vacía.
         return dimension == (0, 0)
    

    return (len(grilla), len(grilla[0])) == dimension

# HASTA ACA FUNCIONA EL CODIGO


def indice_del_minimo_entre(lista:list[int], inicio:int) -> int:
    
    """
    Busca el indice del numero más chico de la lista

    PRE: True
    Args: 
        lista (list[int]): La lista de enteros a ordenar.
        inicio (int): Desde qué posicion de la lista busca 
    Returns: 
        int: El indice del menor número de la lista
   
    """
    índiceDelMínimoPorAhora = inicio
    for j in range(inicio + 1, len(lista)):
        if lista[j] < lista[índiceDelMínimoPorAhora]:
            índiceDelMínimoPorAhora = j
    return índiceDelMínimoPorAhora  


def intercambiar_dos_elementos(lista: list[int], i: int, j: int) -> None:
    """
    Intercambia los elementos que se encuentran en las posiciones i y j.

    PRE: 0 <= i < len(lista) and 0 <= j < len(lista)
    Args: 
        lista (list[int]): La lista donde se hará el cambio.
        i (int) : Índice del primer elemento.
        j (int) : Índice del segundo elemento.
    Returns: 
        None: Modifica la lista in-situ (no devuelve nada).
    """
    lista[i], lista[j] = lista[j], lista[i]


def listaOrdenada(lista:list[int]) -> list[int]:

    """
    Ordena una lista de enteros de menor a mayor y devuelve una copia  de la lista

    PRE: True
    Args:
        lista (list[int]): La lista de enteros a ordenar
    Returns:
        list[int]: La nueva lista con los elementos ordenados
    """

    lista_ordenada = lista.copy() 
    n = len(lista_ordenada)

    for i in range(n):

        indice_minimo = indice_del_minimo_entre(lista_ordenada, i)
        
        intercambiar_dos_elementos(lista_ordenada, i, indice_minimo)
        
    return lista_ordenada


def tamaño_barco_encontrado(grilla: Grilla, visitados: list[list[bool]], posicion_fila: int, posicion_columna: int) -> Barco:
    
    """
    Obtiene el tamaño del barco encontrado. 

    PRE: True
    Args:
        grilla (Grilla): La grilla que contiene los barcos colocados
        visitados (list[list[bool]]): La matriz que uso para dejar registro de las posiciones por las cuales ya pasé
        posicion_fila (int): La fila de la posición donde se encontró el barco
        posicion_columna (int): La columna de la posición donde se encontró el barco

    Returns:
        int: El tamaño del barco que se encontré
    """

    if len(grilla) == 0:
        return 0
    
    tamañoPorAhora = 1
    visitados[posicion_fila][posicion_columna] = True

    # barco horizontal: 
    if posicion_columna + 1 < len(grilla[0]) and grilla[posicion_fila][posicion_columna + 1] == BARCO:

        posicion_adyascente = posicion_columna + 1

        while posicion_adyascente < len(grilla[0]) and grilla[posicion_fila][posicion_adyascente] == BARCO:

            visitados[posicion_fila][posicion_adyascente] = True
            tamañoPorAhora += 1
            posicion_adyascente += 1
            
    # barco vertical:
    elif posicion_fila + 1 < len(grilla) and grilla[posicion_fila + 1][posicion_columna] == BARCO:

        posicion_adyascente = posicion_fila + 1

        while posicion_adyascente < len(grilla) and grilla[posicion_adyascente][posicion_columna] == BARCO:

            visitados[posicion_adyascente][posicion_columna] = True
            tamañoPorAhora += 1
            posicion_adyascente += 1

    return tamañoPorAhora


def obtener_barcos_en_grilla(grilla: Grilla) -> list[Barco]:
    
    """
    Obtiene los barcos colocados en la grilla a partir de ella

    PRE: True
    Args:
        grilla (Grilla): La grilla que contiene los barcos colocados.
    Returns:
        list[Barco]: La lista de los barcos que se encuentran en la grilla
    """

    fila: int = len(grilla)
    columna: int = len(grilla[0])
    barcos_ya_vistos: list[list[bool]] = []
    
    for i in range(fila):

        barcos_ya_vistos.append([False] * columna)
    
    tamaños_encontrados:list[Barco] = []

    for i in range(fila):
        for j in range(columna):

            if grilla[i][j] == BARCO and not barcos_ya_vistos[i][j]:
                
                tamaños_encontrados.append(tamaño_barco_encontrado(grilla, barcos_ya_vistos, i, j))
                
    return tamaños_encontrados


def son_barcos_en_grilla_validos(grilla: Grilla, barcos: list[Barco]) -> bool:
    
    """
    Verifica si los barcos presentes en la grilla 
    coinciden con la lista de barcos esperados para el juego

    PRE: True
    Args:
        grilla (Grilla): La grilla que contiene los barcos colocados
        barcos (list[Barco]): La lista de tamaños de barcos esperados
    Returns:
        bool: True si la lista de tamaños de barcos encontrados en la grilla se corresponde con la lista de los barcos esperados
    """

    barcos_en_grilla = obtener_barcos_en_grilla(grilla)

    tamaños_en_grilla_ordenada = listaOrdenada(barcos_en_grilla)
    barcos_ordenados = listaOrdenada(barcos)

    return tamaños_en_grilla_ordenada == barcos_ordenados


def tablero_valido_en_juego(tablero: Tablero, dimension: tuple[int, int], barcos: list[Barco]) -> bool:

    """
    Valida un tablero de un jugador verificando que sus dimensiones y y los barcos (cantidad y tamaños) en la grilla local sean correctas

    PRE: True
    Args:
        tablero (Tablero): El tablero a validar
        dimension (tuple[int, int]): Las dimensiones (filas, columnas) esperadas para el juego
        barcos (list[Barco]): Los barcos esperados (tanto en cantidad como en tamaños)
    Returns:
        bool: True si ambas grillas del tablero tienen las dimensiones correctas y la grilla local tiene los barcos esperados
    """

    return grilla_valida_en_juego(tablero[0], dimension) and grilla_valida_en_juego(tablero[1], dimension) and son_barcos_en_grilla_validos(tablero[0], barcos)
    

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:

    """
    Valida todos los componentes de un estado de juego (EstadoJuego)
    Comprueba las dimensiones, la lista de barcos, el turno y 
    la validez de los tableros de ambos jugadores.

    PRE: True
    Args:
        estadoDeJuego (EstadoJuego): El estado del juego en progreso
    Returns:
        bool: True si todos los componentes del estado del juego son válidos, False en caso contrario
    """

    return dimension_valida(estadoDeJuego[0]) and len(estadoDeJuego[2]) == 1  and (len(estadoDeJuego[1]) > 0) and  tablero_valido_en_juego(estadoDeJuego[3], estadoDeJuego[0], estadoDeJuego[1]) and tablero_valido_en_juego(estadoDeJuego[4], estadoDeJuego[0], estadoDeJuego[1]) 

# EJERCICIO 4

def transforma_letra_en_indice(letra: str) -> int:

    """
    Convierte una letra mayúscula en su índice numérico correspondiente

    PRE: El valor de letra debe ser una única letra mayúscula de la "A" a la "Z"
    Args:
        letra (str): La letra de la fila a convertir
    Returns:
        int: El índice numérico correspondiente a esa letra
    """

    return ord(letra) - ord("A")


def procesar_impacto(grilla_atacada: Grilla, grilla_oponente_conocida: Grilla, fila: int, columna: int) -> ResultadoDisparo:
    
    """
    Simula el disparo efectuado y
    devuelve el resultado del disparo

    PRE: La posición que le paso debe ser una coordenada válida dentro de las dimensiones del tablero
    Args:
        grilla_atacada (Grilla): La grilla local del jugador bajo ataque 
        grilla_oponente_conocida (Grilla): La grilla que representa la grilla del oponente en el tablero del jugador que dispara 
        fila (int): La fila de la posición bajo ataque
        columna (int): La columna de la posición bajo ataque
    Returns:
        ResultadoDisparo: El resultado del disparo (NADA o TOCADO)
    """

    celda = grilla_atacada[fila][columna]

    if celda == VACÍO:

        grilla_atacada[fila][columna] = AGUA

        grilla_oponente_conocida[fila][columna] = AGUA

        return NADA

    elif celda == BARCO:

        grilla_atacada[fila][columna] = BARCO 

        grilla_oponente_conocida[fila][columna] = BARCO 

        return TOCADO
    


def dispararEnPosición(estado_de_juego: EstadoJuego, posicion: Posición) -> ResultadoDisparo:
    
    """
    Simula un disparo en una posición del tablero, actualiza el estado 
    del juego (solo las grillas y el turno) y devuelve el resultado del disparo

    PRE: La posición que le paso debe ser una coordenada válida dentro de las dimensiones del tablero
    Args:
        estado_de_juego (EstadoJuego): El estado actual del juego
        posicion (Posición): La posición hacia donde se dispara
    Returns:
        ResultadoDisparo: El resultado del disparo (NADA o TOCADO)
    """

    fila_disparo = transforma_letra_en_indice(posicion[0])
    columna_disparo = posicion[1] - 1

    lista_turno = estado_de_juego[2] 

    # estado[3] es tablero jugador ([0]: grilla local del jugador, [1]: grilla del oponente)
    # estado[4] es tablero oponente ([0]: grilla local del oponente, [1]: grilla del jugador como oponente)

    if lista_turno[0] == UNO:

        grilla_local_atacada = estado_de_juego[4][0]
        grilla_oponente_conocida = estado_de_juego[3][1]
        
        proximo_turno = DOS

    else:

        grilla_local_atacada = estado_de_juego[3][0]
        grilla_oponente_conocida = estado_de_juego[4][1]
        
        proximo_turno = UNO

    lista_turno[0] = proximo_turno

    resultado = procesar_impacto(grilla_local_atacada, grilla_oponente_conocida, fila_disparo, columna_disparo)

    
    return resultado
    

# EJERCICIO 5

def es_barco_valido_vertical(barco:BarcoEnGrilla) -> bool:

    """
    Verifica si un barco es vertical. Todas sus coordenadas 
    tienen el mismo número y las letras de las filas son consecutivas

    PRE: barco es no vacía.
    Args:
        barco (BarcoEnGrilla):  El barco a verificar
    Returns:
        bool: True si el barco es vertical y sus posiciones son adyascentes, False en caso contrario
    """

    for i in range(1, len(barco)):

        letra_actual, numero_actual = barco[i]
        letra_anterior, numero_anterior = barco[i-1]

        if numero_actual != numero_anterior:

            return False

        if ord(letra_actual) != ord(letra_anterior)+ 1:
            
            return False

    return True  


def es_barco_valido_horizontal(barco:BarcoEnGrilla) -> bool:

    """
    Verifica si un barco es horizontal. Todas sus coordenadas 
    tienen la misma letra (fila) y los números de las columnas son consecutivas

    PRE: barco es no vacía
    Args:
        barco (BarcoEnGrilla): El barco a verificar
    Returns:
        bool: True si el barco es horizontal y sus posiciones son adyascentes, False en caso contrario
    """

    for i in range(1, len(barco)):

        letra_actual, numero_actual = barco[i]
        letra_anterior, numero_anterior = barco[i-1]

        if letra_actual != letra_anterior:

            return False

        if numero_actual != numero_anterior + 1:

            return False    

    return True 


def es_barco_valido(barco:BarcoEnGrilla) -> bool:

    """
    Verifica si un barco es válido, vertical y horizontalmente

    PRE: `barco` es una lista de coordenadas no vacía.
    Args:
        barco (BarcoEnGrilla): La lista de coordenadas (letra, numero) que componen el barco
    Returns:
        bool: True si el barco es horizontal o vertical, False si no es ninguno
    """

    return es_barco_valido_horizontal(barco) or es_barco_valido_vertical(barco)


def sonBarcosValidos(barcos: list[BarcoEnGrilla]) -> bool:

    """
    Verifica si todos los barcos en una lista de barcos son válidos

    PRE: True
    Args:
        barcos (list[BarcoEnGrilla]): Una lista de barcos
    Returns:
        bool: True si todos los barcos en la lista son válidos (horizontales 
              o verticales), False si al menos uno no lo es
    """

    barco_actual:int = 0

    while barco_actual < len(barcos) and es_barco_valido(barcos[barco_actual]):

        barco_actual += 1

    return barco_actual == len(barcos)


def indice_a_letra(indice: int) -> str:

    """
    Convierte un índice de fila en su letra de fila correspondiente

    PRE: El índice debe ser un entero entre 0 y 25
    Args:
        indice (int): El índice numérico de la fila
    Returns:
        str: La letra mayúscula correspondiente
    """

    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[indice]


def indice_a_numero(indice: int) -> int:

    """
    Convierte un índice de columna en su número de columna correspondiente

    PRE: True
    Args:
        indice (int): El índice numérico de la columna
    Returns:
        int: El número de columna
    """

    return indice + 1

    
def identificar_barco_encontrado(grilla: Grilla, visitados: list[list[bool]], fila_inicio_barco: int, columna_inicio_barco: int) -> BarcoEnGrilla:
    
    """
    Identifica el barco entero a partir de la posicion inicial hallada
    y marca las posiciones como visitadas

    PRE: grilla y visitados son ambas no vacios y tienen las mismas dimensiones
    Args:
        grilla (Grilla): La grilla local de un jugador rellena con BARCO o VACÍO
        visitados (list[list[bool]): La matriz que uso para dejar registro de las posiciones por las cuales ya pasé
        fila_inicio_barco (int): La fila de la posición donde se encontró el barco
        columna_inicio_barco (int): La columna de la posición donde se encontró el barco
    Returns:
        list[BarcoEnGrilla]: Los barcos encontrados en la grilla.
        
    """

    filas_totales = len(grilla)
    columas_totales = len(grilla[0])
    

    posicion_inicial = (indice_a_letra(fila_inicio_barco), indice_a_numero(columna_inicio_barco))

    barco = [posicion_inicial]
    
    visitados[fila_inicio_barco][columna_inicio_barco] = True


    if columna_inicio_barco + 1 < columas_totales and grilla[fila_inicio_barco][columna_inicio_barco + 1] == BARCO:
        
        k = columna_inicio_barco + 1

        while k < columas_totales and grilla[fila_inicio_barco][k] == BARCO:

            visitados[fila_inicio_barco][k] = True
            nueva_coord = (indice_a_letra(fila_inicio_barco), indice_a_numero(k))
            barco.append(nueva_coord)

            k += 1


    elif fila_inicio_barco + 1 < filas_totales and grilla[fila_inicio_barco + 1][columna_inicio_barco] == BARCO:

        k = fila_inicio_barco + 1

        while k < filas_totales and grilla[k][columna_inicio_barco] == BARCO:

            visitados[k][columna_inicio_barco] = True
            nueva_coord = (indice_a_letra(k), indice_a_numero(columna_inicio_barco))
            barco.append(nueva_coord)

            k += 1
            
    return barco


def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    
    """
    Toma una grilla y guarda todos los barcos adyascentes (horizontales 
    y verticales) que encuentra. Luego, valida que los barcos encontrados sean válidos

    PRE: True
    Args:
        grilla (Grilla): La grilla local de un jugador rellena con BARCO o VACÍO
    Returns:
        list[BarcoEnGrilla]: Los barcos encontrados en la grilla
        
    """

    fila:int = len(grilla)
    columna:int = len(grilla[0])
    barcos_descubiertos: list[BarcoEnGrilla] = []
    
    barcos_ya_vistos: list[list[bool]] = []

    for i in range(fila):
        
        barcos_ya_vistos.append([False] * columna)

    for i in range(fila):
        for j in range(columna):
            
            if grilla[i][j] == BARCO and not barcos_ya_vistos[i][j]:
                
                barco_encontrado = identificar_barco_encontrado(grilla, barcos_ya_vistos, i, j)
                
                barcos_descubiertos.append(barco_encontrado)

    if sonBarcosValidos(barcos_descubiertos):

        return barcos_descubiertos


# EJERCICIO 6

def barco_descubierto_en(barco: BarcoEnGrilla, grilla: Grilla) -> bool:

    """
    Verifica si al menos una parte del barco fue descubierta/tocada por el oponente

    PRE:
        grilla es una grilla válida
        barco es un barco válido
        barco es un barco válido en la grilla 
    Args:
        barco (BarcoEnGrilla) : El barco a checkear
        grilla (Grilla): La grilla que representa la grilla local del oponente en el tablero del jugador
    Returns: 
        Devuelve True si el barco fue tocado al menos en una posición. False si no fue descubierto 
    """

    for posicion in barco:

        fila, columna = posicion

        fila_indice:int = transforma_letra_en_indice(fila) 
        columna_indice: int = columna - 1

        if grilla[fila_indice][columna_indice] == BARCO:

            return True
    
    return False

            
def hay_agua_en_grilla(grilla: Grilla) -> bool:
    
    """
    Verifica si hay alguna celda marcada como AGUA en la grilla

    PRE: grilla es una grilla válida
    Args: grilla (Grilla): La grilla que representa la grilla local del oponente en el tablero del jugador
    Returns:
        bool: True si hay al menos una celda con AGUA, False en caso contrario 
    """

    filas = len(grilla)
    columnas = len(grilla[0])

    for i in range(filas):
        for j in range(columnas):

            if grilla[i][j] == AGUA:

                return True
    
    return False


def todos_barcos_descubiertos(barcos: list[BarcoEnGrilla], grilla: Grilla) -> bool:
    
    """
    Verifica si todos los barcos de la lista han sido descubiertos

    PRE:
        grilla es una grilla válida
        barco es un barco válido
        barco es un barco válido en la grilla 
    Args:
        barcos (list[BarcoEnGrilla]): Los barcos a verificar
        grilla (Grilla): La grilla que representa la grilla local del oponente en el tablero del jugador
    Returns:
        bool: True si TODOS los barcos de barcos fueron descubiertos, False en caso contrario
    """

    for barcoActual in barcos:
       
        if not barco_descubierto_en(barcoActual, grilla):

            return False
        
    return True 
    

def es_jugador_perfecto(estadoDeJuego: EstadoJuego, jugador:Jugador) -> bool:

    """
    Se fija si un jugador determinado descubrió todos los barcos de su oponente sin haber "tocado agua"

    PRE: 
        estadoDeJuego es un estado válido
        jugador es UNO o Dos
    Args:
        estadoDeJuego (EstadoJuego): El estado actual del juego
        jugador (Jugador): El jugador bajo verificacion 
    Returns:
        Devuelve True si el jugador no tocó agua y descubrió todos los barcos de su oponente. Caso contrario, devuelve False
        
    """

    # estado[3] es tablero jugador ([0]: grilla local del jugador, [1]: grilla del oponente)
    # estado[4] es tablero oponente ([0]: grilla local del oponente, [1]: grilla del jugador como oponente)

    if (jugador == UNO):

        grilla_mis_ataques = estadoDeJuego[3][1]
        grilla_barcos_oponente = estadoDeJuego[4][0]
        
    else:

        grilla_mis_ataques = estadoDeJuego[4][1]
        grilla_barcos_oponente = estadoDeJuego[3][0]
    
    barcos_oponente = barcosEnGrilla(grilla_barcos_oponente)

    todos_descubiertos = todos_barcos_descubiertos(barcos_oponente, grilla_mis_ataques)
    nunca_toco_agua = not hay_agua_en_grilla(grilla_mis_ataques)
        

    return todos_descubiertos and nunca_toco_agua


def hayJugadorPerfecto (estadoDeJuego: EstadoJuego) -> bool:

    """
    Se fija que alguno de los jugadores haya descubierto todos los barcos de su oponente sin haber "tocado agua"

    PRE: estadoDeJuego es un estado válido 
    Args:
        estadoDeJuego: EstadoJuego: El estado actual del juego
    Returns:
        Devuelve True si alguno de los dos jugadores no tocó agua y descubrió todos los barcos de su oponente. Caso contrario, devuelve False
        
    """

    return es_jugador_perfecto(estadoDeJuego, estadoDeJuego[2][0]) or es_jugador_perfecto(estadoDeJuego, estadoDeJuego[2][1])