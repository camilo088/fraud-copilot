# Fraud Copilot 🛡️

Copiloto de IA para analistas de fraude: un modelo de ML detecta transacciones sospechosas y un agente LLM **explica por qué** cada alerta parece fraude, con evidencia, para que el analista decida más rápido.

> 🚧 En construcción — Semana 1: setup y análisis exploratorio.

## El problema
Los equipos antifraude reciben miles de alertas y gastan buena parte de su tiempo entendiendo cada una. Este proyecto busca reducir ese tiempo combinando detección con ML y explicaciones generadas por un LLM, con defensas contra prompt injection y monitoreo de calidad, costo y latencia.

## Dataset
[PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1): ~6.3 M transacciones sintéticas de dinero móvil con fraude etiquetado. No se incluye en el repo.

## Arquitectura (planeada)
| Pieza | Estado |
|---|---|
| Modelo de detección (XGBoost) | ⏳ Semana 2 |
| API (FastAPI) | ⏳ Semana 2 |
| RAG de tipologías (pgvector) | ⏳ Semana 3 |
| Agente explicador con herramientas | ⏳ Semana 4 |
| Defensas contra prompt injection | ⏳ Semana 5 |
| Evals, tracing, costos | ⏳ Semanas 6–7 |
| Despliegue en AWS + prueba de carga (k6) | ⏳ Semanas 8–10 |

## Cómo correrlo

Requisitos: [uv](https://docs.astral.sh/uv/), Docker, y una cuenta de Kaggle.

```bash
# 1. Dependencias
uv sync

# 2. Variables de entorno
cp .env.example .env

# 3. Base de datos
docker compose up -d
docker compose ps        # debe aparecer "healthy"

# 4. Datos (ver "Descargar PaySim" abajo)

# 5. Verificar
uv run pytest
uv run ruff check .
```

### Descargar PaySim
**Opción A — navegador:** descarga el ZIP desde Kaggle y descomprime el CSV en `data/raw/`.

**Opción B — CLI:** crea un token en Kaggle → *Settings → API → Create New Token*, guarda `kaggle.json` en `~/.kaggle/` y corre:
```bash
uvx kaggle datasets download -d ealaxi/paysim1 -p data/raw --unzip
```

## Estructura
```
data/            raw/ y processed/ (fuera de Git)
db/init/         SQL que corre al crear la base (activa pgvector)
docs/            bitácora de decisiones
notebooks/       análisis exploratorio
src/fraud_copilot/  código del proyecto
tests/
```

## Decisiones
Ver [`docs/decisions.md`](docs/decisions.md).
