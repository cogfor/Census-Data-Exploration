import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Polygon, PathPatch
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, axisbg='w', frame_on=False)
fig.suptitle('PUMA Shapefiles: An Example with Basemap', fontsize=20)


# create a map object with the Albert Equal Areas projection.
# This projection tends to look nice for the contiguous us.
m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='aea',\
            lat_1=30.,lat_2=50,lon_0=-96,lat_0=38# state codes from http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMSDataDict13.txt
# note that areas outside of the conus have been commented out
state_codes = {'01': 'Alabama',
            #   '02': 'Alaska',                               
               '04': 'Arizona',                              
               '05': 'Arkansas',                             
               '06': 'California',                           
               '08': 'Colorado',                             
               '09': 'Connecticut',                          
               '10': 'Delaware',                            
               '11': 'District of Columbia',                 
               '12': 'Florida',                              
               '13': 'Georgia',                              
               '15': 'Hawaii',                               
               '16': 'Idaho',                                
               '17': 'Illinois',                             
               '18': 'Indiana',                              
               '19': 'Iowa',
               '20': 'Kansas',                               
               '21': 'Kentucky',                             
               '22': 'Louisiana',                            
               '23': 'Maine',                                
               '24': 'Maryland',                             
               '25': 'Massachusetts',                        
               '26': 'Michigan',                         
               '27': 'Minnesota',                            
               '28': 'Mississippi',                          
               '29': 'Missouri',                           
               '30': 'Montana',                              
               '31': 'Nebraska',                             
               '32': 'Nevada',                              
               '33': 'New Hampshire',                        
               '34': 'New Jersey',                         
               '35': 'New Mexico',                           
               '36': 'New York',                             
               '37': 'North Carolina',                       
               '38': 'North Dakota',                         
               '39': 'Ohio',                                 
               '40': 'Oklahoma',                             
               '41': 'Oregon',                              
               '42': 'Pennsylvania',                         
               '44': 'Rhode Island',                         
               '45': 'South Carolina',                       
               '46': 'South Dakota',                         
               '47': 'Tennessee',                            
               '48': 'Texas',                                
               '49': 'Utah',                                 
               '50': 'Vermont',                              
               '51': 'Virginia',                             
               '53': 'Washington',                           
               '54': 'West Virginia',                        
               '55': 'Wisconsin',                            
               '56': 'Wyoming',                              
            #   '72': 'Puerto Rico'
               }            


