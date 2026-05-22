# Data Lifecycle and Publishing

## From observation to public artefact

The source presentation describes a workflow in which observations move from field imagery to a geodatabase and then into a public, versioned repository.

The current repository formalises that workflow by adding MkDocs-based documentation and GitHub Pages publication.

## Intended lifecycle

1. collect images and metadata in the field
2. upload imagery to a cloud location
3. geolocate and interpret images in an office workflow
4. digitise or reuse patch geometries
5. store tags in polygon attributes or a geodatabase
6. export the dataset regularly
7. publish structured outputs and documentation through GitHub

## Why GitHub Pages is part of the workflow

Documentation is part of the data product. A public, versioned documentation site helps with:

- transparent definitions of tags and workflows
- reproducibility for training data preparation
- coordination between contributors and evaluators
- traceability when tag sets evolve over time

## Current repository implementation

This repository now includes:

- a MkDocs site
- a GitHub Actions workflow that builds and deploys the site on commits to `main`
- versionable markdown pages derived from the v06.may2026 presentation

That gives the project an initial publication layer even before the full cloud-service vision is implemented.
