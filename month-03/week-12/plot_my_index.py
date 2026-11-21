import matplotlib.pyplot as plt
import rasterio
from rasterio.mask import mask
import geopandas as gpd



with rasterio.open("data/processed/my_ndvi.tif") as src:
    Abk_boundary = gpd.read_file("05-data-used/processed/ABK_boundary.gpkg", layer="abokut").to_crs(src.crs)
    study_area = Abk_boundary.dissolve()
    clipped, clipped_transform = mask(src, study_area.geometry, crop=True)
    profile = src.profile
    print("Before clip:", src.width, "x", src.height, "pixels")

profile.update(
    height=clipped.shape[1], width=clipped.shape[2], transform=clipped_transform
)
with rasterio.open("data/processed/abk_ndvi.tif", "w", **profile) as dst:
    dst.write(clipped)
print("After clip:", clipped.shape[2], "x", clipped.shape[1], "pixels")




with rasterio.open("data/processed/abk_ndvi.tif") as src:
    ndvi = src.read(1, masked=True)
fig, ax = plt.subplots(figsize=(7,8))
image = ax.imshow(ndvi, cmap="RdYlGn",vmin=-0.2, vmax=0.9)
fig.colorbar(image, ax=ax, label="NDVI")
ax.set_title("Vegetation index, Abeokuta Zones")
ax.set_axis_off()
fig.savefig("month-03/week-12/my_map.png", dpi=150, bbox_inches="tight")
print("Saved ndvi_map.png")