from sympy import * #libreria que convierte strings en expresiones matematicas

x = symbols('x') #declarar la variable que se usara

funcion_string = input("Indique la funcion a evaluar\n[arctan = atan(), e = exp(), potencia = **, logaritmo natural = ln()]\n")
try:
    funcion_expresion = sympify(funcion_string) #conversion de string a expresion simbolica
except Exception as R:
    print(f"Error al interpretar la función: {R}")
    exit()

a = float(input("\nIndique el intervalo (a,b)\na = "))
b = float(input("b = "))
objetivo = float(input("Indique el porcentaje de error deseado (ej. escriba 3 para indicar un error de 0.03))\n"))

if a > b:
    a, b = b, a #si el usuario los puso al reves se acomodan
elif a == b:
    print("Indique 2 numeros diferentes para el intervalo")
    exit()

#validar la funcion
f = lambdify(x, funcion_expresion, modules=['math']) #convertir a función ejecutable por Python

try:
    fa = f(a) #evaluar la funcion en los extremo
    fb = f(b)
except Exception as t:
    print(f"Error al evaluar la función: {t}")
    exit()

if fa * fb > 0: #validar si hay cambio de signo
    print("La función no cambia de signo en el intervalo. No se puede aplicar bisección.")
    exit()

i = 0
i_max = 50 #un limite seguro para evitar bucles infinitos
error = 100
m = a #inicializamos m con un valor del intervalo

print(f"\nResultados para f(x) = {funcion_expresion}:")
print(f"{'Iteración':<12} | {'Raíz (m)':<12} | {'Error (%)':<12}")
print("-" * 45)

while error > objetivo and i < i_max:
    m_anterior = m
    m = (a + b) / 2 # calcular punto medio
    fm = f(m)
    
    i += 1
    
    #calculo del error relativo porcentual (mas preciso que el absoluto)
    if m != 0:
        error = abs((m - m_anterior) / m) * 100
    
    print(f"{i:<12} | {m:<12.6f} | {error:<12.6f}%")

    if fm == 0: #raiz exacta
        break
        
    if fa * fm < 0: #decidir qué lado del intervalo descartar
        b = m
        fb = fm
    else:
        a = m
        fa = fm

print("-" * 45)
print(f"Resultado final: {m}")