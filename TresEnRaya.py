#!/usr/bin/env python
# coding: utf-8

# In[3]:


player1_name = input("Introduce el nombre del jugador 1: ")
player2_name = input("Introduce el nombre del jugador 2: ")

character = input("Con que icono quieres jugar " + player1_name + "? x ó o ")

if character == "x":
    player1 = "x"
    player2 = "o"
elif character == "o":
    player2 = "o"
    player1 = "x"
else:
    print("Icono Invalido")

a1 = " "; a2 = " "; a3 = " "
b1 = " "; b2 = " "; b3 = " "
c1 = " "; c2 = " "; c3 = " "

turnosp1 = 5
turnosp2 = 5

print("_",a1,"_ | _",a2,"_ | _",a3,"_\n_",b1,"_ | _",b2,"_ | _",b3,"_\n_",c1,"_ | _",c2,"_ | _",c3,"_\n")

while turnosp1 > 0 and turnosp2 > 0:
    selection_p1 = input(player1_name + ", donde quiere poner su ficha? ")
    if selection_p1 == "a1":
        a1 = player1
    elif selection_p1 == "a2":
        a2 = player1
    elif selection_p1 == "a3":
        a3 = player1
    elif selection_p1 == "b1":
        b1 = player1
    elif selection_p1 == "b2":
        b2 = player1
    elif selection_p1 == "b3":
        b3 = player1
    elif selection_p1 == "c1":
        c1 = player1
    elif selection_p1 == "c2":
        c2 = player1
    elif selection_p1 == "c3":
        c3 = player1
    else:
        print("La casilla es invalida.")
    turnosp1 -= 1
    print("_",a1,"_ | _",a2,"_ | _",a3,"_\n_",b1,"_ | _",b2,"_ | _",b3,"_\n_",c1,"_ | _",c2,"_ | _",c3,"_\n")
    
    if a1 == "x" and a2 == "x" and a3 == "x":
        print(player1_name + " gana el juego")
        break 
    elif b1 == "x" and b2 == "x" and b3 == "x":
        print(player1_name + " gana el juego")
        break 
    elif c1 == "x" and c2 == "x" and c3 == "x":
        print(player1_name + " gana el juego")
        break 
    elif a1 == "x" and b1 == "x" and c1 == "x":
        print(player1_name + " gana el juego")
        break 
    elif a2 == "x" and b2 == "x" and c2 == "x":
        print(player1_name + " gana el juego")
        break 
    elif a3 == "x" and b3 == "x" and c3 == "x":
        print(player1_name + " gana el juego")
        break 
    elif a1 == "x" and b2 == "x" and c1 == "x":
        print(player1_name + " gana el juego")
        break 
    elif a3 == "x" and b2 == "x" and c1 == "x":
        print(player1_name + " gana el juego")
        break 
    
    selection_p2 = input(player2_name + ", donde quiere poner su ficha? ")
    if selection_p2 == "a1":
        a1 = player2
    elif selection_p2 == "a2":
        a2 = player2
    elif selection_p2 == "a3":
        a3 = player2
    elif selection_p2 == "b1":
        b1 = player2
    elif selection_p2 == "b2":
        b2 = player2
    elif selection_p2 == "b3":
        b3 = player2
    elif selection_p2 == "c1":
        c1 = player2
    elif selection_p2 == "c2":
        c2 = player2
    elif selection_p2 == "c3":
        c3 = player2
    else:
        print("La casilla es invalida.")
    turnosp2 -= 1
    print("_",a1,"_ | _",a2,"_ | _",a3,"_\n_",b1,"_ | _",b2,"_ | _",b3,"_\n_",c1,"_ | _",c2,"_ | _",c3,"_\n")
    
    if a1 == "o" and a2 == "o" and a3 == "o":
        print(player2_name + " gana el juego")
        break 
    elif b1 == "o" and b2 == "o" and b3 == "o":
        print(player2_name + " gana el juego")
        break 
    elif c1 == "o" and c2 == "o" and c3 == "o":
        print(player2_name + " gana el juego")
        break 
    elif a1 == "o" and b1 == "o" and c1 == "o":
        print(player2_name + " gana el juego")
        break 
    elif a2 == "o" and b2 == "o" and c2 == "o":
        print(player2_name + " gana el juego")
        break 
    elif a3 == "o" and b3 == "o" and c3 == "o":
        print(player2_name + " gana el juego")
        break 
    elif a1 == "o" and b2 == "o" and c1 == "o":
        print(player2_name + " gana el juego")
        break 
    elif a3 == "o" and b2 == "o" and c1 == "o":
        print(player2_name + " gana el juego")
        break 


# In[ ]:


print("x")


# In[ ]:




