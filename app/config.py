from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("FIELDOBS_DATA_DIR", BASE_DIR / "data")).resolve()
BACKUP_DIR = Path(os.getenv("FIELDOBS_BACKUP_DIR", DATA_DIR / "backups")).resolve()
DEFAULT_LAYER = os.getenv("FIELDOBS_DEFAULT_LAYER", "")

# Curated attributes that are safe to edit in the first MVP.
PREFERRED_EDITABLE_FIELDS = [
    "obs",
    "observation",
    "notation",
    "type",
    "status",
    "intensity",
    "certainty",
    "start_date",
    "end_date",
    "notes",
    "comment",
]
