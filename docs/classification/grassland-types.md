# Grassland Types

## Purpose

Grassland type tags describe the dominant management practice or structural category observed for a patch. The slides identify the following initial tag set in version `v0.2.jul2024`.

## Grassland Characterisation: Types (slide 8)

| Tag | Type & Management | Example |
| --- | --- | --- |
| `#hayfield` | Meadow (`Wiese`, `Heuwiese`) with traditional 2x cut (`Mad`) | `Wiese vorm' Haus` |
| `#sillage` | Meadow with >2 cuts (typically >=4 cuts) and intense fertilisation. Harvest to make sillage balls or by using a shredder (`Hächsler`) plus transport. | `Sillage Wiese Bern` |
| `#pasture_dairy` | Pasture with obvious cattle use (`Weide_Milchvieh` / cattle) | `Wiese Landwirt Hauptstrasse` |
| `#pasture_horses` | Pasture with obvious horse use |  |
| `#pasture_sheep` | Pasture with obvious sheep use |  |
| `#pasture_unspecified` | Pasture with unknown specific use but clear visual signs of pasture |  |
| `#mixed_pasture_sillage` | Known mixed use by animal grazing and cutting (for example from repeated observations) |  |
| `#mixed_pasture_hayfield` | Known mixed use by animal grazing and cutting (for example from repeated observations) |  |
| `#orchard_meadow` | `Streuobstwiese` oder `-weide` |  |
| `#mixed_grassland_arable` | Grassland in change with arable crop, often maize | `Patches between Neuenhof and woods` |
| `#grassland_natural` | Obviously (almost) unmanaged (semi-)natural grassland | `Sengbach upstream grassland areas` |
| `#grassland_wetland` | `Feuchtwiese` | `Wiesen bei Teichen in Wetterfeld` |
| `#grassland_setAside` | Actually used and managed grassland, yet currently or seasonally not managed. Typically one cut at the end of summer. | `Some grassland patches in the area in 2024` |

This table is the direct operational reference for assigning persistent grassland type labels. In practice, tags should encode the dominant management identity of the polygon, while short-lived management actions are added separately as events.

## Related crop classes

The presentation also lists adjacent land-use crop tags (slide 9):

| Tag | Type & Management | Example |
| --- | --- | --- |
| `#maize` |  |  |
| `#cereals` |  |  |
| `#potatoes` |  |  |
| `#beet` |  |  |

These are useful where training data spans both grassland and neighbouring agricultural classes.

## Interpretation guidance

- Prefer the most specific type tag that can be defended from imagery and context.
- Use mixed-use tags only when mixed management is known or repeatedly observed.
- Use non-grassland crop tags where the field is clearly under arable production.
