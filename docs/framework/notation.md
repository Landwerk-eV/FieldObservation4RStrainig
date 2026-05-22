# Observation Notation

## Simple syntax

The presentation defines a compact observation syntax:

`#TYPE_OR_EVENT(DATE[, INTENSITY][, CERTAINTY])`

For time spans, `DATE` becomes a range:

`dd.mm.yyyy-dd.mm.yyyy`

## Semantics

The notation is intended to support both enduring land-use characterisations and transient events.

Each expression contains:

- `TYPE_OR_EVENT`: a tag from the documented vocabulary
- `DATE`: either a single date or a validity period
- `INTENSITY`: an optional management intensity class
- `CERTAINTY`: an optional confidence class for the interpretation

## Examples from the slides

```text
#hayfield(01.01.2022-31.12.2024,i2,c99)
#sillage(1.1.2018-30.12.2021,i4,c90)
#pasture_dairy(01.01.2005-31.12.2023,i3,c99)
```

The presentation also states that time periods may overlap. That allows a polygon to carry long-running type assignments together with short-lived events such as cutting or grazing.

## Polygon-level storage

An example polygon record in the slides uses comma-separated tags attached to one geometry identifier:

```text
#sillage(01.01.2005-31.12.2024), #cut(30.3.2021), #cut(29.4.2021), #grazing_cows(10.7.2021)
```

This supports time-series training because the same field patch can accumulate multiple observations across years.

## Versioning rule

The source presentation treats the tag vocabulary as agile but versioned. When tags change, the tag set should move to a new documented version so historical data remains interpretable.
