import random

from turtle import *

while True :
    fd(10)
    nb = random.randint(0,2)
    if nb==0:
        lt(90)
    if nb==1:
        rt(90)