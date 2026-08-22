"""Genera la población didáctica de arsénico usada en el manual.

Los valores son completamente sintéticos y no representan pozos reales.
"""

from pathlib import Path

import numpy as np
import pandas as pd


SEMILLA = 2026
N = 1000


def generar() -> pd.DataFrame:
    rng = np.random.default_rng(SEMILLA)
    x = rng.uniform(0, 100_000, N)
    y = rng.uniform(0, 80_000, N)
    profundidad = np.clip(rng.normal(38 + 0.00012 * x, 12, N), 8, 85)
    unidad = np.select(
        [profundidad < 25, profundidad < 55],
        ["Pampeano somero", "Pampeano profundo"],
        default="Arenas Puelches",
    )

    foco = 27 * np.exp(-(((x - 72_000) / 24_000) ** 2 + ((y - 55_000) / 19_000) ** 2))
    tendencia = 5 + 0.00008 * x + 0.00004 * y
    efecto_unidad = np.select(
        [unidad == "Pampeano somero", unidad == "Pampeano profundo"],
        [8.0, 3.0],
        default=-2.0,
    )
    ruido = rng.lognormal(mean=1.0, sigma=0.45, size=N) - np.exp(1.0 + 0.45**2 / 2)
    arsenico = np.clip(tendencia + foco + efecto_unidad + ruido, 0.2, None)

    muestra_aleatoria = np.zeros(N, dtype=bool)
    muestra_aleatoria[rng.choice(N, 50, replace=False)] = True

    prob = arsenico / arsenico.sum()
    muestra_preferencial = np.zeros(N, dtype=bool)
    muestra_preferencial[rng.choice(N, 50, replace=False, p=prob)] = True

    return pd.DataFrame(
        {
            "pozo_id": [f"S{i:04d}" for i in range(1, N + 1)],
            "x_m": np.round(x, 1),
            "y_m": np.round(y, 1),
            "profundidad_m": np.round(profundidad, 1),
            "unidad_sintetica": unidad,
            "as_ug_l": np.round(arsenico, 2),
            "muestra_aleatoria_50": muestra_aleatoria,
            "muestra_preferencial_50": muestra_preferencial,
        }
    )


if __name__ == "__main__":
    destino = Path(__file__).resolve().parents[1] / "datos" / "arsenico_sintetico.csv"
    generar().to_csv(destino, index=False)
    print(f"Escritas {N} filas en {destino}")
