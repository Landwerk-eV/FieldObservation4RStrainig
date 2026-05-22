# Events and Status

## Event tags

The presentation defines events as activities happening at the time of observation or shortly beforehand. They represent transient evidence rather than the long-term identity of a patch.

| Tag | Meaning |
| --- | --- |
| `#cutting` | Grassland has just been cut, or was cut in the preceding days |
| `#fertilisation` | Fertiliser was recently applied |
| `#grazing_cows` | Cows are grazing at the time of the image |
| `#grazing_horses` | Horses are grazing at the time of the image |
| `#grazing_sheeps` | Sheep are grazing at the time of the image |
| `#sillage_production` | Mechanical activity linked to silage production is visible |
| `#arable_harvest` | Mechanical crop harvest activity is visible |

## Status tags

Status tags capture noteworthy observed conditions of the patch. The slides list three initial examples:

- `#recently_cut`
- `#full_developed`
- `#max_grazed`

These are especially useful when training time-series models that need to recognise vegetation state transitions rather than only field type.

## How events and status differ

- Use a type tag for the persistent land-use interpretation.
- Use an event tag for a specific management action.
- Use a status tag for the visible condition of the sward or field at observation time.

The same polygon may carry all three layers when justified by the evidence.
