"""Controles editoriales mínimos para el manual."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]

# Al ejecutar `python scripts/check_manual.py`, Python agrega `scripts/` y no la
# raíz del repositorio a sys.path. Incorporamos explícitamente ROOT para poder
# importar los módulos reproducibles del manual tanto localmente como en CI.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def claves_bib() -> set[str]:
    texto = (ROOT / "referencias.bib").read_text(encoding="utf-8")
    return set(re.findall(r"^@\w+\{([^,]+),", texto, flags=re.MULTILINE))


class LectorHTML(HTMLParser):
    """Extrae identificadores y destinos sin dependencias externas."""

    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        atributos = dict(attrs)
        if atributos.get("id"):
            self.ids.add(atributos["id"] or "")
        if tag == "a" and atributos.get("href"):
            self.hrefs.append(atributos["href"] or "")


def main() -> None:
    errores: list[str] = []
    bib = claves_bib()
    marcadores_editoriales = [
        "codex:class-update",
        "Borrador de actualización docente",
        "Debe revisarse y transformarse",
    ]
    ids_explicitos: dict[str, Path] = {}
    textos_publicados: list[str] = []

    for archivo in ROOT.rglob("*.qmd"):
        if "_book" in archivo.parts:
            continue
        texto = archivo.read_text(encoding="utf-8")
        textos_publicados.append(texto)

        for posicion, caracter in enumerate(texto):
            if ord(caracter) < 32 and caracter not in "\n\r\t":
                errores.append(
                    f"{archivo.relative_to(ROOT)}: carácter de control U+{ord(caracter):04X} "
                    f"en posición {posicion}"
                )

        for id_explicito in re.findall(r"\{#([A-Za-z0-9_.:-]+)[^}]*\}", texto):
            if id_explicito in ids_explicitos:
                errores.append(
                    f"{archivo.relative_to(ROOT)}: id duplicado #{id_explicito}; "
                    f"ya aparece en {ids_explicitos[id_explicito].relative_to(ROOT)}"
                )
            else:
                ids_explicitos[id_explicito] = archivo

        for marcador in marcadores_editoriales:
            if marcador in texto:
                errores.append(
                    f"{archivo.relative_to(ROOT)}: marcador editorial visible: {marcador}"
                )

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
        if "_book" in notebook.parts:
            continue
        with notebook.open(encoding="utf-8") as entrada:
            contenido = json.load(entrada)
        ids_celdas: set[str] = set()
        for numero, celda in enumerate(contenido.get("cells", []), start=1):
            id_celda = celda.get("id")
            if not id_celda:
                errores.append(
                    f"{notebook.relative_to(ROOT)}: celda {numero} sin id estable"
                )
            elif id_celda in ids_celdas:
                errores.append(
                    f"{notebook.relative_to(ROOT)}: id de celda duplicado {id_celda}"
                )
            else:
                ids_celdas.add(id_celda)

    # Todo término definido debe estar conectado desde el cuerpo del manual.
    glosario = (ROOT / "glosario.qmd").read_text(encoding="utf-8")
    cuerpo = "\n".join(textos_publicados).replace(glosario, "")
    for ancla in re.findall(r"\{#(glosario-[A-Za-z0-9-]+)\}", glosario):
        if f"glosario.qmd#{ancla}" not in cuerpo:
            errores.append(f"glosario.qmd: término sin enlace entrante #{ancla}")

    # Si ya existe una construcción HTML, comprueba páginas y fragmentos internos.
    html_dir = ROOT / "_book"
    if html_dir.exists():
        documentos: dict[Path, LectorHTML] = {}
        for html in html_dir.rglob("*.html"):
            lector = LectorHTML()
            lector.feed(html.read_text(encoding="utf-8"))
            documentos[html.resolve()] = lector
        for html, lector in documentos.items():
            for href in lector.hrefs:
                partes = urlsplit(href)
                if partes.scheme or partes.netloc or href.startswith(("mailto:", "tel:")):
                    continue
                ruta = unquote(partes.path)
                destino = html if not ruta else (html.parent / ruta).resolve()
                if destino.suffix not in {"", ".html"}:
                    continue
                if destino.is_dir():
                    destino = destino / "index.html"
                if not destino.exists():
                    errores.append(
                        f"{html.relative_to(html_dir)}: enlace HTML inexistente {href}"
                    )
                elif partes.fragment and destino.resolve() in documentos:
                    if unquote(partes.fragment) not in documentos[destino.resolve()].ids:
                        errores.append(
                            f"{html.relative_to(html_dir)}: fragmento inexistente {href}"
                        )

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
