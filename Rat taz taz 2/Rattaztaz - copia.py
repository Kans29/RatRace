import pygame
import random
import math

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)

    def update(self,screen,cursor):
        if(cursor.colliderect(self.rect)):
           self.imagen_actual = self.imagen_seleccion
        else:
           self.imagen_actual = self.imagen_normal

        screen.blit(self.imagen_actual,self.rect)
        
class Gato(pygame.sprite.Sprite):
    def __init__(self,x,y):
        #creo 4 imagenes para el raton
        self.imagen1=pygame.image.load("Gato.png")
        self.imagen2=pygame.image.load("Gato2.png")
     

        self.imagenes = [self.imagen1,self.imagen2]
        
        
        self.imagen_actual=0
        self.p = x-20
        self.q = y-20
        self.imagen = self.imagenes[self.imagen_actual]
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-20,-20)
        self.rect.top,self.rect.left = (x,y)


    def update(self,screen,vx,vy,tag):


        # si el a==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        
        if (tag == 21):
            self.imagen_actual = 0
        elif(tag < 21):
            self.imagen_actual = 1

            
        self.rect.move_ip(-vx,-vy)# hace que su movimiento no este descuadrado con el mapa, los sincroniza

        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen = self.imagenes[self.imagen_actual]

        #finalmente pintar en la pantalla

        screen.blit(self.imagen,self.rect)

    
        
        
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
        
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()
        
# esta clase general la pantalla gris del lado izquierdo, donde aparece el radar
class Lado(pygame.sprite.Sprite):
    def __init__(self,imagen):

        self.imagen = pygame.image.load(imagen)
        self.rect = self.imagen.get_rect()
        self.rect.top = 0
        self.rect.left = 565

    def update(self,screen,vx,vy):

        vx = 0
        vy = 0
        self.rect.move_ip(vx,vy)
        screen.blit(self.imagen,self.rect)

class Estrellas(pygame.sprite.Sprite): # Esta clase es la del poder de la rata, cuando teclea espacio para detener enemigos

    def __init__(self): # se inicializa el sprite de el poder
        self.imagen = pygame.image.load("pared.png")
        self.rect = self.imagen.get_rect()
        self.rect.left = 230
        self.rect.top = 171

    def update(self,screen,vx,vy): # actualiza el poder mienras esta en el juego
        
        self.rect.move_ip(-vx,-vy)
        screen.blit(self.imagen,self.rect)
            
        
class Queso(pygame.sprite.Sprite): # con esta clase se generan los quesos
    def __init__(self,x,y,imagen):

        self.imagen = pygame.image.load(imagen)
        self.rect = self.imagen.get_rect()
        self.rect.top = y
        self.rect.left = x
        
    def update(self,screen,vx,vy):
        
        self.rect.move_ip(-vx,-vy)
        screen.blit(self.imagen,self.rect)
        
    

# esta clase crea los muros invisibles por los que el raton no avanza
class Paredes(pygame.Rect):
    def __init__(self):

        #lista de paredes
        self.recs = [
                    pygame.Rect((-20,-20),(83,1203)), # pared izquierda
                    pygame.Rect((63,-20),(1170,107)), # pared arriba
                    pygame.Rect((63,1034),(1170,150)), #pared abajo
                    pygame.Rect((1148,107),(103,946)), # pared derecha
                    pygame.Rect((123,180),(99,210)),
                    pygame.Rect((124,466),(104,200)),
                    pygame.Rect((128,735),(99,36)),
                    pygame.Rect((133,831),(95,138)),
                    pygame.Rect((325,176),(121,39)),
                    pygame.Rect((419,215),(27,70)),
                    pygame.Rect((324,293),(29,100)),
                    pygame.Rect((353,362),(94,31)),
                    pygame.Rect((324,467),(112,61)),
                    pygame.Rect((393,528),(42,106)),
                    pygame.Rect((292,620),(27,135)),
                    pygame.Rect((319,720),(68,35)),
                    pygame.Rect((295,832),(292,135)),
                    pygame.Rect((535,177),(129,225)),
                    pygame.Rect((533,483),(362,61)),
                    pygame.Rect((532,621),(112,139)),
                    pygame.Rect((756,177),(132,223)),
                    pygame.Rect((765,620),(134,142)),
                    pygame.Rect((657,827),(258,141)),
                    pygame.Rect((965,175),(106,220)),
                    pygame.Rect((964,478),(106,67)),
                    pygame.Rect((964,620),(108,140)),
                    pygame.Rect((972,827),(103,137))
                    ]
    def update(self,screen,vx,vy):
        
        #para que las paredes se muevan junto al fondo
        for rect in self.recs:
            rect.move_ip(-vx,-vy)
class Paredes2(pygame.Rect):
    def __init__(self):

        #lista de paredes
        self.recs = [pygame.Rect((-20,-20),(107,1105)),
                     pygame.Rect((87,-20),(1149,105)),
                     pygame.Rect((87,975),(1159,117)),
                     pygame.Rect((1133,80),(115,891)),
                     pygame.Rect((161,87),(131,131)),
                     pygame.Rect((365,87),(93,131)),
                     pygame.Rect((531,87),(125,127)),
                     pygame.Rect((163,295),(127,139)),
                     pygame.Rect((365,297),(93,219)),
                     pygame.Rect((163,511),(495,63)),
                     pygame.Rect((527,293),(129,141)),
                     pygame.Rect((85,879),(79,101)),
                     pygame.Rect((163,643),(137,331)),
                     pygame.Rect((369,643),(137,253)),
                     pygame.Rect((567,643),(137,253)),
                     pygame.Rect((731,167),(97,405)),
                     pygame.Rect((915,167),(97,405)),
                     pygame.Rect((789,647),(225,83)),
                     pygame.Rect((789,803),(127,81)),
                     pygame.Rect((1031,801),(103,173))]
        
    def update(self,screen,vx,vy):
        
        #para que las paredes se muevan junto al fondo
        for rect in self.recs:
            rect.move_ip(-vx,-vy)
class Paredes3(pygame.Rect):
    def __init__(self):

        #lista de paredes
        self.recs = [pygame.Rect((-20,-20),(105,1279)),
                     pygame.Rect((-20,-20),(1559,109)),
                     pygame.Rect((-20,1089),(1559,171)),
                     pygame.Rect((1385,-20),(155,1279)),
                     pygame.Rect((185,185),(125,233)),
                     pygame.Rect((221,613),(253,77)),
                     pygame.Rect((193,761),(137,61)),
                     pygame.Rect((193,965),(141,45)),
                     pygame.Rect((293,909),(45,81)),
                     pygame.Rect((425,197),(29,93)),
                     pygame.Rect((421,361),(209,45)),
                     pygame.Rect((553,89),(77,321)),
                     pygame.Rect((421,489),(49,53)),
                     pygame.Rect((421,509),(129,33)),
                     pygame.Rect((457,773),(133,37)),
                     pygame.Rect((557,649),(41,149)),
                     pygame.Rect((421,881),(297,141)),
                     pygame.Rect((709,205),(45,89)),
                     pygame.Rect((881,193),(89,137)),
                     pygame.Rect((1113,189),(133,45)),
                     pygame.Rect((1069,297),(149,145)),
                     pygame.Rect((913,517),(305,69)),
                     pygame.Rect((781,625),(41,137)),
                     pygame.Rect((793,721),(161,37)),
                     pygame.Rect((921,729),(41,137)),
                     pygame.Rect((937,821),(101,33)),
                     pygame.Rect((841,997),(137,25)),
                     pygame.Rect((941,937),(45,81)),
                     pygame.Rect((1029,661),(53,77)),
                     pygame.Rect((1309,661),(73,81)),
                     pygame.Rect((1029,661),(349,25)),
                     pygame.Rect((1309,969),(81,41)),
                     pygame.Rect((1133,817),(85,217)),
                     pygame.Rect((1201,845),(77,37))
                     ]
        
    def update(self,screen,vx,vy):
        
        #para que las paredes se muevan junto al fondo
        for rect in self.recs:
            rect.move_ip(-vx,-vy)
            
            
        
# genera el fondo como un sprite
class Fondo(pygame.sprite.Sprite):

    def __init__(self,imagen):
        self.imagen=pygame.image.load(imagen)
        self.rect=self.imagen.get_rect()
        self.rect.top= -20
        self.rect.left = -20

    def update(self,screen,vx,vy):
        self.rect.move_ip(-vx,-vy)
        screen.blit(self.imagen,self.rect)


class EnemigoA(pygame.sprite.Sprite): # esta clase esta especifica para el enemigo que sale aba
# Maneja casi los mismos parametros que el Player, y solo se direfencia del otro por el movimiento

    def __init__(self,x,y):
        #creo 4 imagenes para el raton
        self.imagen1=pygame.image.load("ratonmalod1.png")
        self.imagen2=pygame.image.load("ratonmalod2.png")
        self.imagen3=pygame.image.load("ratonmalol1.png")
        self.imagen4=pygame.image.load("ratonmalol2.png")

        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]

        self.imagenes = [[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]

        self.imagen_actual=0
        self.p = x
        self.q = y
        self.imagen = self.imagenes[self.imagen_actual][0]
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-25,-25)
        self.rect.left,self.rect.top = (x-10,y-10)

        #variable par ver si se esta moviendo

        self.estamoviendo = False

        # 0 si va ala derecha 1 si va la izquierda

        self.orientacion = 0

    

    #funcion principal de actualizacion

    def update(self,screen,vx,vy,evx,evy,a):

        # si no se mueve self.estamoviendo=FALSE
        if ((evx,evy)==(0,0)):

            self.estamoviendo = False

        else:
            self.estamoviendo = True # si se mueve que este en TRUE

        # con estas 2 lineas cambio la orientacion

        if (evx > 0):
            self.orientacion=0
        elif (evx < 0):
            self.orientacion=1

        # si el a==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if (a==1 and self.estamoviendo):
            self.nextimage()

        # mover el rectangulo
        self.rect.move_ip(-vx,-vy)# hace que su movimiento no este descuadrado con el mapa, los sincroniza
        self.rect.move_ip(evx,evy)#lo mueve independiente del mapa

        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen = self.imagenes[self.orientacion][self.imagen_actual]

        #finalmente pintar en la pantalla

        screen.blit(self.imagen,self.rect)

    #funcion que se encarga de cambiar de imagen

    def nextimage(self):

        self.imagen_actual = self.imagen_actual + 1

        if (self.imagen_actual > (len(self.imagenes)-1)):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0

class EnemigoB(pygame.sprite.Sprite):
    #muy parecido al EnemigoA, solo que este en vez de evx y evy, recibe mvx y mvy
    def __init__(self,x,y):
        #creo 4 imagenes para el raton
        self.imagen1=pygame.image.load("ratonmalod1.png")
        self.imagen2=pygame.image.load("ratonmalod2.png")
        self.imagen3=pygame.image.load("ratonmalol1.png")
        self.imagen4=pygame.image.load("ratonmalol2.png")

        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]

        self.imagenes = [[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]

        self.imagen_actual=0
        self.p = x
        self.q = y
        self.imagen = self.imagenes[self.imagen_actual][0]
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-25,-25)
        self.rect.left,self.rect.top = (x-10,y-10)

        #variable par ver si se esta moviendo

        self.estamoviendo = False

        # 0 si va ala derecha 1 si va la izquierda

        self.orientacion = 0

    

    #funcion principal de actualizacion

    def update(self,screen,vx,vy,mvx,mvy,a):

        # si no se mueve self.estamoviendo=FALSE
        if ((mvx,mvy)==(0,0)):

            self.estamoviendo = False

        else:
            self.estamoviendo = True # si se mueve que este en TRUE

        # con estas 2 lineas cambio la orientacion

        if (mvx > 0):
            self.orientacion=0
        elif (mvx < 0):
            self.orientacion=1

        # si el a==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if (a==1 and self.estamoviendo):
            self.nextimage()

        # mover el rectangulo
        self.rect.move_ip(-vx,-vy) # con este llamado se sincroniza con el mapa
        self.rect.move_ip(mvx,mvy) # con este se mueve por si mismo

        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen = self.imagenes[self.orientacion][self.imagen_actual]

        #finalmente pintar en la pantalla

        screen.blit(self.imagen,self.rect)

    #funcion que se encarga de cambiar de imagen

    def nextimage(self):

        self.imagen_actual = self.imagen_actual + 1

        if (self.imagen_actual > (len(self.imagenes)-1)):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0

class Player(pygame.sprite.Sprite): # la clase del jugador principal
    def __init__(self,x,y):
        #creo 4 imagenes para el raton
        self.imagen1=pygame.image.load("ratond1.png")
        self.imagen2=pygame.image.load("ratond2.png")
        self.imagen3=pygame.image.load("ratonl1.png")
        self.imagen4=pygame.image.load("ratonl2.png")
        self.imagen5=pygame.image.load("ratatran.png")

        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]

        self.imagenes = [[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        self.imagenes2 = [[self.imagen1,self.imagen5,self.imagen2],[self.imagen3,self.imagen5,self.imagen4]]
        
        self.imagen_actual=0
        self.p = x-20
        self.q = y-20
        self.imagen = self.imagenes[self.imagen_actual][0]
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-20,-20)
        self.rect.top,self.rect.left = (x,y)

        #variable par ver si se esta moviendo

        self.estamoviendo = False

        # 0 si va ala derecha 1 si va la izquierda

        self.orientacion = 0

    def mover(self,vx,vy):

       self.rect.move_ip(vx,vy)

    #funcion principal de actualizacion

    def update(self,screen,vx,vy,t,espera):

        # si no se mueve self.estamoviendo=FALSE
        if ((vx,vy)==(0,0)):

            self.estamoviendo = False

        else:
            self.estamoviendo = True # si se mueve que este en TRUE

        # con estas 2 lineas cambio la orientacion

        if (vx > 0):
            self.orientacion=0
        elif (vx < 0):
            self.orientacion=1
        elif(vx > 0 and espera != 36):
            self.orientacion = 2
        elif(vx < 0 and espera != 36):
            self.orientacion = 3

        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if (t==1 and self.estamoviendo):
            self.nextimage(espera)

        # mover el rectangulo
        vx=0
        vy=0
        self.mover(vx, vy)

        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        if ( espera == 36):
            self.imagen = self.imagenes[self.orientacion][self.imagen_actual]
        else:
            self.imagen = self.imagenes2[self.orientacion][self.imagen_actual]
        #finalmente pintar en la pantalla

        screen.blit(self.imagen,(self.q,self.p))

    #funcion que se encarga de cambiar de imagen

    def nextimage(self,espera):

        self.imagen_actual = self.imagen_actual + 1
        if( espera == 36):
            if (self.imagen_actual > (len(self.imagenes)-1)):# si se fue de rango que lo ponga en 0
                self.imagen_actual=0
        else:
            if (self.imagen_actual > (len(self.imagenes2)-1)):# si se fue de rango que lo ponga en 0
                self.imagen_actual=0


def principal(): 
    """
    Va a dar inicio a todos los eventos de pygames,
    y a su ves abre la interfaz inicial.
    """


    pygame.init()  # Inicializa todos los modulos de pygames a la vez
    screen = pygame.display.set_mode([821,461]) # abre la ventana
    pygame.display.set_caption("Rat Taz Taz Game!") # le da el titulo a la ventana de la interfaz
    Cerrar = False # condicional que indica cuando esta abierto el juego
    reloj = pygame.time.Clock() # crea un reloj de tiempo
    tiempoj = pygame.time.get_ticks()/1000
    Jugar1 = False
    Jugar2 = False
    Jugar3 = False
    Tecleo = False
    Menu = True
    Menu2 = False
    Menu3 = False
    Muerte = False
    Enpausa = False
    Howtoplay = False
    Negro1 = False
    Negro2 = False
    Terminar = False
    Creditos = False
    

    # algunos colores
    amarillo = (255,255,0)
    azul = (70,70,190)
    blanco = (255,255,255)
    rojo = (255,36,0)

    #nombre
    A = ""
    B = ""
    C = ""
    D = ""
    E = ""
    F = ""

    #tiempo
    cronometro01= 200
    cronometro1 = 200
    cronometro2 = 150
    cronometro3 = 100
    contadorsegundos = 20
    coj = 0

    #textos
    letra = pygame.font.Font(None,20)
    letra2 = pygame.font.Font(None,50)
    letra3 = pygame.font.Font(None,45)
    letra4 = pygame.font.SysFont("Arial",20,True,True)
    letra5 = pygame.font.SysFont("Arial",20,True,False)
    letra6 = pygame.font.SysFont("Comic Sans MS",30,True,True)
    letra7 = pygame.font.SysFont("Arial",25,True,True)

    playimg1 = pygame.image.load("botonjugar1.png")
    playimg2 = pygame.image.load("botonjugar2.png")
    how1 = pygame.image.load("Howto1.png")
    how2 = pygame.image.load("Howto2.png")
    menu = pygame.image.load("Menu.png")
    menu2 = pygame.image.load("Menu2.png")
    menu3 = pygame.image.load("Menu3.png")
    tecleando = pygame.image.load("Nombre.png")
    guia = pygame.image.load("Guia.png")
    negro = pygame.image.load("Negro.png")

    Fin = pygame.image.load("Fin.png")
    continuarimg1 = pygame.image.load("continuar1.png")
    continuarimg2 = pygame.image.load("continuar2.png")
    salirimg1 = pygame.image.load("Exit1.png")
    salirimg2 = pygame.image.load("Exit2.png")
    men1 = pygame.image.load("botonmen1.png")
    men2 = pygame.image.load("botonmen2.png")

    terminar = pygame.image.load("Terminar.jpg")
    

    Pausa = pygame.image.load("Pause.png")
    
    Cursor1 = Cursor()
    BotonPlay = Boton(playimg1,playimg2,120,260)
    BotonHow = Boton(how1,how2, 420, 210)

    BotonVolver = Boton(men1,men2,557,362)

    BotonContinuarF = Boton(continuarimg1,continuarimg2,413,177)
    BotonSalirF = Boton(salirimg1,salirimg2,463,290)
    
    BotonContinuarP = Boton(continuarimg1,continuarimg2,73,249)
    BotonSalirP = Boton(salirimg1,salirimg2,448,249)

    BotonVolverT = Boton(men1,men2,575,164)
    
    vidas = 3
    puntaje1 = 0
    puntaje2 = 0
    puntaje3 = 0
    espera = 36
    enemigos = [] # lista de enemigos
    genemigos = []
    minienemigos = [] # lista de la imagen de los enemigos en el radar
    quesos = [] # lista de quesos
    mapa1 = Fondo("mapa.jpg") # se inicializa el mapa del nivel 1
    mapa2 = Fondo("mapa2.jpg")
    mapa3 = Fondo("mapa3.jpg")
    raton1 = Player(191,250) # se inicializa el jugador
    fondo1 = Lado("int1.png") # se inicializa el meni donde aparece el radar al lado derecho de la pantalla
    muros = Paredes() # se inicializan las paredes del mapa , para que el raton tenga su laberinto
    enemigo1 = EnemigoA(595,975) # se inicializa un enemigo en la parte de abajo
    enemigo2 = EnemigoB(906,409) # se inicializa un enemigo en la parte de la derecha
    gato1 = Gato(85,342)
    gato2 = Gato(535,800)
    pygame.time.set_timer((pygame.KEYDOWN),1000) # este es un cronometro que no se ha implementado aun, solo esta programado para llevar cuentas daca segundo
    duracion = 21 # variable con la cual se lleva cuenta del tiempo que debe durar el poder del raton en el mapa
    mordida = pygame.mixer.Sound("5969.wav") # se inicializa un sonido, no lo implemente aun porque se bugea
    minirat =  pygame.Rect((620,289),(11,11)) # representacion del raton en el radar

    radar2 = Lado("int2.png")
    radar3 = Lado("int3.png")
    muros2 = Paredes2()
    muros3 = Paredes3()
    
    # se inicializan los quesos del nivel
    queso1 = Queso(385,308,"queso.png") 
    queso2 = Queso(670,644,"queso.png")
    queso3 = Queso(1072,109,"queso.png")
    queso4 = Queso(230,978,"queso.png")


    cuaq5 = pygame.Rect((1070,991),(2,2))
    cuaq6 = pygame.Rect((145,125),(2,2))
    cuaq7 = pygame.Rect((99,693),(2,2))
    cuaq8 = pygame.Rect((696,125),(2,2))
    

    # se adicionan a la lista quesos
    quesos.append(queso1)
    quesos.append(queso2)
    quesos.append(queso3)
    quesos.append(queso4)


    # se adicionan enemigos a la lista enemigos
    enemigos.append(enemigo1)
    enemigos.append(enemigo2)
    genemigos.append(gato2)
    genemigos.append(gato1)
    #se inicializan las imagenes de los quesos en el radar
    miniques1 = pygame.Rect((650,310),(10,10))
    miniques2 = pygame.Rect((712,379),(10,10))
    miniques3 = pygame.Rect((793,279),(10,10))
    miniques4 = pygame.Rect((622,442),(10,10))
    miniques5 = pygame.Rect((796,444),(10,10))
    miniques6 = pygame.Rect((600,277),(10,10))
    miniques7 = pygame.Rect((588,383),(10,10))
    miniques8 = pygame.Rect((711,281),(10,10))
    
    #se inicializan las imagenes de los enemigos en el radar
    minienem1 = pygame.Rect((692,444),(10,10))
    minienem2 = pygame.Rect((754,333),(10,10))
    #se adicionan las imagenes de los enemigos a una lista
    minienemigos.append(minienem1)
    minienemigos.append(minienem2)
    minigat1 = pygame.Rect((645,278),(10,10))
    minigat2 = pygame.Rect((737,360),(10,10))
    #variables para indicar cuando hay o no hay un queso
    noqueso1 = False
    noqueso2 = False
    noqueso3 = False
    noqueso4 = False
    noqueso5 = False
    noqueso6 = False
    noqueso7 = False
    noqueso8 = False
    #velocidad del jugador
    vx,vy = 0,0
    # velocidad del enemigo A
    evx,evy = 10,0
    # velocidad del enemigo B
    mvx,mvy = 10,0
    #variable para indicar velocidad
    velocidad = 10
    #variables temporales implementadas en los ratones para orientacion
    t = 0
    a = 0
    w = 100
    #masvel = False
    tag = 21
    

    # auxiliares de movimiento (rsp = rigth sigue apretada, etc)
    rsp,lsp,usp,dsp = False,False,False,False




    while ( Cerrar == False ): # Loop principal
        
        while( Menu == True): # Loop del menu inicial
           
           screen.blit(menu,(0,0))
           
           for event in pygame.event.get():
               # si se da click en exit, se cierra el juego
               if(event.type == pygame.MOUSEBUTTONDOWN):
                   if (Cursor1.colliderect(BotonHow.rect)):
                       Menu = False
                       Howtoplay = True
                   if (Cursor1.colliderect(BotonPlay.rect)):

                        Tecleo = True
                        Menu = False
                        screen.fill(blanco)
                        vidas = 3
                        puntaje1 = 0
                        puntaje2 = 0
                        puntaje3 = 0
                        espera = 36
                        #nombre
                        A = ""
                        B = ""
                        C = ""
                        D = ""
                        E = ""
                        F = ""
                        cronometro01 = 200
                        cronometro1 = 200
                        contadorsegundos = 20
                        enemigos = [] # lista de enemigos
                        genemigos = []
                        minienemigos = [] # lista de la imagen de los enemigos en el radar
                        quesos = [] # lista de quesos
                        mapa1 = Fondo("mapa.jpg") # se inicializa el mapa del nive
                        raton1 = Player(191,250) # se inicializa el jugador
                        fondo1 = Lado("int1.png") # se inicializa el meni donde aparece el radar al lado derecho de la pantalla
                        muros = Paredes() # se inicializan las paredes del mapa , para que el raton tenga su laberinto
                        enemigo1 = EnemigoA(595,975) # se inicializa un enemigo en la parte de abajo
                        enemigo2 = EnemigoB(906,409) # se inicializa un enemigo en la parte de la derecha
                        pygame.time.set_timer((pygame.KEYDOWN),1000) # este es un cronometro que no se ha implementado aun, solo esta programado para llevar cuentas daca segundo
                        duracion = 21 # variable con la cual se lleva cuenta del tiempo que debe durar el poder del raton en el mapa
                        mordida = pygame.mixer.Sound("5969.wav") # se inicializa un sonido, no lo implemente aun porque se bugea
                        minirat =  pygame.Rect((620,289),(11,11)) # representacion del raton en el radar

                        # se inicializan los quesos del nivel
                        queso1 = Queso(385,308,"queso.png") 
                        queso2 = Queso(670,644,"queso.png")
                        queso3 = Queso(1072,109,"queso.png")
                        queso4 = Queso(230,978,"queso.png")


                        # se adicionan a la lista quesos
                        quesos.append(queso1)
                        quesos.append(queso2)
                        quesos.append(queso3)
                        quesos.append(queso4)


                        cuaq5 = pygame.Rect((1050,991),(2,2))
                        cuaq6 = pygame.Rect((145,125),(2,2))
                        cuaq7 = pygame.Rect((77,690),(2,2))
                        cuaq8 = pygame.Rect((676,105),(2,2))

                        # se adicionan enemigos a la lista enemigos
                        enemigos.append(enemigo1)
                        enemigos.append(enemigo2)
                        gato1 = Gato(85,342)
                        genemigos.append(gato1)
                        gato2 = Gato(535,800)
                        genemigos.append(gato2)

                        #se inicializan las imagenes de los quesos en el radar
                        miniques1 = pygame.Rect((650,310),(10,10))
                        miniques2 = pygame.Rect((712,379),(10,10))
                        miniques3 = pygame.Rect((793,279),(10,10))
                        miniques4 = pygame.Rect((622,442),(10,10))
                        miniques5 = pygame.Rect((796,444),(10,10))
                        miniques6 = pygame.Rect((600,277),(10,10))
                        miniques7 = pygame.Rect((588,383),(10,10))
                        miniques8 = pygame.Rect((711,281),(10,10))

                        #se inicializan las imagenes de los enemigos en el radar
                        minienem1 = pygame.Rect((692,444),(10,10))
                        minienem2 = pygame.Rect((754,333),(10,10))
                        minigat1 = pygame.Rect((645,278),(10,10))
                        minigat2 = pygame.Rect((737,360),(10,10))

                        #se adicionan las imagenes de los enemigos a una lista
                        minienemigos.append(minienem1)
                        minienemigos.append(minienem2)

                        #variables para indicar cuando hay o no hay un queso
                        noqueso1 = False
                        noqueso2 = False
                        noqueso3 = False
                        noqueso4 = False
                        noqueso5 = False
                        noqueso6 = False
                        noqueso7 = False
                        noqueso8 = False

                        #velocidad del jugador
                        vx,vy = 0,0
                        # velocidad del enemigo A
                        evx,evy = 10,0
                        # velocidad del enemigo B
                        mvx,mvy = 10,0
                        #variable para indicar velocidad
                        velocidad = 10
                        #variables temporales implementadas en los ratones para orientacion
                        t = 0
                        a = 0
                        w = 100
                        #masvel = False
                        tag = 21
                                                
                    

                        # auxiliares de movimiento (rsp = rigth sigue apretada, etc)
                        rsp,lsp,usp,dsp = False,False,False,False

                       
                        
               if(event.type == pygame.QUIT):
                   Menu = False
                   Cerrar = True
           
           Cursor1.update()
           BotonPlay.update(screen,Cursor1)
           BotonHow.update(screen,Cursor1)
           pygame.display.update()
           
        while(Howtoplay == True):

            screen.blit(guia,(0,0))

            for event in pygame.event.get():
               # si se da click en exit, se cierra el juego
               if(event.type == pygame.MOUSEBUTTONDOWN):
                   if (Cursor1.colliderect(BotonVolver.rect)):
                       Howtoplay = False
                       Menu = True
                        
                        
               if(event.type == pygame.QUIT):
                   Howtoplay = False
                   Cerrar = True

            texto1 = letra5.render("-Con estas teclas se mueve el jugador",0,(0,0,0))
            texto2 = letra5.render("-Con esta tecla se usa el poder",0,(0,0,0))
            texto3 = letra5.render("-Con 'P' se pausa el juego",0,(0,0,0))
            texto4 = letra5.render("-Jugador principal",0,(0,0,0))
            texto5 = letra5.render("-Enemigos-",0,(0,0,0))
            texto6 = letra5.render("-Quesos principales a recoger ",0,(0,0,0))
            texto7 = letra5.render("-Queso que da una vida extra",0,(0,0,0))
            texto8 = letra5.render("-Queso que aumenta el tiempo",0,(0,0,0))
            texto9 = letra5.render("-Queso que disminuye el puntaje",0,(0,0,0))
            texto10 = letra5.render("y el tiempo en gran cantidad",0,(0,0,0))
            texto11 = letra5.render("y el puntaje",0,(0,0,0))
            texto12 = letra5.render("parapasar de nivel",0,(0,0,0))
            texto13 = letra5.render("(Bloquea los a los ratones)",0,(0,0,0))

            screen.blit(texto1,(138,31))
            screen.blit(texto2,(185,142))
            screen.blit(texto13,(185,162))
            screen.blit(texto3,(148,214))
            screen.blit(texto4,(144,310))
            screen.blit(texto5,(144,401))
            screen.blit(texto6,(547,20))
            screen.blit(texto12,(547,40))
            screen.blit(texto7,(547,116))
            screen.blit(texto8,(547,211))
            screen.blit(texto11,(547,231))
            screen.blit(texto9,(547,297))
            screen.blit(texto10,(547,317))
            
            Cursor1.update()
            BotonVolver.update(screen,Cursor1)
            pygame.display.update()
            
        
        while (Tecleo == True):

            screen.blit(tecleando,(0,0))

            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        if(A != ""):
                            Tecleo = False
                            Jugar1 = True
                            screen.fill(blanco)
                    elif (event.key == pygame.K_DELETE):
                        if (F != ""):
                            F = ""
                        elif(E != ""):
                            E = ""
                        elif(D != ""):
                            D = ""
                        elif(C != ""):
                            C = ""
                        elif(B != ""):
                            B = ""
                        elif(A != ""):
                            A = ""
                    elif(event.key  == pygame.K_a):
                        if (A == ""):
                            A = "A"
                        elif(B == ""):
                            B = "A"
                        elif(C == ""):
                            C = "A"
                        elif(D == ""):
                            D = "A"
                        elif(E == ""):
                            E = "A"
                        elif(F == ""):
                            F = "A"
                    elif(event.key  == pygame.K_b):
                        if (A == ""):
                            A = "B"
                        elif(B == ""):
                            B = "B"
                        elif(C == ""):
                            C = "B"
                        elif(D == ""):
                            D = "B"
                        elif(E == ""):
                            E = "B"
                        elif(F == ""):
                            F = "B"
                    elif(event.key  == pygame.K_c):
                        if (A == ""):
                            A = "C"
                        elif(B == ""):
                            B = "C"
                        elif(C == ""):
                            C = "C"
                        elif(D == ""):
                            D = "C"
                        elif(E == ""):
                            E = "C"
                        elif(F == ""):
                            F = "C"
                    elif(event.key  == pygame.K_d):
                        if (A == ""):
                            A = "D"
                        elif(B == ""):
                            B = "D"
                        elif(C == ""):
                            C = "D"
                        elif(D == ""):
                            D = "D"
                        elif(E == ""):
                            E = "D"
                        elif(F == ""):
                            F = "D"
                    elif(event.key  == pygame.K_e):
                        if (A == ""):
                            A = "E"
                        elif(B == ""):
                            B = "E"
                        elif(C == ""):
                            C = "E"
                        elif(D == ""):
                            D = "E"
                        elif(E == ""):
                            E = "E"
                        elif(F == ""):
                            F = "E"
                    elif(event.key  == pygame.K_f):
                        if (A == ""):
                            A = "F"
                        elif(B == ""):
                            B = "F"
                        elif(C == ""):
                            C = "F"
                        elif(D == ""):
                            D = "F"
                        elif(E == ""):
                            E = "F"
                        elif(F == ""):
                            F = "F"
                    elif(event.key  == pygame.K_g):
                        if (A == ""):
                            A = "G"
                        elif(B == ""):
                            B = "G"
                        elif(C == ""):
                            C = "G"
                        elif(D == ""):
                            D = "G"
                        elif(E == ""):
                            E = "G"
                        elif(F == ""):
                            F = "G"
                    elif(event.key  == pygame.K_h):
                        if (A == ""):
                            A = "H"
                        elif(B == ""):
                            B = "H"
                        elif(C == ""):
                            C = "H"
                        elif(D == ""):
                            D = "H"
                        elif(E == ""):
                            E = "H"
                        elif(F == ""):
                            F = "H"
                    elif(event.key  == pygame.K_i):
                        if (A == ""):
                            A = "I"
                        elif(B == ""):
                            B = "I"
                        elif(C == ""):
                            C = "I"
                        elif(D == ""):
                            D = "I"
                        elif(E == ""):
                            E = "I"
                        elif(F == ""):
                            F = "I"
                    elif(event.key  == pygame.K_j):
                        if (A == ""):
                            A = "J"
                        elif(B == ""):
                            B = "J"
                        elif(C == ""):
                            C = "J"
                        elif(D == ""):
                            D = "J"
                        elif(E == ""):
                            E = "J"
                        elif(F == ""):
                            F = "J"
                    elif(event.key  == pygame.K_k):
                        if (A == ""):
                            A = "K"
                        elif(B == ""):
                            B = "K"
                        elif(C == ""):
                            C = "K"
                        elif(D == ""):
                            D = "K"
                        elif(E == ""):
                            E = "K"
                        elif(F == ""):
                            F = "K"
                    elif(event.key  == pygame.K_l):
                        if (A == ""):
                            A = "L"
                        elif(B == ""):
                            B = "L"
                        elif(C == ""):
                            C = "L"
                        elif(D == ""):
                            D = "L"
                        elif(E == ""):
                            E = "L"
                        elif(F == ""):
                            F = "L"
                    elif(event.key  == pygame.K_m):
                        if (A == ""):
                            A = "M"
                        elif(B == ""):
                            B = "M"
                        elif(C == ""):
                            C = "M"
                        elif(D == ""):
                            D = "M"
                        elif(E == ""):
                            E = "M"
                        elif(F == ""):
                            F = "M"
                    elif(event.key  == pygame.K_n):
                        if (A == ""):
                            A = "N"
                        elif(B == ""):
                            B = "N"
                        elif(C == ""):
                            C = "N"
                        elif(D == ""):
                            D = "N"
                        elif(E == ""):
                            E = "N"
                        elif(F == ""):
                            F = "N"
                    elif(event.key  == pygame.K_o):
                        if (A == ""):
                            A = "O"
                        elif(B == ""):
                            B = "O"
                        elif(C == ""):
                            C = "O"
                        elif(D == ""):
                            D = "O"
                        elif(E == ""):
                            E = "O"
                        elif(F == ""):
                            F = "O"
                    elif(event.key  == pygame.K_p):
                        if (A == ""):
                            A = "P"
                        elif(B == ""):
                            B = "P"
                        elif(C == ""):
                            C = "P"
                        elif(D == ""):
                            D = "P"
                        elif(E == ""):
                            E = "P"
                        elif(F == ""):
                            F = "P"
                    elif(event.key  == pygame.K_q):
                        if (A == ""):
                            A = "Q"
                        elif(B == ""):
                            B = "Q"
                        elif(C == ""):
                            C = "Q"
                        elif(D == ""):
                            D = "Q"
                        elif(E == ""):
                            E = "Q"
                        elif(F == ""):
                            F = "Q"
                    elif(event.key  == pygame.K_r):
                        if (A == ""):
                            A = "R"
                        elif(B == ""):
                            B = "R"
                        elif(C == ""):
                            C = "R"
                        elif(D == ""):
                            D = "R"
                        elif(E == ""):
                            E = "R"
                        elif(F == ""):
                            F = "R"
                    elif(event.key  == pygame.K_s):
                        if (A == ""):
                            A = "S"
                        elif(B == ""):
                            B = "S"
                        elif(C == ""):
                            C = "S"
                        elif(D == ""):
                            D = "S"
                        elif(E == ""):
                            E = "S"
                        elif(F == ""):
                            F = "S"
                    elif(event.key  == pygame.K_t):
                        if (A == ""):
                            A = "T"
                        elif(B == ""):
                            B = "T"
                        elif(C == ""):
                            C = "T"
                        elif(D == ""):
                            D = "T"
                        elif(E == ""):
                            E = "T"
                        elif(F == ""):
                            F = "T"
                    elif(event.key  == pygame.K_u):
                        if (A == ""):
                            A = "U"
                        elif(B == ""):
                            B = "U"
                        elif(C == ""):
                            C = "U"
                        elif(D == ""):
                            D = "U"
                        elif(E == ""):
                            E = "U"
                        elif(F == ""):
                            F = "U"
                    elif(event.key  == pygame.K_v):
                        if (A == ""):
                            A = "V"
                        elif(B == ""):
                            B = "V"
                        elif(C == ""):
                            C = "V"
                        elif(D == ""):
                            D = "V"
                        elif(E == ""):
                            E = "V"
                        elif(F == ""):
                            F = "V"
                    elif(event.key  == pygame.K_w):
                        if (A == ""):
                            A = "W"
                        elif(B == ""):
                            B = "W"
                        elif(C == ""):
                            C = "W"
                        elif(D == ""):
                            D = "W"
                        elif(E == ""):
                            E = "W"
                        elif(F == ""):
                            F = "W"
                    elif(event.key  == pygame.K_x):
                        if (A == ""):
                            A = "X"
                        elif(B == ""):
                            B = "X"
                        elif(C == ""):
                            C = "X"
                        elif(D == ""):
                            D = "X"
                        elif(E == ""):
                            E = "X"
                        elif(F == ""):
                            F = "X"
                    elif(event.key  == pygame.K_y):
                        if (A == ""):
                            A = "Y"
                        elif(B == ""):
                            B = "Y"
                        elif(C == ""):
                            C = "Y"
                        elif(D == ""):
                            D = "Y"
                        elif(E == ""):
                            E = "Y"
                        elif(F == ""):
                            F = "Y"
                    elif(event.key  == pygame.K_z):
                        if (A == ""):
                            A = "Z"
                        elif(B == ""):
                            B = "Z"
                        elif(C == ""):
                            C = "Z"
                        elif(D == ""):
                            D = "Z"
                        elif(E == ""):
                            E = "Z"
                        elif(F == ""):
                            F = "Z"
                        
                   
                       
                if(event.type == pygame.QUIT):
                    Tecleo = False
                    Cerrar = True
                    
                    
            NombreJ = A+B+C+D+E+F
            texto1 = letra2.render("Teclee su nombre:", 0 ,(255,255,255))
            texto2 = letra2.render(A+B+C+D+E+F ,0,(0,0,255))
            texto3 = letra3.render("-Nombre maximo de 6 caracteres(solo letras)",0,(255,0,0))
            texto4 = letra3.render("-'Espacio' para entrar al juego al acabar su nombre",0,(255,0,0))
            texto5 = letra3.render("-'Suprimir' para borrar un caracter",0,(255,0,0))

            screen.blit(texto1,(100,400))
            screen.blit(texto2,(450,400))
            screen.blit(texto3,(20,100))
            screen.blit(texto4,(20,180))
            screen.blit(texto5,(20,260))

            pygame.display.update()
        while (Muerte == True):
            screen.blit(Fin,(0,0))
           
            for event in pygame.event.get():
                # si se da click en exit, se cierra el juego
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if (Cursor1.colliderect(BotonContinuarF.rect)):

                        Menu = True
                        Muerte = False
                    if (Cursor1.colliderect(BotonSalirF.rect)):
                        Muerte = False
                        Cerrar = True
                        
                if(event.type == pygame.QUIT):
                   Muerte = False
                   Cerrar = True
                   
            Cursor1.update()
            BotonContinuarF.update(screen,Cursor1)
            BotonSalirF.update(screen,Cursor1)
            pygame.display.update()

            
            
        while( Jugar1 == True):
            
            while ( Enpausa == True):
            
                screen.blit(Pausa,(20,20))

                for event in pygame.event.get():
                    # si se da click en exit, se cierra el juego
                    if(event.type == pygame.MOUSEBUTTONDOWN):
                        if (Cursor1.colliderect(BotonContinuarP.rect)):

                            Enpausa = False
                            
                        if (Cursor1.colliderect(BotonSalirP.rect)):
                            EnPausa = False
                            Jugar1 = False
                            Menu = True
                            
                    if(event.type == pygame.QUIT):
                        EnPausa = False
                        Jugar1 = False
                        Cerrar = True
                        
                Cursor1.update()
                BotonContinuarP.update(screen,Cursor1)
                BotonSalirP.update(screen,Cursor1)
                pygame.display.update()
            
            
            for rect in muros.recs:
                
               #Colision del raton con el mapa
                if (raton1.rect.colliderect(rect)):
                    
                    if ( vx == velocidad ):
                        mapa1.update(screen,vx-20,vy)
                        muros.update(screen,vx-20,vy)
                        for enem in enemigos:
                            enem.update(screen,vx-20,vy,0,0,a)
                        gato1.update(screen,vx-20,vy,tag)
                        gato2.update(screen,vx-20,vy,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx-20,vy)
                        for ques in quesos:
                            ques.update(screen,vx-20,vy)
                        
                        vx = 0
                        vy = random.randrange(-10,11,20)
                        
                    elif( vx == -velocidad ):
                        mapa1.update(screen,vx+30,vy)
                        muros.update(screen,vx+30,vy)
                        for enem in enemigos:
                            enem.update(screen,vx+30,vy,0,0,a)
                        gato1.update(screen,vx+30,vy,tag)
                        gato2.update(screen,vx+30,vy,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx+30,vy)
                        for ques in quesos:
                            ques.update(screen,vx+30,vy)
                              
                        vx = 0
                        vy = random.randrange(-10,11,20)
                       
                    elif ( vy == velocidad ):
                        mapa1.update(screen,vx,vy-20)
                        muros.update(screen,vx,vy-20)
                        for enem in enemigos:
                            enem.update(screen,vx,vy-20,0,0,a)
                        gato1.update(screen,vx,vy-20,tag)
                        gato2.update(screen,vx,vy-20,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx,vy-20)
                        for ques in quesos:  
                            ques.update(screen,vx,vy-20)
                        
                        vy = 0
                        vx = random.randrange(-10,11,20)
                        
                    elif( vy == -velocidad ):
                        mapa1.update(screen,vx,vy+25)
                        muros.update(screen,vx,vy+25)
                        for enem in enemigos:
                            enem.update(screen,vx,vy+25,0,0,a)
                        gato2.update(screen,vx,vy+25,tag)
                        gato1.update(screen,vx,vy+25,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx,vy+25)
                        for ques in quesos:
                            ques.update(screen,vx,vy+25)
                                
                        vy = 0
                        vx = random.randrange(-10,11,20)
                        
                # colision del enemigo A con el mapa
                if(enemigo1.rect.colliderect(rect)):
                    if(evx == 10):
                        enemigo1.update(screen,vx,vy,-23,0,a)
                        
                        evx = 0
                        evy = random.randrange(-10,11,20)
                    elif(evx == -10):
                        enemigo1.update(screen,vx,vy,23,0,a)
                        evx = 0
                        evy = random.randrange(-10,11,20)
                    elif(evy == 10):
                        enemigo1.update(screen,vx,vy,0,-23,a)
                        evx = random.randrange(-10,11,20)
                        evy = 0
                    elif(evy == -10):
                        enemigo1.update(screen,vx,vy,0,23,a)
                        evx = random.randrange(-10,11,20)
                        evy = 0
                 #colision del enemigo B con el mapa
                if(enemigo2.rect.colliderect(rect)):
                    if(mvx == 10):
                        enemigo2.update(screen,vx,vy,-23,0,a)
                        mvx = 0
                        mvy = random.randrange(-10,11,20)
                    elif(mvx == -10):
                        enemigo2.update(screen,vx,vy,23,0,a)
                        mvx = 0
                        mvy = random.randrange(-10,11,20)
                    elif(mvy == 10):
                        enemigo2.update(screen,vx,vy,0,-23,a)
                        mvx = random.randrange(-10,11,20)
                        mvy = 0
                    elif(mvy == -10):
                        enemigo2.update(screen,vx,vy,0,23,a)
                        mvx = random.randrange(-10,11,20)
                        mvy = 0
            for enem in enemigos:
                if(raton1.rect.colliderect(enem) and espera == 36):
                    vidas = vidas - 1
                    espera = 35
            for gato in genemigos:
                if(raton1.rect.colliderect(gato)and espera == 36):
                    vidas = vidas - 1
                    espera = 35
                    tag = 20
                    
                    
            # Se indican los eventos, las acciones de las teclas
            for event in pygame.event.get():
                # si se da click en exit, se cierra el juego
                if(event.type == pygame.QUIT):
                    Jugar1 = False
                    Cerrar = True
                # para cuando se unde alguna tecla
                if (event.type == pygame.KEYDOWN):
                     # para cuando se unde la flecha hacia la derecha, el raton se mueva hacia la derecha
                    if (event.key == pygame.K_RIGHT):
                        if( vy != 0):
                            vy = 0
                            rsp = True
                            vx =  velocidad
                        else:
                            rsp = True
                            vx =  velocidad
                    # cuando se unde hacia la izquierda, va a la izquierda
                    elif (event.key == pygame.K_LEFT):
                        if( vy != 0):
                            vy = 0
                            lsp = True
                            vx = -velocidad
                        else:
                            lsp = True
                            vx = -velocidad
                    # para cuando se unde la flecha hacia arriba, el raton se mueva hacia arriba
                    elif (event.key == pygame.K_UP):
                        if( vx != 0):
                            vx = 0
                            usp = True
                            vy = -velocidad
                        else:
                            usp = True
                            vy = -velocidad
                    # para cuando se unde la flecha hacia abajo, el raton se mueva hacia abajo
                    elif (event.key == pygame.K_DOWN):
                        if( vx != 0):
                            vx = 0
                            dsp = True
                            vy = velocidad
                        else:
                            dsp = True
                            vy = velocidad
                     # para que cuando se unda ESPACIO, aparezca el bloque para defenderse de los enemigos
                    if(event.key == pygame.K_SPACE):
                        if( duracion >20): # regula el tiempo que va a durar

                            duracion = duracion -1
                            estrellas = Estrellas()
                            
                    if(event.key == pygame.K_p):
                        Enpausa = True
                        
                                
                                

            reloj.tick(20) # Hace que este ciclo se repita a 20 fps(frames per second)
            # se suma el contador de animacion
            t = t + 1
            if (t > 1):
                t = 0
            a = a + 1
            if (a > 1):
                a = 0
##            if(masvel == True):
##                if(w > 0):
##                    if(vx > 0):
##                        vx = vx + 0.5
##                    if(vx < 0):
##                        vx = vx - 0.5
##                    if(vy > 0):
##                        vy = vy + 0.5
##                    if (vy < 0):
##                        vy = vy - 0.5
##                    w = w - 1
##                if(w == 0):
##                    masvel = False
##                    w = 100
         
                    
            textnombre = letra4.render("Jugador : "+NombreJ,0,(0,0,0))
            texttiempo = letra4.render("Tiempo Restante : "+str(cronometro1),0,(0,0,0))
            textvidas = letra4.render("Vidas : "+str(vidas) , 0 , (0,0,0))
            textpuntaje1 = letra4.render("Puntaje : "+str(puntaje1),0,(0,0,0))
            textnivel = letra4.render("Nivel 1",0,(0,0,0))
            screen.fill(blanco) # pinta el fondo blanco para empezar
            # se actualizan todos los sprites y rectandulos del juego con las nuevas variables
            mapa1.update(screen,vx,vy)
            muros.update(screen,vx,vy)
            cuaq5.move_ip(-vx,-vy)
            cuaq6.move_ip(-vx,-vy)
            cuaq7.move_ip(-vx,-vy)
            cuaq8.move_ip(-vx,-vy)
            raton1.update(screen,vx,vy,t,espera)
            enemigo1.update(screen,vx,vy,evx,evy,a)
            enemigo2.update(screen,vx,vy,mvx,mvy,a)
            gato1.update(screen,vx,vy,tag)
            gato2.update(screen,vx,vy,tag)
            #Estos condicionales, revisan si el queso ya fue comido o no
            if(noqueso1 == False):
                queso1.update(screen,vx,vy)
            if(noqueso2 == False):
                queso2.update(screen,vx,vy)
            if(noqueso3 == False):
                queso3.update(screen,vx,vy)
            if(noqueso4 == False):
                queso4.update(screen,vx,vy)
            if(cronometro01 < 100 and cronometro01 > 80):
                if(noqueso5 == False):
                    queso5.update(screen,vx,vy)
            if(cronometro01 < 150 and cronometro01 > 120):
                if(noqueso6 == False):
                    queso6.update(screen,vx,vy)
            if(cronometro01 < 180 and cronometro01 > 160):
                if(noqueso7 == False):
                    queso7.update(screen,vx,vy)
            if(cronometro01 < 180 and cronometro01 > 40):
                if(noqueso8 == False):
                    queso8.update(screen,vx,vy)
            # este condicional reviza si el poder ha sido actuvado o no
            if(duracion > 0 and duracion < 21):
                estrellas.update(screen,vx,vy)
            fondo1.update(screen,vx,vy)
            screen.blit(textnivel,(584,37))
            screen.blit(textvidas,(584,127))
            screen.blit(textpuntaje1,(584,157))
            screen.blit(textnombre,(584,97))
            screen.blit(texttiempo,(584,67))

            # se inicializan las imagenes del radar
            pygame.draw.rect(screen,azul,minirat)
            pygame.draw.rect(screen,rojo,minigat1)
            pygame.draw.rect(screen,rojo,minigat2)
            pygame.draw.rect(screen,rojo,minienem1)
            pygame.draw.rect(screen,rojo,minienem2)


                
            
            # para sincronizar al raton principal con el raton del mapa
            if(vx == 0 and vy == velocidad):

                m = 0
                n = 2
                for rect in muros.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(0,-2.5)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                        
                minirat.move_ip(m,n)
                    
                
            elif(vx == 0 and vy == -velocidad):

                m = 0
                n = -2
                for rect in muros.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(0,3)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                        
                minirat.move_ip(m,n)
                    

            elif(vx == velocidad and vy == 0):

                m = 2
                n = 0
                for rect in muros.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(-2.5,0)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                minirat.move_ip(m,n)
                    

            elif(vx == -velocidad and vy == 0):

                m = -2
                n = 0
                for rect in muros.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(4,0)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                        
                minirat.move_ip(m,n)

            # Indica que mientras este en el juego el bloque, si algun enemigo colisiona con el, cambia de direccion
            if(duracion > 0 and duracion < 21):
                if(enemigo1.rect.colliderect(estrellas.rect)):
                    if(evx == 10):
                        enemigo1.update(screen,vx,vy,-25,0,a)
                        evx = -10
                        
                    elif(evx == -10):
                        enemigo1.update(screen,vx,vy,25,0,a)
                        evx = 10
                    elif(evy == 10):
                        enemigo1.update(screen,vx,vy,0,-25,a)
                        evy = -10
                    elif(evy == -10):
                        enemigo1.update(screen,vx,vy,0,25,a)
                        evy = 10

                if(enemigo2.rect.colliderect(estrellas.rect)):
                    if(mvx == 10):
                        enemigo2.update(screen,vx,vy,-25,0,a)
                        mvx = -10
                    elif(mvx == -10):
                        enemigo2.update(screen,vx,vy,25,0,a)
                        mvx = 10
                    elif(mvy == 10):
                        enemigo2.update(screen,vx,vy,0,-25,a)
                        mvy = -10
                    elif(mvy == -10):
                        enemigo2.update(screen,vx,vy,0,25,a)
                        mvy = 10
                        
            # sincroniza al enemigo A con su imagen en el radar        
            if(evx == 10 and evy == 0):

                    g = 2
                    f = 0
                    for rect in muros.recs:
                        if( enemigo1.rect.colliderect(rect)):
                            minienem1.move_ip(-4,0)
                    minienem1.move_ip(g,f)

            elif(evx == -10 and evy == 0):

                    g = -2
                    f = 0
                    for rect in muros.recs:
                        if( enemigo1.rect.colliderect(rect)):
                            minienem1.move_ip(4,0)
                    minienem1.move_ip(g,f)

            elif(evy == 10 and evx == 0):

                    g = 0
                    f = 2
                    for rect in muros.recs:
                        if( enemigo1.rect.colliderect(rect)):
                            minienem1.move_ip(0,-4)
                    minienem1.move_ip(g,f)

            elif(evy == -10 and evx == 0):

                    g = 0
                    f = -2
                    for rect in muros.recs:
                        if( enemigo1.rect.colliderect(rect)):
                            minienem1.move_ip(0,4)
                    minienem1.move_ip(g,f)

            # sincroniza al enemigo B con su imagen en el radar
            if(mvx == 10 and mvy == 0):

                    p = 2
                    q = 0
                    for rect in muros.recs:
                        if( enemigo2.rect.colliderect(rect)):
                            minienem2.move_ip(-4,0)
                    minienem2.move_ip(p,q)
                    
            elif(mvx == -10 and mvy == 0):

                    p = -2
                    q = 0
                    for rect in muros.recs:
                        if( enemigo2.rect.colliderect(rect)):
                            minienem2.move_ip(4,0)
                    minienem2.move_ip(p,q)

            elif(mvy == 10 and mvx == 0):

                    p = 0
                    q = 2
                    for rect in muros.recs:
                        if( enemigo2.rect.colliderect(rect)):
                            minienem2.move_ip(0,-4)
                    minienem2.move_ip(p,q)

            elif(mvy == -10 and mvx == 0):

                    p = 0
                    q = -2
                    for rect in muros.recs:
                        if( enemigo2.rect.colliderect(rect)):
                            minienem2.move_ip(0,4)
                    minienem2.move_ip(p,q)
            
            # Siempre que esta variable sea falza, el queso se va a dibujar en el radar
            if(noqueso1 == False):
                pygame.draw.rect(screen,amarillo,miniques1)

            # cuando colisiona el raton con el queso, este tiene que desaparecer, es igual con todos los demas quesos
            if(raton1.rect.colliderect(queso1.rect)):
                    queso1.rect.left,queso1.rect.top = (-67,-47)
                    miniques1.move(-11,-11)
                    noqueso1 = True
                    puntaje1 = puntaje1 + 200
                    coj = coj + 1
                    
                    

            if(noqueso2 == False):
                pygame.draw.rect(screen,amarillo,miniques2)

            if(raton1.rect.colliderect(queso2.rect)):
                    queso2.rect.left,queso2.rect.top =(-67,-47)
                    miniques2.move(-11,-11)
                    noqueso2 = True
                    puntaje1 = puntaje1 + 200
                    coj = coj + 1
                    

            if(noqueso3 == False):
                pygame.draw.rect(screen,amarillo,miniques3)

            if(raton1.rect.colliderect(queso3.rect)):
                    queso3.rect.left,queso3.rect.top =(-67,-47)
                    miniques3.move(-11,-11)
                    noqueso3 = True
                    puntaje1 = puntaje1 + 200
                    coj = coj + 1
                    

            if(noqueso4 == False):
                pygame.draw.rect(screen,amarillo,miniques4)

            if(raton1.rect.colliderect(queso4.rect)):
                    queso4.rect.left,queso4.rect.top =(-67,-47)
                    miniques4.move(-11,-11)
                    noqueso4 = True
                    puntaje1 = puntaje1 + 200
                    coj = coj + 1
                    
            if(cronometro01 == 100):
                queso5 = Queso(cuaq5.left,cuaq5.top,"quesoblanco.png")
                quesos.append(queso5)

            if(cronometro01 < 100 and cronometro01 > 80):
                    
                if(noqueso5 == False):
                    pygame.draw.rect(screen, blanco,miniques5)

                if(raton1.rect.colliderect(queso5.rect)):
                        queso5.rect.left,queso5.rect.top =(-67,-47)
                        miniques5.move(-11,-11)
                        noqueso5 = True
                        vidas = vidas + 1
                        puntaje1 = puntaje1 + 20
                        coj = coj + 1
                        
            if(cronometro01 == 150):
                
                        queso6 = Queso(cuaq6.left,cuaq6.top,"quesoblanco.png")
                        quesos.append(queso6)
            if(cronometro01 < 150 and cronometro01 > 120):
                    
                if(noqueso6 == False):
                    pygame.draw.rect(screen, blanco,miniques6)

                if(raton1.rect.colliderect(queso6.rect)):
                        queso6.rect.left,queso6.rect.top =(-67,-47)
                        miniques6.move(-11,-11)
                        noqueso6 = True
                        vidas = vidas + 1
                        puntaje1 = puntaje1 + 20
                        coj = coj + 1
                        
            if(cronometro01 == 180):
                queso7 = Queso(cuaq7.left,cuaq7.top,"quesorojo.png")
                quesos.append(queso7)
            if(cronometro01 < 180 and cronometro01 > 160):
                    
                if(noqueso7 == False):
                    pygame.draw.rect(screen,(230, 95, 0),miniques7)

                if(raton1.rect.colliderect(queso7.rect)):
                        queso7.rect.left,queso7.rect.top =(-67,-47)
                        miniques7.move(-11,-11)
                        noqueso7 = True
                        #masvel = True
                        puntaje1 = puntaje1 + 20
                        cronometro1 = cronometro1 + 10
                        coj = coj + 1
                        
            if(cronometro01 == 180):
                queso8 = Queso(cuaq8.left,cuaq8.top,"quesoverde.png")
                quesos.append(queso8)
                
            if(cronometro01 < 180 and cronometro01 > 40):
                    
                if(noqueso8 == False):
                    pygame.draw.rect(screen,(0, 255, 0),miniques8)

                if(raton1.rect.colliderect(queso8.rect)):
                        queso8.rect.left,queso8.rect.top =(-67,-47)
                        miniques8.move(-11,-11)
                        noqueso8 = True
                        puntaje1 = puntaje1 - 300
                        cronometro1 = cronometro1 -50
                        coj = coj + 1
                        

            # se regula la duracion del poder del raton, debe durar aprox 1s, y cuando este contador llega a 0, se reinicia a 21, su valor inicial
            if( duracion < 21):
                duracion = duracion -1
            if(duracion == 0):
                duracion = 21
                
            if( espera < 36):
                espera = espera - 1
            if( espera == 0):
                espera = 36
                
            if(tag < 21):
                tag = tag - 1
            if(tag ==0):
                tag = 21

            contadorsegundos = contadorsegundos - 1

            if( contadorsegundos == 0):
                contadorsegundos = 20
                cronometro1 = cronometro1 - 1
                cronometro01 = cronometro01 - 1
                
            if(cronometro1 == 0 or vidas == 0):
                Jugar1 = False
                Muerte = True
            if( noqueso1 == True and noqueso2 == True and noqueso3 == True and noqueso4 == True):
                Jugar1 = False
                Menu2 = True

            pygame.display.update() # Actualiza la pantalla cada vez que se hace un evento
             # Los eventos son cualquier interaccion con el juego(clicks, teclas, etc), tambien sirve la funcion pygame.display.flip()

        while(Menu2 == True):
            
            screen.blit(menu2,(0,0))

            for event in pygame.event.get():
               # si se da click en exit, se cierra el juego
               if(event.type == pygame.MOUSEBUTTONDOWN):
                   if (Cursor1.colliderect(BotonPlay.rect)):
                       
                        Negro1 = True
                        Menu2 = False
                        radar2 = Lado("int2.png")
                        raton1 = Player(221,243)

                       
                        screen.fill(blanco)
                        puntaje2 = 0
                        puntaje3 = 0
                        espera = 36
                        
                        cronometro02 = 140
                        cronometro2 = 140
                        contadorsegundos = 20
                        
    
                        quesos = [] # lista de quesos
                        enemigos = []
                        genemigos = []
                        gato1 = Gato(557,201)
                        gato2 = Gato(81,923)
                        gato3 = Gato(879,517)
                        gato4 = Gato(215,535)
                        enemigo1 = EnemigoA(295,443) # se inicializa un enemigo en la parte de abajo
                        enemigo2 = EnemigoB(1043,713) # se inicializa un enemigo en la parte de la derecha
                    
                        duracion = 21 # variable con la cual se lleva cuenta del tiempo que debe durar el poder del raton en el mapa
                        mordida = pygame.mixer.Sound("5969.wav") # se inicializa un sonido, no lo implemente aun porque se bugea
                        minirat =  pygame.Rect((622,296),(11,11)) # representacion del raton en el radar

                        # se inicializan los quesos del nivel
                        queso1 = Queso(101,825,"queso.png") 
                        queso2 = Queso(481,447,"queso.png")
                        queso3 = Queso(1033,107,"queso.png")
                        queso4 = Queso(943,895,"queso.png")
                        queso9 = Queso(315,899,"queso.png")


                        # se adicionan a la lista quesos
                        quesos.append(queso1)
                        quesos.append(queso2)
                        quesos.append(queso3)
                        quesos.append(queso4)
                        quesos.append(queso9)


                        cuaq5 = pygame.Rect((595,597),(2,2))
                        cuaq6 = pygame.Rect((311,99),(2,2))
                        cuaq7 = pygame.Rect((841,315),(2,2))
                        cuaq8 = pygame.Rect((401,895),(2,2))
                        cuaq10 = pygame.Rect((99,99),(2,2))
                        cuaq11 = pygame.Rect((99,645),(2,2))

                        # se adicionan enemigos a la lista enemigos
                        enemigos.append(enemigo1)
                        enemigos.append(enemigo2)
                        genemigos.append(gato1)
                        genemigos.append(gato2)
                        genemigos.append(gato3)
                        genemigos.append(gato4)

                        #se inicializan las imagenes de los quesos en el radar
                        miniques1 = pygame.Rect((596,425),(10,10))
                        miniques2 = pygame.Rect((675,348),(10,10))
                        miniques3 = pygame.Rect((792,278),(10,10))
                        miniques4 = pygame.Rect((770,445),(10,10))
                        miniques5 = pygame.Rect((699,379),(10,10))
                        miniques6 = pygame.Rect((635,276),(10,10))
                        miniques7 = pygame.Rect((754,327),(10,10))
                        miniques8 = pygame.Rect((715,303),(10,10))
                        miniques9 = pygame.Rect((642,446),(10,10))
                        miniques10 = pygame.Rect((594,275),(10,10))
                        miniques11 = pygame.Rect((594,386),(10,10))


                        #variables para indicar cuando hay o no hay un queso
                        noqueso1 = False
                        noqueso2 = False
                        noqueso3 = False
                        noqueso4 = False
                        noqueso5 = False
                        noqueso6 = False
                        noqueso7 = False
                        noqueso8 = False
                        noqueso9 = False
                        noqueso10 = False
                        noqueso11 = False

                        #velocidad del jugador
                        vx,vy = 0,0
                        # velocidad del enemigo A
                        evx,evy = 10,0
                        # velocidad del enemigo B
                        mvx,mvy = 10,0
                        #variable para indicar velocidad
                        velocidad = 10
                        #variables temporales implementadas en los ratones para orientacion
                        t = 0
                        a = 0
                        w = 100
                        tag = 21
                        
                        rsp,lsp,usp,dsp = False,False,False,False
                        
                        
               if(event.type == pygame.QUIT):
                   Menu2 = False
                   Cerrar = True
            Cursor1.update()
            BotonPlay.update(screen,Cursor1)
           
            pygame.display.update()
        while(Negro1 == True):

            screen.blit(negro,(0,0))

            texto1 = letra6.render("Muy Facil???",0,amarillo)
            texto2 = letra6.render("Ahora no se veran los enemigos en el radar",0,rojo)
            texto3 = letra6.render("Teclear 'Espacio' para continuar",0,azul)

            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                     # para cuando se unde la flecha hacia la derecha, el raton se mueva hacia la derecha
                    if (event.key == pygame.K_SPACE):
                        screen.fill(blanco)
                        Negro1 = False
                        Jugar2 = True
                if(event.type == pygame.QUIT):
                    Negro1 = False
                    Cerrar = True
            screen.blit(texto1,(350,110))
            screen.blit(texto2,(70,240))
            screen.blit(texto3,(200,360))
            
            

            pygame.display.update()
            
            
        while(Jugar2 == True):
            while ( Enpausa == True):
                screen.blit(Pausa,(20,20))

                for event in pygame.event.get():
                    # si se da click en exit, se cierra el juego
                    if(event.type == pygame.MOUSEBUTTONDOWN):
                        if (Cursor1.colliderect(BotonContinuarP.rect)):

                            Enpausa = False
                            
                        if (Cursor1.colliderect(BotonSalirP.rect)):
                            EnPausa = False
                            Jugar2 = False
                            Menu = True
                            
                    if(event.type == pygame.QUIT):
                        EnPausa = False
                        Jugar2 = False
                        Cerrar = True
                Cursor1.update()
                BotonContinuarP.update(screen,Cursor1)
                BotonSalirP.update(screen,Cursor1)
                pygame.display.update()
            
            
            for rect in muros2.recs:
                
               #Colision del raton con el mapa
                if (raton1.rect.colliderect(rect)):
                    
                    if ( vx == velocidad ):
                        mapa2.update(screen,vx-20,vy)
                        muros2.update(screen,vx-20,vy)
                        for enem in enemigos:
                            enem.update(screen,vx-20,vy,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx-20,vy,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx-20,vy)
                        for ques in quesos:
                            ques.update(screen,vx-20,vy)
                        
                        vx = 0
                        vy = random.randrange(-10,11,20)
                        
                    elif( vx == -velocidad ):
                        mapa2.update(screen,vx+30,vy)
                        muros2.update(screen,vx+30,vy)
                        for enem in enemigos:
                            enem.update(screen,vx+30,vy,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx+30,vy,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx+30,vy)
                        for ques in quesos:
                            ques.update(screen,vx+30,vy)
                              
                        vx = 0
                        vy = random.randrange(-10,11,20)
                       
                    elif ( vy == velocidad ):
                        mapa2.update(screen,vx,vy-20)
                        muros2.update(screen,vx,vy-20)
                        for enem in enemigos:
                            enem.update(screen,vx,vy-20,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx,vy-20,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx,vy-20)
                        for ques in quesos:  
                            ques.update(screen,vx,vy-20)
                        
                        vy = 0
                        vx = random.randrange(-10,11,20)
                        
                    elif( vy == -velocidad ):
                        mapa2.update(screen,vx,vy+25)
                        muros2.update(screen,vx,vy+25)
                        for enem in enemigos:
                            enem.update(screen,vx,vy+25,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx,vy+25,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx,vy+25)
                        for ques in quesos:
                            ques.update(screen,vx,vy+25)
                                
                        vy = 0
                        vx = random.randrange(-10,11,20)
                    # colision del enemigo A con el mapa
                if(enemigo1.rect.colliderect(rect)):
                    if(evx == 10):
                        enemigo1.update(screen,vx,vy,-23,0,a)
                        
                        evx = 0
                        evy = random.randrange(-10,11,20)
                    elif(evx == -10):
                        enemigo1.update(screen,vx,vy,23,0,a)
                        evx = 0
                        evy = random.randrange(-10,11,20)
                    elif(evy == 10):
                        enemigo1.update(screen,vx,vy,0,-23,a)
                        evx = random.randrange(-10,11,20)
                        evy = 0
                    elif(evy == -10):
                        enemigo1.update(screen,vx,vy,0,23,a)
                        evx = random.randrange(-10,11,20)
                        evy = 0
                 #colision del enemigo B con el mapa
                if(enemigo2.rect.colliderect(rect)):
                    if(mvx == 10):
                        enemigo2.update(screen,vx,vy,-23,0,a)
                        mvx = 0
                        mvy = random.randrange(-10,11,20)
                    elif(mvx == -10):
                        enemigo2.update(screen,vx,vy,23,0,a)
                        mvx = 0
                        mvy = random.randrange(-10,11,20)
                    elif(mvy == 10):
                        enemigo2.update(screen,vx,vy,0,-23,a)
                        mvx = random.randrange(-10,11,20)
                        mvy = 0
                    elif(mvy == -10):
                        enemigo2.update(screen,vx,vy,0,23,a)
                        mvx = random.randrange(-10,11,20)
                        mvy = 0
                        
            for enem in enemigos:
                if(raton1.rect.colliderect(enem) and espera == 36):
                    vidas = vidas - 1
                    espera = 35

                        
            for gato in genemigos:
                if(raton1.rect.colliderect(gato)and espera == 36):
                    vidas = vidas - 1
                    espera = 35
                    tag = 20
                        

                    
                    
            # Se indican los eventos, las acciones de las teclas
            for event in pygame.event.get():
                # si se da click en exit, se cierra el juego
                if(event.type == pygame.QUIT):
                    Jugar2 = False
                    Cerrar = True
                # para cuando se unde alguna tecla
                if (event.type == pygame.KEYDOWN):
                     # para cuando se unde la flecha hacia la derecha, el raton se mueva hacia la derecha
                    if (event.key == pygame.K_RIGHT):
                        if( vy != 0):
                            vy = 0
                            rsp = True
                            vx =  velocidad
                        else:
                            rsp = True
                            vx =  velocidad
                    # cuando se unde hacia la izquierda, va a la izquierda
                    elif (event.key == pygame.K_LEFT):
                        if( vy != 0):
                            vy = 0
                            lsp = True
                            vx = -velocidad
                        else:
                            lsp = True
                            vx = -velocidad
                    # para cuando se unde la flecha hacia arriba, el raton se mueva hacia arriba
                    elif (event.key == pygame.K_UP):
                        if( vx != 0):
                            vx = 0
                            usp = True
                            vy = -velocidad
                        else:
                            usp = True
                            vy = -velocidad
                    # para cuando se unde la flecha hacia abajo, el raton se mueva hacia abajo
                    elif (event.key == pygame.K_DOWN):
                        if( vx != 0):
                            vx = 0
                            dsp = True
                            vy = velocidad
                        else:
                            dsp = True
                            vy = velocidad
                     # para que cuando se unda ESPACIO, aparezca el bloque para defenderse de los enemigos
                    if(event.key == pygame.K_SPACE):
                        if( duracion >20): # regula el tiempo que va a durar

                            duracion = duracion -1
                            estrellas = Estrellas()
                            
                    if(event.key == pygame.K_p):
                        Enpausa = True
                        
                                
                                

            reloj.tick(20) # Hace que este ciclo se repita a 20 fps(frames per second)
            # se suma el contador de animacion
            t = t + 1
            if (t > 1):
                t = 0
            a = a + 1
            if (a > 1):
                a = 0

            textnombre = letra4.render("Jugador : "+NombreJ,0,(0,0,0))
            texttiempo = letra4.render("Tiempo Restante : "+str(cronometro2),0,(0,0,0))
            textvidas = letra4.render("Vidas : "+str(vidas) , 0 , (0,0,0))
            textpuntaje1 = letra4.render("Puntaje : "+str(puntaje2),0,(0,0,0))
            textnivel = letra4.render("Nivel 2",0,(0,0,0))
            screen.fill(blanco)
            mapa2.update(screen,vx,vy)
            muros2.update(screen,vx,vy)
            if(duracion > 0 and duracion < 21):
                estrellas.update(screen,vx,vy)
            raton1.update(screen,vx,vy,t,espera)
            enemigo1.update(screen,vx,vy,evx,evy,a)
            enemigo2.update(screen,vx,vy,mvx,mvy,a)
            gato1.update(screen,vx,vy,tag)
            gato2.update(screen,vx,vy,tag)
            gato3.update(screen,vx,vy,tag)
            gato4.update(screen,vx,vy,tag)
            #Estos condicionales, revisan si el queso ya fue comido o no
            if(noqueso1 == False):
                queso1.update(screen,vx,vy)
            if(noqueso2 == False):
                queso2.update(screen,vx,vy)
            if(noqueso3 == False):
                queso3.update(screen,vx,vy)
            if(noqueso4 == False):
                queso4.update(screen,vx,vy)
            if(noqueso9 == False):
                queso9.update(screen,vx,vy)
            if(cronometro02 < 60 and cronometro02 > 45):
                if(noqueso5 == False):
                    queso5.update(screen,vx,vy)
            if(cronometro02 < 100 and cronometro02 > 80):
                if(noqueso6 == False):
                    queso6.update(screen,vx,vy)
            if(cronometro02 < 70 and cronometro02 > 30):
                if(noqueso7 == False):
                    queso7.update(screen,vx,vy)
            if(cronometro02 < 30 and cronometro02 > 5):
                if(noqueso8 == False):
                    queso8.update(screen,vx,vy)
            if(cronometro02 < 100 and cronometro02 > 5):
                if(noqueso10 == False):
                    queso10.update(screen,vx,vy)
            if(cronometro02 < 100 and cronometro02 > 20):
                if(noqueso11 == False):
                    queso11.update(screen,vx,vy)
            radar2.update(screen,vx,vy)
            screen.blit(textnivel,(584,37))
            screen.blit(textvidas,(584,127))
            screen.blit(textpuntaje1,(584,157))
            screen.blit(textnombre,(584,97))
            screen.blit(texttiempo,(584,67))
            

            pygame.draw.rect(screen,azul,minirat)

                
            
            # para sincronizar al raton principal con el raton del mapa
            if(vx == 0 and vy == velocidad):

                m = 0
                n = 2
                for rect in muros2.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(0,-2.5)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                        
                minirat.move_ip(m,n)
                    
                
            elif(vx == 0 and vy == -velocidad):

                m = 0
                n = -2
                for rect in muros2.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(0,3)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                        
                minirat.move_ip(m,n)
                    

            elif(vx == velocidad and vy == 0):

                m = 2
                n = 0
                for rect in muros2.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(-2.5,0)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                minirat.move_ip(m,n)
                    

            elif(vx == -velocidad and vy == 0):

                m = -2
                n = 0
                for rect in muros2.recs:
                    if (raton1.rect.colliderect(rect)):
                        minirat.move_ip(4,0)
                        for mini in minienemigos:
                            mini.move_ip(0,0)
                        
                minirat.move_ip(m,n)

            # Indica que mientras este en el juego el bloque, si algun enemigo colisiona con el, cambia de direccion
            if(duracion > 0 and duracion < 21):
                if(enemigo1.rect.colliderect(estrellas.rect)):
                    if(evx == 10):
                        enemigo1.update(screen,vx,vy,-25,0,a)
                        evx = -10
                        
                    elif(evx == -10):
                        enemigo1.update(screen,vx,vy,25,0,a)
                        evx = 10
                    elif(evy == 10):
                        enemigo1.update(screen,vx,vy,0,-25,a)
                        evy = -10
                    elif(evy == -10):
                        enemigo1.update(screen,vx,vy,0,25,a)
                        evy = 10

                if(enemigo2.rect.colliderect(estrellas.rect)):
                    if(mvx == 10):
                        enemigo2.update(screen,vx,vy,-25,0,a)
                        mvx = -10
                    elif(mvx == -10):
                        enemigo2.update(screen,vx,vy,25,0,a)
                        mvx = 10
                    elif(mvy == 10):
                        enemigo2.update(screen,vx,vy,0,-25,a)
                        mvy = -10
                    elif(mvy == -10):
                        enemigo2.update(screen,vx,vy,0,25,a)
                        mvy = 10

            if(noqueso1 == False):
                pygame.draw.rect(screen,amarillo,miniques1)

            # cuando colisiona el raton con el queso, este tiene que desaparecer, es igual con todos los demas quesos
            if(raton1.rect.colliderect(queso1.rect)):
                    queso1.rect.left,queso1.rect.top = (-67,-47)
                    #miniques1.move(-11,-11)
                    noqueso1 = True
                    puntaje2 = puntaje2 + 200
                    coj = coj + 1
                    
                    

            if(noqueso2 == False):
                pygame.draw.rect(screen,amarillo,miniques2)

            if(raton1.rect.colliderect(queso2.rect)):
                    queso2.rect.left,queso2.rect.top =(-67,-47)
                    #miniques2.move(-11,-11)
                    noqueso2 = True
                    puntaje2 = puntaje2 + 200
                    coj = coj + 1
                    

            if(noqueso3 == False):
                pygame.draw.rect(screen,amarillo,miniques3)

            if(raton1.rect.colliderect(queso3.rect)):
                    queso3.rect.left,queso3.rect.top =(-67,-47)
                    #miniques3.move(-11,-11)
                    noqueso3 = True
                    puntaje2 = puntaje2 + 200
                    coj = coj + 1
                    

            if(noqueso4 == False):
                pygame.draw.rect(screen,amarillo,miniques4)

            if(raton1.rect.colliderect(queso4.rect)):
                    queso4.rect.left,queso4.rect.top =(-67,-47)
                    #miniques4.move(-11,-11)
                    noqueso4 = True
                    puntaje2 = puntaje2 + 200
                    coj = coj + 1
                    
            if(noqueso9 == False):
                pygame.draw.rect(screen,amarillo,miniques9)

            if(raton1.rect.colliderect(queso9.rect)):
                    queso9.rect.left,queso9.rect.top =(-67,-47)
                    #miniques4.move(-11,-11)
                    noqueso9 = True
                    puntaje2 = puntaje2 + 200
                    coj = coj + 1

            if(cronometro02 == 60):
                queso5 = Queso(cuaq5.left,cuaq5.top,"quesoblanco.png")
                quesos.append(queso5)

            if(cronometro02 < 60 and cronometro02 > 45):
                    
                if(noqueso5 == False):
                    pygame.draw.rect(screen, blanco,miniques5)

                if(raton1.rect.colliderect(queso5.rect)):
                        queso5.rect.left,queso5.rect.top =(-67,-47)
                        miniques5.move(-11,-11)
                        noqueso5 = True
                        vidas = vidas + 1
                        puntaje2 = puntaje2 + 20
                        coj = coj + 1
                        
            if(cronometro02 == 100):
                
                        queso6 = Queso(cuaq6.left,cuaq6.top,"quesoblanco.png")
                        quesos.append(queso6)
            if(cronometro02 < 100 and cronometro02 > 80):
                    
                if(noqueso6 == False):
                    pygame.draw.rect(screen, blanco,miniques6)

                if(raton1.rect.colliderect(queso6.rect)):
                        queso6.rect.left,queso6.rect.top =(-67,-47)
                        miniques6.move(-11,-11)
                        noqueso6 = True
                        vidas = vidas + 1
                        puntaje2 = puntaje2 + 20
                        coj = coj + 1
                        
            if(cronometro02 == 70):
                queso7 = Queso(cuaq7.left,cuaq7.top,"quesorojo.png")
                quesos.append(queso7)
            if(cronometro02 < 70 and cronometro02 > 30):
                    
                if(noqueso7 == False):
                    pygame.draw.rect(screen,(230, 95, 0),miniques7)

                if(raton1.rect.colliderect(queso7.rect)):
                        queso7.rect.left,queso7.rect.top =(-67,-47)
                        miniques7.move(-11,-11)
                        noqueso7 = True
                        #masvel = True
                        puntaje2 = puntaje2 + 20
                        cronometro2 = cronometro2 + 10
                        coj = coj + 1
                        
            if(cronometro02 == 30):
                queso8 = Queso(cuaq8.left,cuaq8.top,"quesoverde.png")
                quesos.append(queso8)
                
            if(cronometro02 < 30 and cronometro02 > 5):
                    
                if(noqueso8 == False):
                    pygame.draw.rect(screen,(0, 255, 0),miniques8)

                if(raton1.rect.colliderect(queso8.rect)):
                        queso8.rect.left,queso8.rect.top =(-67,-47)
                        miniques8.move(-11,-11)
                        noqueso8 = True
                        puntaje2 = puntaje2 - 300
                        cronometro2 = cronometro2 -50
                        coj = coj + 1
                        
            if(cronometro02 == 100):
                queso10 = Queso(cuaq10.left,cuaq10.top,"quesorojo.png")
                quesos.append(queso10)
                
            if(cronometro02 < 100 and cronometro02 > 5):
                    
                if(noqueso10 == False):
                    pygame.draw.rect(screen,(0, 255, 0),miniques10)

                if(raton1.rect.colliderect(queso10.rect)):
                        queso10.rect.left,queso10.rect.top =(-67,-47)
                        miniques10.move(-11,-11)
                        noqueso10 = True
                        puntaje2 = puntaje2 + 20
                        cronometro2 = cronometro2 + 10
                        coj = coj + 1
                        
            if(cronometro02 == 100):
                queso11 = Queso(cuaq11.left,cuaq11.top,"quesoverde.png")
                quesos.append(queso11)
                
            if(cronometro02 < 100 and cronometro02 > 20):
                    
                if(noqueso11 == False):
                    pygame.draw.rect(screen,(0, 255, 0),miniques11)

                if(raton1.rect.colliderect(queso11.rect)):
                        queso11.rect.left,queso11.rect.top =(-67,-47)
                        miniques11.move(-11,-11)
                        noqueso11 = True
                        puntaje2 = puntaje2 -300
                        cronometro2 = cronometro2 -50
                        coj = coj + 1


            if( duracion < 21):
                duracion = duracion -1
            if(duracion == 0):
                duracion = 21
                
            if( espera < 36):
                espera = espera - 1
            if( espera == 0):
                espera = 36
                
            if(tag < 21):
                tag = tag - 1
            if(tag ==0):
                tag = 21
            contadorsegundos = contadorsegundos - 1

            if( contadorsegundos == 0):
                contadorsegundos = 20
                cronometro2 = cronometro2 - 1
                cronometro02 = cronometro02 - 1
                
            if(cronometro2 == 0 or vidas == 0):
                Jugar2 = False
                Muerte = True
            if( noqueso9 == True and noqueso1 == True and noqueso2 == True and noqueso3 == True and noqueso4 == True):
                Jugar2 = False
                Menu3 = True
            
            
            pygame.display.update()
        while(Menu3 == True):
            
            screen.blit(menu3,(0,0))

            for event in pygame.event.get():
               # si se da click en exit, se cierra el juego
               if(event.type == pygame.MOUSEBUTTONDOWN):
                   if (Cursor1.colliderect(BotonPlay.rect)):
                       
                        Negro2 = True
                        Menu3 = False
                        radar3 = Lado("int2.png")
                        raton1 = Player(205,325)

                       
                        screen.fill(blanco)
                        puntaje3 = 0
                        espera = 36
                        
                        cronometro03 = 90
                        cronometro3 = 90
                        contadorsegundos = 20
                        
    
                        quesos = [] # lista de quesos
                        enemigos = []
                        genemigos = []
                        gato1 = Gato(237,117)
                        gato2 = Gato(217,757)
                        gato3 = Gato(1013,1013)
                        gato4 = Gato(701,469)
                        gato5 = Gato(565,1301)
                        gato6 = Gato(1017,221)
                        enemigo1 = EnemigoA(637,841) # se inicializa un enemigo en la parte de abajo
                        enemigo2 = EnemigoB(101,101) # se inicializa un enemigo en la parte de la derecha
                    
                        duracion = 21 # variable con la cual se lleva cuenta del tiempo que debe durar el poder del raton en el mapa
                        mordida = pygame.mixer.Sound("5969.wav") # se inicializa un sonido, no lo implemente aun porque se bugea
                        minirat =  pygame.Rect((621,299),(11,11)) # representacion del raton en el radar

                        # se inicializan los quesos del nivel
                        queso1 = Queso(477,297,"queso.png") 
                        queso2 = Queso(1289,113,"queso.png")
                        queso3 = Queso(685,805,"queso.png")
                        queso4 = Queso(101,765,"queso.png")
                        queso9 = Queso(1309,1025,"queso.png")


                        # se adicionan a la lista quesos
                        quesos.append(queso1)
                        quesos.append(queso2)
                        quesos.append(queso3)
                        quesos.append(queso4)
                        quesos.append(queso9)


                        cuaq5 = pygame.Rect((717,657),(2,2))
                        cuaq6 = pygame.Rect((865,761),(2,2))
                        cuaq7 = pygame.Rect((961,781),(2,2))
                        cuaq8 = pygame.Rect((1309,425),(2,2))
                        cuaq10 = pygame.Rect((341,917),(2,2))
                        cuaq11 = pygame.Rect((713,413),(2,2))

                        # se adicionan enemigos a la lista enemigos
                        enemigos.append(enemigo1)
                        enemigos.append(enemigo2)
                        genemigos.append(gato1)
                        genemigos.append(gato2)
                        genemigos.append(gato3)
                        genemigos.append(gato4)
                        genemigos.append(gato5)
                        genemigos.append(gato6)


                        noqueso1 = False
                        noqueso2 = False
                        noqueso3 = False
                        noqueso4 = False
                        noqueso5 = False
                        noqueso6 = False
                        noqueso7 = False
                        noqueso8 = False
                        noqueso9 = False
                        noqueso10 = False
                        noqueso11 = False

                        #velocidad del jugador
                        vx,vy = 0,0
                        # velocidad del enemigo A
                        evx,evy = 10,0
                        # velocidad del enemigo B
                        mvx,mvy = 10,0
                        #variable para indicar velocidad
                        velocidad = 10
                        #variables temporales implementadas en los ratones para orientacion
                        t = 0
                        a = 0
                        w = 100
                        tag = 21
                        
                        rsp,lsp,usp,dsp = False,False,False,False
                        
                        
               if(event.type == pygame.QUIT):
                   Menu3 = False
                   Cerrar = True
            Cursor1.update()
            BotonPlay.update(screen,Cursor1)
           
            pygame.display.update()
        while(Negro2 == True):

            screen.blit(negro,(0,0))

            texto1 = letra6.render("Muy bien, ahora se complica",0,amarillo)
            texto2 = letra6.render("No tendras radar, y el tiempo sera menor",0,rojo)
            texto3 = letra6.render("Teclear 'Espacio' para continuar",0,azul)
            texto4 = letra6.render("Suerte...",0,rojo)

            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                     # para cuando se unde la flecha hacia la derecha, el raton se mueva hacia la derecha
                    if (event.key == pygame.K_SPACE):
                        screen.fill(blanco)
                        Negro2 = False
                        Jugar3 = True
                if(event.type == pygame.QUIT):
                    Negro1 = False
                    Cerrar = True
            screen.blit(texto1,(270,110))
            screen.blit(texto2,(60,240))
            screen.blit(texto4,(350,280))
            screen.blit(texto3,(200,360))
            
            

            pygame.display.update()
        while(Jugar3 == True):
            while ( Enpausa == True):
                screen.blit(Pausa,(20,20))

                for event in pygame.event.get():
                    # si se da click en exit, se cierra el juego
                    if(event.type == pygame.MOUSEBUTTONDOWN):
                        if (Cursor1.colliderect(BotonContinuarP.rect)):

                            Enpausa = False
                            
                        if (Cursor1.colliderect(BotonSalirP.rect)):
                            EnPausa = False
                            Jugar3 = False
                            Menu = True
                            
                    if(event.type == pygame.QUIT):
                        EnPausa = False
                        Jugar3 = False
                        Cerrar = True
                Cursor1.update()
                BotonContinuarP.update(screen,Cursor1)
                BotonSalirP.update(screen,Cursor1)
                pygame.display.update()
            
            
            for rect in muros3.recs:
                
               #Colision del raton con el mapa
                if (raton1.rect.colliderect(rect)):
                    
                    if ( vx == velocidad ):
                        mapa3.update(screen,vx-20,vy)
                        muros3.update(screen,vx-20,vy)
                        for enem in enemigos:
                            enem.update(screen,vx-20,vy,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx-20,vy,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx-20,vy)
                        for ques in quesos:
                            ques.update(screen,vx-20,vy)
                        
                        vx = 0
                        vy = random.randrange(-10,11,20)
                        
                    elif( vx == -velocidad ):
                        mapa3.update(screen,vx+30,vy)
                        muros3.update(screen,vx+30,vy)
                        for enem in enemigos:
                            enem.update(screen,vx+30,vy,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx+30,vy,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx+30,vy)
                        for ques in quesos:
                            ques.update(screen,vx+30,vy)
                              
                        vx = 0
                        vy = random.randrange(-10,11,20)
                       
                    elif ( vy == velocidad ):
                        mapa3.update(screen,vx,vy-20)
                        muros3.update(screen,vx,vy-20)
                        for enem in enemigos:
                            enem.update(screen,vx,vy-20,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx,vy-20,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx,vy-20)
                        for ques in quesos:  
                            ques.update(screen,vx,vy-20)
                        
                        vy = 0
                        vx = random.randrange(-10,11,20)
                        
                    elif( vy == -velocidad ):
                        mapa3.update(screen,vx,vy+25)
                        muros3.update(screen,vx,vy+25)
                        for enem in enemigos:
                            enem.update(screen,vx,vy+25,0,0,a)
                        for gato in genemigos:
                            gato.update(screen,vx,vy+25,tag)
                        if( duracion <20):
                            estrellas.update(screen,vx,vy+25)
                        for ques in quesos:
                            ques.update(screen,vx,vy+25)
                                
                        vy = 0
                        vx = random.randrange(-10,11,20)
                    # colision del enemigo A con el mapa
                if(enemigo1.rect.colliderect(rect)):
                    if(evx == 10):
                        enemigo1.update(screen,vx,vy,-23,0,a)
                        
                        evx = 0
                        evy = random.randrange(-10,11,20)
                    elif(evx == -10):
                        enemigo1.update(screen,vx,vy,23,0,a)
                        evx = 0
                        evy = random.randrange(-10,11,20)
                    elif(evy == 10):
                        enemigo1.update(screen,vx,vy,0,-23,a)
                        evx = random.randrange(-10,11,20)
                        evy = 0
                    elif(evy == -10):
                        enemigo1.update(screen,vx,vy,0,23,a)
                        evx = random.randrange(-10,11,20)
                        evy = 0
                 #colision del enemigo B con el mapa
                if(enemigo2.rect.colliderect(rect)):
                    if(mvx == 10):
                        enemigo2.update(screen,vx,vy,-23,0,a)
                        mvx = 0
                        mvy = random.randrange(-10,11,20)
                    elif(mvx == -10):
                        enemigo2.update(screen,vx,vy,23,0,a)
                        mvx = 0
                        mvy = random.randrange(-10,11,20)
                    elif(mvy == 10):
                        enemigo2.update(screen,vx,vy,0,-23,a)
                        mvx = random.randrange(-10,11,20)
                        mvy = 0
                    elif(mvy == -10):
                        enemigo2.update(screen,vx,vy,0,23,a)
                        mvx = random.randrange(-10,11,20)
                        mvy = 0
                        
            for enem in enemigos:
                if(raton1.rect.colliderect(enem) and espera == 36):
                    vidas = vidas - 1
                    espera = 35

                        
            for gato in genemigos:
                if(raton1.rect.colliderect(gato)and espera == 36):
                    vidas = vidas - 1
                    espera = 35
                    tag = 20
                        

                    
                    
            # Se indican los eventos, las acciones de las teclas
            for event in pygame.event.get():
                # si se da click en exit, se cierra el juego
                if(event.type == pygame.QUIT):
                    Jugar2 = False
                    Cerrar = True
                # para cuando se unde alguna tecla
                if (event.type == pygame.KEYDOWN):
                     # para cuando se unde la flecha hacia la derecha, el raton se mueva hacia la derecha
                    if (event.key == pygame.K_RIGHT):
                        if( vy != 0):
                            vy = 0
                            rsp = True
                            vx =  velocidad
                        else:
                            rsp = True
                            vx =  velocidad
                    # cuando se unde hacia la izquierda, va a la izquierda
                    elif (event.key == pygame.K_LEFT):
                        if( vy != 0):
                            vy = 0
                            lsp = True
                            vx = -velocidad
                        else:
                            lsp = True
                            vx = -velocidad
                    # para cuando se unde la flecha hacia arriba, el raton se mueva hacia arriba
                    elif (event.key == pygame.K_UP):
                        if( vx != 0):
                            vx = 0
                            usp = True
                            vy = -velocidad
                        else:
                            usp = True
                            vy = -velocidad
                    # para cuando se unde la flecha hacia abajo, el raton se mueva hacia abajo
                    elif (event.key == pygame.K_DOWN):
                        if( vx != 0):
                            vx = 0
                            dsp = True
                            vy = velocidad
                        else:
                            dsp = True
                            vy = velocidad
                     # para que cuando se unda ESPACIO, aparezca el bloque para defenderse de los enemigos
                    if(event.key == pygame.K_SPACE):
                        if( duracion >20): # regula el tiempo que va a durar

                            duracion = duracion -1
                            estrellas = Estrellas()
                            
                    if(event.key == pygame.K_p):
                        Enpausa = True
                        
                                
                                

            reloj.tick(20) # Hace que este ciclo se repita a 20 fps(frames per second)
            # se suma el contador de animacion
            t = t + 1
            if (t > 1):
                t = 0
            a = a + 1
            if (a > 1):
                a = 0

            textnombre = letra4.render("Jugador : "+NombreJ,0,(0,0,0))
            texttiempo = letra4.render("Tiempo Restante : "+str(cronometro3),0,(0,0,0))
            textvidas = letra4.render("Vidas : "+str(vidas) , 0 , (0,0,0))
            textpuntaje1 = letra4.render("Puntaje : "+str(puntaje3),0,(0,0,0))
            textnivel = letra4.render("Nivel 3",0,(0,0,0))
            screen.fill(blanco)
            mapa3.update(screen,vx,vy)
            muros3.update(screen,vx,vy)
            if(duracion > 0 and duracion < 21):
                estrellas.update(screen,vx,vy)
            raton1.update(screen,vx,vy,t,espera)
            enemigo1.update(screen,vx,vy,evx,evy,a)
            enemigo2.update(screen,vx,vy,mvx,mvy,a)
            gato1.update(screen,vx,vy,tag)
            gato2.update(screen,vx,vy,tag)
            gato3.update(screen,vx,vy,tag)
            gato4.update(screen,vx,vy,tag)
            gato5.update(screen,vx,vy,tag)
            gato6.update(screen,vx,vy,tag)
            #Estos condicionales, revisan si el queso ya fue comido o no
            if(noqueso1 == False):
                queso1.update(screen,vx,vy)
            if(noqueso2 == False):
                queso2.update(screen,vx,vy)
            if(noqueso3 == False):
                queso3.update(screen,vx,vy)
            if(noqueso4 == False):
                queso4.update(screen,vx,vy)
            if(noqueso9 == False):
                queso9.update(screen,vx,vy)
            if(cronometro02 < 60 and cronometro02 > 45):
                if(noqueso5 == False):
                    queso5.update(screen,vx,vy)
            if(cronometro03 < 45 and cronometro03 > 30):
                if(noqueso6 == False):
                    queso6.update(screen,vx,vy)
            if(cronometro02 < 70 and cronometro02 > 35):
                if(noqueso7 == False):
                    queso7.update(screen,vx,vy)
            if(cronometro02 < 30 and cronometro02 > 5):
                if(noqueso8 == False):
                    queso8.update(screen,vx,vy)
            if(cronometro02 < 60 and cronometro02 > 45):
                if(noqueso10 == False):
                    queso10.update(screen,vx,vy)
            if(cronometro03 < 50 and cronometro03 > 40):
                if(noqueso11 == False):
                    queso11.update(screen,vx,vy)
            radar3.update(screen,vx,vy)
            screen.blit(textnivel,(584,37))
            screen.blit(textvidas,(584,127))
            screen.blit(textpuntaje1,(584,157))
            screen.blit(textnombre,(584,97))
            screen.blit(texttiempo,(584,67))
        

            # Indica que mientras este en el juego el bloque, si algun enemigo colisiona con el, cambia de direccion
            if(duracion > 0 and duracion < 21):
                if(enemigo1.rect.colliderect(estrellas.rect)):
                    if(evx == 10):
                        enemigo1.update(screen,vx,vy,-25,0,a)
                        evx = -10
                        
                    elif(evx == -10):
                        enemigo1.update(screen,vx,vy,25,0,a)
                        evx = 10
                    elif(evy == 10):
                        enemigo1.update(screen,vx,vy,0,-25,a)
                        evy = -10
                    elif(evy == -10):
                        enemigo1.update(screen,vx,vy,0,25,a)
                        evy = 10

                if(enemigo2.rect.colliderect(estrellas.rect)):
                    if(mvx == 10):
                        enemigo2.update(screen,vx,vy,-25,0,a)
                        mvx = -10
                    elif(mvx == -10):
                        enemigo2.update(screen,vx,vy,25,0,a)
                        mvx = 10
                    elif(mvy == 10):
                        enemigo2.update(screen,vx,vy,0,-25,a)
                        mvy = -10
                    elif(mvy == -10):
                        enemigo2.update(screen,vx,vy,0,25,a)
                        mvy = 10



            # cuando colisiona el raton con el queso, este tiene que desaparecer, es igual con todos los demas quesos
            if(raton1.rect.colliderect(queso1.rect)):
                    queso1.rect.left,queso1.rect.top = (-67,-47)
                    
                    noqueso1 = True
                    puntaje3 = puntaje3 + 200
                    coj = coj + 1
                    

            if(raton1.rect.colliderect(queso2.rect)):
                    queso2.rect.left,queso2.rect.top =(-67,-47)
                    
                    noqueso2 = True
                    puntaje3 = puntaje3 + 200
                    coj = coj + 1

            if(raton1.rect.colliderect(queso3.rect)):
                    queso3.rect.left,queso3.rect.top =(-67,-47)
                    
                    noqueso3 = True
                    puntaje3 = puntaje3 + 200
                    coj = coj + 1

            if(raton1.rect.colliderect(queso4.rect)):
                    queso4.rect.left,queso4.rect.top =(-67,-47)
                    
                    noqueso4 = True
                    puntaje3 = puntaje3 + 200
                    coj = coj + 1

            if(raton1.rect.colliderect(queso9.rect)):
                    queso9.rect.left,queso9.rect.top =(-67,-47)
                    
                    noqueso9 = True
                    puntaje3 = puntaje3 + 200
                    coj = coj + 1
            if(cronometro03 == 60):
                queso5 = Queso(cuaq5.left,cuaq5.top,"quesoblanco.png")
                quesos.append(queso5)

            if(cronometro03 < 60 and cronometro03 > 45):

                if(raton1.rect.colliderect(queso5.rect)):
                        queso5.rect.left,queso5.rect.top =(-67,-47)
                        
                        noqueso5 = True
                        vidas = vidas + 1
                        puntaje3 = puntaje3 + 20
                        coj = coj + 1
            if(cronometro03 == 45):
                
                        queso6 = Queso(cuaq6.left,cuaq6.top,"quesoblanco.png")
                        quesos.append(queso6)
            if(cronometro03 < 45 and cronometro03 > 30):

                if(raton1.rect.colliderect(queso6.rect)):
                        queso6.rect.left,queso6.rect.top =(-67,-47)
                        
                        noqueso6 = True
                        vidas = vidas + 1
                        puntaje3 = puntaje3 + 20
                        coj = coj + 1
            if(cronometro03 == 70):
                queso7 = Queso(cuaq7.left,cuaq7.top,"quesorojo.png")
                quesos.append(queso7)
            if(cronometro03 < 70 and cronometro03 > 35):

                if(raton1.rect.colliderect(queso7.rect)):
                        queso7.rect.left,queso7.rect.top =(-67,-47)
                        
                        noqueso7 = True
                        puntaje3 = puntaje3 + 20
                        cronometro3 = cronometro3 + 10
                        coj = coj + 1
            if(cronometro03 == 30):
                queso8 = Queso(cuaq8.left,cuaq8.top,"quesoverde.png")
                quesos.append(queso8)
                
            if(cronometro02 < 30 and cronometro02 > 5):

                if(raton1.rect.colliderect(queso8.rect)):
                        queso8.rect.left,queso8.rect.top =(-67,-47)
                        
                        noqueso8 = True
                        puntaje3 = puntaje3 - 300
                        cronometro3 = cronometro3 -50
                        coj = coj + 1
            if(cronometro03 == 60):
                queso10 = Queso(cuaq10.left,cuaq10.top,"quesorojo.png")
                quesos.append(queso10)
                
            if(cronometro03 < 60 and cronometro03 > 45):

                if(raton1.rect.colliderect(queso10.rect)):
                        queso10.rect.left,queso10.rect.top =(-67,-47)
                        
                        noqueso10 = True
                        puntaje3 = puntaje3 + 20
                        cronometro3 = cronometro3 + 10
                        coj = coj + 1
            if(cronometro03 == 50):
                queso11 = Queso(cuaq11.left,cuaq11.top,"quesoverde.png")
                quesos.append(queso11)
                
            if(cronometro03 < 50 and cronometro03 > 40):

                if(raton1.rect.colliderect(queso11.rect)):
                        queso11.rect.left,queso11.rect.top =(-67,-47)
                        
                        noqueso11 = True
                        puntaje3 = puntaje3 -300
                        cronometro3 = cronometro3 -50
                        coj = coj + 1


            if( duracion < 21):
                duracion = duracion -1
            if(duracion == 0):
                duracion = 21
                
            if( espera < 36):
                espera = espera - 1
            if( espera == 0):
                espera = 36
                
            if(tag < 21):
                tag = tag - 1
            if(tag ==0):
                tag = 21
            contadorsegundos = contadorsegundos - 1

            if( contadorsegundos == 0):
                contadorsegundos = 20
                cronometro3 = cronometro3 - 1
                cronometro03 = cronometro03 - 1
                
            if(cronometro3 == 0 or vidas == 0):
                Jugar3 = False
                Muerte = True
            if( noqueso9 == True and noqueso1 == True and noqueso2 == True and noqueso3 == True and noqueso4 == True):
                Jugar3 = False
                Terminar = True
            
            
            
            pygame.display.update()
        while(Terminar == True):

            screen.blit(terminar,(0,0))

            
            for event in pygame.event.get():
                    # si se da click en exit, se cierra el juego
                    if(event.type == pygame.MOUSEBUTTONDOWN):
                        if (Cursor1.colliderect(BotonVolverT.rect)):

                            Terminar = False
                            Menu = True
                        
                            
                    if(event.type == pygame.QUIT):
                        Terminar = False
                        Cerrar = True
            puntaje = puntaje1 + puntaje2 + puntaje3
            texto0 = letra7.render("Jugador : "+NombreJ,0,(0,0,0))
            texto1 = letra7.render("Nivel 1 : " +str(puntaje1),0,(0,0,0))
            texto2 = letra7.render("Nivel 2 : " +str(puntaje2),0,(0,0,0))
            texto3 = letra7.render("Nivel 3 : " +str(puntaje3),0,(0,0,0))
            texto4 = letra7.render("Vidas : " +str(vidas),0,(0,0,0))
            texto5 = letra7.render("Quesos : "+str(coj)+"/"+"30",0,(0,0,0))
            texto6 = letra7.render("Puntaje total :" + str(puntaje),0,(0,0,0))

            screen.blit(texto0,(28,24))
            screen.blit(texto1,(28,54))
            screen.blit(texto2,(28,84))
            screen.blit(texto3,(28,104))
            screen.blit(texto4,(28,134))
            screen.blit(texto5,(28,154))
            screen.blit(texto6,(28,184))
            
            Cursor1.update()
            BotonVolverT.update(screen,Cursor1)
            pygame.display.update()
        
            


            

    pygame.quit() # cuando se cierra el primer ciclo entra aqui para cerrar la interfaz

principal() # se llama toda la funcion
