from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Global variables for Ismail's background work
shooting_stars = []
comets = []  # Initialize comets list
saturn_planets = []  # Initialize saturn_planets list

def resetGame(): ###   RODEL Assignment 3 Mod  ####
    global playerLife, score, bulletMissed, camera_pos, fovY, GRID_LENGTH, playerPos, playerOrientation, death, fat, time, enemyList, shotSpeed, liveRounds, cheat, Aspeed, nspeed
    global bulletCount, enemyNo, fpsView, mouse_x, mouse_y, W_Width, W_Height, mouse_held, targetPos, targetX, fire_scale_angle, enemy_bullets, shotSize, bullet_speed,last_speed_increment, mainMenu
    mouse_x, mouse_y = 0, 0
    global paused
    paused = False
    last_speed_increment = 0
    ###Ismail's bg work ###
    global stars, sun_positions, black_hole_pos, shooting_stars  # Add new global variables
    global extra_black_holes, saturn_planets
    global center_black_holes, center_suns, saturn_ring_angle

    saturn_ring_angle = 0

    
    # Initialize stars
    stars = []
    for _ in range(1000):
        x = random.uniform(-2000, 2000)
        y = random.uniform(-2000, 2000)
        z = random.uniform(-2000, 2000)
        size = random.uniform(0.5, 2.5)
        stars.append([x, y, z, size])

    # Initialize multiple suns
    sun_positions = []
    for _ in range(8):  # 8 suns
        # Randomly choose which edge to spawn from
        edge = random.choice(['top_left', 'top_right', 'top', 'bottom'])
        if edge == 'top_left':
            x = random.uniform(-2000, -1500)
            y = -2000
            z = random.uniform(-2000, 2000)
        elif edge == 'top_right':
            x = random.uniform(1500, 2000)
            y = -2000
            z = random.uniform(-2000, 2000)
        elif edge == 'top':
            x = random.uniform(-1500, 1500)
            y = -2000
            z = random.uniform(1500, 2000)
        else:  # bottom
            x = random.uniform(-1500, 1500)
            y = -2000
            z = random.uniform(-2000, -1500)
        size = random.uniform(8, 12)
        sun_positions.append([x, y, z, size])

    # Initialize main black hole position (top right)
    black_hole_pos = [1800, -1800, 500]

    # Initialize additional black holes
    extra_black_holes = []
    for _ in range(3):  # Add 3 more black holes
        # Randomly choose which edge to spawn from
        edge = random.choice(['top_left', 'top_right', 'top', 'bottom'])
        if edge == 'top_left':
            x = random.uniform(-2000, -1500)
            y = -2000
            z = random.uniform(-2000, 2000)
        elif edge == 'top_right':
            x = random.uniform(1500, 2000)
            y = -2000
            z = random.uniform(-2000, 2000)
        elif edge == 'top':
            x = random.uniform(-1500, 1500)
            y = -2000
            z = random.uniform(1500, 2000)
        else:  # bottom
            x = random.uniform(-1500, 1500)
            y = -2000
            z = random.uniform(-2000, -1500)
        size = random.uniform(12, 18)
        extra_black_holes.append([x, y, z, size])

    # Initialize shooting stars and comets
    shooting_stars = []
    comets = []  # New list for comets
    for _ in range(5):  # Initialize some comets
        x = random.uniform(-1800, 1800)
        y = random.uniform(-1800, 1800)
        z = random.uniform(-1800, 1800)
        speed_x = random.uniform(-3, 3)
        speed_y = random.uniform(-3, 3)
        speed_z = random.uniform(-3, 3)
        size = random.uniform(3, 5)
        comets.append([x, y, z, speed_x, speed_y, speed_z, size, 100])  # Last number is trail length

    # Remove center black holes and suns
    center_black_holes = []
    center_suns = []

    ###End of Ismail's bg work ###

    W_Width, W_Height = 1280, 720 #Window Height and Width

    global shake_timer, shake_offset, shake_direction
    shake_timer = 0
    shake_offset = 0
    shake_direction = 1

    global spawn_positions
    spawn_positions = [
        [0, -2000, 0], #Point for stars and background spawn (Center Origin)
        [0, -2000, 300], #North (UP)
        [0, -2000, -300], #South (DOWN)

        [350, -2000, 0], #West (Left)
        [350, -2000, 300], #North West (UP LEFT)
        [350, -2000, -300], #South West (DOWN LEFT)

        [-350, -2000, 0], #East (Right)
        [-350, -2000, 300], #North East (UP RIGHT)
        [-350, -2000, -300] #South East (DOWN RIGHT)

    ]
    #Bullet variables
    mouse_held = False
    # if cheat:
    #     shotSpeed = 7.5
    # else:
    shotSpeed = 2.2
    shotSize = 15
    liveRounds = []
    bulletCount = 0

    #Death Blast variables
    global blast_triggered, blast_radius
    blast_triggered = False
    blast_radius = 0


    #Initiate game variables
    playerLife = 5
    score = 0
    bulletMissed = 0
    playerPos = [0,1400,0]  
    targetPos = playerPos[2]  # Target position for the camera
    targetX = playerPos[0]
    playerOrientation = 180
    death = False
    
    #Enemy variables
    fat = 5
    time = 0
    # Enemy vars
    global enemies, enemy_size, enemy_speed, enemy_num, scaling_rate, scale, enemyMax
    enemies = []
    enemy_size = 50
    enemy_speed = 1.5
    enemy_num = 5
    scaling_rate = 0.01
    scale = 1
    enemyList = []
    enemyMax = 3
    bullet_speed = 2

    enemy_bullets = []
    fire_scale_angle = 0.0

    global shake_time_accumulator
    shake_time_accumulator = 0.0
    
    
    fpsView = False  # First Person View

    global targetCamAngle, targetCamDistance, targetCamHeight
    targetCamAngle, targetCamDistance, targetCamHeight = -15, 2000, 155
    # Camera-related variables
    global camAngle, camDistance, camHeight
    camera_pos = (0,500,500)
    camAngle= -15
    camDistance= 2000
    camHeight= 155
    
    fovY = 90  # Field of view
    GRID_LENGTH = 600  # Length of grid lines 
    
    ##CAMERA VARIABLES
    global camMinZ, camMaxZ, camMinY, camMaxY
    camMinY = 100
    camMaxY = 1000
    camMinZ = 100
    camMaxZ = 1000
    
    global asteroidList, asteroidMax
    asteroidList = []
    asteroidMax = 3
    Aspeed = 0.8
    global bombList, bombMax, nuke, blast_expand
    bombList = []
    bombMax = 1
    blast_expand = False
    nuke = False
    nspeed = 2.5
    mainMenu = False #SAJID 
resetGame()
mainMenu = True
def pause():
    """
    Pauses the game by stopping the idle function.
    """
    global paused
    if not paused:
        paused = True
        glutIdleFunc(None)  # Stop the idle function
    else:
        paused = False
        glutIdleFunc(idle)
     
#Assignment 2 of Rodel
#convert screen coordinates to OpenGL coordinates as theyre apparently different wth
def screen_to_opengl(x, y): ###   RODEL   ####
    opengl_x = (x / W_Width) * 2 - 1  
    opengl_y = 1 - (y / W_Height) * 2 
    return opengl_x, opengl_y

def crosshairPoints(m, n): ###   RODEL   ####
    gl_x, gl_y = screen_to_opengl(m, n)

def draw_crosshair(x, y): ###   RODEL   ####
    global mouse_held

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # 2D overlay
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_DEPTH_TEST)
    glLineWidth(2)
    glColor3f(1, 1, 1)

    size = 0.03
    glBegin(GL_LINES)
    if mouse_held:
        # Draw "X"
        glVertex2f(x - size, y - size)
        glVertex2f(x + size, y + size)
        glVertex2f(x - size, y + size)
        glVertex2f(x + size, y - size)
    else:
        # Draw "+"
        glVertex2f(x - size, y)
        glVertex2f(x + size, y)
        glVertex2f(x, y - size)
        glVertex2f(x, y + size)
    glEnd()

    glEnable(GL_DEPTH_TEST)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18): ### ISMAIL ###
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    # Set up an orthographic projection that matches window coordinates
    gluOrtho2D(0, 1000, 0, 800)  # left, right, bottom, top
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Draw text at (x, y) in screen coordinates
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    
    # Restore original projection and modelview matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def keyboardListener(key, x, y):
    """
    Handles keyboard inputs for player movement, gun rotation, camera updates, and cheat mode toggles.
    """
    global playerOrientation, playerPos, cheat, shake_timer

    angle = playerOrientation - 90  # Adjust angle for forward movement
    # Move Upwards (W key)
    global targetPos, targetX, death #TargetPos is targetZ
    if not death: 
        #If space pressed, game pauses
        if key == b' ' and not mainMenu:
            pause()
            print("Pause Triggered!")
        elif key == b' ' and mainMenu:
            resetGame()
        if not mainMenu:
            if key == b'w' or key == b'W' or key == GLUT_KEY_UP:
                if targetPos < 300:
                    targetPos += 300  # Snap forward in steps
                elif playerPos[2] == 300:
                    shake_timer = 50  # Trigger shake
            
            elif key == b's' or key == b'S' or key == GLUT_KEY_DOWN:
                if targetPos > -300:
                    targetPos -= 300  # Snap backward in steps
                elif playerPos[2] == -300:
                    shake_timer = 10  # Trigger shake
        
            elif key == b'd' or key == b'D' or key == GLUT_KEY_RIGHT:
                if targetX > -350:
                    if targetX == 0:
                        targetX -= 350 #Was 400
                    elif targetX == 350:
                        targetX -= 350
                elif playerPos[0] == 350:
                    shake_timer = 10
            
            elif key == b'a' or key == b'A' or key == GLUT_KEY_LEFT:
                if targetX < 350: #Was 400
                    if targetX == 0:
                        targetX += 350
                    elif targetX == -350:#Was 400
                        targetX += 350 #Was 400
                elif playerPos[0] == -350:
                    shake_timer = 10

    # Reset the game if R key is pressed
    if key == b'r' and not mainMenu:
        resetGame()
        print("Game Reset!")


def specialKeyListener(key, x, y): #
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """

    # global camera_pos, camMinZ, camMaxZ, camMinY, camMaxY, camHeight, camDistance, camAngle
    global playerOrientation, playerPos, shake_timer

    angle = playerOrientation - 90  # Adjust angle for forward movement
    # Move Upwards (W key)
    global targetPos, targetX, death #TargetPos is targetZ
    if not death: 
        #If space pressed, game pauses
        if key == b' ' and not mainMenu:
            pause()
            print("Pause Triggered!")
        elif key == b' ' and mainMenu:
            resetGame()
        if not mainMenu:
            if key == GLUT_KEY_UP:
                if targetPos < 300:
                    targetPos += 300  # Snap forward in steps
                elif playerPos[2] == 300:
                    shake_timer = 50  # Trigger shake
            
            elif key == GLUT_KEY_DOWN:
                if targetPos > -300:
                    targetPos -= 300  # Snap backward in steps
                elif playerPos[2] == -300:
                    shake_timer = 10  # Trigger shake
        
            elif key == GLUT_KEY_RIGHT:
                if targetX > -350:
                    if targetX == 0:
                        targetX -= 350 #Was 400
                    elif targetX == 350:
                        targetX -= 350
                elif playerPos[0] == 350:
                    shake_timer = 10
            
            elif key == GLUT_KEY_LEFT:
                if targetX < 350: #Was 400
                    if targetX == 0:
                        targetX += 350
                    elif targetX == -350:#Was 400
                        targetX += 350 #Was 400
                elif playerPos[0] == -350:
                    shake_timer = 10
    # #x, y, z = camera_pos
    
    # # Move camera up (UP arrow key)
    # if key == GLUT_KEY_UP:
    #     if camHeight > camMinY:
    #         camHeight -= 5
    #     # if z > camMinZ:
    #     #     z -= 5

    # # # Move camera down (DOWN arrow key)
    # if key == GLUT_KEY_DOWN:
    #     if camHeight < camMaxY:
    #         camHeight += 5
    #     # if z < camMaxZ:
    #     #     z += 5

    # # moving camera left (LEFT arrow key)
    # if key == GLUT_KEY_LEFT:
    #     # if camDistance > 0:
    #         camAngle -= 1 
    #     # if camHeight > camMinY:
    #         # y -= 5

    # # moving camera right (RIGHT arrow key)
    # if key == GLUT_KEY_RIGHT:
    #     # if camDistance < 2000: 
    #         camAngle += 1
    #     # x += 5  
    #     # if camHeight < camMaxY:
    #     #     camHeight += 5

    # #camera_pos = (x, y, z)
    # # Print the camera position for debugging
    print(f"camAngle: {camAngle}, camDistance: {camDistance}, camHeight: {camHeight}")


def mouseMotion(x, y): ###   RODEL  Ass 2 ####
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y

def mouseListener(button, state, x, y): ###   RODEL   ####
    """
    Handles mouse inputs for firing bullets (left click) and toggling camera mode (right click).
    """
    # Left mouse button fires a bullet
    global bulletCount , mouse_held, fpsView, death, score
    if not mainMenu:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            fireBullet()  
            mouse_held = True
            bulletCount = bulletCount + 1 - score
            # if bulletCount > 10:
            #     death = True
            #     print("Game Over!")
            print("Bullet fired!")
            print(f'Mouse position: {mouse_x}, {mouse_y}')
        elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
            mouse_held = False

        # Right mouse button toggles FPV camera mode
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            fpsView = not fpsView  # Toggle first-person view
            if not fpsView:
                global targetCamAngle, targetCamDistance, targetCamHeight
                targetCamAngle = 0
                targetCamDistance = 2000
                targetCamHeight = 270
            else:
                targetCamAngle = -15
                targetCamDistance = 2000
                targetCamHeight = 155
   

def mouseMotion(x, y): ###   RODEL   ####
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y



def setupCamera(): ###   RODEL Assignment 3 Mod  ####
    global camAngle, camDistance, camHeight, camera_pos, shake_z_offset, shake_time_accumulator
    """
    Configures the camera's projection and view settings.
    Uses a perspective projection and positions the camera to look at the target.
    """
    glMatrixMode(GL_PROJECTION)  # Switch to projection matrix mode
    glLoadIdentity()  # Reset the projection matrix
    # Set up a perspective projection (field of view, aspect ratio, near clip, far clip)
    gluPerspective(fovY, 1.25, 0.1, 3500) # Think why aspect ration is 1.25?
    glMatrixMode(GL_MODELVIEW)  # Switch to model-view matrix mode
    glLoadIdentity()  # Reset the model-view matrix
    x, y, z = camera_pos
    angle = math.radians(camAngle)
    x = camDistance * math.sin(angle)
    y = camDistance * math.cos(angle)
    z = camHeight #+ math.sin(shake_time_accumulator)  # Subtle shake added here

    gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)

def fatEnemy(): ###   RODEL  Assignment 3 ####
    global fat, time, death
    
    if not death:
        time += 0.01
        fat = -abs(5 * math.sin(time))

def idle():
    """
    Idle function that runs continuously:
    - Triggers screen redraw for real-time updates.
    """
    # Ensure the screen updates with the latest changes
    global playerLife, death, bulletMissed, cheat, targetPos, shake_timer, shake_offset, shake_direction
    update_stars()
    update_space_elements()  # Update sun, black hole, and shooting stars
    fatEnemy()  # Update enemy size
    bulletMovement()
    difficulty_inc()
    if not death and not mainMenu:  ###   RODEL   ####
        asteroidSpawn()
        spawnNuclearBombList()
        enemySpawn()
        enemyMovement()
        update_enemy_bullets()
        enemyThruster_fire()
        nuclearBombMovement()
    asteroidMovement()
    
    
    ###   RODEL   ####
    if playerLife == 0 :  #or bulletMissed > 20
        death = True
    if not death:
        enemyMovement()  # Move enemies toward player


    # Smooth interpolation toward targetZ ###   RODEL   ####
    speed = 2
    if abs(playerPos[2] - targetPos) > speed:
        if playerPos[2] < targetPos:
            playerPos[2] += speed
        elif playerPos[2] > targetPos:
            playerPos[2] -= speed
    else:
        playerPos[2] = targetPos
        
    # Smooth interpolation toward targetX ###   RODEL   ####
    if abs(playerPos[0] - targetX) > speed:
        if playerPos[0] < targetX:
            playerPos[0] += speed
        elif playerPos[0] > targetX:
            playerPos[0] -= speed
    else:
        playerPos[0] = targetX

    global camAngle, camDistance, camHeight, targetCamAngle, targetCamDistance, targetCamHeight

    speed = 0.7
    ###   RODEL   ####
    # Smooth camAngle ###   RODEL   ####
    if abs(camAngle - targetCamAngle) > 0.5:
        camAngle += speed * ((targetCamAngle - camAngle) / abs(targetCamAngle - camAngle))
    
    # Smooth camDistance 
    if abs(camDistance - targetCamDistance) > 1:
        camDistance += speed * ((targetCamDistance - camDistance) / abs(targetCamDistance - camDistance))
    
    # Smooth camHeight
    if abs(camHeight - targetCamHeight) > 1:
        camHeight += speed * ((targetCamHeight - camHeight) / abs(targetCamHeight - camHeight))

    # Shake effect logic if corner case is triggered
    if shake_timer > 0:
        shake_offset = 10 * shake_direction
        shake_direction *= -1
        shake_timer -= 1
    else:
        shake_offset = 0


    ###   RODEL   ####
    global blast_triggered, blast_radius, nuke, blast_expand
    #DEATH BLAST
    if death and not blast_triggered:
        blast_triggered = True
        blast_radius = 1
    
    #expanding blast radius w time
    # if (blast_triggered and blast_radius < 500):
    #     blast_radius += 5
    if blast_triggered:
        if blast_expand or death:
            if blast_radius < 500:
                blast_radius += 5
            else:
                blast_expand = False  # Start contracting
        else:
            if blast_radius > 0:
                blast_radius -= 5
            else:
                # Blast is over
                blast_triggered = False
                nuke = False

    
    # Subtle continuous rocket shake effect (on camHeight)
    global shake_time_accumulator, shake_z_offset
    shake_time_accumulator += 0.05  # Controls speed of the oscillation
    shake_z_offset = math.sin(shake_time_accumulator) * 0.8  # Subtle Z oscillation
    ###   RODEL ENDS  ####
    

    glutPostRedisplay()

def draw_axes(length=2000): ###   RODEL Assignment 3 Mod  ####
    glLineWidth(3)
    glBegin(GL_LINES)

    # X axis – Red
    glColor3f(1, 0, 0)
    glVertex3f(-length, 0, 0)
    glVertex3f(length, 0, 0)

    # Y axis – Green
    glColor3f(0, 1, 0)
    glVertex3f(0, -length, 0)
    glVertex3f(0, length, 0)

    # Y Side axis
    glColor3f(0, 1, 0.5)
    glVertex3f(-400, -length, 0)
    glVertex3f(-400, length, 0)

    # Y Side axis-2
    glColor3f(0, 1, 0.5)
    glVertex3f(350, -length, 0)
    glVertex3f(350, length, 0)

    # Y/Z Side axis bottom
    glColor3f(0, 1, 1)
    glVertex3f(0 , -length, -300)
    glVertex3f(0, length, -300)
    # Y/Z Side axis top
    glColor3f(0, 1, 1)
    glVertex3f(0 , -length, 300)
    glVertex3f(0, length, 300)

    # Y/Z Side axis-2 bottom
    glColor3f(0, 1, 1)
    glVertex3f(350 , -length, 300)
    glVertex3f(350, length, 300)
    # Y/Z Side axis-2 top
    glColor3f(0, 1, 1)
    glVertex3f(-350 , -length, 300)
    glVertex3f(-350, length, 300)
    # Y/Z Side axis-2 bottom
    glColor3f(1, 1, 1)
    glVertex3f(350 , -length, -300)
    glVertex3f(350, length, -300)
    # Y/Z Side axis-2 top
    glColor3f(1, 1, 1)
    glVertex3f(-350 , -length, -300)
    glVertex3f(-350, length, -300)

    # Z axis – Blue
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -length)
    glVertex3f(0, 0, length)

    glEnd()
    glLineWidth(1)  #Resetting to def line widfh 

    #Debugging cam global var
    
def drawSpaceship():    ###   RODEL   ####
    global fat, playerPos
    glPushMatrix() #Parent Matrix Start
    glTranslatef(*playerPos)  # Move to the center of the screen
    glTranslate(0, 0, shake_offset)  #Apply shake effect if corner case
    glScalef(1.5, 1.5, 1.5)  # Scale down the spaceship
    glRotatef(90, 1, 0, 0)  # Rotate to face the camera

    #Spaceship wings 
    glPushMatrix()
    glTranslatef(0, 0, -20) #Move the sphere above the ground
    glColor3f(1, 1, 0.92)
    #glRotatef(90, 0, 1, 0)  # Rotate to align with the ground
    glScalef(3, 0.2, 0.5)  # Scale down the wings 
    glutSolidCube(100) #parameters are: radius, slices, stacks
    glPopMatrix()

    #Spaceship Window (on top of head)
    glPushMatrix()
    #glRotatef(90, 1, 0, 0)  
    glTranslatef(0, 0, 45) 
    glScalef(1, 1.4, 1.2)
    glColor3f(0, 0, 1)
    glutSolidSphere(21, 10, 10) #parameters are: radius, slices, stacks
    glPopMatrix()

    #Spaceship head 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor3f(1, 1, 1)
    glutSolidSphere(50, 10, 10) #parameters are: radius, slices, stacks
    glPopMatrix()

    #Spaceship bottom cylinder 
    glPushMatrix()
    glTranslatef(0, 0, -120) #Move the sphere above the ground
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCylinder(50, 20, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()

    #Spaceship body (Cylinder)
    glPushMatrix()
    glTranslatef(0, 0, -100) #Move the sphere above the ground
    glColor3f(1, 1, 1)
    glutSolidCylinder(50, 100, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()
    

    #Spaceship bottom base (Circle made from cylinder)
    glPushMatrix()
    glTranslatef(0, 0, -120) #Move the sphere above the ground
    glColor3f(0.3, 0.5, 0.5)
    glutSolidCylinder(50, 0, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()

    #Spaceship thruster flames (Cylinders)
    glPushMatrix()
    glTranslatef(0, -30, -140) #Move the sphere above the ground
    glRotatef(90, 0, 0, 1)  # Rotate to align with the ground
    glColor3f(1, 0.5, 0)
    glScalef(1, 1, fat/5)  # Scale down the flames
    glutSolidCylinder(10, 20, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()

    #Thursters 2
    glPushMatrix()
    glTranslatef(0, 30, -140) #Move the sphere above the ground
    glRotatef(90, 0, 0, 1)  # Rotate to align with the ground
    glColor3f(1, 0.5, 0)
    glScalef(1, 1, fat/5.5)  # Scale down the flames
    glutSolidCylinder(10, 20, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()


    #Spaceship Thrusters (Cylinders)
    glPushMatrix()
    glTranslatef(0, -30, -140) #Move the sphere above the ground
    glRotatef(90, 0, 0, 1)  # Rotate to align with the ground
    glColor3f(0.7, 0.7, 0.7)
    glutSolidCylinder(10, 20, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()
    #Thursters 2
    glPushMatrix()
    glTranslatef(0, 30, -140) #Move the sphere above the ground
    glRotatef(90, 0, 0, 1)  # Rotate to align with the ground
    glColor3f(0.7, 0.7, 0.7)
    glutSolidCylinder(10, 20, 10, 10) #parameters are: radius, height, slices, stacks
    glPopMatrix()

    #Spaceship body windows (Spheres)
    glPushMatrix()
    glTranslatef(-50, 18, -85) #Move the sphere above the ground
    glColor3f(0.1, 0.2 , 0.2)
    glutSolidSphere(10, 10, 10) #parameters are: radius, slices, stacks
    glTranslatef(0, 0, 40) #Move the sphere above the ground
    glutSolidSphere(10, 10, 10) #parameters are: radius, slices, stacks
    glTranslatef(0, 0, 40) #Move the sphere above the ground
    glutSolidSphere(10, 10, 10) #parameters are: radius, slices, stacks
    glPopMatrix()

    #Spaceship body windows (Spheres)
    glPushMatrix()
    glTranslatef(50, 18, -85) #Move the sphere above the ground
    glColor3f(0.1, 0.2 , 0.2)
    glutSolidSphere(10, 10, 10) #parameters are: radius, slices, stacks
    glTranslatef(0, 0, 40) #Move the sphere above the ground
    glutSolidSphere(10, 10, 10) #parameters are: radius, slices, stacks
    glTranslatef(0, 0, 40) #Move the sphere above the ground
    glutSolidSphere(10, 10, 10) #parameters are: radius, slices, stacks
    glPopMatrix()

    #Gun on top of spaceship (Cylinder)
    glPushMatrix()
    glTranslatef(0, 50, 0) #Move the sphere above the ground
    #glRotatef(90, 0, 1, 0)  # Rotate to align with the ground
    glColor3f(0.5, 0.5, 0.5)
    glScalef(1, 1, 0.5)  # Scale down the flames
    glutSolidCylinder(10, 20, 10, 10) #parameters are: radius, height, slices, stacks

    #Gun pointer (Cone)
    glutSolidCone(10, 100, 50, 40) #parameters are: base radius, height, slices, stacks
    glPopMatrix()

    glPopMatrix() #Parent Matrix End

def asteroids(): ###   RODEL  but unused ####
    glPushMatrix()
    glRotatef(90, 0, 1, 0)  # Rotate to align with the ground
    glTranslatef(0, 0, -2500) #Move the sphere above the ground
    glColor3f(1, 0.2 , 0.2)
    glScalef(1.5, 1.5, 1.5) 
    n = 40
    for i in range(30):
        #binary random 
        #if random.randint(0, 1) == 0:
        if True:
            glutSolidSphere(30, 10, 10) #parameters are: radius, slices, stacks
            glTranslatef(0, 0, n) #Move the sphere above the ground
        else:
            glutSolidCube(40) #parameters are: radius, slices, stacks
            glTranslatef(0, 0, n) #Move the sphere above the ground
        n = 100
    glPopMatrix()

def asteroidMovement(): ###   RODEL   ####
    global asteroidList, playerPos, death, score, last_speed_increment, Aspeed
    player_x, player_y = playerPos[0], playerPos[1]
    player_z = playerPos[2]
    
    for asteroid in asteroidList:
        asteroid[1] += Aspeed  # Move down along Y-axis
        if asteroid[1] > 2000:
            asteroidList.remove(asteroid)

    for enemy in asteroidList:
        enemy_x, enemy_y = enemy[0], enemy[1]

        dx = abs(player_x - enemy_x)
        dy = abs(player_y - enemy_y)
        dz = abs(player_z - enemy[2])

        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        if distance < 100 and enemy in asteroidList :  # If asteroid is close to player
            death = True
            print("Game Over!")

def asteroidSpawn(): ###   RODEL   ####
    global asteroidList
    global spawn_positions


    while len(asteroidList) < asteroidMax:
        # Pick a position not already used
        available = [pos for pos in spawn_positions if pos not in asteroidList]
        if not available:
            break

        pos = random.choice(available)
        asteroidList.append(pos.copy())  # Use copy to avoid reference issues

def drawAsteroids():###   RODEL   ####
    glColor3f(0.7, 0.7, 0.7)
    for asteroid in asteroidList:
        glPushMatrix()
        glTranslatef(*asteroid)
        glutSolidSphere(30, 10, 10)
        glPopMatrix()

def drawEnemies():###   SAJID   ####
    glColor3f(0.9, 0.1, 0.1)
    global enemyList, playerPos
    for enemy in enemyList:
        glPushMatrix()
        glTranslatef(enemy[0], enemy[1], enemy[2]+80)
        glScalef(1.4, 1.4, 1.4)

        # === Thrusters ===

        glPushMatrix()
        glTranslatef(0, 0, -10)  # Position below UFO
        glRotatef(-180, 1, 0, 0)  # Point downwards
        # Compute scale using sine wave
        flame_scale = 1.0 + 0.3 * math.sin(fire_scale_angle)
        glScalef(1.0, 1.0, flame_scale)
        # Flame color (orange)
        glColor3f(1.0, 0.4, 0.0)
        gluCylinder(gluNewQuadric(), 20, 0.5, 30, 10, 5)
        glPopMatrix()
        # === Red Border Around Base ===
        glPushMatrix()
        glColor3f(1, 0, 0)  # Red color
        gluCylinder(gluNewQuadric(), 60, 0, 10, 30, 30)  # Cylinder for the border
        glPopMatrix()
        # === UFO Base ===
        glPushMatrix()
        glColor3f(0.4, 0.7, 0.9)  # Light blue base
        glRotatef(-90, 1, 0, 0)  # Rotate to face the camera
        glScalef(1.8, 0.4, 1.8)
        glutSolidSphere(30, 30, 30)  # Scaled flattened sphere
        glPopMatrix()

        # === Dome on top ===
        glPushMatrix()
        glTranslatef(0, 0, 10)  # Move dome above base
        glColor3f(0.7, 0.9, 0.8)  
        glScalef(0.9, 0.9, 0.9)
        glutSolidSphere(30, 30, 30)
        glPopMatrix()
        # === Rotating Gun Towards Player (tracks player in 3D) ===
        glPushMatrix()
        # Direction vector from enemy to player
        dx = playerPos[0] - enemy[0]
        dy = playerPos[1] - enemy[1]
        dz = playerPos[2] - enemy[2]

        # Horizontal angle (x)
        x_angle = math.degrees(math.atan2(dy, dx))
        # Vertical angle (y)
        distance = math.sqrt(dx**2 + dy**2)
        y_angle = -math.degrees(math.atan2(dz, distance))

        # Translate to gun mount
        glTranslatef(0, 50, 5)

        # If player is behind, reset to default forward position
        if dy < 0:  # Behind UFO 
            target_x = 90   # Forward
            target_y = 0  # Level
        else:
            target_x = x_angle
            target_y = y_angle

        glRotatef(target_x, 0, 0, 1)
        glRotatef(target_y, 0, 1, 0)
        glRotatef(90, 0, 1, 0)

        # Draw the gun
        glColor3f(0.75, 0.75, 0.75)
        gluCylinder(gluNewQuadric(), 9, 3, 50, 10, 10)
        glPopMatrix()

        # === Glowing Lights ===
        for angle in range(0, 360, 60):
            glPushMatrix()
            rad = math.radians(angle)
            x = 40 * math.cos(rad)
            y = 40 * math.sin(rad)
            glTranslatef(x, y, 10)
            glColor3f(1.0, 1.0, 0.0) 
            glutSolidSphere(3, 10, 10)
            glPopMatrix()

        glPopMatrix()

def enemyThruster_fire():
    global fire_scale_angle
    fire_scale_angle += 0.1
    if fire_scale_angle > 2 * math.pi:
        fire_scale_angle -= 2 * math.pi

def enemySpawn():  ###   SAJID   ####
    global enemyList, spawn_positions
    while len(enemyList) < enemyMax:
        available = [pos for pos in spawn_positions if pos not in enemyList]
        if not available:
            break
        pos = random.choice(available)
        enemyList.append(pos.copy())

def enemyMovement(): ###   SAJID   ####
    global enemyList, playerPos, death, score, enemy_speed
    player_x, player_y, player_z = playerPos

    for enemy in enemyList[:]:

        if len(enemy) < 4:
            enemy.append(enemy[1])

        enemy[1] += enemy_speed  # Move up toward player

        # Remove enemy if it crosses threshold
        if enemy[1] > 2000:
            enemyList.remove(enemy)

        dx = player_x - enemy[0]
        dy = player_y - enemy[1]
        dz = player_z - enemy[2]

        distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        if distance < 100:
            death = True
            print("Player hit by enemy. Game Over!")
            enemyList.remove(enemy)
        last_shot_y = enemy[3]
        if dy > 0 and distance < 2000: # Shoot only when close enough
            if abs(enemy[1] - last_shot_y) >= 700:
                enemyBullet(enemy, playerPos)
                enemy[3] = enemy[1]

def enemyBullet(enemy, playerPos): ###   SAJID   ####
    global bullet_speed, score
    # Direction vector from enemy to player
    dx = playerPos[0] - enemy[0]
    dy = playerPos[1] - enemy[1]
    dz = playerPos[2] - enemy[2]

    length = math.sqrt(dx**2 + dy**2 + dz**2)
    if length == 0:
        return  # Avoid division by zero

    # Normalize direction
    dx /= length
    dy /= length
    dz /= length
    ebullet = {
        'x': enemy[0],
        'y': enemy[1]+50,
        'z': enemy[2]+5,
        'vx': dx * bullet_speed,
        'vy': dy * bullet_speed,
        'vz': dz * bullet_speed
    }
    enemy_bullets.append(ebullet)


def update_enemy_bullets():
    global death, playerLife
    for ebullet in enemy_bullets:
        ebullet['x'] += ebullet['vx']
        ebullet['y'] += ebullet['vy']
        ebullet['z'] += ebullet['vz']

        dx = abs(playerPos[0] - ebullet['x'])
        dy = abs(playerPos[1] - ebullet['y'])
        dz = abs(playerPos[2] - ebullet['z'])
        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        if distance < 50:  
            if playerLife != 0:
                playerLife -= 1
                enemy_bullets.remove(ebullet)
            else:
                death = True
                print("Game Over!")
    

def draw_enemy_bullets():
    global shotSize
    glColor3f(1, 0, 0)
    for ebullet in enemy_bullets:
        glPushMatrix()
        glTranslatef(ebullet['x'], ebullet['y'], ebullet['z'])
        glutSolidCube(shotSize)
        glPopMatrix()

def bullet(x,y,z): ###   RODEL   ####
    global shotSize
    glPushMatrix()
    #glScalef(1.2,1.2,1.2)
    glTranslatef(x, y, z)  
    glRotatef(90, 0, 1, 0) 
    glColor3f(0.5, 0.5, 0.5)
    glutSolidCube(shotSize)
    glPopMatrix() 

def fireBullet(): ###   RODEL Assignment 3 Mod  ####
    global liveRounds, playerPos, playerOrientation, cheat, fpsView
    
    #Bullet spawns EXACTLY at player position, slightly up at gun heighta
    bullet_x, bullet_y, bullet_z = playerPos[0], playerPos[1], playerPos[2] + 80

    bullet_angle = playerOrientation

    liveRounds.append([bullet_x, bullet_y, bullet_z, bullet_angle])

def is_colliding(x1, y1, z1, size1, x2, y2, z2, size2): #SAJID
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return distance < (size1 / 2 + size2 / 2) + 25

def bulletMovement(): #SAJID
    global liveRounds, score, enemyList, shotSpeed
    bullets_to_remove = []
    enemies_to_remove = []

    for shot in liveRounds:
        angle_rad = math.radians(shot[3] + 90)
        shot[0] += shotSpeed * math.cos(angle_rad)
        shot[1] += shotSpeed * math.sin(angle_rad)

    for enemyPos in enemyList:
        for shot in liveRounds:
            if is_colliding(shot[0], shot[1], shot[2], shotSize,
                            enemyPos[0], enemyPos[1], enemyPos[2]+80, enemy_size):
                bullets_to_remove.append(shot)
                enemies_to_remove.append(enemyPos)
                score += 1
                break

    for shot in bullets_to_remove:
        if shot in liveRounds:
            liveRounds.remove(shot)

    for enemy in enemies_to_remove:
        if enemy in enemyList:
            enemyList.remove(enemy)


def drawBlast(x, y, z):   ###   RODEL   ####
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor4f(1.0, 0.5, 0.0, 0.6)  # Orange glow with transparency
    glutSolidSphere(blast_radius, 20, 20)
    glPopMatrix()

def drawNuclearBomb(): #SAJID
    for bomb in bombList:
        glPushMatrix()
        # === Bomb Body ===
        glTranslatef(bomb[0],bomb[1],bomb[2])
        glColor3f(0.2, 0.2, 0.2)  # Dark gray
        glRotatef(-45, 0, 1, 0)   
        glutSolidCylinder(30, 80, 20, 20) 

        # === Bomb head ===
        glColor3f(1, 0, 0)  
        glTranslatef(0, 0, 80)
        gluCylinder(gluNewQuadric(), 30, 0, 30, 20, 20)

        # === Tail ===
        glTranslatef(0, 0, -80)  # back to base of bomb
        glColor3f(1, 0, 0)  
        for angle in range(0, 360, 90):
            glPushMatrix()
            glRotatef(angle, 0, 0, 1)
            glTranslatef(30, 0, 0)
            glScalef(2, 6, 20)
            glutSolidCube(2)
            glPopMatrix()

        glPopMatrix()

def spawnNuclearBombList(): #SAJID
    global bombList, spawn_positions
    while len(bombList) < bombMax:
        available = [pos for pos in spawn_positions if pos not in bombList]
        if not available:
            break
        # pos = random.choice(available)
        # bombList.append(pos.copy()) 
        rand = random.random()
        if rand < 0.05: 
            # print(rand)
            pos = random.choice(available)  
            bombList.append(pos.copy())

def nuclearBombMovement(): #SAJID
    global bombList, playerPos, score, enemyList, enemy_bullets, nuke, blast_triggered, blast_expand, nspeed

    for bomb in bombList:
        bomb[1] += nspeed
        if bomb[1] > 2000:
            bombList.remove(bomb)

    for bomb in bombList:
        dx = playerPos[0] - bomb[0]
        dy = playerPos[1] - bomb[1]
        dz = playerPos[2] - bomb[2]
        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        if distance < 100:
            nuke = True
            blast_triggered = True
            blast_expand = True
            score += len(enemyList)
            enemyList.clear()
            bombList.clear()
            asteroidList.clear()
            enemy_bullets.clear()

            print("KABOOM")
            print("All aliens and asteroids destroyed!")

def difficulty_inc(): #SAJID
    global score, Aspeed, enemy_speed, last_speed_increment, bullet_speed, shotSpeed, nspeed
    if score >= last_speed_increment + 10:
        Aspeed += 0.5 # asteroid speed
        shotSpeed += 0.5
        bullet_speed += 0.5
        enemy_speed += 0.5
        nspeed += 0.8 # nuke speed
        last_speed_increment = score



### Start of Ismail's function ###

def update_stars():
    global stars, score
    for star in stars:
        star[1] += 2
        if star[1] > 2000:  # If star goes beyond screen
            star[1] = -2000  # Reset to top
            star[0] = random.uniform(-2000, 2000)  # Random x position
            star[2] = random.uniform(-2000, 2000)  # Random z position

def draw_stars():
    glPushMatrix()
    try:
        for star in stars:
            glPushMatrix()
            glTranslatef(star[0], star[1], star[2])
            glColor3f(1.0, 1.0, 1.0)
            glutSolidSphere(0.5, 8, 8)
            glPopMatrix()
    finally:
        glPopMatrix()

def update_space_elements():
    global sun_positions, black_hole_pos, shooting_stars, saturn_ring_angle, comets, extra_black_holes

    # Update ring rotation angle
    saturn_ring_angle = (saturn_ring_angle + 0.5) % 360

    # Move suns backwards and remove when too far
    for sun in sun_positions[:]:
        sun[1] += 0.8
        if sun[1] > 2000:
            sun_positions.remove(sun)
            # Randomly choose which edge to spawn from
            edge = random.choice(['top_left', 'top_right', 'top', 'bottom'])
            if edge == 'top_left':
                x = random.uniform(-2000, -1500)
                y = -2000
                z = random.uniform(-2000, 2000)
            elif edge == 'top_right':
                x = random.uniform(1500, 2000)
                y = -2000
                z = random.uniform(-2000, 2000)
            elif edge == 'top':
                x = random.uniform(-1500, 1500)
                y = -2000
                z = random.uniform(1500, 2000)
            else:  # bottom
                x = random.uniform(-1500, 1500)
                y = -2000
                z = random.uniform(-2000, -1500)
            size = random.uniform(8, 12)
            sun_positions.append([x, y, z, size])

    # Move extra black holes backwards like suns
    for bh in extra_black_holes[:]:
        bh[1] += 0.8
        if bh[1] > 2000:
            extra_black_holes.remove(bh)
            # Randomly choose which edge to spawn from
            edge = random.choice(['top_left', 'top_right', 'top', 'bottom'])
            if edge == 'top_left':
                x = random.uniform(-2000, -1500)
                y = -2000
                z = random.uniform(-2000, 2000)
            elif edge == 'top_right':
                x = random.uniform(1500, 2000)
                y = -2000
                z = random.uniform(-2000, 2000)
            elif edge == 'top':
                x = random.uniform(-1500, 1500)
                y = -2000
                z = random.uniform(1500, 2000)
            else:  # bottom
                x = random.uniform(-1500, 1500)
                y = -2000
                z = random.uniform(-2000, -1500)
            size = random.uniform(12, 18)
            extra_black_holes.append([x, y, z, size])

    # Update shooting stars
    for star in shooting_stars[:]:
        star[0] += star[3]  # Move x
        star[1] += star[4]  # Move y
        star[2] += star[5]  # Move z
        star[6] -= 1  # Decrease trail length

        # Remove shooting star if trail is gone
        if star[6] <= 0:
            shooting_stars.remove(star)

    # Update comets
    for comet in comets[:]:
        comet[0] += comet[3]  # Move x
        comet[1] += comet[4]  # Move y
        comet[2] += comet[5]  # Move z
        comet[7] -= 0.5  # Decrease trail length slowly

        # Remove comet if trail is gone or out of bounds
        if comet[7] <= 0 or abs(comet[0]) > 2000 or abs(comet[1]) > 2000 or abs(comet[2]) > 2000:
            comets.remove(comet)
            # Add new comet
            x = random.uniform(-1800, 1800)
            y = random.uniform(-1800, 1800)
            z = random.uniform(-1800, 1800)
            speed_x = random.uniform(-3, 3)
            speed_y = random.uniform(-3, 3)
            speed_z = random.uniform(-3, 3)
            size = random.uniform(3, 5)
            comets.append([x, y, z, speed_x, speed_y, speed_z, size, 100])

    # Randomly spawn new shooting stars more frequently
    if random.random() < 0.03:  # Increased from 0.01 to 0.03
        x = random.uniform(-2000, 2000)
        y = random.uniform(-2000, 2000)
        z = random.uniform(-2000, 2000)
        speed_x = random.uniform(-4, 4)  # Increased speed range
        speed_y = random.uniform(-4, 4)
        speed_z = random.uniform(-4, 4)
        trail_length = 30  # Longer trail
        shooting_stars.append([x, y, z, speed_x, speed_y, speed_z, trail_length])

    # Optionally animate center black holes (slow orbit)
    for i, bh in enumerate(center_black_holes):
        angle = (globals().get(f'center_bh_angle_{i}', i * (2 * math.pi / 3)) + 0.003) % (2 * math.pi)
        r = 120
        bh[0] = r * math.cos(angle)
        bh[1] = r * math.sin(angle)
        globals()[f'center_bh_angle_{i}'] = angle
    # Optionally animate center suns (slow orbit)
    for i, sun in enumerate(center_suns):
        angle = (globals().get(f'center_sun_angle_{i}', i * (2 * math.pi / 2) + math.pi/4) + 0.002) % (2 * math.pi)
        r = 60
        sun[0] = r * math.cos(angle)
        sun[1] = r * math.sin(angle)
        globals()[f'center_sun_angle_{i}'] = angle

def draw_sun():
    glPushMatrix()
    try:
        for sun in sun_positions:
            glPushMatrix()
            glTranslatef(sun[0], sun[1], sun[2])

            # Core - Brighter and more golden
            glColor3f(1.0, 0.95, 0.3)  # Bright golden yellow
            glutSolidSphere(sun[3], 24, 24)  # More detailed sphere

            # Inner glow - More intense
            glColor4f(1.0, 0.8, 0.2, 0.5)  # Golden glow
            glutSolidSphere(sun[3] + 3, 24, 24)

            # Outer glow - Softer
            glColor4f(1.0, 0.6, 0.1, 0.3)  # Orange glow
            glutSolidSphere(sun[3] + 6, 24, 24)

            # Saturn-like rings with multiple layers
            glPushMatrix()
            glRotatef(saturn_ring_angle, 0, 1, 0)

            # Inner ring - Bright and thin
            glColor4f(1.0, 0.9, 0.4, 0.7)  # Bright golden
            glutSolidTorus(1.5, sun[3] + 4, 32, 32)

            # Middle ring - Gradient effect
            glColor4f(1.0, 0.7, 0.2, 0.5)  # Orange-gold
            glutSolidTorus(2, sun[3] + 8, 32, 32)

            # Outer ring - Faint and wide
            glColor4f(1.0, 0.5, 0.1, 0.3)  # Deep orange
            glutSolidTorus(2.5, sun[3] + 12, 32, 32)
            glPopMatrix()

            # Orbiting particles - More numerous and smaller
            glColor4f(1.0, 0.8, 0.3, 0.4)  # Golden particles
            for i in range(16):  # More particles
                glPushMatrix()
                glRotatef(22.5 * i, 0, 1, 0)  # Evenly spaced
                glTranslatef(0, 0, sun[3] + 15)
                glutSolidSphere(2, 8, 8)  # Smaller particles
                glPopMatrix()
            glPopMatrix()
    finally:
        glPopMatrix()

def draw_black_hole():
    glPushMatrix()
    try:
        glTranslatef(black_hole_pos[0], black_hole_pos[1], black_hole_pos[2])

        # Enable blending for transparency
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Event horizon (black core)
        glColor3f(0.0, 0.0, 0.0)
        glutSolidSphere(15, 32, 32)

        # Gravitational lensing effect (dark ring)
        glColor4f(0.1, 0.1, 0.1, 0.8)
        glutSolidTorus(2, 18, 32, 32)

        # Inner accretion disk (bright and intense)
        glColor4f(0.8, 0.4, 0.1, 0.7)  # Orange-red
        glutSolidTorus(3, 25, 32, 32)

        # Middle accretion disk (glowing)
        glColor4f(0.9, 0.6, 0.2, 0.5)  # Bright orange
        glutSolidTorus(4, 35, 32, 32)

        # Outer accretion disk (faint)
        glColor4f(0.7, 0.3, 0.1, 0.3)  # Deep orange
        glutSolidTorus(5, 45, 32, 32)

        # Gravitational lensing particles
        for i in range(24):
            glPushMatrix()
            angle = (i * 15) % 360
            glRotatef(angle, 0, 1, 0)
            glTranslatef(0, 0, 30)
            # Inner particles
            glColor4f(0.9, 0.5, 0.1, 0.6)
            glutSolidSphere(1.5, 8, 8)
            # Outer particles
            glTranslatef(0, 0, 15)
            glColor4f(0.7, 0.3, 0.1, 0.4)
            glutSolidSphere(1, 8, 8)
            glPopMatrix()

        glDisable(GL_BLEND)
    finally:
        glPopMatrix()

def draw_shooting_stars():
    # Draw shooting stars
    for star in shooting_stars:
        glPushMatrix()
        try:
            glTranslatef(star[0], star[1], star[2])
            # Star
            glColor3f(1.0, 1.0, 1.0)
            glutSolidSphere(2, 8, 8)
            # Trail
            glBegin(GL_LINES)
            glColor4f(1.0, 1.0, 1.0, 0.8)
            glVertex3f(0, 0, 0)
            glColor4f(1.0, 1.0, 1.0, 0.0)
            glVertex3f(-star[3] * 30, -star[4] * 30, -star[5] * 30)
            glEnd()
        finally:
            glPopMatrix()

    # Draw comets
    for comet in comets:
        glPushMatrix()
        try:
            glTranslatef(comet[0], comet[1], comet[2])

            # Comet head
            glColor3f(1.0, 0.9, 0.7)  # Bright white-yellow
            glutSolidSphere(comet[6], 12, 12)

            # Comet glow
            glColor4f(1.0, 0.8, 0.4, 0.3)
            glutSolidSphere(comet[6] + 2, 12, 12)

            # Comet trail
            glBegin(GL_LINES)
            for i in range(20):  # Multiple trail lines
                alpha = 1.0 - (i / 20.0)
                glColor4f(1.0, 0.8, 0.4, alpha * 0.5)
                glVertex3f(0, 0, 0)
                glColor4f(1.0, 0.4, 0.1, 0.0)
                glVertex3f(-comet[3] * comet[7] * (i/20.0),
                           -comet[4] * comet[7] * (i/20.0),
                           -comet[5] * comet[7] * (i/20.0))
            glEnd()
        finally:
            glPopMatrix()

def draw_extra_black_holes():
    for bh in extra_black_holes:
        glPushMatrix()
        glTranslatef(bh[0], bh[1], bh[2])

        # Enable blending for transparency
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Event horizon
        glColor3f(0.0, 0.0, 0.0)
        glutSolidSphere(bh[3], 32, 32)

        # Gravitational lensing effect
        glColor4f(0.1, 0.1, 0.1, 0.8)
        glutSolidTorus(2, bh[3] + 3, 32, 32)

        # Accretion disk layers
        glColor4f(0.8, 0.4, 0.1, 0.7)
        glutSolidTorus(3, bh[3] + 8, 32, 32)

        glColor4f(0.9, 0.6, 0.2, 0.5)
        glutSolidTorus(4, bh[3] + 15, 32, 32)

        glColor4f(0.7, 0.3, 0.1, 0.3)
        glutSolidTorus(5, bh[3] + 25, 32, 32)

        # Particles
        for i in range(16):
            glPushMatrix()
            angle = (i * 22.5) % 360
            glRotatef(angle, 0, 1, 0)
            glTranslatef(0, 0, bh[3] + 20)
            glColor4f(0.9, 0.5, 0.1, 0.6)
            glutSolidSphere(1.5, 8, 8)
            glPopMatrix()

        glDisable(GL_BLEND)
        glPopMatrix()

def draw_saturn_planets():
    for planet in saturn_planets:
        glPushMatrix()
        glTranslatef(planet[0], planet[1], planet[2])
        # Planet body
        glColor3f(*planet[3])
        glutSolidSphere(planet[4], 16, 16)
        # Ring
        glRotatef(saturn_ring_angle, 0, 1, 0)
        glColor4f(0.8, 0.8, 0.6, 0.5)
        glutSolidTorus(2, planet[4]+6, 30, 40)
        glPopMatrix()

def draw_center_black_holes():
    for bh in center_black_holes:
        glPushMatrix()
        glTranslatef(bh[0], bh[1], bh[2])
        # Core
        glColor3f(1, 1, 1)
        glutSolidSphere(bh[3], 20, 20)
        # Accretion disk
        glColor4f(0.5, 0.0, 0.5, 0.3)
        glutSolidSphere(bh[3]+6, 20, 20)
        # Particles
        glColor4f(0.3, 0.0, 0.3, 0.15)
        for i in range(10):
            glPushMatrix()
            glRotatef(36 * i, 0, 1, 0)
            glTranslatef(0, 0, bh[3]+12)
            glutSolidSphere(2, 8, 8)
            glPopMatrix()
        glPopMatrix()

def draw_center_suns():
    for sun in center_suns:
        glPushMatrix()
        glTranslatef(sun[0], sun[1], sun[2])
        # Core
        glColor3f(1.0, 0.85, 0.1)
        glutSolidSphere(sun[3], 20, 20)
        # Glow
        glColor4f(1.0, 0.7, 0.1, 0.3)
        glutSolidSphere(sun[3]+5, 20, 20)
        # Rays
        glColor4f(1.0, 0.5, 0.1, 0.2)
        for i in range(8):
            glPushMatrix()
            glRotatef(45 * i, 0, 1, 0)
            glTranslatef(0, 0, sun[3]+10)
            glutSolidSphere(3, 8, 8)
            glPopMatrix()
        glPopMatrix()

### End of Ismail' functions ###

def showScreen(): ###   RODEL Assignment 3 Mod  ####
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    originX, originY, originZ = 1000,000,500
    # Clear color and depth buffers
    global mouse_x, mouse_y, mainMenu
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1280, 720)  # Set viewport size
    glTranslatef(originX, originY, originZ)  
    setupCamera()  # Configure camera perspective
    gl_x, gl_y = screen_to_opengl(mouse_x, mouse_y) ###   RODEL   ####
    draw_crosshair(gl_x, gl_y)
    #asteroids()
    
    # Draw space elements (Ismail's BG)
    draw_stars()
    draw_center_black_holes()
    draw_center_suns()
    draw_sun()
    draw_black_hole()
    draw_extra_black_holes()
    draw_saturn_planets()
    draw_shooting_stars()
    if not mainMenu:
        drawAsteroids() ###   RODEL   ####

    if not death and not mainMenu:
        drawEnemies()  
        drawNuclearBomb()
        draw_enemy_bullets()

    if blast_triggered or (nuke and blast_triggered) and not mainMenu:
        drawBlast(playerPos[0], playerPos[1], playerPos[2])

# Game info text at a fixed screen position
    global paused
    if mainMenu: #SAJID
        draw_text(400, 500, f"Welcome to Space Wars 2169!")
        draw_text(395, 470, f"Press 'space' to save the galaxy!")
        draw_text(360, 100, f"A Galaxy War Tale By Rodel, Sajid and Ismail")

    elif death:
        draw_text(400, 700, "Game Over! Press R to reset")
    elif paused:
        draw_text(460, 670, "SPACE WARS 2169")  
        draw_text(400, 700, "Game Paused! Press 'Space' to resume")
    else:
        draw_text(10, 770, f"Press 'Space' to pause")
        draw_text(455, 740, f"KILLS : {score}")
        health = str(playerLife*' * ')
        draw_text(400, 700, f"BULLET SHIELD HEALTH")
        draw_text(450, 670, f"{health}")
        #draw_text(10, 710, f"Player Bullets Missed: {bulletMissed}")
        #draw_text(10, 680, f"x axis red, y axis green, z axis blue")
    if nuke:
        draw_text(400, 700, "Nuclear Bomb Activated! All projectiles destroyed!")
        
    #draw_axes()  ###   RODEL   ####
    if not death: ###   RODEL   ####
        drawSpaceship() ###   RODEL   ####
        for shot in liveRounds: ###   RODEL   ####
            bullet(shot[0], shot[1], shot[2]) ###   RODEL   ####
    # Swap buffers for smooth rendering (double buffering)
    glutSwapBuffers()


# Main function to set up OpenGL window and loop
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(W_Width, W_Height)  # Window size
    glutInitWindowPosition(0, 0)  # Window position
    glutCreateWindow(b"Space Wars 2169")  
    #enemySpawn()
    glutDisplayFunc(showScreen)  # Register display function
    glutKeyboardFunc(keyboardListener)  # Register keyboard listener
    glutSpecialFunc(specialKeyListener)
    glutPassiveMotionFunc(mouseMotion)  # Register mouse motion listener
    glutSetCursor(GLUT_CURSOR_NONE) ## Hides the cursor, NOT ALLOWED for submission maybe
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  # Register the idle function to move the bullet automatically

    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()