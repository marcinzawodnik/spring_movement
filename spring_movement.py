
from vpython import *

#wychylenie początkowe:
x1 = 5  
#prędkość początkowa:      
v0 = 0.5 
#współczynnik sprężystości:     
k  = 0.1 
#współczynnik tłumienia:      
c  = 0.001      

print('Podaj wychylenie początkowe: ')
try:
    x1 = float(input())
except: 
    print("Nie wprowadzono liczby. Przyjęto wartoś domyślną.")

print('Podaj prędkość początkową: ')
try:
    v0 = float(input())
except: 
    print("Nie wprowadzono liczby. Przyjęto wartoś domyślną.")

print('Podaj współczynnik sprężystości: ')
try:
    k = float(input())
except: 
    print("Nie wprowadzono liczby. Przyjęto wartoś domyślną.")

print('Podaj współczynnik tłumienia: ')
try:
    c = float(input())
except: 
    print("Nie wprowadzono liczby. Przyjęto wartoś domyślną.")

if (k>0):
    c = c*(-1)
m  = 2
t  = 0
delta_t = 0.1

scena = canvas(title='Ruch kulki na sprężynie', width=600, height=450, center=vector(8,0,0), background=color.cyan) 
sciana=box(pos=vector(0,0,0),size=vector(0.1,6,6),color=color.orange)
kulka = sphere(pos=vector(x1,-2,0), v=vector(v0,0,0), radius = 0.5, color=color.red)
sprezyna=helix(pos=vector(0,-2,0), axis=kulka.pos -vector(0,-2,0), radius=0.3, thickness=0.05, coils=25, color=color.black)
pozycja_rownowagi=vector(10,-2,0)

while (True):
  rate(60)
  wychylenie = pozycja_rownowagi - kulka.pos
  acc=(wychylenie)*(k/m) + (kulka.v * c/m)
  k1 = acc * delta_t
  k2 = (acc + 0.5 * k1)* delta_t
  k3 = (acc + 0.5 * k2)* delta_t
  k4 = (acc + 0.5 * k3)* delta_t
  kulka.v=kulka.v + acc * delta_t + (k1 + k2 + k3 + k4)/6

  k5 = kulka.v * delta_t
  k6 = (kulka.v + 0.5 * k5) * delta_t
  k7 = (kulka.v + 0.5 * k6) * delta_t
  k8 = (kulka.v + 0.5 * k7) * delta_t
  kulka.pos=kulka.pos+kulka.v * delta_t + (k5 + k6 + k7 + k8)/6
  sprezyna.axis=kulka.pos-sprezyna.pos
  t=t+delta_t