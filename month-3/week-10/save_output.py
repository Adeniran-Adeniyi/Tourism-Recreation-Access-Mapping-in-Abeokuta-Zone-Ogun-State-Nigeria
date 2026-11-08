import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
wards.to_file("data/processed/week10_outputs.gpkg", layer="wards_copy")
wards.drop(columns='geometry').to_csv("data/processed/wards_tables.csv")
print(gpd.list_layers("data/processed/week10_outputs.gpkg"))