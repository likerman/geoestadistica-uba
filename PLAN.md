# Plan vivo del manual

Este archivo mantiene la correspondencia entre el desarrollo del curso y el libro. Debe actualizarse cuando cambia la presentación fuente, el guión docente o el caso reproducible.

## Estados

- `borrador`: estructura o notas iniciales.
- `en desarrollo`: texto sustantivo, todavía incompleto.
- `revisión docente`: contenido completo pendiente de revisión final.
- `estable`: auditado contra la versión vigente de la materia y sus recursos.

| Parte | Contenido del curso | Capítulo | Estado |
|---|---|---|---|
| Introducción | estadística, geoestadística, contexto, escala, incertidumbre | 01 | estable |
| Introducción | población, muestra, parámetro, estadístico, muestreo | 02 | estable |
| Introducción | variables, calidad, soporte y preparación | 03 | estable |
| Descriptiva | frecuencias, histogramas, densidad, ECDF, KDE | 04 | estable |
| Descriptiva | media aritmética, geométrica y cuadrática; mediana, moda y cuantiles | 05 | estable |
| Descriptiva | rango, IQR, varianza, desvío, $n-1$ y CV | 06 | estable |
| Descriptiva | momentos, asimetría, curtosis, boxplot, QQ-plot y normalidad | 07 | estable |
| Probabilidad | variable aleatoria, densidad, acumulación, normal, estandarización, cuantiles y QQ-plot | 08 | estable |
| Inferencia | distribución muestral, TCL, error estándar, t e intervalos | 09 | estable |
| Inferencia | comparación de medias, hipótesis, α, región crítica, p e IC-test | 10 | revisión docente — alineado con la clase vigente; falta el cierre sobre errores I/II, potencia y tamaño de efecto |
| Bivariado | correlación y regresión | 11 | borrador |
| Comparación de grupos | ANOVA y comparaciones múltiples | 12 | borrador |
| Multivariado | cluster, PCA y LDA | 13 | borrador |
| Espacial | variable regionalizada y supuestos | 14 | borrador |
| Espacial | variograma | 15 | borrador |
| Espacial | kriging | 16 | borrador |
| Integración | simulación, validación, comunicación y límites | 17 | borrador |

## Fuentes docentes vigentes para el tramo auditado

La auditoría del 4 de septiembre de 2026 contrastó el manual con:

- presentaciones y guiones efectivamente utilizados en las clases de introducción, descriptiva, probabilidad e inferencia;
- la versión vigente de la presentación `03_Inferencia`, revisada hasta su cierre en IC, pruebas de hipótesis y p-valor;
- notebooks y exploradores de muestreo repetido, error estándar, TCL, cobertura, ancho de intervalos y distribución $t$;
- el caso de planificación del espesor medio de un banco sedimentario;
- el ejemplo final de intensidad de fracturamiento en B06 y B07;
- bibliografía estadística y geoestadística vigente: Alperin, Davis, McKillup y Dyar, Isaaks y Srivastava, Pyrcz, Goovaerts, Chilès y Delfiner, Cressie, Remy et al., Wackernagel y Tolosana-Delgado y Mueller.

## Caso conductor vigente

El caso publicado para este tramo es completamente sintético. La receta autoritativa está en `ejemplos/generar_caso_arsenico.py` y coincide con los notebooks docentes de 2026:

- $N=1000$ pozos;
- semilla de población `20260819`;
- tendencia regional + dos anomalías + ruido lognormal centrado;
- campaña de 50 pozos mediante `random_state=2026`.

Valores de control de la campaña:

- $n=50$;
- media $\approx18.013$ µg/L;
- mediana $\approx15.736$ µg/L;
- $s\approx10.965$ µg/L;
- asimetría $\approx1.662$;
- exceso de curtosis $\approx3.130$.

Estos números deben mantenerse sincronizados entre capítulos, notebooks y futuras figuras. Cualquier cambio de receta requiere actualizar primero este control.

## Decisiones de la auditoría pre-inferencia

1. Los capítulos 01–07 se consideran conceptualmente sólidos y alineados con lo efectivamente enseñado.
2. El capítulo 08 fue consolidado y alineado con el caso y la narrativa de clase. Se reforzaron las distinciones ECDF/KDE/PDF/CDF, la normal como modelo, la estandarización como cambio de escala —no de forma—, la diferencia entre puntuación muestral y $Z$ poblacional, la interpretación de cuantiles y el uso diagnóstico del QQ-plot.
3. Se unificó la receta reproducible del caso conductor en `ejemplos/generar_caso_arsenico.py` y se sincronizaron el laboratorio y notebook integrador.
4. Se completó `referencias.bib` con Remy-Boucher-Wu, Wackernagel y Tolosana-Delgado-Mueller, además del núcleo ya existente.

## Actualización de inferencia — 4 de septiembre de 2026

Los capítulos 09 y 10 fueron reescritos contra la versión final de la clase de Inferencia Estadística I y reincorporados a la navegación pública.

### Capítulo 09

Quedaron consolidados:

1. distribución muestral de $\bar X$;
2. diferencia entre distribución de $X$ y distribución de $\bar X$;
3. centro de la distribución muestral;
4. varianza de la media y error estándar;
5. regla $SE\propto1/\sqrt n$ y la consecuencia $n\times4\Rightarrow SE/2$;
6. advertencia sobre dependencia espacial e información efectiva;
7. TCL como aproximación para la distribución muestral, sin regla mágica de $n=30$;
8. estandarización de la media en unidades de error estándar;
9. parámetro, estimador y estimación;
10. intervalos de confianza, cobertura y la interpretación frecuentista correcta del 95 %;
11. separación entre confianza, ancho del intervalo y precisión;
12. distribución $t$, grados de libertad y diferencia con la normal estándar;
13. planificación de tamaño muestral y análisis posterior del ejemplo de espesor.

### Capítulo 10

Quedaron incorporados los contenidos ya efectivamente dados:

1. comparación de dos medias mediante B06 y B07;
2. IC individuales y por qué su solapamiento no constituye un test de igualdad;
3. definición de $\Delta=\mu_7-\mu_6$;
4. error estándar de la diferencia;
5. IC95% de la diferencia $[0.31,6.09]$;
6. formulación $H_0:\Delta=0$;
7. interpretación de $t_{obs}\approx2.26$ como distancia en errores estándar;
8. hipótesis bilateral, unilateral derecha y unilateral izquierda;
9. $\alpha$, región crítica y valor crítico;
10. p-valor bilateral $\approx0.031$ y su interpretación correcta;
11. regla de decisión y distinción entre rechazar y demostrar;
12. equivalencia IC-test para el mismo modelo y nivel;
13. diferencia entre significación estadística e importancia geológica;
14. supuestos del modelo pooled e indicación de la alternativa de Welch;
15. independencia, dependencia espacial y riesgo de pseudorreplicación.

El camino conceptual que debe permanecer visible es:

$$
\text{muestra}\rightarrow\text{estadístico}\rightarrow\text{distribución muestral}
\rightarrow\text{TCL + SE}\rightarrow\text{estandarización}\rightarrow z/t
\rightarrow\text{IC}\rightarrow H_0\rightarrow t_{obs}\rightarrow\alpha,p\rightarrow\text{decisión}.
$$

## Próximo corte de trabajo

Antes de pasar formalmente a correlación y regresión falta cerrar un tramo corto de inferencia:

1. error tipo I;
2. error tipo II;
3. potencia $1-\beta$;
4. tamaño de efecto;
5. relación entre potencia, tamaño muestral, variabilidad, efecto y $\alpha$;
6. pseudorreplicación e independencia espacial como condición de validez.

Una vez dado y auditado ese bloque, el capítulo 10 pasará de `revisión docente` a `estable` y el curso avanzará a correlación y regresión.
