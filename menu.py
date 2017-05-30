import pygame
import random

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update (self):
        self.left,self.top=pygame.mouse.get_pos()
        
class Boton (pygame.sprite.Sprite):
    def __init__(self,rojo1,rojo2,x=350,y=300):                
        self.imagen_normal=rojo1
        self.imagen_seleccion=rojo2
        self.imagen_actual=self.imagen_normal
        self.rect= self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update (self,pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)
       
def main():
    pygame.init()
    pantalla=pygame.display.set_mode((850,650))
    pygame.display.set_caption("QUEMA-2")
    icono= pygame.image.load("imagenes/icono.png")
    pygame.display.set_icon(icono)
    nombre=pygame.image.load("imagenes/nombre.png")
    reloj1=pygame.time.Clock()
    celeste=(0,255,255)
    salir=False
    rojo1=pygame.image.load("imagenes/boton1.png")
    rojo2=pygame.image.load("imagenes/boton2.png")
    pygame.mixer.music.load("musica y sonidos/musica/inicio.mp3")
    minombre= pygame.image.load("imagenes/minombre.png")
    otrologo= pygame.image.load("imagenes/otrologo.png")
    fondodeljuego=pygame.image.load("imagenes/fondodeljuego.png")
    sonidoboton=pygame.mixer.Sound("musica y sonidos/sonido/boton.wav")
    musica=pygame.mixer.music.load("musica y sonidos/musica/menu.mp3")
    pygame.mixer.music.play(-1)
    while salir!=True:
        for event in pygame.event.get():                
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    sonidoboton.play()
                    pygame.mixer.music.stop()
                    import iniciodeljuego                     
            if event.type == pygame.QUIT:
                salir=True               
        reloj1.tick(60)
        pantalla.fill(celeste)
        pantalla.blit(nombre,(20,30))
        pantalla.blit(minombre,(625,550))
        pantalla.blit(otrologo,(20,530))
        boton1=Boton(rojo1,rojo2)
        cursor1=Cursor()
        cursor1.update()
        boton1.update(pantalla,cursor1)        
        pygame.display.update()
    pygame.quit()

main()
