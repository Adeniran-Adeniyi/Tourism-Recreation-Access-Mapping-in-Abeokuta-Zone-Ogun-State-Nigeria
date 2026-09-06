# Project Brief

**Project:** Tourism & Recreation Access Mapping — Abeokuta Zone, Ogun State, Nigeria  
**Author:** Adeniyi Adeniran Damilola  
**Cohort:** GeoDev Lab Africa, Cohort One  
**Date:** 6/9/2026

## 1. The Question

**Where are the tourist and recreational sites in the Abeokuta Zone, how quickly can visitors reach them, and which hotels are located nearby?**

## 2. Why This Matters

The Abeokuta Zone has several tourist attractions, recreational centres and accommodation facilities spread across different parts of the zone.

However, information about their locations, accessibility and nearby hotels is scattered across different platforms.

This project brings these locations together on one map to make it easier to see where attractions are, how accessible they are by road, and where visitors can stay nearby.

## 3. Study Area

The study area covers six Local Government Areas in Ogun State: Abeokuta North, Abeokuta South, Odeda, Ewekoro, Obafemi Owode and Ifo. The study area lies approximately between latitudes 6.75°N and 7.35°N and longitudes 3.05°E and 3.60°E.
## 4. The Data I Need

- Abeokuta Zone administrative boundaries
- Tourist and recreational sites
- Hotels
- Road network


## 5. Where Each Dataset Comes From

| Data item | Source | Format |
|---|---|---|
| LGA administrative boundaries | [GRID 3](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5) | Shapefile |
| Tourist & recreational sites | [OpenStreetMap](https://www.openstreetmap.org/export#map=8/7.400/3.785) | GeoJSON |
| Hotels | [OpenStreetMap](https://www.openstreetmap.org/export#map=8/7.400/3.785) | GeoJSON |
| Road network | [OpenStreetMap](https://www.openstreetmap.org/export#map=8/7.400/3.785) | GeoJSON |

## 6. What I Would Build

A web map showing tourist and recreational sites across the Abeokuta Zone, with nearby hotels and road connections.

The map will show:

-Tourist & Recreational Sites Map
-Hotel Distribution Map
-Tourist Site Accessibility Map
-Tourist Site–Hotel Proximity Map
-Fastest Route Map

## Note on Data Quality

OpenStreetMap will be used as the main source for hotels, tourist and recreational sites, and the road network.

Because OpenStreetMap is community-maintained, the completeness of hotels and attractions may vary between locations. Tourist locations will be checked against available Ogun State Government tourism information where possible.

The road network will be used for route analysis, with road classification helping to identify the main roads connecting tourist destinations.
