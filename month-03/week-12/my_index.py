import numpy as np 
import rasterio



folder = "data/raw/my_landsat/"
scene = "LC09_L2SP_191055_20241208_20241210_02_T1"

with rasterio.open(folder + scene + "_SR_B4.TIF") as src:
    red_raw = src.read(1).astype("float32")

with rasterio.open(folder + scene + "_SR_B5.TIF") as src:
    nir_raw = src.read(1).astype("float32")

    profile = src.profile
valid = (red_raw > 0) & (nir_raw > 0)

red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

ndvi = np.full(red.shape, -32768.0, dtype="float32")
total = nir + red
ok = valid & (total != 0)
ndvi[ok] = (nir[ok] - red[ok]) / total[ok]
low = round(float(ndvi[ok].min()), 3)
high = round(float(ndvi[ok].max()), 3)

print("NDVI range:", low, "to", high)
print("Mean NDVI:", round(float(ndvi[ok].mean()), 3))

profile.update(dtype="float32", nodata=-32768.0, count=1)
with rasterio.open("data/processed/my_ndvi.tif", "w", **profile) as dst:
    dst.write(ndvi, 1)
print("saved data/processed/ndvi.tif")