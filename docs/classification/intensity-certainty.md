# Intensity and Certainty

## Intensity scale

The slides define a five-step management intensity scale.

| Tag | Type & Management | Example |
| --- | --- | --- |
| `i0` | no management | set-aside, natural |
| `i1` | extensive use, low/no fertilisation | sheep grazing twice a year, one cut in late season |
| `i2` | conventional management as typical agricultural practice | dairy cows/cattle (horse) pasture, where animals are 2x grazing, sometimes with a cut before, in between or in late season; hay meadow |
| `i3` | intense | sillage meadow, 3-4 cuts per year, moderate fertilisation; pasture near stable with animals almost every day present and grazing |
| `i4` | max intense | sillage meadow, >4 cuts per year, intense fertilisation after each cut using slurry and mineral fertilizer; pasture near stable with animals every day present and grazing; low density vegetation with many bare soil areas |

This slide-12 table is used to classify management pressure, not grassland type identity. The examples help separate conventional meadow and pasture use (`i2`) from intensive or maximum-intensive regimes (`i3` to `i4`).

The presentation also links use intensity to cutting frequency, with a simple example classification:

- low intensity: cutting frequency `<= 2`
- moderate intensity: `2 < CF <= 3`
- high intensity: `CF >= 4`

## Certainty scale

The certainty tag records how strongly the evaluator trusts the classification.

| Tag | Certainty level | Example note |
| --- | --- | --- |
| `c50` | low certainty | significant uncertainty, for example due to partial land-use change |
| `c75` | moderate certainty | use when not highly certain |
| `c90` | very certain | should be the typical level |
| `c99` | highly certain | use when almost 100% certain |

The certainty table from slide 12 encodes interpretation confidence independent from type or event semantics. It allows later model training and validation steps to filter or weight observations by confidence level.

## Usage guidance

- `c90` is described as the typical level for well-supported observations.
- `c99` should be reserved for cases that are almost fully certain.
- Lower certainty values are appropriate where management transitions, incomplete visibility, or missing local context make interpretation less robust.

Intensity and certainty are optional in the notation, but they become important once observations are reused for training data curation and model validation.
