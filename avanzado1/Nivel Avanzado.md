Nivel Avanzado

1. El departamento de bienestar de campus desea organizar un torneo de tenis de mesa y requiere
Un programa que le permita llevar el control de los juegos llevados a cabo por cada uno de los
Inscritos en el torneo. El programa debe cumplir con los siguientes requerimientos:
1. Se tienen 3 categorías (Novato, Intermedio y Avanzado)
2. Cada partido ganado representa 2 puntos para el ganador.
3. Puntos a favor. Los puntos a favor se calculan con los puntos realizados en el juegos restando lo puntos
Recibidos en contra. Ej. Si en el set uno gano 11-7 tiene 4 puntos a favor.
4. El programa debe permitir registrar a cada jugador por categoría.
5. Cada categoría debe tener un mínimo de 5 inscritos para iniciar los juegos en la categoría.
6. En la categoría novatos solo se permiten jugadores entre 15 y 16 años, en intermedio jugadores entre
17 y 20 años y Avanzado jugadores mayores a 20 años.
7. El programa debe permitir llevar un registro detallado de cada jugador. Por ejemplo:

Id Jugador PJ PG PP PA TP
125 Abc 1 1 0 5 2

8. El programa debe permitir conoce el ganador por categoría.
================================================================================================================


Los datos se almacenan mediante un diccinario llamado jugadores, el cual guarda en su interior las llaves('id','nombre': 'variable con el nombre', 'edad': 'edad'), cada llave almacena uan lista ordenada, lacual sirve para organizar los datos que futuramente de ingresaran,esto gracias al identificador del id, que es quien define la ubicion de los datos de cada usuario poniendolos en una posicion especifica.
El diccionario de categoria, sirve para clasificar dad estudiante usando como punto de anclaje su id 
se crea una fucnion para cada opcion del menu. 
la funcion def egitrasj() pide 3 datos basicos y luego crea un ubicion especifica en el diccionario jugadores, asu ve compara si ya  fue registrado
registrar partido valida la existencia del jugador y usando el id busca dodne deven ir almacenados los datos de este jugador y los alamcena en su lugar correspondiente
gandor recorre el diccionario jugadores en la clave "total putos y de fine cual es el mayor le sal la ubiciacion para poder imprimir los datos ese jugador 