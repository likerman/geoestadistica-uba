"""Controles editoriales mínimos para el manual."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def claves_bib() -> set[str]:
    texto = (ROOT / "referencias.bib").read_text(encoding="utf-8")
    return set(re.findall(r"^@\w+\{([^,]+),", texto, flags=re.MULTILINE))


def main() -> None:
    errores: list[str] = []
    bib = claves_bib()

    for archivo in ROOT.rglob("*.qmd"):
        if "_book" in archivo.parts:
            continue
        texto = archivo.read_text(encoding="utf-8")

        for clave in re.findall(r"@([A-Za-z0-9_:-]+)", texto):
            if clave not in bib:
                errores.append(f"{archivo.relative_to(ROOT)}: cita inexistente @{clave}")

        lineas = texto.splitlines()
        for i, linea in enumerate(lineas):
            if linea.startswith("#| fig-cap:"):
                ventana = "\n".join(lineas[i : i + 4])
                if "#| fig-alt:" not in ventana:
                    errores.append(
                        f"{archivo.relative_to(ROOT)}:{i + 1}: figura sin fig-alt"
                    )

        for destino in re.findall(r"\]\(([^)]+)\)", texto):
            if destino.startswith(("http://", "https://", "mailto:")):
                continue
            ruta = destino.split("#", 1)[0]
            if not ruta:
                continue
            objetivo = (archivo.parent / ruta).resolve()
            if not objetivo.exists():
                errores.append(
                    f"{archivo.relative_to(ROOT)}: enlace local inexistente {destino}"
                )

    for notebook in ROOT.rglob("*.ipynb"):
        with notebook.open(encoding="utf-8") as entrada:
            json.load(entrada)

    datos = ROOT / "datos" / "arsenico_sintetico.csv"
    filas = datos.read_text(encoding="utf-8").splitlines()
    if len(filas) != 1001:
        errores.append(f"datos sintéticos: se esperaban 1000 filas y hay {len(filas) - 1}")

    if errores:
        raise SystemExit("\n".join(errores))
    print("Controles editoriales superados")


if __name__ == "__main__":
    main()
