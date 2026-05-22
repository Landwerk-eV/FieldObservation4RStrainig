# Overview and Objectives

## Project objective

The short-term objective is to provide field observation data as labelled samples for the training and validation of satellite-based grassland characterisation. The presentation explicitly names Sentinel-1 and Sentinel-2 as example target data sources.

The mid-term objective is broader: build a cloud-based observation service that supports imagery upload, backend processing, human evaluation, data provisioning, analysis, and visualisation.

## Observation concept

Grassland characterisation combines several dimensions:

- cultivation type, for example hayfield, silage meadow, or pasture
- cultivation intensity, for example inferred from cutting frequency and fertilisation
- observed cultivation events, such as cutting, fertilising, or grazing
- pollinator forage relevance and flowering-related interpretation when available
- observation date, time span, and location geometry

This makes the observation model suitable for both snapshot interpretation and time-series training.

## Design principles

The presentation points to several design choices that shape this documentation:

- use an explicit tag set rather than free-form descriptions
- keep the approach agile so tags can evolve over time
- version the documentation whenever the tag set changes
- store observations against geometries so time-bounded labels can be attached to the same patch
- keep the workflow understandable for contributors, processors, and downstream analysts

## Intended outcome

The intended outcome is a versioned observation dataset in which polygons represent grassland patches and tags describe type, events, status, intensity, and certainty across one or more time periods.
