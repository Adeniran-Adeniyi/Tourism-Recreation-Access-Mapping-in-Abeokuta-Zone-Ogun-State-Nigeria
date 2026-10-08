import pandas as pd
import geopandas as gpd
def main() -> None:
    nga = gpd.read_file(r"C:\Users\DELL LATITUDE 7490\Desktop\tourism_rec\NGA_adm\NGA_adm1.shp")
    print(nga.info())


if __name__ == "__main__":
    main()