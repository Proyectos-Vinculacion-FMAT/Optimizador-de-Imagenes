
### En este documento hablare un poco de los avances que se han hecho en estos dias para avanzar con el optimizador de imagenes.
# Investigacion avance
- Lo primero es la investigacion acerca de las posibles soluciones principales son 3
- Reescalado de imagenes - Podrian ser de hasta la mitad para no perder la posibilidad de lectura
- Cambio de imagen a color a blanco y negro - Esto ya que la imagen necesita solo ser leida no necesita tener la imagen en los colores originales
- Cambio en el tipo de formato de la imagen - Se puede cambiar a dos tipos de archivos que pueden servir en el caso de jpg que seria de jpg a jpeg y de jpg a webp(

Aqui hay una explicacion sencilla de algunos de los conceptos de la libreria que estoy utilizando
https://konfuzio.com/es/cv2/#cv2imread
Tambien se va a utilizar otra libreria que nos ayudara a convertir nuestros archivos de jpg y pdf a imagenes webp
https://pypi.org/project/Pillow/
Con la mayoria de las pruebas me mostro que no era la desicion mas optima el utilizar open cv ya que utiliza metodos muy agresivos a la hora de la prosecamiento de imagenes por esto mismo la descarte con el paso del tiempo y no solo eso si no que el tipo de formatos en los que se convierte se corre el riesgo de que no se pueda utilizar en web de forma sencilla por lo que podria ocasionar muchos mas errores por esto mismo decidi utilizar una libreria un poco mas sencilla que trabaja justo con el apartado de conversion de imagenes que se llama pillow esta es mucha mas sencilla y sirve para muchas funciones de edicion de imagenes incluye recortes, cambio de colores, contrastes y tambien tiene una funcion muy importante