import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import point, polygon
# %matplotlib inline

street_map = gpd.read_file('/home/user/Pictures/karnataka_highway/karnataka_highway.shp')

fig, ax = plt.subplots(figsize=(15,15))
street_map.plot(ax=ax)
plt.show()