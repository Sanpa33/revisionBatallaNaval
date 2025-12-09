import unittest
from batallaNaval import *

# Tests
# Tests Ejercicio 1
class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_longitud_2_hay_uno_en_el_medio(self): 
        barcos = [[('H',3), ('H',4), ('H',5)],
                  [('F',4), ('E',4)],
                  [('B',4), ('B',3), ('B',2)]] 
              
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                  [('F',4), ('E',4)],
                                  [('B',4), ('B',3), ('B',2)]] )
    
    def test_lista_vacia(self):
        self.assertEqual(cantidadDeBarcosDeTamaño([], 5), 0)
    
    def test_no_hay_barcos_de_ese_tamaño(self):
        barcos = [[('A',1), ('A',2), ('A',3)],
                  [('C',5), ('D',5)]]
        
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos, 4), 0)
    
    def test_todos_tienen_el_mismo_tamaño(self):
        barcos = [[('A',1), ('A',2)],
                  [('C',3), ('C',4)],
                  [('F',2), ('F',3)]]
         
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos, 2), 3)
    
    def test_tamaño_cero(self):
        barcos = [[('A',1)],
                 [('B',2), ('B',3)]]

        self.assertEqual(cantidadDeBarcosDeTamaño(barcos, 0), 0)


# Tests Ejercicio 2
class nuevoJuego_Test(unittest.TestCase):
    def test_2x2_y_un_barco_longitud_2(self): 
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        juego = nuevoJuego(2,2,[2])
        
        self.assertEqual(juego[0], (2,2))
        self.assertEqual(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))
    
    def test_tablero_1x1(self):

        juego = nuevoJuego(1, 1, [1])
        grilla_esperada = [[VACÍO]]
        
        self.assertEqual(juego[0], (1, 1))
        self.assertEqual(juego[3][0], grilla_esperada)
    
    def test_tablero_26_filas(self):
         
        juego = nuevoJuego(26, 5, [2])

        self.assertEqual(juego[0], (26,5))
        self.assertEqual(len(juego[3][0]), 26)
        self.assertEqual(len(juego[3][0][0]), 5)        

    def test_varios_barcos(self):

        lista_barcos = [5, 4, 3, 3, 2]
        juego = nuevoJuego(10, 10, lista_barcos)
        
        self.assertEqual(juego[1], lista_barcos)

# Tests Ejercicio 3
class esEstadoDeJuegoVálido_Test(unittest.TestCase):
    def test_grilla_DOS_local_no_coincide_con_disponibles(self): 

        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_no_hay_barcos_en_grilla(self): 
        
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        

        estado = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))
        
    def test_tableros_distintas_dimensiones_entre_si(self): 

        grillaUnoLocal = [[VACÍO, VACÍO],
                          [VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO],
                             [VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,2), [], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,2), [], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

# Tests Ejercicio 4
class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)


    def test_disparo_en_posicion_con_barco_turno_uno(self):
            
            estado_inicial = ((5,5), [3, 2], [UNO],
                ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
                ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
            )
            
            
            estado_esperado = ((5,5), [3, 2], [DOS],
                ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
                [[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], 
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
                ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
            )
            
            resultado = dispararEnPosición(estado_inicial, ("A", 2))
            
            self.assertEqual(resultado, TOCADO)
            self.assertEqual(estado_inicial, estado_esperado)


    def test_disparo_en_posicion_con_barco_turno_dos(self):

            estado_inicial = ((5,5), [3, 2], [DOS],
                ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO], 
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
                ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
            )
            


            estado_esperado = ((5,5), [3, 2], [UNO],
                ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO], 
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
                ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
                [[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], 
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
            )
            

            resultado = dispararEnPosición(estado_inicial, ("A", 2))
            
            self.assertEqual(resultado, TOCADO)
            self.assertEqual(estado_inicial, estado_esperado)


    def test_disparo_en_posicion_vacia_turno_dos(self):

            estado_inicial = ((5,5), [3, 2], [DOS],
                ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO], 
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
                ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
            )


            estado_esperado = ((5,5), [3, 2], [UNO],
                ([[VACÍO, BARCO, AGUA, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO], 
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
                ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
                [[VACÍO, VACÍO, AGUA, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
            )
            
            resultado = dispararEnPosición(estado_inicial, ("A", 3)) 
            
            self.assertEqual(resultado, NADA)
            self.assertEqual(estado_inicial, estado_esperado)



# Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamanios(self): 
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('D',3), ('D',4)],
                                                [('B',6), ('B',5), ('B',4)],
                                                [('D',6), ('E',6)],
                                                [('D',1),('C',1), ('B',1)]]
        

        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])

# Tests Ejercicio 6

class hayJugadorPerfecto_Test(unittest.TestCase):

    import unittest

class TestHayJugadorPerfecto(unittest.TestCase):

    def test_jugador_uno_es_perfecto(self):

        grilla_local_jugador = [[VACÍO, VACÍO, VACÍO], 
                               [VACÍO, VACÍO, VACÍO], 
                               [VACÍO, VACÍO, VACÍO]]
        
        grilla_local_opo = [[BARCO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO]]
        
        grilla_ataques_jug = [[BARCO, VACÍO, VACÍO], 
                             [VACÍO, VACÍO, VACÍO], 
                             [VACÍO, VACÍO, VACÍO]]

        grilla_ataques_opo = [[BARCO, VACÍO, VACÍO], 
                             [VACÍO, VACÍO, VACÍO], 
                             [VACÍO, AGUA, VACÍO]]
        
        tablero_jugador = [grilla_local_jugador, grilla_ataques_jug]
        tablero_oponente = [grilla_local_opo, grilla_ataques_opo]
        
        estado = [0, 0, [UNO, DOS], tablero_jugador, tablero_oponente]

        self.assertTrue(hayJugadorPerfecto(estado))

    def test_jugador_dos_perfecto(self):
        
        grilla_local_jug = [[VACÍO, VACÍO, VACÍO], 
                            [VACÍO, BARCO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO]]
        
        grilla_ataques_opo = [[VACÍO, VACÍO, VACÍO], 
                              [VACÍO, BARCO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO]]
        
        grilla_local_opo = [[VACÍO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO]]

        grilla_ataques_jug = [[AGUA, VACÍO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO]]

        tablero_jugador = [grilla_local_jug, grilla_ataques_jug]
        tablero_oponente = [grilla_local_opo, grilla_ataques_opo]

        estado = [0, 0, [UNO, DOS], tablero_jugador, tablero_oponente]

        self.assertTrue(hayJugadorPerfecto(estado))

    def test_ambos_tocaron_agua(self):
        
        grilla_barcos = [[BARCO, VACÍO, VACÍO], 
                         [VACÍO, VACÍO, VACÍO], 
                         [VACÍO, VACÍO, VACÍO]]
        
        grilla_con_agua = [[VACÍO, AGUA, VACÍO], 
                           [VACÍO, VACÍO, VACÍO], 
                           [VACÍO, VACÍO, VACÍO]]
    

        tablero_jugador = [grilla_barcos, grilla_con_agua]
        tablero_oponente = [grilla_barcos, grilla_con_agua]

        estado = [0, 0, [UNO, DOS], tablero_jugador, tablero_oponente]

        self.assertFalse(hayJugadorPerfecto(estado))

    def test_ninguno_es_perfecto(self):

        grilla_local_jug = [[BARCO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO]]
        
        grilla_local_opo = [[BARCO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO], 
                            [VACÍO, VACÍO, VACÍO]]
        
        grilla_ataques_jug = [[VACÍO, VACÍO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO]]
        
        grilla_ataques_opo = [[VACÍO, VACÍO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO], 
                              [VACÍO, VACÍO, VACÍO]]

        tablero_jugador = [grilla_local_jug, grilla_ataques_jug]
        tablero_oponente = [grilla_local_opo, grilla_ataques_opo]

        estado = [0, 0, [UNO, DOS], tablero_jugador, tablero_oponente]

        self.assertFalse(hayJugadorPerfecto(estado))

# Tests para las funciones auxiliares de validación de barcos
class FuncionesAuxiliares_Test(unittest.TestCase):
    
    def test_indice_minimo_se_actualiza(self):

        lista = [10, 2, 5] 
        
        resultado = indice_del_minimo_entre(lista, 0)
        self.assertEqual(resultado, 1)

    def test_auxiliar_vertical_invalido_por_cambio_de_numero(self):

        barco_invalido = [("A", 1), ("B", 2)] 
        self.assertFalse(es_barco_valido_vertical(barco_invalido))

    def test_auxiliar_vertical_invalido_por_gap_de_letra(self):

        barco_invalido = [("A", 1), ("C", 1)] 
        self.assertFalse(es_barco_valido_vertical(barco_invalido))

    def test_auxiliar_horizontal_invalido_por_gap_de_numero(self):


        barco_invalido = [("A", 1), ("A", 3)]
        self.assertFalse(es_barco_valido_horizontal(barco_invalido))
    
    def test_auxiliar_horizontal_invalido_por_cambio_de_letra(self):

        barco_invalido = [("A", 1), ("B", 2)]
        self.assertFalse(es_barco_valido_horizontal(barco_invalido))


if __name__ == '__main__':
    unittest.main(verbosity=1)
