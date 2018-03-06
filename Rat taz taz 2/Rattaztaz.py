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
        
        
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
        
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()
        
# esta clase general la pantalla gris del lado izquierdo, donde aparece el radar
class Lado(pygame.sprite.Sprite):
    def __init__(self):

        self.imagen = pygame.image.load("int1.png")
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
            
        
# genera el fondo como un sprite
class Fondo(pygame.sprite.Sprite):

    def __init__(self):
        self.imagen=pygame.image.load("mapa.jpg")
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
    def __init__(self):
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
        self.p = 171
        self.q = 230
        self.imagen = self.imagenes[self.imagen_actual][0]
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-20,-20)
        self.rect.top,self.rect.left = (191,250)

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
    cronometro1 = 200
    contadorsegundos = 20

    #textos
    letra = pygame.font.Font(None,20)
    letra2 = pygame.font.Font(None,50)
    letra3 = pygame.font.Font(None,45)
    letra4 = pygame.font.SysFont("Arial",20,True,True)

    playimg1 = pygame.image.load("botonjugar1.png")
    playimg2 = pygame.image.load("botonjugar2.png")
    how1 = pygame.image.load("Howto1.png")
    how2 = pygame.image.load("Howto2.png")
    menu = pygame.image.load("Menu.png")
    tecleando = pygame.image.load("Nombre.png")

    Fin = pygame.image.load("Fin.png")
    continuarimg1 = pygame.image.load("continuar1.png")
    continuarimg2 = pygame.image.load("continuar2.png")
    salirimg1 = pygame.image.load("Exit1.png")
    salirimg2 = pygame.image.load("Exit2.png")

    Pausa = pygame.image.load("Pause.png")
    
    Cursor1 = Cursor()
    BotonPlay = Boton(playimg1,playimg2,120,260)
    BotonHow = Boton(how1,how2, 420, 210)

    BotonContinuarF = Boton(continuarimg1,continuarimg2,413,177)
    BotonSalirF = Boton(salirimg1,salirimg2,463,290)
    
    BotonContinuarP = Boton(continuarimg1,continuarimg2,73,249)
    BotonSalirP = Boton(salirimg1,salirimg2,448,249)
    
    vidas = 3
    puntaje1 = 0
    puntaje2 = 0
    puntaje3 = 0
    espera = 36
    enemigos = [] # lista de enemigos
    minienemigos = [] # lista de la imagen de los enemigos en el radar
    quesos = [] # lista de quesos
    mapa1 = Fondo() # se inicializa el mapa del nivel 1
    raton1 = Player() # se inicializa el jugador
    fondo1 = Lado() # se inicializa el meni donde aparece el radar al lado derecho de la pantalla
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
    queso5 = Queso(1070,991,"quesoblanco.png")

    # se adicionan a la lista quesos
    quesos.append(queso1)
    quesos.append(queso2)
    quesos.append(queso3)
    quesos.append(queso4)
    quesos.append(queso5)

    # se adicionan enemigos a la lista enemigos
    enemigos.append(enemigo1)
    enemigos.append(enemigo2)
    #se inicializan las imagenes de los quesos en el radar
    miniques1 = pygame.Rect((650,310),(10,10))
    miniques2 = pygame.Rect((712,379),(10,10))
    miniques3 = pygame.Rect((793,279),(10,10))
    miniques4 = pygame.Rect((622,442),(10,10))
    miniques5 = pygame.Rect((796,444),(10,10))
    
    #se inicializan las imagenes de los enemigos en el radar
    minienem1 = pygame.Rect((692,444),(10,10))
    minienem2 = pygame.Rect((754,333),(10,10))
    #se adicionan las imagenes de los enemigos a una lista
    minienemigos.append(minienem1)
    minienemigos.append(minienem2)
    #variables para indicar cuando hay o no hay un queso
    noqueso1 = False
    noqueso2 = False
    noqueso3 = False
    noqueso4 = False
    noqueso5 = False
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
    

    # auxiliares de movimiento (rsp = rigth sigue apretada, etc)
    rsp,lsp,usp,dsp = False,False,False,False

##    distancia1 = math.sqrt((abs(raton1.rect.left-enemigo1.rect.left)**2) + (abs(raton1.rect.top-enemigo1.rect.top)**2))
##    distancia2 = math.sqrt((abs(raton1.rect.left-enemigo2.rect.left)**2) + (abs(raton1.rect.top-enemigo2.rect.top)**2))
##
##    angulo1 = math.acos((abs(raton1.rect.left-enemigo1.rect.left))/distancia1)
##    angulo2 = math.acos((abs(raton1.rect.left-enemigo1.rect.left))/discancia)
##


    while ( Cerrar == False ): # Loop principal
        
        while( Menu == True): # Loop del menu inicial
           
           screen.blit(menu,(0,0))
           
           for event in pygame.event.get():
               # si se da click en exit, se cierra el juego
               if(event.type == pygame.MOUSEBUTTONDOWN):
                   if (Cursor1.colliderect(BotonPlay.rect)):

                        Tecleo = True
                        Menu = False
                        screen.fill(blanco)
                        vidas = 3
                        puntaje1 = 0
                        puntaje2 = 0
                        puntaje3 = 0
                        espera = 36
                        cronometro1 = 200
                        contadorsegundos = 20
                        enemigos = [] # lista de enemigos
                        minienemigos = [] # lista de la imagen de los enemigos en el radar
                        quesos = [] # lista de quesos
                        mapa1 = Fondo() # se inicializa el mapa del nivel 1
                        raton1 = Player() # se inicializa el jugador
                        fondo1 = Lado() # se inicializa el meni donde aparece el radar al lado derecho de la pantalla
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
                        queso5 = Queso(1070,991,"quesoblanco.png")

                        # se adicionan a la lista quesos
                        quesos.append(queso1)
                        quesos.append(queso2)
                        quesos.append(queso3)
                        quesos.append(queso4)
                        quesos.append(queso5)

                        # se adicionan enemigos a la lista enemigos
                        enemigos.append(enemigo1)
                        enemigos.append(enemigo2)

                        #se inicializan las imagenes de los quesos en el radar
                        miniques1 = pygame.Rect((650,310),(10,10))
                        miniques2 = pygame.Rect((712,379),(10,10))
                        miniques3 = pygame.Rect((793,279),(10,10))
                        miniques4 = pygame.Rect((622,442),(10,10))
                        miniques5 = pygame.Rect((796,444),(10,10))

                        #se inicializan las imagenes de los enemigos en el radar
                        minienem1 = pygame.Rect((692,444),(10,10))
                        minienem2 = pygame.Rect((754,333),(10,10))

                        #se adicionan las imagenes de los enemigos a una lista
                        minienemigos.append(minienem1)
                        minienemigos.append(minienem2)

                        #variables para indicar cuando hay o no hay un queso
                        noqueso1 = False
                        noqueso2 = False
                        noqueso3 = False
                        noqueso4 = False
                        noqueso5 = False

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
                                                
                    

                        # auxiliares de movimiento (rsp = rigth sigue apretada, etc)
                        rsp,lsp,usp,dsp = False,False,False,False

##                        distancia1 = math.sqrt((abs(raton1.rect.left-enemigo1.rect.left)**2) + (abs(raton1.rect.top-enemigo1.rect.top)**2))
##                        distancia2 = math.sqrt((abs(raton1.rect.left-enemigo2.rect.left)**2) + (abs(raton1.rect.top-enemigo2.rect.top)**2))
##
##                        angulo1 = math.acos((abs(raton1.rect.left-enemigo1.rect.left))/distancia1)
##                        angulo2 = math.acos((abs(raton1.rect.left-enemigo1.rect.left))/discancia)
##                        if((raton1.rect.left-enemigo1.rect.left)> 0 and 
                        
               if(event.type == pygame.QUIT):
                   Menu = False
                   Cerrar = True
           Cursor1.update()
           BotonPlay.update(screen,Cursor1)
           BotonHow.update(screen,Cursor1)
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

            textnombre = letra4.render("Jugador : "+NombreJ,0,(0,0,0))
            texttiempo = letra4.render("Tiempo Restante : "+str(cronometro1),0,(0,0,0))
            textvidas = letra4.render("Vidas : "+str(vidas) , 0 , (0,0,0))
            textpuntaje1 = letra4.render("Puntaje : "+str(puntaje1),0,(0,0,0))
            textnivel = letra4.render("Nivel 1",0,(0,0,0))
            screen.fill(blanco) # pinta el fondo blanco para empezar
            # se actualizan todos los sprites y rectandulos del juego con las nuevas variables
            mapa1.update(screen,vx,vy)
            muros.update(screen,vx,vy)
            raton1.update(screen,vx,vy,t,espera)
            enemigo1.update(screen,vx,vy,evx,evy,a)
            enemigo2.update(screen,vx,vy,mvx,mvy,a)
            #Estos condicionales, revisan si el queso ya fue comido o no
            if(noqueso1 == False):
                queso1.update(screen,vx,vy)
            if(noqueso2 == False):
                queso2.update(screen,vx,vy)
            if(noqueso3 == False):
                queso3.update(screen,vx,vy)
            if(noqueso4 == False):
                queso4.update(screen,vx,vy)
            if(cronometro1 < 100 and cronometro1 > 80):
                if(noqueso5 == False):
                    queso5.update(screen,vx,vy)
            # este condicional reviza si el poder ha sido actuvado o no
            if(duracion > 0 and duracion < 21):
                estrellas.update(screen,vx,vy)
            fondo1.update(screen,vx,vy)
            screen.blit(textnivel,(584,37))
            screen.blit(textvidas,(584,127))
            screen.blit(textpuntaje1,(584,157))
            screen.blit(textnombre,(584,97))
            screen.blit(texttiempo,(584,67))

##            distancia1 = math.sqrt((abs(raton1.rect.left-enemigo1.rect.left)**2) + (abs(raton1.rect.top-enemigo1.rect.top)**2))
##            distancia2 = math.sqrt((abs(raton1.rect.left-enemigo2.rect.left)**2) + (abs(raton1.rect.top-enemigo2.rect.top)**2))
##
##            angulo1 = math.acos((abs(raton1.rect.left-enemigo1.rect.left))/distancia1)
##            angulo2 = math.acos((abs(raton1.rect.left-enemigo1.rect.left))/discancia)
            
            # se inicializan las imagenes del radar
            pygame.draw.rect(screen,azul,minirat)
            pygame.draw.rect(screen,rojo,minienem1)
            pygame.draw.rect(screen,rojo,minienem2)

##            if(distancia1 < 80):
##
##                if(angulo1 < 45 and angulo1 > 315):
##                    evx = 10
##                    evy = 0
##                if(angulo1 < 135 and angulo1 > 45):
##                    evx = 0
##                    evy = -10
##                if(angulo1 > 135 and angulo1 < 225):
##                    evx = -10
##                    evy = 0
##                if(angulo1 > 225 and angulo1 < 315):
##                    evx = 0
##                    evy = 10
                
            
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
                    
                    

            if(noqueso2 == False):
                pygame.draw.rect(screen,amarillo,miniques2)

            if(raton1.rect.colliderect(queso2.rect)):
                    queso2.rect.left,queso2.rect.top =(-67,-47)
                    miniques2.move(-11,-11)
                    noqueso2 = True
                    puntaje1 = puntaje1 + 200
                    

            if(noqueso3 == False):
                pygame.draw.rect(screen,amarillo,miniques3)

            if(raton1.rect.colliderect(queso3.rect)):
                    queso3.rect.left,queso3.rect.top =(-67,-47)
                    miniques3.move(-11,-11)
                    noqueso3 = True
                    puntaje1 = puntaje1 + 200
                    

            if(noqueso4 == False):
                pygame.draw.rect(screen,amarillo,miniques4)

            if(raton1.rect.colliderect(queso4.rect)):
                    queso4.rect.left,queso4.rect.top =(-67,-47)
                    miniques4.move(-11,-11)
                    noqueso4 = True
                    puntaje1 = puntaje1 + 200
            if(cronometro1 < 100 and cronometro1 > 80):
                    
                if(noqueso5 == False):
                    pygame.draw.rect(screen, blanco,miniques5)

                if(raton1.rect.colliderect(queso5.rect)):
                        queso5.rect.left,queso5.rect.top =(-67,-47)
                        miniques5.move(-11,-11)
                        noqueso5 = True
                        vidas = vidas + 1

            # se regula la duracion del poder del raton, debe durar aprox 1s, y cuando este contador llega a 0, se reinicia a 21, su valor inicial
            if( duracion < 21):
                duracion = duracion -1
            if(duracion == 0):
                duracion = 21
                
            if( espera < 36):
                espera = espera - 1
            if( espera == 0):
                espera = 36

            contadorsegundos = contadorsegundos - 1

            if( contadorsegundos == 0):
                contadorsegundos = 20
                cronometro1 = cronometro1 - 1
                
            if(cronometro1 == 0 or vidas == 0):
                Jugar1 = False
                Muerte = True
            


            pygame.display.update() # Actualiza la pantalla cada vez que se hace un evento
             # Los eventos son cualquier interaccion con el juego(clicks, teclas, etc), tambien sirve la funcion pygame.display.flip()


    pygame.quit() # cuando se cierra el primer ciclo entra aqui para cerrar la interfaz

principal() # se llama toda la funcion
