import random
print('Hola jugador, bienvenido al juego...')

palabras = ["mate", "asado", "choclo", "choripán", "milanga", "factura", "bocajuniors", "riverplate", "guiso", "bondiola", "picada", "parrilla", "morcilla", "torta", "taza", "termo", "remera", "zapatillas", "ojotas", "heladera", "ventilador", "fernet", "galletitas", "cuaderno", "mochila", "bondi", "talleres", "gobierno", "peaje", "cana", "chicle", "caramelo", "perro", "gato", "pibe", "reposera", "reloj", "ascenso", "messi", "cerati", "domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "pintura", "pincel", "pared", "reboque", "departamento", "planta", "verde", "azul", "rojo", "amarillo", "blanco", "negro", "madera", "hierro", "plástico", "vidrio", "papel", "lapicera", "lápiz", "goma", "cuaderno", "libro", "biblioteca", "lectura", "escritura", "oración", "párrafo", "palabra", "letra", "sílaba", "acento", "arcoiris", "liquidpaper", "peron", "groncho", "sinónimo", "antónimo", "sierras", "definición", "diccionario", "enciclopedia", "computadora", "internet", "redes", "correo", "mensaje", "teclado", "mouse", "pantalla", "archivo", "carpeta", "documento", "imprimir", "escribir", "leer", "estudiar", "aprender", "enseñar", "clase", "aireacondicionado", "colegio", "universidad", "profesor", "alumno", "aula", "tiza", "pizarrón", "borrador", "recreo", "patio", "merienda", "desayuno", "almuerzo", "cena", "comida", "escabio", "agua", "leche", "jugo", "rucula", "gaseosa", "vino", "cerveza", "sal", "azúcar", "aceite", "vinagre", "harina", "pan", "frutas", "verduras", "carne", "pollo", "pescado", "mariscos", "arroz", "fideos", "sopa", "ensalada", "postre", "helado", "torta", "dulce", "salado", "amargo", "picante", "frío", "caliente", "templado", "congelado", "fresco", "calor", "invierno", "verano", "otoño", "primavera", "sol", "nubes", "lluvia", "viento", "tormenta", "rayo", "trueno", "parabrisas", "estrella", "luna", "planeta", "tierra", "cielo", "aire", "agua", "fuego", "naturaleza", "ambiente", "bosque", "selva", "montaña", "cerro", "colina", "valle", "río", "lago", "mar", "océano", "playa", "arena", "piedra", "barro", "hierba", "flor", "árbol", "arbusto", "hoja", "raíz", "tallo", "ramas", "tronco", "fruto", "semilla", "corteza", "hojas", "ramita", "naturaleza", "vida", "ser", "existir", "respirar", "crecer", "morir", "nacer", "vivir", "muerte", "vida", "alma", "espíritu", "cuerpo", "mente", "corazón", "sangre", "hueso", "piel", "cara", "cabeza", "ojos", "nariz", "boca", "labios", "dientes", "matriz", "orejas", "cabello", "pelo", "barba", "bigote", "cejas", "cuello", "hombros", "brazos", "codos", "manos", "dedos", "uñas", "biceps", "espalda", "panza", "cuadriceps", "cintura", "cadera", "piernas", "omoplatos", "rodillas", "pies", "hoyuelos", "talones", "plantilla", "zapatos", "medias", "pantalón", "remera", "camisa", "campera", "bufanda", "guantes", "gorro", "sombrero", "vestido", "pollera", "traje", "ropa", "calzado", "accesorios", "joyas", "cargador", "anillo", "collar", "pulsera", "aros", "broche", "cadena", "hebilla", "botón", "cremallera", "bolsillo", "cuello", "mangas", "escote", "botas", "sandalias", "tacones", "alpargatas", "corbata", "campera", "apretar"]
largo2 = ""

aleatorio = random.choice(palabras)
fallas = 0
largo = len(aleatorio)
addletras=""  
indice = []

def imprimir_guiones(largo):
    texto=""
    for i in range(largo):u
        texto +=  "_"
    return texto
guiones = imprimir_guiones(largo)
    
def ahorcado(indice,palabras,guiones,aleatorio,fallas,largo2):  
    addletras= input("ingrese una letra ") 
    for i in range(len(addletras)):
        for q in range(len(aleatorio)):
            if addletras[i] == aleatorio[q]:
                largo2 += addletras[i]
            else: 
                largo2 += guiones[q] #
    guiones = largo2 #asi largo se va actualizando
    largo2 = ""       
    print
    buleano=False
    print("El largo de la palabra es:",largo)
# if fallas = 0:


    # for i in range(aleatorio):
        #addletras[i]
  
    #print(aleatorio)
    for i in range(largo):
        if addletras == aleatorio [i]:
            indice.append(i)
            buleano=True
          
           
    
    if buleano==False:
        fallas += 1
        print(f"El contador de fallas es:{fallas}")
    buleano=False
    print(indice)


    print('''
      
     |----|
     0    |
    /|\   |
    / \   |
----------|''')
    print (guiones)          
    
    ahorcado(indice,palabras,guiones,aleatorio,fallas,largo2) #esta reptite
ahorcado(
    indice,palabras,guiones,aleatorio,fallas,largo2)
# Invocamos ahorcado una vez adentro para que inicie la funcion por primera vez y la otra para q se repita







