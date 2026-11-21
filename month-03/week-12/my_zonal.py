import geopandas as gpd
import rasterio
import numpy as np
from rasterio.mask import mask

with rasterio.open("05-data-used/raw/my_SRTM.tif") as src:
    wards = gpd.read_file("05-data-used/processed/Abeokuta_ward.gpkg", layer="ward").to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells,_=mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means, 1)
wards[["NAME_2", "mean_elevation_m"]].to_csv("month-03/week-12/CSV.csv", index=False)
print(wards[["NAME_2", "mean_elevation_m"]])
