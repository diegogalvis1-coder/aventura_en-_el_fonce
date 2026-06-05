# src/main.py
import pygame
import sys
import random 

# CORRECCIÓN: Eliminamos el "src." ya que este archivo está dentro de la misma carpeta.
from setting import ANCHO, ALTO, AGUA, GALLINERAL, ANCHO_MARGEN, FPS_INICIALES
from src.balsa import Balsa
from src.roca import Roca

def juego():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Aventura Extrema en el Fonce ")
    reloj = pygame.time.Clock()
    
    # --- FUENTES ---
    fuente = pygame.font.SysFont("Impact", 24)
    fuente_game_over = pygame.font.SysFont("Impact", 45) 

    # --- VARIABLES PARA EL MOVIMIENTO DEL RÍO ---
    lineas_rio = [[random.randint(ANCHO_MARGEN, ANCHO - ANCHO_MARGEN - 10), random.randint(0, ALTO)] for _ in range(15)]

    jugador = Balsa()
    lista_rocas = [Roca() for _ in range(3)] 
    
    for i, roca in enumerate(lista_rocas):
        roca.rect.y -= i * 180

    puntaje = 0
    fps_actuales = FPS_INICIALES
    jugando = True

    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        jugador.mover(teclas)

        # --- MOVIMIENTO DE LAS PIEDRAS Y COLISIONES ---
        for roca in lista_rocas:
            velocidad_caida = fps_actuales // 10
            esquivada = roca.actualizar(velocidad_caida) 
            
            if esquivada:
                puntaje += 10 
                if puntaje % 50 == 0:
                    fps_actuales += 2 
                    for r in lista_rocas:
                        r.velocidad += 0.5

            # CORRECCIÓN: Si choca, manejamos el Game Over y rompemos el bucle inmediatamente
            if jugador.rect.colliderect(roca.rect):
                pantalla.fill((180, 20, 20)) 
                
                texto_go = fuente_game_over.render("GAME OVER", True, (255, 255, 255))
                texto_pts = fuente.render(f"PUNTOS LOGRADOS: {puntaje}", True, (241, 196, 15)) 
                
                pantalla.blit(texto_go, (ANCHO // 2 - texto_go.get_width() // 2, ALTO // 2 - 40))
                pantalla.blit(texto_pts, (ANCHO // 2 - texto_pts.get_width() // 2, ALTO // 2 + 20))
                
                pygame.display.flip()
                pygame.time.delay(3000) 
                jugando = False 
                break # Rompe el bucle de las rocas para evitar errores

        if not jugando:
            break # Rompe el bucle principal si perdiste

        # --- DIBUJAR EL RÍO Y EL PARQUE ---
        pantalla.fill(AGUA) 

        # LÓGICA DE MOVIMIENTO DEL RÍO
        for linea in lineas_rio:
            linea[1] += (fps_actuales // 10) + 1  
            if linea[1] > ALTO: 
                linea[1] = 0
                linea[0] = random.randint(ANCHO_MARGEN, ANCHO - ANCHO_MARGEN - 10)
            pygame.draw.line(pantalla, (100, 180, 240), (linea[0], linea[1]), (linea[0], linea[1] + 15), 2)

        pygame.draw.rect(pantalla, GALLINERAL, (0, 0, ANCHO_MARGEN, ALTO))
        pygame.draw.rect(pantalla, GALLINERAL, (ANCHO - ANCHO_MARGEN, 0, ANCHO_MARGEN, ALTO))

        # Dibujar personajes
        jugador.dibujar(pantalla)
        for roca in lista_rocas:
            roca.dibujar(pantalla)

        # Mostrar puntaje
        texto_puntaje = fuente.render(f"PUNTOS: {puntaje}", True, (255, 255, 255))
        pantalla.blit(texto_puntaje, (ANCHO_MARGEN + 10, 15))

        pygame.display.flip()
        reloj.tick(fps_actuales)

if __name__ == "__main__":
    juego()