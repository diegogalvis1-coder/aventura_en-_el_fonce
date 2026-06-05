# src/balsa.py
import pygame
# CORREGIDO: Ahora importa directamente desde settings porque están en la misma carpeta
from setting import ANCHO, ALTO, ANCHO_MARGEN

class Balsa:
    def __init__(self):
        try:
            # Busca la balsa en la carpeta assets que está un nivel arriba
            self.imagen = pygame.image.load("assets/images/balsa.png").convert_alpha()
            self.imagen = pygame.transform.scale(self.imagen, (50, 50))
            self.rect = self.imagen.get_rect()
        except pygame.error:
            # Si no encuentra la imagen, dibuja un cuadrado café de respaldo
            self.imagen = None
            self.rect = pygame.Rect(0, 0, 50, 50)
            
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 40
        self.velocidad = 6

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            if self.rect.left > ANCHO_MARGEN:
                self.rect.x -= self.velocidad
                
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            if self.rect.right < ANCHO - ANCHO_MARGEN:
                self.rect.x += self.velocidad

    def dibujar(self, superficie):
        if self.imagen:
            superficie.blit(self.imagen, self.rect)
        else:
            pygame.draw.rect(superficie, (139, 69, 19), self.rect)