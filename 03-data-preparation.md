# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
>Author: Adeniran Adeniyi Damilola

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** <EPSG:4326>

**Why this one:** To measure the area of the boundary i reproject the Abeokuta zone boundary from EPSG:4326 to EPSG:4326

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Abeokuta zone boundary | EPSG:4326 | EPSG:32631 | Reprojected |
| hotel | EPSG:32631 | EPSG:32631 | No change needed |
| Tourism and recreational sites | EPSG:32631 | EPSG:32631 | No change needed |
| Road | EPSG:32631 | EPSG:32631 | No change needed |

> Reprojecting recalculates every coordinate. Assigning a CRS only
> extract only 6 local government that make Abeokuta zone from Nigeria level 2 boundary
> Filled all the necessery field in the attribute table for layer Hotel and Tourism and recreational sites

## 2. Quary for Abeokuta zone
> to get coverage area or boundary i quary 6 lGA out of 775 in nigeria Administrative boundary
> Code
```
MAME_2 IN ('Abeokuta south', 'Abeokuta north', 'Odeda', 'Ifo', 'Obafemi Owode', 'Ewekoro')
```


## 2. Clipping to the study area

- **Boundary used:** > [Abeokuta zone](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5)
- **Features before clipping:** <775>
- **Features after clipping:** <>

<One sentence on anything unexpected, for example features that fell just
outside the boundary and whether you kept them.>

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | <yes / no> | <what you did> |
| Are there nulls in the fields I need? | <count> | <what you did> |
| Are there duplicate features? | <count> | <what you did> |
| Is the geometry valid? | <count invalid> | <what you did> |
| Does coverage span the whole study area? | <yes / no> | <what you did> |

## 4. Problems found, and what I did

**<Problem.>** <What it was, and whether you fixed it or flagged it.
Flagging honestly is acceptable. Hiding it is not.>

## 5. The analysis-ready output

- **File:** `data/processed/<filename>.gpkg`
- **Format:** GeoPackage
- **CRS:** <EPSG:XXXX>
- **Features:** <number>
- **Produced by:** <script name, or "manually in QGIS">

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
