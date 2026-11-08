from fraud_copilot import __version__
from fraud_copilot.config import RAW_DIR


def test_package_imports():
    assert __version__ == "0.1.0"


def test_raw_dir_exists():
    assert RAW_DIR.exists()
