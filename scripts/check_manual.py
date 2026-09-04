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

    # Control de continuidad del caso sintético usado en clases y manual.
    from ejemplos.generar_caso_arsenico import generar, resumen_referencia

    datos = generar()
    if len(datos) != 1000:
        errores.append(f"caso sintético: se esperaban 1000 pozos y hay {len(datos)}")

    ref = resumen_referencia()
    esperados = {
        "n": 50.0,
        "media": 18.0132356850,
        "mediana": 15.7360730757,
        "sd": 10.9647036070,
        "asimetria": 1.6620646060,
        "exceso_curtosis": 3.1297227700,
    }
    for clave, esperado in esperados.items():
        observado = float(ref[clave])
        tolerancia = 1e-8 if clave != "n" else 0.0
        if abs(observado - esperado) > tolerancia:
            errores.append(
                f"caso sintético: {clave}={observado:.10f}; se esperaba {esperado:.10f}"
            )

    if errores:
        raise SystemExit("\n".join(errores))
    print("Controles editoriales superados")


if __name__ == "__main__":
    main()
