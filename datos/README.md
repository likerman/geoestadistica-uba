# Datos de los ejemplos

El caso conductor vigente del manual es **completamente sintético y reproducible**. No representa pozos reales ni debe utilizarse para evaluar exposición, calidad de agua o riesgo sanitario.

La receta autoritativa está en `ejemplos/generar_caso_arsenico.py` y reproduce exactamente la población y la campaña de 50 pozos utilizadas en las clases de Probabilidad e Inferencia de 2026:

- población: 1000 pozos sintéticos;
- semilla de población: `20260819`;
- dominio: `x` entre 0 y 20 km, `y` entre 0 y 15 km;
- concentración: tendencia regional + dos anomalías suaves + ruido lognormal centrado;
- campaña didáctica: 50 pozos seleccionados mediante `random_state=2026`.

Los estadísticos de referencia de esa campaña son aproximadamente:

| Cantidad | Valor |
|---|---:|
| n | 50 |
| media | 18.013 µg/L |
| mediana | 15.736 µg/L |
| desviación estándar muestral | 10.965 µg/L |
| asimetría | 1.662 |
| exceso de curtosis | 3.130 |

La función `muestra_clase()` devuelve esa campaña en el mismo orden que los notebooks docentes. `muestra_preferencial()` genera, con otra semilla, una segunda muestra sintética cuyo mecanismo de selección favorece concentraciones altas y se utiliza únicamente para discutir sesgo de selección y cobertura espacial.

## Sobre datos reales

No se incorporará un conjunto real de arsénico como caso docente hasta que estén documentados, como mínimo, procedencia, licencia, identificadores, unidades, límites de detección, sistema de coordenadas, profundidad, soporte y criterio para seleccionar observaciones repetidas. Hasta entonces, toda cifra numérica del caso conductor debe identificarse explícitamente como sintética.
