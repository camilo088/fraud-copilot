# Bitácora de decisiones

Formato: fecha · decisión · por qué · alternativas descartadas.

## 2026-11-07 · Stack base
- **Decisión:** Python 3.12+, `uv` para dependencias, Postgres 16 + pgvector en Docker.
- **Por qué:** `uv` es rápido y reproducible (lockfile). pgvector evita mantener una base vectorial aparte para el RAG (semana 3).
- **Descartado:** Pinecone/Chroma (otra pieza más que operar), pip + requirements.txt (sin lockfile real).

## 2026-11-07 · Datos
- **Decisión:** Dataset PaySim (sintético, público). Nunca se versiona en Git.
- **Por qué:** Etiquetas de fraude disponibles y sin datos reales de clientes.
- **Regla:** Cero datos de empleadores anteriores en este repo.
