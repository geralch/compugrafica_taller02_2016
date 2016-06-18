#Importar librerias
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random

colorR = 1
colorG= 0
colorB = 0
visualizacion = 0

puntos = [0, 0, 0.35, 0.2, 0.7, 0]

def InitGL(Width, Height):
	
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
def mostrarEscena():
	global visualizacion
	global colorR, colorG, colorB
	
	if visualizacion == 1:
		glViewport(0,0,350,350)
		
	if visualizacion == 2:
		glViewport(0,0,200,200)
		
	if visualizacion == 3:
		glViewport(0,0,50,50)	
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(colorR, colorG, colorB)
	glBegin(GL_TRIANGLES)
	glVertex2f(puntos[0],puntos[1]) 
	glVertex2f(puntos[2],puntos[3])
	glVertex2f(puntos[4],puntos[5]) 
	glEnd()
	
	glColor3f(255/135,255/135,255/135)
	glBegin(GL_LINES)
	glVertex2f(-1,0)
	glVertex2f(1,0)
	glVertex2f(0,-1)
	glVertex2f(0,1)	
	glEnd()
	glViewport(0,0,500,500)
	glutSwapBuffers();
	
def keyPressed(key,x,y):
	
	global visualizacion
	if(key[0]=="q"):
		visualizacion = 1
	if(key[0]=="w"):
		visualizacion = 2
	if(key[0]=="e"):
		visualizacion = 3	
	
	glLoadIdentity()

def clickDerecho(button,state,x,y):
	global colorR
	global colorG 
	global colorB
	if (button==GLUT_LEFT_BUTTON and state==GLUT_UP):
		colorR = random.random()
		colorG = random.random()
		colorB = random.random()
		
def main():
	global window

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	window = glutCreateWindow('Triangulo')

	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(clickDerecho)
	print(
	"Punto 1: [" + str(puntos[0]) + "," + str(puntos[1])+"]\n"+
	"Punto 2: [" + str(puntos[2]) + "," + str(puntos[3])+"]\n"+
	"Punto 3: [" + str(puntos[4]) + "," + str(puntos[5])+"]"
	)
	InitGL(500,500)
	glutMainLoop()


if __name__ == "__main__":
	main()
