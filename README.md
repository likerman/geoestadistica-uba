# Manual de Geoestadística

Manual teórico con ejemplos prácticos, desarrollado progresivamente a partir de la materia **Geoestadística**.

El texto busca ser autosuficiente: sigue la secuencia conceptual del curso, pero no presupone que quien lee haya visto las clases ni reproduce las diapositivas. Los ejemplos geológicos introducen cada herramienta a partir de un problema concreto.

## Estado

Proyecto en construcción. La primera parte desarrolla los fundamentos de estadística descriptiva y prepara la transición hacia el análisis espacial mediante un caso conductor sobre concentraciones de arsénico en aguas subterráneas de la provincia de Buenos Aires.

## Organización

- `capitulos/`: desarrollo teórico principal.
- `ejemplos/`: ejemplos reproducibles y datos derivados o públicos.
- `recursos/`: figuras y material propio del manual.
- `referencias.bib`: bibliografía citada.
- `PLAN.md`: correspondencia entre manual, clases y estado de cada capítulo.
- `CONTRIBUTING.md`: reglas editoriales para mantener consistencia.

## Publicación

El proyecto usa [Quarto](https://quarto.org/) para producir un libro web. Desde la carpeta raíz:

```bash
quarto preview
```

Para generar la versión publicable:

```bash
quarto render
```

## Criterio editorial

Cada capítulo debe distinguir con claridad:

1. el problema que motiva el concepto;
2. la definición y sus supuestos;
3. la interpretación geológica;
4. un ejemplo trabajado;
5. los errores frecuentes;
6. el vínculo con la geoestadística.

