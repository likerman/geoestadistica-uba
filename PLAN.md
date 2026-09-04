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
| Inferencia | distribución muestral, TCL, error estándar, t e intervalos | 09 | en desarrollo — próxima actualización |
| Inferencia | comparación de medias, hipótesis, α, p, errores I/II, potencia y tamaño de efecto | 10 | en desarrollo — próxima actualización |
| Bivariado | correlación y regresión | 11 | borrador |
| Comparación de grupos | ANOVA y comparaciones múltiples | 12 | borrador |
| Multivariado | cluster, PCA y LDA | 13 | borrador |
| Espacial | variable regionalizada y supuestos | 14 | borrador |
| Espacial | variograma | 15 | borrador |
| Espacial | kriging | 16 | borrador |
| Integración | simulación, validación, comunicación y límites | 17 | borrador |

## Fuentes docentes vigentes para el tramo auditado

La auditoría del 4 de septiembre de 2026 contrastó el manual con:

- presentaciones y guiones efectivamente utilizados en las clases de introducción, descriptiva y probabilidad;
- notebooks de muestreo y descriptiva del caso sintético de arsénico;
- `Laboratorio_Arsenico_Probabilidad_Distribuciones_v8.ipynb` y versiones de control;
- guión de Probabilidad y Distribuciones, cuya secuencia explícita es descriptiva → variable aleatoria → densidad/acumulación → distribuciones teóricas → normal → estandarización → probabilidades → cuantiles → QQ-plot → puente a inferencia;
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

1. Los capítulos 01–07 se consideran conceptualmente sólidos y alineados con lo efectivamente enseñado; no se reescribieron para evitar cambios cosméticos sin beneficio pedagógico.
2. El capítulo 08 fue consolidado y alineado con el caso y la narrativa de clase. Se reforzaron las distinciones ECDF/KDE/PDF/CDF, la normal como modelo, la estandarización como cambio de escala —no de forma—, la diferencia entre puntuación muestral y $Z$ poblacional, la interpretación de cuantiles y el uso diagnóstico del QQ-plot.
3. Se unificó la receta reproducible del caso conductor en `ejemplos/generar_caso_arsenico.py` y se sincronizaron el laboratorio y notebook integrador.
4. Se completó `referencias.bib` con Remy-Boucher-Wu, Wackernagel y Tolosana-Delgado-Mueller, además del núcleo ya existente.
5. Los capítulos 09 y 10 se retiraron temporalmente de la navegación pública hasta ser actualizados contra la clase final de inferencia. No se considera aceptable publicar un capítulo planificado sólo por existir en el repositorio.

## Próximo corte de trabajo: inferencia

Actualizar 09–10 contra la presentación y guión final de Inferencia Estadística I e incorporar de manera coherente:

1. distribución muestral de $\bar X$;
2. centro, varianza y error estándar;
3. TCL sin regla mágica de $n=30$;
4. parámetro, estimador y estimación;
5. $z$ y $t$ como distribuciones de referencia;
6. intervalos de confianza, cobertura, α y precisión;
7. ejemplo de planificación de tamaño muestral;
8. comparación de dos medias mediante el caso de intensidad de fracturamiento en B06 y B07;
9. IC de la diferencia, $H_0$, $t_{obs}$, alternativas bilateral/unilateral, región crítica y p-valor;
10. equivalencia IC-test bajo el mismo modelo;
11. errores tipo I y II, potencia y tamaño de efecto;
12. independencia, pseudorreplicación y advertencia espacial.

El objetivo de esa actualización será conservar explícito el camino:

$$
\text{muestra}\rightarrow\text{estadístico}\rightarrow\text{distribución muestral}
\rightarrow\text{TCL + SE}\rightarrow\text{estandarización}\rightarrow z/t
\rightarrow\text{IC}\rightarrow H_0\rightarrow t_{obs}\rightarrow\alpha,p\rightarrow\text{decisión}.
$$
