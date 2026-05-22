from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class SaveFeaturesRequest(BaseModel):
    layer: str | None = Field(default=None, description="GeoPackage layer name to write")
    feature_collection: dict[str, Any] = Field(
        ..., description="GeoJSON FeatureCollection in EPSG:4326"
    )


class SplitRequest(BaseModel):
    feature: dict[str, Any] = Field(..., description="GeoJSON feature to split")
    splitter: dict[str, Any] = Field(..., description="GeoJSON LineString geometry")


class MergeRequest(BaseModel):
    features: list[dict[str, Any]] = Field(
        ..., description="GeoJSON features to merge"
    )
