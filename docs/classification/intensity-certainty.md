# Intensity and Certainty

## Intensity scale

The slides define a five-step management intensity scale.

| Tag | Meaning | Typical interpretation |
| --- | --- | --- |
| `i0` | no management | set-aside or natural grassland |
| `i1` | extensive use | low or no fertilisation, very low cutting or grazing intensity |
| `i2` | conventional management | typical agricultural practice such as hay meadow or moderate pasture |
| `i3` | intense | silage meadow with 3 to 4 cuts, or heavily used pasture |
| `i4` | maximum intensity | more than 4 cuts with strong fertilisation, or near-stable high-pressure pasture |

The presentation also links use intensity to cutting frequency, with a simple example classification:

- low intensity: cutting frequency `<= 2`
- moderate intensity: `2 < CF <= 3`
- high intensity: `CF >= 4`

## Certainty scale

The certainty tag records how strongly the evaluator trusts the classification.

| Tag | Meaning |
| --- | --- |
| `c50` | low certainty |
| `c75` | moderate certainty |
| `c90` | very certain |
| `c99` | highly certain |

## Usage guidance

- `c90` is described as the typical level for well-supported observations.
- `c99` should be reserved for cases that are almost fully certain.
- Lower certainty values are appropriate where management transitions, incomplete visibility, or missing local context make interpretation less robust.

Intensity and certainty are optional in the notation, but they become important once observations are reused for training data curation and model validation.
