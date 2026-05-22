# Events and Status

## Event tags

The presentation defines events as activities happening at the time of observation or shortly beforehand. They represent transient evidence rather than the long-term identity of a patch.

| Tag | Event | Example |
| --- | --- | --- |
| `#cutting` | Grassland in the image has just being cut (or about the days before) |  |
| `#fertilisation` | Grassland in the image has just being fertilized (or about the days before) | `Gülle- oder Mineraldünger-Ausbringung` |
| `#grazing_cows` | Cows (cattle) grazing at the time of the image |  |
| `#grazing_horses` | Horses grazing at the time of the image |  |
| `#grazing_sheeps` | Sheep grazing at the time of the image |  |
| `#sillage_production` | (Mechanical) farming activities at the time of the image showing sillage production | `Sillage balls pressing or its preparation` |
| `#arable_harvest` | (Mechanical) farming activities at the time of the image showing harvesting | `Mähdreschen, Mais häckseln` |

The event table from slide 10 should be interpreted as a short-term activity layer. Event tags can coexist with persistent type tags on the same geometry and are especially relevant for time-series training labels.

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
