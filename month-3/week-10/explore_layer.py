import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")

print(wards.head())
print('Rows and Columns:', wards.shape)
print(wards.geom_type.value_counts())
print("crs:", wards.crs)
print('bounds:', wards.total_bounds)