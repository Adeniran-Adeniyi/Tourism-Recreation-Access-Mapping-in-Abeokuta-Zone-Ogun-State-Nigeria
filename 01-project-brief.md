# Project brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.

>**Author**: Adeniran Adeniyi Damilola

## 1. The question

> Where are the Tourism and Recreational sites in Abeokuta zone, how can visitors reach them and which hotel are located nearby?

## 2. The question

>Where are the tourism and recreation sites in Abeokuta zone, how quick can visitors reach them and which hotels are located nearby?

### Why this matters

>The Abeokuta zone hes several Tourism attractions, Recreational sites and accomodation facilities spread across different parts of the zones
>however, information about their location, accesibility and nearby hotels is scattered across platforms.
>this project brings those locations together on one map to make it easier to see where attractions are, how accesible they are by the road and where visitors can stay nearby.

## 3. Study area

>The study area covers six Local Government Areas in Ogun State: Abeokuta North, Abeokuta South, Odeda, Ewekoro, Obafemi Owode and Ifo. The study area lies approximately between latitudes 6.75°N and 7.35°N and longitudes 3.05°E and 3.60°E.

![Abeokuta Zone Study Area Map](Images/tourism-study-area.png)

## 4. What I mean by the terms

- Tourism attractions, Recreational sites : *this are the places of historical, cultural, archiological heritage site* 

- visitors : *they can also the known as tourist*
- accomodation facilities : *this are places of shealter for the tourrist or visitors*

## 5. Where Each Dataset Comes From

| Data item | Source | Format |
|---|---|---|
| LGA administrative boundaries | [GRID 3](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5) | Shapefile |
| Tourist & recreational sites | [OpenStreetMap](https://www.openstreetmap.org/export#map=8/7.400/3.785) | GeoJSON |
| Hotels | [OpenStreetMap](https://www.openstreetmap.org/export#map=8/7.400/3.785) | GeoJSON |
| Road network | [OpenStreetMap](https://www.openstreetmap.org/export#map=8/7.400/3.785) | GeoJSON |


## 6. What "done" looks like

>A web map showing tourist and recreational sites across the Abeokuta Zone, with nearby hotels and road connections.

>The map will show:

1.  Tourism & Recreational Sites Map
2. Hotel Distribution Map
3. Tourism Site Accessibility Map
4. Tourist Site–Hotel Proximity Map
5. Fastest Route Map

## Note on Data Quality

  >OpenStreetMap will be used as the main source for hotels, tourist and recreational sites, and the road network.

>Because OpenStreetMap is community-maintained, the completeness of hotels and attractions may vary between locations. Tourist locations will be checked against available Ogun State Government tourism information where possible.
>The road network will be used for route analysis, with road classification helping to identify the main roads connecting tourist destinations.

**Status:** Week 1 complete. Data acquisition in Week 2, see
[02-data-notes.md](02-data-notes.md).
