from __future__ import annotations

import re
from datetime import datetime

KNOWN_TAGS = {
    "hayfield",
    "sillage",
    "pasture_dairy",
    "pasture_horses",
    "pasture_sheep",
    "pasture_unspecified",
    "mixed_pasture_sillage",
    "mixed_pasture_hayfield",
    "orchard_meadow",
    "mixed_grassland_arable",
    "grassland_natural",
    "grassland_wetland",
    "grassland_setAside",
    "maize",
    "cereals",
    "potatoes",
    "beet",
    "cutting",
    "fertilisation",
    "grazing_cows",
    "grazing_horses",
    "grazing_sheeps",
    "sillage_production",
    "arable_harvest",
    "recently_cut",
    "full_developed",
    "max_grazed",
}

VALID_INTENSITY = {"i0", "i1", "i2", "i3", "i4"}
VALID_CERTAINTY = {"c50", "c75", "c90", "c99"}
NOTATION_COLUMNS = {"obs", "observation", "notation", "notes", "comment"}
TAG_EXPR_RE = re.compile(r"#([a-zA-Z0-9_]+)\(([^()]*)\)")
DATE_RE = re.compile(r"^(\d{1,2})\.(\d{1,2})\.(\d{4})$")


def validate_feature_collection_properties(features: list[dict]) -> None:
    for idx, feature in enumerate(features):
        props = feature.get("properties", {}) or {}
        for col_name, value in props.items():
            if not isinstance(value, str):
                continue
            if "#" not in value and col_name.lower() not in NOTATION_COLUMNS:
                continue
            text = value.strip()
            if not text:
                continue
            _validate_notation_text(text, idx, col_name)


def _validate_notation_text(text: str, feature_idx: int, column: str) -> None:
    matches = list(TAG_EXPR_RE.finditer(text))
    if not matches:
        raise ValueError(
            f"Feature {feature_idx} column '{column}' is not valid notation: '{text}'"
        )

    consumed = ", ".join(match.group(0) for match in matches)
    if consumed.replace(" ", "") != text.replace(" ", ""):
        raise ValueError(
            f"Feature {feature_idx} column '{column}' has invalid notation separators"
        )

    for match in matches:
        tag = match.group(1)
        args = [part.strip() for part in match.group(2).split(",") if part.strip()]
        if not args:
            raise ValueError(
                f"Feature {feature_idx} column '{column}' tag '#{tag}' misses DATE"
            )

        if tag not in KNOWN_TAGS:
            raise ValueError(
                f"Feature {feature_idx} column '{column}' uses unknown tag '#{tag}'"
            )

        _validate_date_or_range(args[0], feature_idx, column)
        for arg in args[1:]:
            if arg in VALID_INTENSITY or arg in VALID_CERTAINTY:
                continue
            raise ValueError(
                f"Feature {feature_idx} column '{column}' has invalid qualifier '{arg}'"
            )


def _validate_date_or_range(date_text: str, feature_idx: int, column: str) -> None:
    parts = date_text.split("-")
    if len(parts) == 1:
        _validate_date(parts[0], feature_idx, column)
        return
    if len(parts) == 2:
        start = _validate_date(parts[0], feature_idx, column)
        end = _validate_date(parts[1], feature_idx, column)
        if start > end:
            raise ValueError(
                f"Feature {feature_idx} column '{column}' has inverted date range"
            )
        return
    raise ValueError(
        f"Feature {feature_idx} column '{column}' has invalid date/range '{date_text}'"
    )


def _validate_date(date_text: str, feature_idx: int, column: str) -> datetime:
    token = date_text.strip()
    match = DATE_RE.match(token)
    if not match:
        raise ValueError(
            f"Feature {feature_idx} column '{column}' has invalid date '{token}'"
        )

    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))
    return datetime(year, month, day)
