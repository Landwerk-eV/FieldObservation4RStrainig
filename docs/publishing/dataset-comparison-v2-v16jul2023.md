# Dataset comparison draft: v2 vs v16jul2023

This page starts a structured comparison between:

- `grassland_fieldObs_v2_export22may2026.gpkg`
- `grassland_fieldObs_v16jul2023_export22may2026.gpkg`

The goal is to document what changed between both exports and prepare a reproducible changelog for downstream remote-sensing training pipelines.

For a compact tabular view, see: [Dataset differences table](dataset-differences-table-v2-v16jul2023.md).

For the concrete per-record geometry additions/removals, see: [Geometry delta table](geometry-delta-table-v2-v16jul2023.md).

## 1) Technical container and geometry profile

Both datasets are GeoPackage files with one feature layer each.

- CRS (`srs_id`): `3857` in both datasets
- Geometry type: `MULTIPOLYGON` in both datasets
- Geometry column: `SHAPE` in both datasets

## 2) Layer identity and size

- v2 layer: `grassland_fieldObs_v2`
- v16jul2023 layer: `grassland_fieldObs_v16jul2023`

Feature counts:

- v2: `2860` features
- v16jul2023: `2906` features
- Difference: `+46` features in v16jul2023

## 3) Schema differences

v2 columns:

- `FID` (INTEGER, primary key)
- `SHAPE` (MULTIPOLYGON)
- `LandUse` (TEXT(254))
- `Management` (TEXT(254))
- `LULC` (TEXT(256))

v16jul2023 columns:

- `OBJECTID` (INTEGER, primary key)
- `SHAPE` (MULTIPOLYGON)
- `LandUse` (TEXT(1000))
- `Management_activity` (TEXT(1000))

Observed schema-level changes:

- Primary key renamed: `OBJECTID` -> `FID`
- Management field renamed: `Management_activity` -> `Management`
- `LULC` exists in v2 only (currently fully null)
- Text capacity reduced from `TEXT(1000)` to `TEXT(254)` for `LandUse` and management field

## 4) Completeness and value-shape signals

Field completeness snapshot:

- v2 `LandUse`: 0 nulls, but 4 blank-or-whitespace entries
- v16jul2023 `LandUse`: 6 null/blank entries
- v2 `Management`: 0 nulls, but 2593 blank-or-whitespace entries
- v16jul2023 `Management_activity`: 2624 null/blank entries
- v2 `LULC`: 2860/2860 null

Interpretation:

- Most management entries are absent in both datasets.
- A significant part of the observed management difference is likely due to null vs blank normalization.

## 5) Geometry and attribute drift (first pass)

Comparison by exact geometry bytes (`SHAPE`) gives:

- Geometries present in both: `2859`
- Geometries only in v2: `1`
- Geometries only in v16jul2023: `47`

For shared geometries (`2859`), normalized attribute differences (trimmed, null treated as empty):

- `LandUse` changed in `118` features
- Management field changed in `21` features
- Fully equal (`LandUse` + management): `2736` features

Examples show many `LandUse` updates are extended validity windows, for example:

- `#fallow(01.01.2022-31.07.2023,...)` -> `#fallow(01.01.2022-04.05.2024,...)`
- `#sillage(01.01.2005-31.12.2023,...)` -> `#sillage(01.01.2005-17.08.2024,...)`

## 6) ID behavior

ID ranges:

- v2: `FID` from `1` to `2860`
- v16jul2023: `OBJECTID` from `1` to `2906`

ID overlap:

- All IDs `1..2860` exist in both datasets
- IDs `2861..2906` exist only in v16jul2023

This indicates the extra records in v16jul2023 are appended IDs, while at least one geometry differs among overlapping IDs.

## 7) Open checks for next elaboration pass

- Identify the single geometry present only in v2 and why it is missing/replaced in v16jul2023.
- Build a category-level diff for `LandUse` tags (new tags, removed tags, changed time windows).
- Quantify management-history extensions vs genuinely new management events.
- Decide how to treat null vs blank normalization in the publication pipeline.
- Define whether `LULC` in v2 should be populated or removed from schema in a next export.
