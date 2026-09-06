# Auditoría profunda del manual — 2026-09-06

Esta auditoría revisa el estado conceptual, editorial, reproducible y UX del manual de Geoestadística. El objetivo es sostener el crecimiento del libro como material académico de consulta para estudiantes de la materia.

## Estado general

El manual tiene una base sólida para el tramo ya dictado: introducción, datos, muestreo, descriptiva, probabilidad, inferencia por intervalos y pruebas de hipótesis. La narrativa mantiene una buena decisión didáctica: cada concepto aparece como respuesta a una limitación previa y se conecta, cuando corresponde, con la pregunta espacial que organizará la geoestadística.

La parte publicada no debe confundirse con el plan completo del curso. Los capítulos 11–17 existen como archivos de planificación, pero no están en la navegación pública. Esa decisión es correcta: evita que el lector encuentre páginas vacías o capítulos que parezcan definitivos cuando todavía no fueron desarrollados.

## Correcciones realizadas en esta auditoría

1. Se eliminaron bloques visibles de “borrador de actualización docente” que habían quedado al final de los capítulos 09 y 10. Eran útiles como trazabilidad interna, pero rompían el tono de libro y exponían comentarios editoriales al lector.
2. Se reforzó el control automático `scripts/check_manual.py` para fallar si reaparecen marcadores editoriales internos en archivos `.qmd`.
3. Se corrigió la explicación de tablas de frecuencia en el capítulo 04, separando frecuencia relativa, frecuencia absoluta acumulada y frecuencia relativa acumulada:

   \[
   r_j=\frac{f_j}{n},\qquad
   F_j=\sum_{\ell=1}^{j}f_\ell,\qquad
   R_j=\sum_{\ell=1}^{j}r_\ell=\frac{F_j}{n}.
   \]

   La versión anterior podía inducir a mezclar recuento acumulado con proporción acumulada.
4. Se actualizó el README para recomendar `quarto render --to html`, coherente con el flujo real de publicación.
5. Se quitó temporalmente el formato PDF de `_quarto.yml`, porque el render local completo fallaba en LaTeX. La versión HTML es la salida estable actual; el PDF debe retomarse como tarea específica de producción editorial.
6. Se agregó una sección de estado actual en la portada para que el lector entienda qué parte del libro está desarrollada y qué parte se incorporará con la cursada.
7. Se refinó la capa visual en `recursos/identidad/tema.scss`: interlineado, espaciado de títulos, tamaño de código, captions, callouts y ancho máximo de lectura.
8. Se eliminó una redundancia menor del README: “Docentes: Docentes de Geoestadística”.
9. Se normalizó en el plan el uso de “desviación estándar” en lugar de “desvío” para mantener terminología consistente.
10. Se dejó `recursos/clases/` fuera de git mediante `.gitignore`, para conservar dossiers locales sin publicarlos.

## Evaluación conceptual

### Fortalezas

- El manual distingue bien población, muestra, parámetro, estadístico, estimador y estimación.
- La separación entre distribución de datos y distribución muestral está bien desarrollada.
- El tratamiento de error estándar evita el error frecuente de escribir \(s/n\) en lugar de \(s/\sqrt n\).
- El capítulo de inferencia evita la regla mágica de \(n=30\) y subraya la dependencia de los supuestos.
- El capítulo de pruebas de hipótesis interpreta correctamente el p-valor como probabilidad condicionada a \(H_0\), no como probabilidad de que \(H_0\) sea verdadera.
- La advertencia “no rechazar \(H_0\) no equivale a aceptar \(H_0\)” quedó explícita y correctamente formulada.
- La diferencia entre significación estadística e importancia geológica está bien marcada.
- La dependencia espacial aparece de manera temprana como límite de la estadística clásica, sin forzar todavía el formalismo geoestadístico.

### Riesgos o puntos a vigilar

- El uso de ejemplos sintéticos es adecuado, pero debe seguir declarado con mucha claridad para evitar que el lector los confunda con datos reales de arsénico.
- El test \(t\) de dos muestras se presenta con modelo pooled por continuidad didáctica. Conviene desarrollar pronto la alternativa de Welch y explicar cuándo preferirla.
- La inferencia clásica aparece bajo supuestos de independencia que luego serán problematizados espacialmente. Este puente debe mantenerse visible para que el lector no naturalice \(n\) como cantidad de información independiente.
- Falta todavía cerrar error tipo I, error tipo II, potencia y tamaño de efecto. Ese cierre es importante antes de avanzar a correlación/regresión.
- La parte de censura y límites de detección está bien planteada, pero merece más desarrollo práctico cuando se incorporen datos hidrogeoquímicos reales.

## Evaluación UX y legibilidad

### Fortalezas

- La portada y el banner generan identidad visual clara.
- La navegación pública contiene sólo los capítulos desarrollados, más glosario y laboratorio integrador.
- Los capítulos tienen una arquitectura docente estable: objetivos, desarrollo conceptual, ejemplos, errores frecuentes, preguntas y ejercicios.
- Las figuras reproducibles incluyen `fig-cap` y `fig-alt`, lo cual mejora accesibilidad y lectura.
- El glosario es una pieza fuerte del manual y funciona como columna vertebral terminológica.

### Problemas detectados

- Había bloques de borrador visibles en capítulos publicados; ya fueron removidos.
- La salida PDF estaba configurada pero no era estable; ya fue retirada de la configuración por ahora.
- El README sugería un comando que podía intentar construir PDF y fallar; ya fue corregido.
- La portada no aclaraba suficientemente el estado vivo del manual; se agregó esa sección.

## Mejoras recomendadas

### Prioridad alta

1. Completar el cierre de inferencia: error tipo I, error tipo II, potencia, tamaño de efecto, independencia efectiva y pseudorreplicación.
2. Agregar una figura conceptual del flujo de inferencia:

   \[
   \text{muestra}\rightarrow\text{estadístico}\rightarrow
   \text{distribución muestral}\rightarrow
   \text{IC/test}\rightarrow
   \text{decisión e interpretación}.
   \]

3. Incorporar una figura o simulación sobre potencia: cómo cambia la probabilidad de detectar una diferencia según \(n\), \(\sigma\), \(\Delta\) y \(\alpha\).
4. Agregar un ejemplo reproducible de Welch vs pooled para que el lector vea el efecto de varianzas desiguales.
5. Revisar manualmente anchors del glosario en HTML publicado. El chequeo actual valida que el archivo exista, pero todavía no verifica todos los anchors internos.

### Prioridad media

1. Construir una plantilla de capítulo para los temas nuevos: problema geológico, definición, supuestos, ejemplo mínimo, errores frecuentes, puente espacial.
2. Crear una página “Cómo citar este manual” con versión, fecha y repositorio.
3. Agregar notebooks descargables por capítulo, no sólo código embebido.
4. Incorporar una tabla de símbolos viva, conectada con el capítulo de notación.
5. Homogeneizar el tratamiento de “distribución teórica”, “modelo” y “distribución empírica” con pequeños recuadros comparativos.

### Prioridad baja pero deseable

1. Preparar una salida PDF profesional con tipografía, portada, licencia y control de saltos de página.
2. Agregar una guía docente separada del manual público, para conservar decisiones de clase sin exponer borradores al lector.
3. Incorporar ejercicios con soluciones breves o pistas desplegables.
4. Agregar una página de historial de versiones del manual.

## Reglas editoriales que conviene mantener

- No publicar transcripciones ni dossiers de clase como capítulos.
- Toda figura numérica debe tener código reproducible, semilla fija y unidades.
- Toda figura tomada de una fuente externa debe tener fuente, licencia y justificación.
- La primera aparición sustantiva de un término central debe enlazar al glosario.
- Toda fórmula debe estar acompañada por interpretación verbal y condiciones de uso.
- No presentar la estadística clásica como “verdad final”: siempre marcar sus supuestos antes de pasar a la lectura espacial.

## Conclusión

El manual está en buen estado para el tramo inicial y ya tiene rasgos de libro académico: narrativa, notación, glosario, ejemplos reproducibles y bibliografía. La prioridad inmediata no es reescribirlo desde cero, sino proteger su consistencia mientras crece: controles automáticos, capítulos sólo publicados cuando estén maduros, figuras reproducibles y cierre conceptual de inferencia antes de avanzar hacia correlación, regresión y geoestadística espacial.
