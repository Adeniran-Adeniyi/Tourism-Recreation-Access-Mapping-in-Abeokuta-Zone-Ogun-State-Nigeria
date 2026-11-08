import pandas as pd
import geopandas as gpd

tables = pd.read_csv("data/raw/health_facilities.csv")
print(tables.head())

facilities = gpd.GeoDataFrame(
    tables, geometry=gpd.points_from_xy(tables["longitude"], tables["latitude"]), crs= "EPSG:4326")
print(facilities.head())
print(facilities.crs)

facilities.to_file("data/raw/facilities.gpkg", layer="facilities")
print("saved", len(facilities), "facilities")