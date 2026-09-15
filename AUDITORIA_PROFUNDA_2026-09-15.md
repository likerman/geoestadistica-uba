# Auditoría profunda del manual — 15 de septiembre de 2026

## Alcance

Se auditó el manual publicado como libro Quarto, el repositorio fuente y la alineación con los materiales docentes disponibles en la carpeta de clases:

- `01_INTRO`
- `02_DISTRIBUCION`
- `03_INFERENCIA`
- `04_RESUMEN`
- `05_REGRESION`

La revisión se concentró en el tramo actualmente publicado: introducción, datos, muestreo, descriptiva, probabilidad, inferencia, pruebas de hipótesis, varianzas/categorías, síntesis integradora y laboratorio sintético.

## Resultado general

El manual está conceptualmente bien orientado para funcionar como libro de consulta: mantiene una progresión clara desde dato y muestra hacia distribución muestral, intervalos, pruebas, errores, potencia y dependencia espacial como puente hacia geoestadística.

El ajuste más importante realizado en esta auditoría fue transformar el capítulo de repaso en una síntesis estable de manual, sin preguntas de parcial ni referencias al contexto evaluativo. También se incorporó una simulación reproducible de errores tipo I y II para mostrar que rechazar o no rechazar una hipótesis puede depender de la variabilidad muestral.

## Correcciones aplicadas

1. **Navegación**
   - Se configuró la barra lateral con `collapse-level: 1`.
   - En la portada, las partes principales del libro comienzan colapsadas.
   - En páginas internas, Quarto mantiene abierta la parte activa para orientar al lector.

2. **Numeración del laboratorio**
   - El laboratorio integrador dejó de aparecer como capítulo numerado.
   - Se marcó como sección no numerada para evitar la lectura extraña de un laboratorio que “arranca en 16”.

3. **Síntesis integradora**
   - Se eliminó la estructura de preguntas y respuestas.
   - Se quitó toda referencia al parcial.
   - Se reescribió como resumen conceptual: problema geológico → datos → descripción → modelo probabilístico → distribución muestral → intervalo/prueba → interpretación.
   - Se incorporó una figura reproducible de descriptiva comparada.
   - Se incorporó una simulación reproducible de error tipo I, error tipo II y potencia.

4. **Estado del manual**
   - Se ajustó el texto de portada para que hable del avance conceptual del manual y no del contexto de cursada o evaluación.
   - Se actualizó `PLAN.md` para reemplazar la referencia a “parcial” por “síntesis integradora”.

5. **Glosario y enlaces**
   - Se detectaron seis enlaces rotos desde el glosario hacia anchors inexistentes del capítulo 09.
   - Se agregaron identificadores estables en el capítulo 09.
   - Se corrigió el enlace de “sesgo” para apuntar al capítulo de muestreo, donde el tema está mejor ubicado.

6. **CSS**
   - Se eliminó una regla duplicada de ocultamiento del encabezado automático en la portada.

## Alineación con las clases

### Bloque 01–02: introducción, datos, muestreo y descriptiva

El manual conserva la narrativa trabajada en la primera presentación: la estadística aparece como una representación parcial de un sistema geológico, no como una colección de fórmulas. La incorporación de soporte, población, muestra, parámetro, estadístico, representatividad y espacialidad está alineada con el enfoque de la materia.

### Bloque 03–04: inferencia y consolidación

El manual cubre los puntos centrales de los guiones y presentaciones:

- distribución muestral de la media;
- diferencia entre dispersión de los datos y error estándar;
- efecto de $n$ sobre la precisión;
- ausencia de un umbral mágico del tipo $n=30$;
- intervalos de confianza como procedimientos con cobertura;
- uso de la distribución $t$ cuando $\sigma$ es desconocida;
- hipótesis nula, alternativa, valor crítico, región crítica y p-valor;
- interpretación correcta de $p$;
- distinción entre rechazar y no rechazar $H_0$;
- errores tipo I y II;
- potencia y sus factores: $n$, tamaño de efecto, variabilidad y $\alpha$;
- equivalencia entre IC y prueba bilateral bajo los mismos supuestos.

La nueva síntesis integradora está especialmente alineada con el guión `guión_08`, pero evita mencionar actividades de clase, preguntas de repaso o parcial.

### Bloque 05: regresión

La carpeta `05_REGRESION` aparece disponible, pero al momento de esta auditoría no contiene archivos listables mediante el conector. En el repositorio existen capítulos esqueleto para correlación/regresión y temas posteriores, pero no están desarrollados como capítulos publicados estables. La próxima actualización debería comenzar allí cuando los materiales estén accesibles.

## Auditoría conceptual

### Fortalezas

- La progresión didáctica es sólida y acumulativa.
- Los conceptos inferenciales se presentan como respuesta a problemas concretos, no como recetas.
- El manual evita interpretaciones incorrectas frecuentes: p-valor como probabilidad de $H_0$, IC como probabilidad posterior, $n=30$ como regla mágica, no rechazo como aceptación de $H_0$.
- La conexión con geoestadística aparece antes de variograma/kriging mediante soporte, dominio, dependencia espacial e información efectiva.
- El glosario está bien poblado y funciona como capa de consulta.

### Riesgos conceptuales a seguir cuidando

1. **Diferenciar muestra aleatoria, diseño espacial y muestra preferencial**
   - El manual lo menciona, pero cuando empiecen los capítulos espaciales convendrá formalizar mejor el contraste entre inferencia basada en diseño e inferencia basada en modelo.

2. **No sobregeneralizar normalidad**
   - El texto actual es cuidadoso. Mantener esta línea cuando se incorporen regresión, ANOVA y variograma.

3. **Potencia y tamaño de efecto**
   - La base es correcta. A futuro conviene agregar un ejemplo geológico más realista donde el efecto sea pequeño pero geológicamente relevante, para evitar que potencia quede sólo como concepto estadístico.

4. **Varianzas y categorías**
   - El capítulo 11 existe y compila. Conviene auditarlo específicamente contra las diapositivas de varianzas, F y $\chi^2$ antes de seguir ampliándolo.

5. **Correlación y regresión**
   - Hay un capítulo esqueleto. No conviene publicarlo como estable hasta tener el desarrollo completo y una narrativa que anticipe el problema espacial: correlación no implica causalidad, regresión no resuelve dependencia espacial por sí sola, y residuales espacialmente estructurados rompen supuestos clásicos.

## Auditoría UX y visual

### Fortalezas

- La portada quedó alineada con la identidad visual del curso.
- El banner principal aparece arriba y centrado dentro del contenido.
- El contenido mantiene ancho de lectura razonable.
- La paleta azul/cobre funciona bien para jerarquía, énfasis y gráficos.
- Todas las imágenes revisadas en el HTML tienen texto alternativo.
- El laboratorio ya no queda jerárquicamente confundido con los capítulos teóricos.

### Riesgos visuales a mejorar

1. **Orden de capítulos en navegación**
   - La síntesis aparece como capítulo 15 porque el capítulo 14 es varianzas/categorías. No es incorrecto, pero conviene decidir si “Síntesis integradora” debe cerrar la parte III o funcionar como capítulo no numerado.

2. **Densidad de texto**
   - Algunos capítulos son extensos y con pocos descansos visuales. Conviene incorporar más callouts conceptuales, mini-esquemas y figuras generadas por código.

3. **Consistencia de figuras**
   - Las figuras nuevas usan la paleta del manual. A futuro conviene centralizar una función/helper de estilo para que todos los notebooks produzcan gráficos con la misma estética.

4. **Capítulos futuros**
   - Los archivos esqueleto de capítulos 11–17 que no estén publicados deben mantenerse fuera de navegación o con una indicación clara de “en desarrollo” cuando se decida mostrarlos.

## Prioridades recomendadas

1. Auditar y consolidar el capítulo de varianzas, distribución F y datos categóricos.
2. Preparar el capítulo de correlación/regresión cuando estén disponibles los materiales de `05_REGRESION`.
3. Crear una plantilla común para figuras Python del manual.
4. Agregar una tabla viva de símbolos y notación.
5. Incrementar referencias bibliográficas en inferencia aplicada y estadística para geociencias.
6. Revisar la numeración final de “síntesis” y “laboratorio” según la experiencia de lectura deseada.

## Controles ejecutados

- Render completo del libro con Quarto.
- Control editorial con `scripts/check_manual.py`.
- Revisión de marcadores editoriales visibles.
- Revisión de menciones residuales a parcial/clase de repaso en capítulos publicados.
- Revisión de imágenes sin texto alternativo en HTML.
- Revisión de enlaces internos y anchors del glosario.
- Revisión de estado de GitHub Actions para publicación.
