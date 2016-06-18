# Geraldine Caicedo Hidalgo - 1527691
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

DIRECTION = 1


def InitGL(Width, Height):

    glClearColor(0.53,0.53,0.53,0.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-4,4,-4,4,-4,4)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def mostrarEscena():
	global DIRECTION
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
	# ----------------Cubo
	glLoadIdentity()
	glTranslatef(0,0,-6)
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
	global colorR
	global colorG 
	global colorB
	global visualizacion
	# Proyeccion Paralela 
	if(key[0]=="r"):
		
		print("r")
	# Proyeccion Prespectiva
	if(key[0]=="f"):
		visualizacion = 2
	# Camara Inicial
	if(key[0]=="0"):
		visualizacion = 3
	# Camara 1
	if(key[0]=="1"):
		visualizacion = 3
	# Camara 2
	if(key[0]=="2"):
		visualizacion = 3
	# Camara 3
	if(key[0]=="3"):
		visualizacion = 3
	# Iniciar Marquesina
	if(key[0]=="m"):
		visualizacion = 3
	# Detener Marquesina
	if(key[0]=="n"):
		visualizacion = 3

def main():

		global window

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
