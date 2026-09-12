# Data notes
## GRID3 Nigeria Operational Local Government Area (LGA) Boundaries (administrative level 2)
- source: [GRID3](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5)
- Downloaded:Friday, September 4, 2026 5:30:38 PM
- Total size: 19 KB,
- CRS: EPSG:4326 - WGS 84
- 6 features, polygons
- columns:ID_0, ISO, NAME_0, ID_1, NAME_1, ID_2, NAME_2, TYPE_2, ENGTYPE_2, NL_NAME_2, VARNAME_2
- No null in ward name
- cover my study area fully

## OSM roads, Extracted via Quick OSM
- Source: [openstreetmap](https://openstreetmap.org/)
- Quary: highway=* within Abeokuta zone
- Extracted: Extracted date: Friday, September 4, 2026 8:31:38 PM
- Total size: (1.2 MB),
- CRS: EPSG:4326 - WGS 84
- 5,551 features, lines
- many have no surface tag, so paved and unpaved can not be separeted everywhere
- Coverage looks good in the built-up area, sparse at the edge

## Tourism and Recreational sites
- source: [openstreetmap](https://openstreetmap.org/)
- Query: tourism = * within the layer extent (Abeokuta zone)
- Extracted: Friday, September 4, 2026 9:31:38 PM
- 38 features, nodes
- columns: full_id, osm_id, osm_type, tourism, phone, mobile, email, bar, air_conditioning, rooms, internet_access:fee, internet_access, addr:street, addr:postcode, addr:housenumber, addr:city
artwork_type, wikidata, website, name
- Total size: 191 KB,
- CRS: EPSG:4326 - WGS 84
- Their null values in the column phone, mobile, email, bar, air_condit, room, internet among other
- It is fully within my study area


## Hotel 
- source: [openstreetmap](https://openstreetmap.org/)
- Query: tourism with the value 'hotel' = * within the layer extent (Abeokuta zone)
- Extracted: Friday, September 4, 2026 9:25:38 PM
- 8 features, nodes
- Total size: 191 KB,
- CRS: [EPSG:4326 - WGS 84]
- columns:full_id, osm_id, osm_type, tourism, phone, mobile, email, Bar, air_conditioning, rooms, internet_access:fee, internet_access, addr:street, addr:postcode
addr:housenumber, addr:city, website, name
- There is null value in the following columns internet_access:fee, internet_access, though there are website in some of the features
- Some of the feature are found out side the study area.




