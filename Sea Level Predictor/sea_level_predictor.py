import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Data', color='blue')


    # Create first line of best fit (Year range to 2050)
    extended_years = np.arange(x.min(), 2051) # Range with extended fitted line to 2050

    res = scipy.stats.linregress(x, y) # Linear regression with scipy
    plt.plot(extended_years, res.intercept + res.slope * extended_years, 'r', label='Fitted line')


    # Create second line of best fit (Year range to 2000 - 2050)
    # Filter x and y values
    x = df.loc[df['Year']>=2000,'Year']
    y = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']

    extended_years = np.arange(x.min(), 2051) # Range with extended fitted line to 2050
    
    res = scipy.stats.linregress(x, y) # Linear regression with scipy
    plt.plot(extended_years, res.intercept + res.slope * extended_years, 'g', label='Fitted line')  


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
 
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()