# Observation Workflow

## Core process

The presentation summarises the main imagery workflow as:

`Field -> Cloud -> Evaluation -> geoDB`

That sequence is the backbone of the current documentation design.

## Initial imagery workflow

In the initial phase, contributors upload imagery to a cloud drive. The presentation lists mobile phones, GoPro cameras, and drones as typical sources, with GPS metadata treated as highly desirable for subsequent geolocation.

The next steps are:

1. collect imagery in the field, ideally with location metadata
2. upload the imagery to a shared cloud location
3. notify the image processor or evaluator about new imagery
4. geolocate the images and identify the relevant grassland patch
5. interpret the imagery in a human review workflow
6. digitise missing polygons if the observed patch is not yet represented
7. assign tags to the polygon object in the observation database

## Web application workflow

The presentation describes a concrete office workflow based on ArcGIS Online:

- pre-prepare imagery geolocation using services such as OneDrive, Google, or Apple Maps
- inspect high-resolution background imagery in an ArcGIS Online web application
- digitise observation patches as polygons
- enter observations through a form stored in polygon attributes
- export the observation polygon layer regularly
- upload the geodatabase to GitHub with versioning

## Publication workflow

The publication path is summarised in the slides as:

`ArcGIS Online -> Local -> GitHub`

This is why the repository now contains versioned documentation alongside the source material. The documentation makes the observation logic visible even before a full public database publication pipeline is available.

## Operational notes

- If image location cannot be identified reliably, the slide notes recommend ignoring the image.
- If a patch already exists, reuse the polygon object ID instead of creating duplicates.
- Events and status are interpreted on top of the persistent patch geometry.
