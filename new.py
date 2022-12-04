import pandas as pd
import matplotlib.pyplot as plt
import os.path
import numpy as np
from os import path
import re
import string 
from string import Formatter
import csv
#import plotly.express as px

gdp = pd.read_csv("new_gdp.csv")
pop = pd.read_csv("new_world_population.csv")

pop.set_index('Country/Territory', inplace=True)
gdp.set_index('Country Name', inplace=True)

country = ["Afghanistan","United Arab Emirates","Argentina","Armenia","Australia","Azerbaijan", 'Belgium', 'Bangladesh', 'Bahrain', 'Brazil','Canada', 'Switzerland', 'Chile', 'China', 'Colombia', 'Cuba', 'Cayman Islands', 'Denmark', 'Spain', 'Finland', 'France', 'United Kingdom', 'Greece', 'Haiti', 'India', 'Ireland', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Kenya', 'Lebanon', 'Libya', 'Sri Lanka', 'Madagascar', 'Mexico', 'Malaysia', 'Nigeria', 'Netherlands', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Philippines', 'Poland', 'Romania', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Singapore', 'Sweden', 'Thailand', 'Uganda', 'Ukraine', 'United States', 'Vietnam', 'Zimbabwe']


for country_name in country:
	gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
	pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

	div_value =0
	gp_capital = []
	result_b = []

	for i in range(0,7):
	    div_value = gdp_value[i]/pop_value[i]
	    result_b.append(div_value)

	    data = {
	    	'country':country_name,
	    	'year':[1970,1980,1990,2000,2010,2015,2020],
	       	'gdp_rate': result_b 
	    }

	df = pd.DataFrame(data)
	plt.plot(df['year'], df['gdp_rate'],'', marker='o')
    
plt.legend(country, loc='upper left')
plt.title('GDP Grap', fontsize=14)
plt.xlabel('year', fontsize=14)
plt.ylabel('GDP/Capital', fontsize=14)
plt.grid(True)
plt.show()

