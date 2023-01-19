import pgzrun
from pgzhelper import *

WIDTH = 560
HEIGHT = 400


encender_sonidos_de_animales = False

do4 = Actor("do-fa")
do4.pos = 20, 50

dosus4 = Actor("sus")
dosus4.pos = 40, 30
re4 = Actor("re-sol-la")
re4.pos = 60, 50
resus4 = Actor("sus")
resus4.pos = 80, 30
mi4 = Actor("mi-si")
mi4.pos = 100, 50
fa4 = Actor("do-fa")
fa4.pos = 140, 50
fasus4 = Actor("sus")
fasus4.pos = 160, 30
sol4 = Actor("re-sol-la")
sol4.pos = 180, 50
solsus4 = Actor("sus")
solsus4.pos = 200, 30
la4 = Actor("re-sol-la")
la4.pos = 220, 50
lasus4 = Actor("sus")
lasus4.pos =240, 30
si4 = Actor("mi-si")
si4.pos = 260, 50
#quinta octava
do5 = Actor("do-fa")
do5.pos = 300, 50

dosus5 = Actor("sus")
dosus5.pos = 320, 30
re5 = Actor("re-sol-la")
re5.pos = 340, 50
resus5 = Actor("sus")
resus5.pos = 360, 30
mi5 = Actor("mi-si")
mi5.pos = 380, 50
fa5 = Actor("do-fa")
fa5.pos = 420, 50
fasus5 = Actor("sus")
fasus5.pos = 440, 30
sol5 = Actor("re-sol-la")
sol5.pos = 460, 50
solsus5 = Actor("sus")
solsus5.pos = 480, 30
la5 = Actor("re-sol-la")
la5.pos = 500, 50
lasus5 = Actor("sus")
lasus5.pos =520, 30
si5 = Actor("mi-si")
si5.pos = 540, 50
botondeanimal = Actor("botondeanimal")
botondeanimal.pos = 280, 250
botondeanimal.scale = 3.0


def dibujar_teclas():
    global do4, dosus4, re4, resus4, mi4, fa4, fasus4, sol4, solsus4, la4, lasus4, si4
    global do5, dosus5, re5, resus5, mi5, fa5, fasus5, sol5, solsus5, la5, lasus5, si5
    global botondeanimal
    botondeanimal.draw()
    do4.draw()
    dosus4.draw()
    re4.draw()
    resus4.draw()
    mi4.draw()
    fa4.draw()
    fasus4.draw()
    sol4.draw()
    solsus4.draw()
    la4.draw()
    lasus4.draw()
    si4.draw()

    do5.draw()
    dosus5.draw()
    re5.draw()
    resus5.draw()
    mi5.draw()
    fa5.draw()
    fasus5.draw()
    sol5.draw()
    solsus5.draw()
    la5.draw()
    lasus5.draw()
    si5.draw()


def draw():
    dibujar_teclas()
    
"""
Do - C
Re - D
Mi - E
Fa - F
Sol - G
La - A
Si - B
"""
def update():
    global encender_sonidos_de_animales
    if encender_sonidos_de_animales == True:

        if keyboard.q:
            music.play_once("caballo")
        if keyboard.w:
            music.play_once("gato")
        
        if keyboard.e:
            music.play_once("leon")
        if keyboard.r:
            music.play_once("gallo")
        if keyboard.t:
            music.play_once("perro")


    else:
        if keyboard.q:
            tone.play("C4", 0.2)
        if keyboard.k_2:
            tone.play("C#4", 0.2)
        if keyboard.w:
            tone.play("D4", 0.2)
        # D#4
        if keyboard.k_3:
            tone.play("D#4", 0.2)
        if keyboard.e:
            tone.play("E4", 0.2)
        if keyboard.r:
            tone.play("F4", 0.2)
        # F#4
        if keyboard.k_5:
            tone.play("F#4", 0.2)
        if keyboard.t:
            tone.play("G4", 0.2)
        # G#4
        if keyboard.k_6:
            tone.play("G#4", 0.2)
        if keyboard.y:
            tone.play("A4", 0.2)
        # A#4
        if keyboard.k_7:
            tone.play("A#4", 0.2)
        if keyboard.u:
            tone.play("B4", 0.2)
        if keyboard.z:
            tone.play("C5", 0.2)
        if keyboard.x:
            tone.play("D5", 0.2)
        if keyboard.c:
            tone.play("E5", 0.2)
        if keyboard.v:
            tone.play("F5", 0.2)
        if keyboard.b:
            tone.play("G5", 0.2)
        if keyboard.n:
            tone.play("A#5", 0.2)
        if keyboard.m:
            tone.play("B#5", 0.2) 


def on_mouse_down(pos):
    global encender_sonidos_de_animales
    if do4.collidepoint(pos):
        tone.play("C4", 0.2)
    if re4.collidepoint(pos):
        tone.play("D4", 0.2)   
    if botondeanimal.collidepoint(pos):
        if encender_sonidos_de_animales == False:
            encender_sonidos_de_animales = True
        elif encender_sonidos_de_animales == True:
            encender_sonidos_de_animales = False
# HACER UN PIANO QUE VAYA DESDE C1 A C6
#pgzrun.go()
