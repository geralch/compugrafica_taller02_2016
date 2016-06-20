## Geraldine Caicedo Hidalgo - 1527691
# Sebastian Salazar - 0938596
# Computacion Grafica
# Practica 02 - Junio 2016
# Cubo | Piramide

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import os
import threading
import random

window = 0
proyeccion = 0
vista = 0
visualizacion = 0
DIRECTION = 1

## Variables para ir acomodando el lookup
varUPx = 0
varUPy = 0
varUPz = 0
varEyex = 0
varEyey = 0
varEyez = 0
varCentx = 0
varCenty = 0
varCentz = 0

varT = ""




def InitGL(Width, Height):

    glClearColor(0.53,0.53,0.53,0.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

def elegirProyeccion(proyeccion):
	# Proyeccion Paralela
	if(proyeccion==1):
		glOrtho(-4,4,-4,4,-4,4)
		
	#Proyeccion Prespectiva
	if(proyeccion==2):
		gluPerspective(120, 6/4, 10, 2)
		
def elegirVista(vista):
	# Vista 1
	if(vista==1):
		gluLookAt(0,0,0,1,1,1,0,0,0)
		
	# Vista 2
	if(vista==2):
		gluLookAt(0,0,0,1,1,1,0,0,0)
		
	# Vista 3
	if(vista==3):
		gluLookAt(0,0,0,1,1,1,0,0,0)
		
def accionesMarquesina(visualizacion):
	# Marquesina
	if (visualizacion==1):
		gluLookAt(0,0,0,1,1,1,0,0,0)

def mostrarEscena():
	global DIRECTION, proyeccion, vista, visualizacion
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	# ----------------Cubo
	glLoadIdentity()
	elegirProyeccion(proyeccion)
	elegirVista(vista)
	accionesMarquesina(visualizacion)
	# Vista Principal
	#if(vista==4):
	#	gluLookAt(0,0,0,1,1,1,0,0,0)
	
	# Arriba
	
	glBegin(GL_QUADS)
	glColor3f(1,0,0) # Rojo
	glVertex3f(0.5, 1.5,  0.5)
	glVertex3f(0.5, 1.5,  1.5)
	glVertex3f(1.5, 1.5,  1.5)
	glVertex3f(1.5, 1.5,  0.5)
	glEnd()
	
	# Abajo
	glBegin(GL_QUADS)
	glColor3f(1,1,1) # Blanco
	glVertex3f(0.5, 0.5,  0.5)
	glVertex3f(0.5, 0.5,  1.5)
	glVertex3f(1.5, 0.5,  1.5)
	glVertex3f(1.5, 0.5,  0.5)
	glEnd()
	
	# Frente
	glBegin(GL_QUADS)
	glColor3f(0,0,1) # Azul
	glVertex3f(0.5, 1.5,  1.5)
	glVertex3f(0.5, 0.5,  1.5)
	glVertex3f(1.5, 0.5,  1.5)
	glVertex3f(1.5, 1.5,  1.5)
	glEnd()
	
	# Derecha
	glBegin(GL_QUADS)
	glColor3f(0,1,0) # Verde
	glVertex3f(1.5, 1.5,  0.5)
	glVertex3f(1.5, 1.5,  1.5)
	glVertex3f(1.5, 0.5,  1.5)
	glVertex3f(1.5, 0.5,  0.5)
	glEnd()
	
	# Izquierda
	glBegin(GL_QUADS)
	glColor3f(0,1,1) # Cyan
	glVertex3f(0.5, 0.5,  0.5)
	glVertex3f(0.5, 0.5,  1.5)
	glVertex3f(0.5, 1.5,  1.5)
	glVertex3f(0.5, 1.5,  0.5)
	glEnd()
	
	# Atras
	glBegin(GL_QUADS)
	glColor3f(0,0,0) # Negro
	glVertex3f(0.5, 0.5,  0.5)
	glVertex3f(0.5, 1.5,  0.5)
	glVertex3f(1.5, 1.5,  0.5)
	glVertex3f(1.5, 0.5,  0.5)
	glEnd()
    
    # ---------------Piramide
	
	glLoadIdentity()
	elegirProyeccion(proyeccion)
	elegirVista(vista)
	accionesMarquesina(visualizacion)
	
	# Base
	glBegin(GL_QUADS)
	
	glColor3f(1,0,0) # Rojo
	glVertex3f(-1.5, -3, -1.5)
	glVertex3f(-1.5, -3, -2.5)
	glVertex3f(-2.5, -3, -2.5)
	glVertex3f(-2.5, -3, -1.5)
	glEnd()
	
	# Frente
	glBegin(GL_TRIANGLES)
	glColor3f(1,1,1) # Blanco
	glVertex3f(-1.5, -3, -1.5)
	glVertex3f(-2.5, -3, -1.5)
	glVertex3f(-2, -1.5, -2)
	glEnd()
	
	# Derecha
	glBegin(GL_TRIANGLES)
	glColor3f(0,0,1) # Azul
	glVertex3f(-1.5, -3, -1.5)
	glVertex3f(-1.5, -3, -2.5)
	glVertex3f(-2, -1.5, -2)
	glEnd()
	
	# Izquierda
	glBegin(GL_TRIANGLES)
	glColor3f(0,1,0) # Verde
	glVertex3f(-2.5, -3, -1.5)
	glVertex3f(-2.5, -3, -2.5)
	glVertex3f(-2, -1.5, -2)
	glEnd()
	
	# Atras
	glBegin(GL_TRIANGLES)
	glColor3f(0,1,1) # Cyan
	glVertex3f(-1.5, -3, -2.5)
	glVertex3f(-2.5, -3, -2.5)
	glVertex3f(-2, -1.5, -2)
	glEnd()
	
	glutSwapBuffers()

def keyPressed(key,x,y):

	global proyeccion, vista
	global varUPx, varUPy, varUPz, varEyex, varEyey, varEyez, varCentx, varCenty, varCentz, varT
	# Proyeccion Paralela 
	if(key[0]=="r"):
		vista = 0
		visualizacion = 0
		proyeccion=1
		
	# Proyeccion Prespectiva
	if(key[0]=="f"):
		vista = 0
		visualizacion = 0
		proyeccion = 2
	# Camara Inicial
	if(key[0]=="0"):
		vista = 0
		proyeccion = 0
		visualizacion = 0
	# Camara 1
	if(key[0]=="1"):
		vista = 0
		proyeccion = 0
		vista = 1
	# Camara 2
	if(key[0]=="2"):
		vista = 0
		proyeccion = 0
		vista = 2
	# Camara 3
	if(key[0]=="3"):
		vista = 0
		proyeccion = 0
		vista = 3
	# Iniciar Marquesina
	if(key[0]=="m"):
		vista = 0
		proyeccion = 0
		visualizacion = 1
	# Detener Marquesina
	if(key[0]=="n"):
		visualizacion = 0
		vista = 0
		proyeccion = 0
	##Para intentar acomodar el lookup t=ojo y=centro u=up
	if(key[0]=="t"):
		varT = "ojo"
	if(key[0]=="y"):
		varT = "centro"
	if(key[0]=="u"):
		varT = "up"
	##cuando sea el ojo
	if(key[0]=="i" && varT=="ojo"):
		varEyex += 1
	if(key[0]=="j" && varT=="ojo"):
		varEyex -= 1
	"""
	if(key[0]=="p"):
		varEyex += 1
	#mover Eye x --
	if(key[0]=="o"):
		varEyex -= 1
	#mover Eye y ++
	if(key[0]=="l"):
		varEyey += 1
	#mover Eye y ++
	if(key[0]=="k"):
		varEyey -= 1
	#mover Eye z ++
	if(key[0]=="i"):
		varEyez += 1
	#mover Eye z --
	if(key[0]=="u"):
		varEyez -= 1
	#Imprimir la config
	"""
	print "upx: %i upy:%i upz:%i eyex:%i eyey:%i eyez%i centx:%i centy:%i centz:%i" % (varUPx, varUPy, varUPz, varEyex, varEyey, varEyez, varCentx, varCenty, varCentz)

def main():

		global window
		global proyeccion

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(500,500)
		glutInitWindowPosition(200,200)

		window = glutCreateWindow('Cubo y Piramide')

		glutDisplayFunc(mostrarEscena)
		glutIdleFunc(mostrarEscena)
		glutKeyboardFunc(keyPressed)
		InitGL(500,500)
		glutMainLoop()

if __name__ == "__main__":
        main()
