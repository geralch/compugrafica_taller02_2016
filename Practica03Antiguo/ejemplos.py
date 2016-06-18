from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random

def main():

    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    window = glutCreateWindow("Test")

    
    InitGL(500,500)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    
    glutMainLoop()

    
def InitGL(Width, Height):
	glClearColor(0.53,0.53,0.53,0.0)
	
	

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	#
	#
	#• glOrtho(left,right,btm,top,near,far);
	#glOrtho(0,1,-1,1,1,-2) 
	glFrustum(-1,1,-1,1,0.25,0.35);      
	# glFrustum(GLdouble x1, GLdouble x2, GLdouble y1GLdouble y2, GLdouble z1, GLdouble z2);
 	

def mostrarEscena():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode (GL_MODELVIEW);
	
	glLoadIdentity();
	glViewport(0,0,500,500)	
	#gluLookAt(-1, 0.1, 0,
	#0, 0, 0,
	#1, 1, 0);  	
	
	glBegin(GL_POLYGON);
 
	glColor3f( 0.0, 1.0, 0.0 );     
	glVertex3f(  0.25, -0.25, -0.25 );      
	glVertex3f(  0.25,  0.25, -0.25 );      
	glVertex3f( -0.25,  0.25, -0.25 );      
	glVertex3f( -0.25, -0.25, -0.25 );      
 
	glEnd();

	glBegin(GL_POLYGON);
	glColor3f( 1.0, 0.0, 0.0 ); 
	glVertex3f(  0.25, -0.25, 0.25 );
	glVertex3f(  0.25,  0.25, 0.25 );
	glVertex3f( -0.25,  0.25, 0.25 );
	glVertex3f( -0.25, -0.25, 0.25 );
	glEnd();
	 

	glBegin(GL_POLYGON);
	glColor3f( 1.0, 0.4, 1.0 );
	glVertex3f( 0.25, -0.25, -0.25 );
	glVertex3f( 0.25,  0.25, -0.25 );
	glVertex3f( 0.25,  0.25,  0.25 );
	glVertex3f( 0.25, -0.25,  0.25 );
	glEnd();
	 
	
	glBegin(GL_POLYGON);
	glColor3f( 0.4, 0.4, 0.0 );
	glVertex3f( -0.25, -0.25,  0.25 );
	glVertex3f( -0.25,  0.25,  0.25 );
	glVertex3f( -0.25,  0.25, -0.25 );
	glVertex3f( -0.25, -0.25, -0.25 );
	glEnd();
	 
	
	glBegin(GL_POLYGON);
	glColor3f( 0.0, 0.4, 0.8 );
	glVertex3f(  0.25,  0.25,  0.25 );
	glVertex3f(  0.25,  0.25, -0.25 );
	glVertex3f( -0.25,  0.25, -0.25 );
	glVertex3f( -0.25,  0.25,  0.25 );
	glEnd();

	glBegin(GL_POLYGON);
	glColor3f( 0.8, 0.4, 0.0 );
	glVertex3f(  0.25, -0.25, -0.25 );
	glVertex3f(  0.25, -0.25,  0.25 );
	glVertex3f( -0.25, -0.25,  0.25 );
	glVertex3f( -0.25, -0.25, -0.25 );
	glEnd()
	glFlush()
	glutSwapBuffers();	glFlush()

	glutSwapBuffers()

    
   
    

if __name__ == '__main__': main()
