import csv
import json
from collections import defaultdict

country_dict = defaultdict(dict)
jsonfile = open('data.json', 'w')

with open('data.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for i,row in enumerate(reader):
		if i >= 2:
  			country = row[0]
  			year = row[1]
  			share_top_10 = (row[2] if row[2]!='' else None)
  			share_top_1 = (row[8] if row[8]!='' else None)
  			share_top_01 = (row[14] if row[14]!='' else None)
  			average_top_10 = (row[18] if row[18]!='' else None)
  			average_top_1 = (row[22] if row[22]!='' else None)
  			average_top_01 = (row[26] if row[26]!='' else None)
  			if not country_dict[country]:
  				data_dict = {'name': country,
                 'share_top_10': [],
  							 'share_top_1': [],
  				 			 'share_top_01': [],
  							 'average_top_10': [],
  							 'average_top_1': [],
  							 'average_top_01': []}
  				country_dict[country] = data_dict
			if share_top_10 is not None:
				country_dict[country]['share_top_10'][year] = share_top_10
			if share_top_1 is not None:
  				country_dict[country]['share_top_1'][year] =share_top_1			
			if share_top_01 is not None:	
  				country_dict[country]['share_top_01'][year] = share_top_01
  			if average_top_10 is not None:
				country_dict[country]['average_top_10'][year] = average_top_10
			if average_top_1 is not None:
  				country_dict[country]['average_top_1'][year] = average_top_1		
  			if average_top_01 is not None:	
  				country_dict[country]['average_top_01'][year] = average_top_01

json.dump(country_dict, jsonfile)