"""Rutas y configuración central del proyecto."""

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Nombre del CSV tal como viene de Kaggle (ealaxi/paysim1)
PAYSIM_CSV = RAW_DIR / "PS_20174392719_1491204439457_log.csv"
