import tkinter as tk
from tkinter import messagebox
import pygame
import random
import math
from perlin_noise import PerlinNoise
pygame.init()
win=pygame.display.set_mode((1000,700))
run=True
score=0
v=5
dv=0
g=0.1
f=0
nf=g-f
x=1000
y=1000
r=[]
c=0
my_font=pygame.font.SysFont('Arial',30)
pbird = pygame.image.load('bird.png')
bird=pygame.transform.scale(pbird,(60,60))
for i in range(500):
    r+=[random.random()]
s=350+dv*c+0.5*(g-f)*c**2
while run:
    c+=1
    pygame.time.delay(100)
    win.fill((0,0,255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_h]: 
        f=0.2
    dv=dv+(g-f)*c
    s+=dv*c+0.5*(g-f)*c**2
    win.blit(bird,(500,s))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    noise = PerlinNoise(octaves=1,seed=100)
    for i in range(100):
        pygame.draw.rect(win,(0,255,0),(x+i*200,0,125,200+200*r[i-1]))
        pygame.draw.rect(win,(255,0,0),(x+i*200,0,5,5))
        pygame.draw.rect(win,(0,255,0),(x+i*200,700-200*r[-i],125,200+200*r[-i]))
        pygame.draw.rect(win,(255,0,0),(x+i*200,700-200*r[-i],5,5))
        pygame.draw.rect(win,(255,0,0),(0,0,5,5))
        if (abs(x+i*200-500)<=50 and s<=200+200*r[i-1]) or (abs(x+i*200-500)<=50 and 700-200*r[-i]-s<=60) :
            run=False
        score+=0.001 
        
    x-=v
    if int(dv)==0:
        c=0
    if int(dv/1000)==0:
        f=0
    if s>700:
        run=False
    if s<0:
        run=False
    text2=my_font.render(str(int(score)), False, (255,255,255))
    win.blit(text2,(0,50))
    pygame.display.update()

subject = "Game Over"
content = ("Score:",int(score))
root = tk.Tk()
root.attributes("-topmost", True)
root.withdraw()
messagebox.showinfo(subject, content)
root.destroy()
