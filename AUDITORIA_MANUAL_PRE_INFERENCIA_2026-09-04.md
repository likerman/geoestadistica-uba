# Auditoría del manual — tramo previo a Inferencia

**Fecha:** 2026-09-04  
**Alcance:** capítulos 00–08, caso conductor, laboratorio integrador, bibliografía y navegación pública.  
**Objetivo:** comprobar que el manual represente de manera fiel, coherente y reproducible lo efectivamente enseñado antes de incorporar la versión final de Inferencia Estadística I.

## 1. Fuentes contrastadas

La revisión no se hizo sólo contra el texto ya publicado. Se contrastaron cuatro familias de fuentes:

1. **Presentaciones y guiones docentes** de introducción, descriptiva y probabilidad, incluyendo el guión de Probabilidad y Distribuciones.
2. **Notebooks y exploradores didácticos**, en especial el laboratorio de muestreo/descriptiva y `Laboratorio_Arsenico_Probabilidad_Distribuciones_v8.ipynb`.
3. **Bibliografía del curso**, incluyendo Davis, Alperin, McKillup y Dyar, Isaaks y Srivastava, Pyrcz, Goovaerts, Chilès y Delfiner, Cressie, Remy-Boucher-Wu, Wackernagel y Tolosana-Delgado-Mueller.
4. **Arquitectura curricular vigente**, que exige que estadística clásica, reproducibilidad y diagnóstico estén siempre al servicio del problema espacial y no se enseñen como un catálogo de técnicas aisladas.

## 2. Diagnóstico general

El tramo previo a inferencia era **conceptualmente sólido**. Los capítulos 01–07 ya tenían una calidad superior a una simple transcripción de diapositivas: desarrollaban supuestos, soporte, diseño de muestreo, representatividad, medidas robustas, grados de libertad, valores extremos, transformaciones y la distinción entre distribución marginal y patrón espacial.

Por esa razón se evitó una reescritura general. Los cambios se concentraron donde había divergencias reales entre el manual y las clases.

## 3. Fortalezas confirmadas

### 3.1. Introducción y muestreo

Los capítulos 01–03 distinguen correctamente:

- sistema físico, mecanismo de observación y modelo;
- población, muestra, parámetro y estadístico;
- inferencia poblacional y predicción local;
- muestreo regular, aleatorio y preferencial;
- representatividad estadística y cobertura espacial;
- unidad de observación y soporte;
- calidad, censura, duplicados, coordenadas y valores extremos.

Esta base es especialmente importante para Geoestadística porque evita presentar la independencia o la representatividad como propiedades automáticas de un conjunto de filas.

### 3.2. Estadística descriptiva

Los capítulos 04–07 cubren adecuadamente:

- frecuencia absoluta, relativa y densidad;
- sensibilidad del histograma al ancho y origen de bins;
- ECDF y KDE;
- media, mediana, moda, cuantiles y promedios ponderados;
- rango, IQR, MAD, varianza, desviación estándar y CV;
- derivación conceptual de $n-1$;
- aclaración de que $n-1$ hace insesgado a $s^2$, no exactamente a $s$;
- asimetría y curtosis sin reducir la curtosis a “altura del pico”;
- boxplot y valores externos sin identificar automáticamente outlier con error;
- transformaciones como decisiones justificadas, no como ritual para obtener normalidad.

Se confirmó además que el manual ya advierte que $SE=\sigma/\sqrt n$ depende de independencia y que la correlación espacial cambia la información efectiva.

### 3.3. Narrativa hacia probabilidad

La transición descriptiva → probabilidad estaba bien planteada: pasar de describir realizaciones observadas a modelar valores posibles. Se conservaron como ejes:

- variable aleatoria y evento;
- densidad como área y no como altura-probabilidad;
- ECDF/KDE frente a PDF/CDF;
- normal como modelo de referencia;
- estandarización;
- probabilidades de cola e intervalo;
- cuantiles;
- QQ-plot como diagnóstico;
- puente desde $X$ hacia $\bar X$.

## 4. Huecos y problemas detectados

### 4.1. Dos casos sintéticos de arsénico incompatibles

Fue el problema principal de consistencia. El manual generaba una población sintética distinta de la usada en las clases y notebooks. Por eso el capítulo de probabilidad reportaba una media cercana a 17.52 µg/L y SD cercana a 8.47 µg/L, mientras que las clases usaban:

- $n=50$;
- media $\approx18.013$ µg/L;
- mediana $\approx15.736$ µg/L;
- SD $\approx10.965$ µg/L;
- asimetría $\approx1.662$;
- exceso de curtosis $\approx3.130$.

Esto debilitaba la continuidad pedagógica: el alumno veía “el mismo caso” pero los números cambiaban.

**Corrección:** `ejemplos/generar_caso_arsenico.py` reproduce ahora exactamente la receta usada en las clases: semilla `20260819`, dominio 20 × 15 km, tendencia regional, dos anomalías, ruido lognormal centrado y campaña seleccionada con `random_state=2026`.

### 4.2. Capítulo 08 desalineado numéricamente

El desarrollo conceptual era bueno, pero las cifras, probabilidades y cuantiles provenían del caso sintético anterior.

**Corrección:** se consolidó el capítulo completo alrededor del caso docente vigente. Se reforzaron además varias aclaraciones trabajadas oralmente en clase:

- proporción observada ≠ probabilidad poblacional exacta;
- altura de densidad ≠ probabilidad;
- kernel normal en KDE ≠ datos normales;
- estandarizar cambia centro y escala, no la forma;
- $z_i=(x_i-\bar x)/s$ y $Z=(X-\mu)/\sigma$ no son el mismo objeto inferencial;
- un z-score es una distancia relativa, no una probabilidad;
- el QQ-plot no debe producir una recta perfecta ni posee un umbral universal;
- una cuenta correcta bajo un modelo puede ser una representación científica insuficiente;
- la distribución marginal de $X$ no contiene información de localización.

### 4.3. Laboratorio y notebook integrador desincronizados

El laboratorio integrador utilizaba el archivo sintético anterior y variables que no coincidían con la receta de clase.

**Corrección:** tanto `ejemplos/01-caso-sintetico.qmd` como `ejemplos/01_caso_arsenico_sintetico.ipynb` utilizan ahora la receta docente y contienen valores de control explícitos.

### 4.4. Bibliografía incompleta respecto del núcleo acordado

`referencias.bib` ya incluía varias fuentes fundamentales, pero faltaban títulos seleccionados en la auditoría bibliográfica del curso.

**Corrección:** se incorporaron:

- Remy, Boucher y Wu — *Applied Geostatistics with SGeMS*;
- Wackernagel — *Multivariate Geostatistics*;
- Tolosana-Delgado y Mueller — *Geostatistics for Compositional Data with R*.

El núcleo bibliográfico queda ahora preparado tanto para los fundamentos actuales como para los bloques espaciales y multivariados posteriores.

### 4.5. PLAN.md y navegación pública desactualizados

El plan seguía registrando como pendiente un caso real de arsénico con una discrepancia 49/50 que ya no corresponde al caso conductor actual. También figuraba el capítulo de probabilidad como borrador y se exponía inferencia en la navegación antes de su auditoría final.

**Corrección:**

- capítulos 01–08 pasan a estado `estable`;
- se documenta el caso sintético vigente y sus números de control;
- capítulos 09–10 quedan como siguiente corte de trabajo;
- inferencia se retiró temporalmente de `_quarto.yml` hasta ser actualizada contra la presentación y guión final.

## 5. Decisiones que se conservaron deliberadamente

No se incorporó todavía un dataset real de arsénico. El manual mantiene datos completamente sintéticos hasta disponer de procedencia, licencia, coordenadas, soporte, límites de detección y criterios de selección documentados.

Tampoco se extendió el tramo estadístico con un catálogo de pruebas. La arquitectura curricular mantiene la decisión de enseñar estadística clásica para comprender incertidumbre, supuestos y decisiones, y reservar la mayor profundidad para dependencia espacial, variograma, kriging, simulación y validación.

## 6. Estado al cierre de la auditoría

El manual queda sólido y coherente **hasta el final de Probabilidad**. La secuencia publicada es:

$$
\text{problema y observación}
\rightarrow
\text{población y muestreo}
\rightarrow
\text{calidad y soporte}
\rightarrow
\text{descripción}
\rightarrow
\text{posición, dispersión y forma}
\rightarrow
\text{probabilidad y modelos}
\rightarrow
\text{puente a inferencia}.
$$

El siguiente corte debe incorporar la versión final de inferencia conservando la dependencia lógica:

$$
\text{muestra}\rightarrow\text{estadístico}\rightarrow\text{distribución muestral}
\rightarrow\text{TCL + SE}\rightarrow\text{estandarización}\rightarrow z/t
\rightarrow\text{IC}\rightarrow H_0\rightarrow t_{obs}\rightarrow\alpha,p\rightarrow\text{decisión}.
$$

A ese bloque habrá que añadir el cierre pendiente de inferencia clásica: errores tipo I y II, potencia, tamaño de efecto, independencia y pseudorreplicación espacial antes de pasar a correlación y regresión.
