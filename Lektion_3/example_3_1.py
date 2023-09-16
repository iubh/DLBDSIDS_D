################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

###############################################################################################
#                                                                                             # 
#   PYTHON ROUTINE zur Veranschaulichung von Use-Cases mit der Routine pandas loc bzw. iloc   #
#                                                                                             # 
############################################################################################### 

# Data housing.csv is also available at : https://github.com/njtierney/melb-housing-data/ #

import pandas as pd

df = pd.read_csv("housing.csv")

print(df.shape)
print(df.columns)

# Lösche das Label '#' nach Bedarf.

# Use case Nr. 1 - select all region names with loc and the corresponding latitude and longitude with iloc
# print('Use Case 1 : ')
# print('')
# print('The region names of the first 5 entries are : ')
# print(df.loc[:5],'council_area') # df.loc[0:5, 'Address'] works as well
# print('')
# print('The corresponding lattitude and longitude of region names for the first 5 entries are : ')
# print(df.iloc[:5, 16:18]) # Lattitude 
# print('')

# Use case Nr. 2 - select 1st, 250th and 500th with loc and the corresponding latitudes and longitudes with iloc
# print('Use Case 2 : ')
# print('')
# print('The region names of the first 5 entries are : ')
# print(df.loc[[1,250,500], 'council_area']) # df.loc[0:5, 'Address'] works as well
# print('')
# print('The corresponding lattitude and longitude of region names for the first 5 entries are : ')
# print(df.iloc[[1,250,500], 16:18]) # Lattitude 
# print('')

# Use case Nr. 3 - find and print all houses with a price larger than 10.000.000 Euros.
# print(df.loc[df.price > 10000000])

# Use case Nr. 4 - find and print all houses with a price larger than '1.000.000 Euros', Type = 't' and Seller_g = 'Marshall'.
# print(df.loc[(df.price > 1000000) & (df.type == 't') & (df.seller_g == 'Marshall')])