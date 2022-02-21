# %% [markdown]
# Ejercicio - Escribir declaraciones if, else, y elif:

# %% [markdown]
# Ejercicio 1:

# %%
v = int(input("Primer número: "))
c = 49
if c >= v:
    print ('ADVERTENCIA, SE ACERCA UN ESTEROIDE A LA TIERA..')
else: 
    print ('Todo esta normal')

# %% [markdown]
# Ejercicio 2:

# %%
visible = 20
prueba = 19
if prueba > visible:
    print ('Se acerca un asterioide a la tierra, buscalo ahora en el cielo...')
elif prueba == visible:
      print ('Se acerca un asterioide a la tierra, buscalo ahora en el cielo...')

else:
    print ('Hay un asteriode que que dirige a la tierra con una velocidad de ' + str(prueba) + 'km/s' ) 

# %% [markdown]
# Ejercicio: Uso de operadores and y or
# 

# %%
# Velocidades
adv = 25  #Advertencia 
luz = 20  #Luz

# Tamaños
t1 = 25   # Información
t2 = 1000  #Advertencia 


Dimension = 50
#int(input("Dimensión del asteride: "))
Velocidad = 30
#int(input("Velocidad del asteride: "))

if Velocidad >= adv :
    print ('ADVERTENCIA, SE ACERCA UN ESTEROIDE A LA TIERA..')
elif Velocidad >= luz: 
    print ('Se acerca un asterioide a la tierra, buscalo ahora en el cielo...')
elif Dimension > t1 or Dimension <= t2 :
      print (' ADVERTENCIA,Un asterioide golperá a la tierra y podría causar mucho daño. ')
else:
      ('Un asteroide entrara a la tierra pero se quemará a medida que entre a la atmoafera..')

# %%
a = 160
b = 25
c = 27
if a > b:
    if b > c:
        print ("a es mayor que b y b es mayor que c")
    else: 
        print ("a es mayor que b y menor que c")
elif a == b:
    print ("a es igual que b")
else:
    print ("a es menor que b")


