from __future__ import annotations

from shapely.geometry import LineString, shape, mapping
from shapely.ops import split, unary_union


def split_polygon_feature(feature: dict, splitter: dict) -> list[dict]:
    geom = shape(feature.get("geometry"))
    if geom.geom_type not in {"Polygon", "MultiPolygon"}:
        raise ValueError("Only Polygon and MultiPolygon can be split")

    line = shape(splitter)
    if not isinstance(line, LineString):
        raise ValueError("Splitter must be a LineString")

    parts = split(geom, line)
    if len(parts.geoms) < 2:
        raise ValueError("Split line did not cut the selected polygon")

    properties = feature.get("properties", {})
    return [
        {
            "type": "Feature",
            "geometry": mapping(part),
            "properties": dict(properties),
        }
        for part in parts.geoms
        if not part.is_empty
    ]


def merge_polygon_features(features: list[dict]) -> dict:
    if len(features) < 2:
        raise ValueError("Select at least two polygons to merge")

    geoms = [shape(feature.get("geometry")) for feature in features]
    for geom in geoms:
        if geom.geom_type not in {"Polygon", "MultiPolygon"}:
            raise ValueError("Only Polygon and MultiPolygon can be merged")

    merged = unary_union(geoms)
    if merged.geom_type not in {"Polygon", "MultiPolygon"}:
        raise ValueError("Merge result is not a valid polygon geometry")

    properties = dict(features[0].get("properties", {}))
    return {
        "type": "Feature",
        "geometry": mapping(merged),
        "properties": properties,
    }
