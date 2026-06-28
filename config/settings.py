"""
Project Configuration
---------------------
Centralized configuration for HedgeFundAI.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(PROJECT_ROOT / ".env")

# =========================
# API Keys
# =========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# =========================
# Default LLM
# =========================

DEFAULT_MODEL = "groq"

SUPPORTED_MODELS = [
    "groq",
    "gemini"
]

# =========================
# Directories
# =========================

DATA_DIR = PROJECT_ROOT / "data"
REPORT_DIR = PROJECT_ROOT / "reports"
LOG_DIR = PROJECT_ROOT / "logs"

DATA_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)