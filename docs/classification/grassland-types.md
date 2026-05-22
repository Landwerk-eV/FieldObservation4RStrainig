# Grassland Types

## Purpose

Grassland type tags describe the dominant management practice or structural category observed for a patch. The slides identify the following initial tag set in version `v0.2.jul2024`.

## Core grassland classes

| Tag | Meaning | Notes from the presentation |
| --- | --- | --- |
| `#hayfield` | Meadow with traditional two-cut management | Typical hay meadow or `Wiese` |
| `#sillage` | Meadow with more than two cuts and intensive fertilisation | Silage-oriented management |
| `#pasture_dairy` | Pasture with clear cattle use | Dairy or cattle pasture |
| `#pasture_horses` | Pasture with clear horse use | Horse pasture |
| `#pasture_sheep` | Pasture with clear sheep use | Sheep pasture |
| `#pasture_unspecified` | Pasture with visible pasture signs but unspecified animal type | Use when animal category is not known |
| `#mixed_pasture_sillage` | Mixed grazing and silage use | Based on repeated or known mixed use |
| `#mixed_pasture_hayfield` | Mixed grazing and hayfield use | Based on repeated or known mixed use |
| `#orchard_meadow` | Orchard meadow or pasture | `Streuobstwiese` or `-weide` |
| `#mixed_grassland_arable` | Patch alternating between grassland and arable use | Often with maize in rotation |
| `#grassland_natural` | Almost unmanaged semi-natural grassland | Very low or no management |
| `#grassland_wetland` | Wet grassland | `Feuchtwiese` |
| `#grassland_setAside` | Managed grassland currently not managed for a period | Often one late-season cut |

## Related crop classes

The presentation also lists adjacent land-use tags for arable reference patches:

- `#maize`
- `#cereals`
- `#potatoes`
- `#beet`

These are useful where training data spans both grassland and neighbouring agricultural classes.

## Interpretation guidance

- Prefer the most specific type tag that can be defended from imagery and context.
- Use mixed-use tags only when mixed management is known or repeatedly observed.
- Use non-grassland crop tags where the field is clearly under arable production.
