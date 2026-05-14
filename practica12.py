from fibonacci_des import fibonacci, fibonacci_des, fibonacci_asc

from time import time
tiempo_asc = []
tiempo_des = [] 
tiempo_recursivo = []

for i in range(1, 41):
    t0 = time()
    fibonacci_des(i)
    tiempo_des.append(round(time()-t0, 6))

    t0 = time()
    fibonacci_asc(i)
    tiempo_asc.append(round(time()-t0, 6))

datos = []
for i range(1, 41):
    datos.append(i)

fig, ax = subplots()
ax.plot(datos, tiempo_asc, label="fib_des", market="*", color="r")
ax.plot(datos, tiempo_asc, label="fib_des", market="o", color="r")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc=2)

pit.title("Tiempos de ejecucion [s] fib_des vs fib_asc")
pit.show()