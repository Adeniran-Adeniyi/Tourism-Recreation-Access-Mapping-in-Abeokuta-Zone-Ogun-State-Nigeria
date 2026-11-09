# Libraries needed
import geopandas as gpd
import matplotlib.pyplot as plt

# Data used
tourism_sites = gpd.read_file("05-data-used/processed/tourism_sites.gpkg", layer="tourism")
Abk_boundary = gpd.read_file("05-data-used/processed/ABK_boundary.gpkg", layer="abokut")
hotel = gpd.read_file("05-data-used/processed/hotel.gpkg", layer="hotelwe")

print("tourism crs before:", tourism_sites.crs)
print("boundary crs before:", Abk_boundary.crs)
print("hotel crs before:", hotel.crs)


tourism_sites = tourism_sites.to_crs("EPSG:32631")
Abk_boundary = Abk_boundary.to_crs("EPSG:32631")
hotel = hotel.to_crs("EPSG:32631")

print("tourism crs after:", tourism_sites.crs)
print("boundary crs after:", Abk_boundary.crs)
print("hotel crs after:", hotel.crs)

# map making
fig, ax = plt.subplots(figsize=(7,8))
Abk_boundary.plot(ax=ax, color='none', edgecolor='red')
tourism_sites.plot(ax=ax, color='green', markersize=10)
hotel.plot(ax=ax, markersize=7, color='black')
ax.set_title("Destribution of tourism and recreation in Abeokuta zone")
ax.set_axis_off()

#save to file
fig.savefig("month-3/week-10/tourism-recreation-distribution3.png", dpi=300, bbox_inches="tight")
print("Map saved")