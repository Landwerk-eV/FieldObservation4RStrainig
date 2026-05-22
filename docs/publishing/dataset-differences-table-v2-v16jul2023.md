# Dataset differences table: v2 vs v16jul2023

Diese Seite dokumentiert die Unterschiede zwischen:

- grassland_fieldObs_v2_export22may2026.gpkg
- grassland_fieldObs_v16jul2023_export22may2026.gpkg

## Summary table

| Dimension | v2 | v16jul2023 | Difference / interpretation |
|---|---:|---:|---|
| File format | GeoPackage | GeoPackage | no change |
| Layer name | grassland_fieldObs_v2 | grassland_fieldObs_v16jul2023 | layer renamed |
| CRS (srs_id) | 3857 | 3857 | no change |
| Geometry type | MULTIPOLYGON | MULTIPOLYGON | no change |
| Feature count | 2860 | 2906 | +46 features in v16jul2023 |
| Shared geometries (exact SHAPE bytes) | 2859 | 2859 | stable overlap |
| Geometries only in v2 | 1 | - | one geometry removed/replaced in v16jul2023 |
| Geometries only in v16jul2023 | - | 47 | net new or changed geometries |

## Schema table

| Logical role | v2 column | v16jul2023 column | Change |
|---|---|---|---|
| Primary key | FID (INTEGER) | OBJECTID (INTEGER) | renamed |
| Geometry | SHAPE (MULTIPOLYGON) | SHAPE (MULTIPOLYGON) | unchanged |
| Land use text | LandUse (TEXT(254)) | LandUse (TEXT(1000)) | max length reduced in v2 |
| Management text | Management (TEXT(254)) | Management_activity (TEXT(1000)) | renamed + max length reduced in v2 |
| LULC | LULC (TEXT(256)) | not present | only in v2 |

## Data completeness table

| Field perspective | v2 | v16jul2023 | Note |
|---|---:|---:|---|
| LandUse null/blank | 4 | 6 | very similar sparsity |
| Management null/blank | 2593 | 2624 | high sparsity in both datasets |
| LULC nulls | 2860/2860 | n/a | v2 LULC currently not populated |

## Attribute drift on shared geometries (normalized)

Normalization rule:

- trim whitespace
- treat null as empty string

| Comparison on 2859 shared geometries | Count | Share |
|---|---:|---:|
| LandUse changed | 118 | 4.13% |
| Management changed | 21 | 0.73% |
| Fully equal (LandUse + Management) | 2736 | 95.70% |

## ID behavior

| ID metric | v2 | v16jul2023 | Interpretation |
|---|---|---|---|
| ID range | 1..2860 | 1..2906 | v16jul2023 extends range |
| Overlapping IDs | 1..2860 | 1..2860 | full overlap for base range |
| IDs only in v16jul2023 | none | 2861..2906 | appended records |

## Example value changes

| Field | Example old value | Example new value | Pattern |
|---|---|---|---|
| LandUse | #fallow(01.01.2022-31.07.2023,...) | #fallow(01.01.2022-04.05.2024,...) | validity window extended |
| LandUse | #sillage(01.01.2005-31.12.2023,...) | #sillage(01.01.2005-17.08.2024,...) | validity window extended |
| Management | mixed event strings | mostly identical with few deltas | sparse and low drift |

## Record-level delta list

For the full record-level list of geometry removals/additions with IDs, see: [Geometry delta table](geometry-delta-table-v2-v16jul2023.md).
