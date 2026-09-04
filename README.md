# Manual de Geoestadística

Manual teórico con ejemplos prácticos, desarrollado progresivamente a partir de la materia **Geoestadística** del Departamento de Geología de la UBA durante 2026.

**Docentes:** Docentes de Geoestadística

[Libro web](https://likerman.github.io/geoestadistica-uba/) · [Repositorio](https://github.com/likerman/geoestadistica-uba)

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

GitHub Actions genera y publica automáticamente el libro web cuando se actualiza la rama `main`.

## Ejemplos en Python

El entorno mínimo utiliza NumPy, pandas, Matplotlib, Seaborn y SciPy. Puede instalarse con:

```bash
python -m pip install -r requirements.txt
```

## Criterio editorial

Cada capítulo debe distinguir con claridad:

1. el problema que motiva el concepto;
2. la definición y sus supuestos;
3. la interpretación geológica;
4. un ejemplo trabajado;
5. los errores frecuentes;
6. el vínculo con la geoestadística.

## Licencias

El texto, las figuras originales y el material docente se publican bajo [CC BY-NC-SA 4.0](LICENSE-CONTENT). El código fuente de los ejemplos se publica bajo [licencia MIT](LICENSE-CODE).
