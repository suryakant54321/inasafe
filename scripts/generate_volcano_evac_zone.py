from safe.engine.utilities import buffer_points
from safe.storage.core import read_layer

H = read_layer('/data_area/InaSAFE/public_data/hazard/Marapi.shp')
print H.get_geometry()

# Generate evacuation circle (as a polygon):
radius = 3000
center = H.get_geometry()[0]
Z = buffer_points(center, radius)
Z.write_to_file('Marapi_evac_zone_%im.shp' % radius)
