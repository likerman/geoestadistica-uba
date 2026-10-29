# Ejemplos reproducibles

Cada ejemplo tendrá su propia carpeta con:

- una pregunta concreta;
- procedencia y licencia de los datos;
- diccionario de variables;
- código ejecutable;
- resultados principales;
- vínculo al capítulo que lo interpreta.

El primer ejemplo es un caso sintético de arsénico que permite reproducir el recorrido completo sin atribuir los valores a pozos reales. El script `generar_caso_arsenico.py` crea los datos con semilla fija y el notebook `01_caso_arsenico_sintetico.ipynb` desarrolla la exploración inicial. Los notebooks siguientes recorren variograma, kriging, clustering, PCA, bootstrap, Random Forest, declustering y simulación secuencial gaussiana. El notebook de PCA combina una simulación geométrica con una pequeña tabla publicada de aguas geotérmicas cuya adaptación se documenta en el capítulo correspondiente; los ejemplos de aprendizaje y simulación son enteramente sintéticos.

Hasta verificar procedencia, licencia, unidades, coordenadas y criterio de selección, no se incorporarán datos reales a este repositorio.
