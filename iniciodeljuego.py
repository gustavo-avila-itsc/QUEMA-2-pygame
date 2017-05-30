import pygame
import random

class Player (pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen= imagen
        self.rect= self.imagen.get_rect()
        self.rect.inflate_ip(-30,-16)
        self.rect.top=550
        self.rect.left=345
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,pantalla):
        pantalla.blit(self.imagen,self.rect)
class Circulo (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)    
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)

class Pelota2 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)
            
class Pelota3 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)

class Pelota4 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)
            
class Pelota5 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)

class Pelota6 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)

class Pelota7 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)
        
class Pelota8 (pygame.sprite.Sprite):  
    def __init__(self,imagen): 
        t=random.randrange(-650,-80)
        l=random.randrange(-20,850)        
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-10,-10)
        self.rect.top= t
        self.rect.left= l
    def mover (self,px,py):
        self.rect.move_ip(px,py)
    def update (self,pantalla):
        pantalla.blit(self.imagen,self.rect)      
    def reagregar (self,imagen,pantalla):
        lanzar=pygame.mixer.Sound("musica y sonidos/sonido/pelota.wav")
        if self.rect.top>=-20 and self.rect.top<3:
            lanzar.play(0)
        if self.rect.top>650:
            t=random.randrange(-650,-80)
            l=random.randrange(-20,850)        
            self.imagen= imagen
            self.rect = self.imagen.get_rect()
            self.rect.inflate_ip(-10,-10)
            self.rect.top= t
            self.rect.left= l
            pantalla.blit(self.imagen,self.rect)

def colision(Player,Circulo,Pelota2,Pelota3,Pelota4,Pelota5,Pelota6,Pelota7,Pelota8): 
    if Player.rect.colliderect(Circulo) or Player.rect.colliderect(Pelota2) or Player.rect.colliderect(Pelota3) or Player.rect.colliderect(Pelota4) or Player.rect.colliderect(Pelota5) or Player.rect.colliderect(Pelota6) or Player.rect.colliderect(Pelota7) or Player.rect.colliderect(Pelota8):#dddddddddddddddddddddddddddd 
        return True
    return False

class Pared1 (pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.top= 1
        self.rect.left= 1
    def update (self, pantalla):
        pantalla.blit(self.imagen,self.rect)
class Pared2 (pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.top= 1
        self.rect.left= 840
    def update (self, pantalla):
        pantalla.blit(self.imagen,self.rect)
class Techo1 (pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.top= 1
        self.rect.left= 1
    def update (self, pantalla):
        pantalla.blit(self.imagen,self.rect)
class Techo2 (pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen= imagen
        self.rect = self.imagen.get_rect()
        self.rect.top= 640
        self.rect.left= 1
    def update (self, pantalla):
        pantalla.blit(self.imagen,self.rect)
def colision2(Player,Pared1,Pared2,Techo1,Techo2):  
    if Player.rect.colliderect(Pared1) or Player.rect.colliderect(Pared2) or Player.rect.colliderect(Techo1) or Player.rect.colliderect(Techo2):
        return True
    return False
        
def main():
    pygame.init()
    ancho= 850
    alto= 650
    pantalla=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("QUEMA-2")
    icono= pygame.image.load("imagenes/icono.png")
    pygame.display.set_icon(icono)
    fondodeljuego=pygame.image.load("imagenes/fondodeljuego.png")
    pygame.mixer.music.load("musica y sonidos/musica/inicio.mp3")
    jugador= pygame.image.load("imagenes/jugador.png")   
    reloj1=pygame.time.Clock()    
    salir=False
    findeljuego=False 
    pygame.mixer.music.play(-1)	
    player1=Player(jugador)
    vx,vy=0,0
    velocidad=13
    leftsigue,rightsigue,upsigue,downsigue=False,False,False,False
    pelota=pygame.image.load("imagenes/pelota.png")
    circulo1=Circulo(pelota)
    px,py=0,8  
    reglas=pygame.image.load("imagenes/reglas.png")
    golpe= pygame.image.load("imagenes/golpe.png")    
    gameover= pygame.image.load("imagenes/gameover.png")
    oh=pygame.mixer.Sound("musica y sonidos/sonido/oh.wav")
    circulo2=Pelota2(pelota)
    circulo3=Pelota3(pelota)
    circulo4=Pelota4(pelota)
    circulo5=Pelota5(pelota)
    circulo6=Pelota6(pelota)
    circulo7=Pelota7(pelota)
    circulo8=Pelota8(pelota)
    p1=pygame.image.load("imagenes/pared1.png")
    p2=pygame.image.load("imagenes/pared2.png")
    t1=pygame.image.load("imagenes/techo1.png")
    t2=pygame.image.load("imagenes/techo2.png")
    pared1=Pared1(p1)
    pared2=Pared2(p2)
    techo1=Techo1(t1)
    techo2=Techo2(t2)

    while salir!=True:
        for event in pygame.event.get():                       
            if event.type == pygame.QUIT:
                salir=True
            if findeljuego==False:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT :
                        leftsigue=True                  
                        vx=-velocidad
                    if event.key==pygame.K_RIGHT:
                        rightsigue=True
                        vx=velocidad
                    if event.key==pygame.K_UP:
                        upsigue=True                     
                        vy=-velocidad
                    if event.key==pygame.K_DOWN:
                        downsigue=True                   
                        vy=velocidad
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        leftsigue=False
                        if rightsigue: vx=velocidad
                        else: vx=0
                    if event.key==pygame.K_RIGHT:
                        rightsigue=False
                        if leftsigue: vx=-velocidad
                        else: vx=0
                    if event.key==pygame.K_UP:
                        upsigue=False
                        if downsigue: vy=velocidad
                        else: vy=0
                    if event.key==pygame.K_DOWN:
                        downsigue=False
                        if upsigue: vy=-velocidad
                        else: vy=0                    
        reloj1.tick(40)
        pantalla.blit(fondodeljuego,(0,0))
        player1.update(pantalla)       
        circulo1.update(pantalla)
        circulo1.reagregar(pelota,pantalla)     
        circulo2.update(pantalla)
        circulo2.reagregar(pelota,pantalla)
        circulo3.update(pantalla)
        circulo3.reagregar(pelota,pantalla)
        circulo4.update(pantalla)
        circulo4.reagregar(pelota,pantalla)
        circulo5.update(pantalla)
        circulo5.reagregar(pelota,pantalla)
        circulo6.update(pantalla)
        circulo6.reagregar(pelota,pantalla)
        circulo7.update(pantalla)
        circulo7.reagregar(pelota,pantalla)
        circulo8.update(pantalla)
        circulo8.reagregar(pelota,pantalla)
        pared1.update(pantalla)
        pared2.update(pantalla)
        techo1.update(pantalla)
        techo2.update(pantalla)        
        if  findeljuego!=True:       
            player1.mover(vx,vy)
            circulo1.mover(px,py)        
            circulo2.mover(px,py)
            circulo3.mover(px,py)
            circulo4.mover(px,py)
            circulo5.mover(px,py)
            circulo6.mover(px,py)
            circulo7.mover(px,py)
            circulo8.mover(px,py)         
        if colision(player1,circulo1,circulo2,circulo3,circulo4,circulo5,circulo6,circulo7,circulo8):
            findeljuego=True 
            pantalla.blit(golpe,(300,160))
            pygame.mixer.music.stop()
            pantalla.blit(gameover,(40,380))        
            oh.play(0)     
        if colision2(player1,pared1,pared2,techo1,techo2):
            vx,vy=(0,0)
        pantalla.blit(reglas,(285,5))
        pygame.display.update()        
    pygame.quit()
main()
