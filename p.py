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

#Question-4,5,6
countries_resources = ['Australia', 'Saudi Arabia', 'Qatar','Brazil']
innovative_countries = ['United States', 'Israel', 'Germany', 'Singapore']

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('GDP Growth', fontsize=10)
fig.supxlabel('Year', fontsize=14)

#countries_resources
for country_name in countries_resources:
    r_gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    r_pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    div_value =0
    r_gp_capital = []
    r_result_b = []

    for i in range(0,7):
        r_div_value = r_gdp_value[i]/r_pop_value[i]
        r_result_b.append(r_div_value)

        r_data = {
            'country':country_name,
            'year':[1970,1980,1990,2000,2010,2015,2020],
            'gdp_rate': r_result_b 
        }

    r_df = pd.DataFrame(r_data)
    
    ax1.plot(r_df['year'], r_df['gdp_rate'],'', marker='o')


ax1.legend(countries_resources, loc='upper left')
ax1.set_ylabel('GDP/Capital', fontsize=14)
ax1.set_title('Countries Resources')



#innovative _ountries
for country_name in innovative_countries:
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

    ax2.plot(df['year'], df['gdp_rate'],'', marker='o')
    ax2.set_title('Innovative Countries')
    
ax2.legend(innovative_countries, loc='upper left')
plt.show()

