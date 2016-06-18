#Importar librerias
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import math 

colorR = 0
colorG= 1
colorB = 0
grado = math.radians(30)
visualizacion = 0

puntos = []
	
traslacionMP = [
1,0,0,0,
0,1,0,0,
0,0,1,0,
0.1,0.2,0,1,
]

traslacionMN = [
1,0,0,0,
0,1,0,0,
0,0,1,0,
-0.1,-0.2,0,1,
]

rotacionM = [
math.cos(grado), math.sin(grado),0,0,
-math.sin(grado),math.cos(grado),0,0,
0,0,1,0,
0,0,0,1]

shearM = [
   1,    0,    0, 0,
   .3,    1,    0, 0,
   0,    0,      1,  0,
   0,    0,    0, 1,
]

reflexionM = [
1,0,0,0,
0,1,0,0,
0,0,1,0,
0,0,0,1,
]

	
def InitGL(Width, Height):
	global puntos, mrotacion
	glClearColor(0.53,0.53,0.53,0.0)
	glClearDepth(1)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	puntos = [
	1.0  ,0.0  ,0.0  ,0.0,
	0.0  ,1.0  ,0.0  ,0.0,
	0.0  ,0.0  ,1.0  ,0.0,
	0.0  ,0.0  ,0.0  ,1.0
	]
	

def mostrarEscena():

	global colorR, colorG, colorB
	global grado, puntos
	global visualizacion
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(colorR, colorG, colorB)
	glLoadMatrixf(puntos)
		
	if visualizacion == 1:
		glViewport(0,0,350,350)
		
	if visualizacion == 2:
		glViewport(0,0,200,200)
		
	if visualizacion == 3:
		glViewport(0,0,50,50)
	
	
	puntos = glGetFloat(GL_PROJECTION_MATRIX)

	glutSolidCube(0.5)	
	glutSwapBuffers();

def keyPressed(key,x,y):
	global colorR
	global colorG 
	global colorB
	global visualizacion
	if(key[0]=="q"):
		visualizacion = 1
	if(key[0]=="w"):
		visualizacion = 2
	if(key[0]=="e"):
		visualizacion = 3	
	
		
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
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	window = glutCreateWindow('Cuadrado')

	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	glutKeyboardFunc(keyPressed)
	InitGL(500,500)
	glutMainLoop()


if __name__ == "__main__":
	main()
