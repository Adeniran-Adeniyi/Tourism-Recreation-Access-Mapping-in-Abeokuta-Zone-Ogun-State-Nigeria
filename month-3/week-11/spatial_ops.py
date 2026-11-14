import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("data/raw/facilities.gpkg", layer="facilities").to_crs(epsg=32631)


#buffer operation

reach = facilities.copy()
reach["geomerty"] = facilities.buffer(20000)
print("buffered", len(reach),"facilities")

joined = gpd.sjoin(facilities, wards[["ward_name", "geometry"]], how="inner", predicate="within")

counts = joined.groupby("ward_name").size().rename("facility_count").reset_index()
wards = wards.merge(counts, on="ward_name", how="left")
wards["facility_count"] = wards["facility_count"].fillna(0).astype(int)
print(wards[["ward_name", "facility_count"]])
print("total count:", wards["facility_count"].sum(), "of", len(facilities))