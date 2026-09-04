"""Caso sintético de arsénico usado en las clases y en el manual.

La receta reproduce exactamente la población y la campaña de 50 pozos utilizadas
en los notebooks docentes de probabilidad e inferencia de 2026. Los valores son
completamente sintéticos: no representan pozos reales ni sirven para evaluar
exposición.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


SEMILLA_POBLACION = 20260819
SEMILLA_CAMPANIA = 2026
SEMILLA_PREFERENCIAL = 20260820
N_POBLACION = 1000
N_CAMPANIA = 50


def generar() -> pd.DataFrame:
    """Genera la población sintética exacta usada en las clases."""
    rng = np.random.default_rng(SEMILLA_POBLACION)

    x = rng.uniform(0, 20, N_POBLACION)
    y = rng.uniform(0, 15, N_POBLACION)

    regional = 8 + 0.45 * x + 0.20 * y
    anomalia_1 = 45 * np.exp(-(((x - 6) / 3.2) ** 2 + ((y - 10) / 2.8) ** 2))
    anomalia_2 = 25 * np.exp(-(((x - 15) / 2.8) ** 2 + ((y - 4) / 2.5) ** 2))
    ruido = rng.lognormal(mean=2.05, sigma=0.55, size=N_POBLACION)
    ruido = ruido - ruido.mean()

    arsenico = np.clip(regional + anomalia_1 + anomalia_2 + ruido, 1, None)

    return pd.DataFrame(
        {
            "pozo": [f"P{i:04d}" for i in range(1, N_POBLACION + 1)],
            "x_km": x,
            "y_km": y,
            "as_ug_l": arsenico,
        }
    )


def muestra_clase(datos: pd.DataFrame | None = None, n: int = N_CAMPANIA) -> pd.DataFrame:
    """Devuelve, en el mismo orden, la campaña aleatoria usada en clase."""
    if datos is None:
        datos = generar()
    return datos.sample(frac=1, random_state=SEMILLA_CAMPANIA).reset_index(drop=True).iloc[:n].copy()


def muestra_preferencial(
    datos: pd.DataFrame | None = None, n: int = N_CAMPANIA
) -> pd.DataFrame:
    """Construye una muestra preferencial reproducible para contrastar diseños."""
    if datos is None:
        datos = generar()
    rng = np.random.default_rng(SEMILLA_PREFERENCIAL)
    pesos = datos["as_ug_l"].to_numpy(dtype=float)
    pesos = pesos / pesos.sum()
    indices = rng.choice(len(datos), size=n, replace=False, p=pesos)
    return datos.iloc[indices].reset_index(drop=True).copy()


def resumen_referencia() -> pd.Series:
    """Estadísticos usados para comprobar continuidad entre notebooks y manual."""
    from scipy import stats

    x = muestra_clase()["as_ug_l"].to_numpy()
    return pd.Series(
        {
            "n": len(x),
            "media": np.mean(x),
            "mediana": np.median(x),
            "sd": np.std(x, ddof=1),
            "asimetria": stats.skew(x, bias=False),
            "exceso_curtosis": stats.kurtosis(x, fisher=True, bias=False),
        }
    )


if __name__ == "__main__":
    print(resumen_referencia().round(3).to_string())
