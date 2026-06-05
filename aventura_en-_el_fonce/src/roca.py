# src/rocas.py
import pygame
import random
# CORREGIDO: Se quitó el punto después de settings
from setting import ANCHO, ALTO, ANCHO_MARGEN, VELOCIDAD_INICIAL_ROCA

class Roca:
    def __init__(self):
        try:
            # Busca la roca en la carpeta assets que está un nivel arriba
            self.imagen = pygame.image.load("assets/images/roca.png").convert_alpha()
            self.imagen = pygame.transform.scale(self.imagen, (45, 45))
            self.rect = self.imagen.get_rect()
        except pygame.error:
            # Si no encuentra la imagen, dibuja un cuadrado gris de respaldo
            self.imagen = None
            self.rect = pygame.Rect(0, 0, 45, 45)
            
        self.reiniciar_posicion()
        self.velocidad = VELOCIDAD_INICIAL_ROCA

    def reiniciar_posicion(self):
        self.rect.x = random.randint(ANCHO_MARGEN, ANCHO - ANCHO_MARGEN - self.rect.width)
        self.rect.y = random.randint(-150, -40) 

    def actualizar(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.reiniciar_posicion()
            return True 
        return False

    def dibujar(self, superficie):
        if self.imagen:
            superficie.blit(self.imagen, self.rect)
        else:
            pygame.draw.rect(superficie, (128, 128, 128), self.rect)