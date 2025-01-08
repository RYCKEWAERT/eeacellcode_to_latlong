# Using the EEA Reference Grid for GBIF Data Cube Generation

This guide explains how to use the **EEA reference grid** (provided by the European Environment Agency) to obtain decimal latitude and longitude coordinates, particularly when working with **GBIF data cubes**. 
It is useful when spatial coordinates are missing in output data from GBIF queries.

## Context

When generating **GBIF data cubes** (see [GBIF Data Cubes Documentation](https://techdocs.gbif.org/en/data-use/data-cubes)), geographic coordinates are essential for spatial analysis. However, latitude and longitude may sometimes be omitted during data retrieval. To fill this gap, the **EEA reference grid** offers a standardized framework to convert grid cell references into decimal coordinates.

The EEA reference grid provides a regular spatial grid based on the **ETRS89 Lambert Azimuthal Equal Area (LAEA) projection**. Using this grid structure allows users to accurately calculate latitude and longitude for grid cells in the **WGS84 coordinate system**.

## Why Use the EEA Reference Grid?

- **Standardization**: Ensures spatial consistency across various datasets.
- **Simplified Conversion**: Facilitates coordinate conversion without complex projection calculations.
- **Compatibility**: Works seamlessly with biodiversity data aggregated from GBIF.

## Conversion Process

1. Identify the grid cell reference from your data output (e.g., 1 km x 1 km).
2. Use lookup tables or conversion formulas based on the grid’s origin and cell size to compute decimal latitude and longitude.
3. Alternatively, the EEA reference grid tools can be downloaded from the [EEA Data Hub](https://www.eea.europa.eu/en/datahub/datahubitem-view/3c362237-daa4-45e2-8c16-aaadfb1a003b).

### Example Use Case

If a GBIF data query does not return longitude and latitude, post-process the data using:

- EEA reference grid cell centers as reference points.
- Grid parameters to calculate WGS84 decimal degrees for each cell.


## Citation

When referencing the EEA reference grid, use the following citation:

```
European Environment Agency (EEA). (2020). EEA reference grid. Version 2020. Retrieved from https://www.eea.europa.eu/data-and-maps/data/eea-reference-grid.
```

## References

- European Environment Agency (EEA): [EEA reference grid](https://www.eea.europa.eu/data-and-maps/data/eea-reference-grid)
- GBIF Data Use Guide: [Data Cubes](https://techdocs.gbif.org/en/data-use/data-cubes)

