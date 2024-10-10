import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Copy 
    df_line = df.copy()

    # Draw line plot
    fig = plt.figure(figsize=(14, 6))
    ax = fig.add_subplot(1,1,1)
    ax.plot(df_line)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019.")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    ###### Draw bar plot ######

    # create a structured dict with df for every year, take the year as key and the df as value
    dict_df_years = {curr_year: df_bar.loc[df_bar.index.year == curr_year] for curr_year in df.index.year.unique()} 

    # set up figure and bar details
    fig, ax = plt.subplots(layout='constrained')
    width = 0.04  # the width of the bars
    years = list(dict_df_years.keys())
    num_years = len(years)

    # Create an array for the x-coordinates for each year
    x = np.arange(num_years)  # x-coordinates for each year


    # calculate daily average and structure it for matplotlib so that every month has values for every year in a list eg as dict item: {3:[4747, 449, 4948], 4 [383, 473, 3738]}
    dict_dailyavg_ls_values = {month: [] for month in range(1, 13)}  # Dictionary to hold avg daily month data in a structured per month list for matplotlib
    dict_df_dailyavg = {}  # dictionary with avg daily month data as DataFrame

    for year, df_year in dict_df_years.items():
        # Group the DataFrame by month and calculate the sum of values for each month
        df_month = df_year.groupby(df_year.index.month).sum()
        # Group the DataFrame by month and calculate the amount of days for each month
        days_per_month = df_year.groupby(df_year.index.month).size()
        # Calculate the daily average by dividing the monthly sum by the number of days
        df_month_dailyavg = df_month.iloc[:,0] / days_per_month
        dict_df_dailyavg[year] = df_month_dailyavg

        # Create the structured list with average daily values for each month
        for month, value_list in dict_dailyavg_ls_values.items():
            # Use the get method to safely retrieve the average for the month, defaulting to 0 if missing
            dict_dailyavg_ls_values[month].append(dict_df_dailyavg[year].get(month, 0))    


    # Create the bars for each month
    for month in range(1, 13):
        ax.bar(x + (month - 1) * width, dict_dailyavg_ls_values[month], width, label=f'Month {month}')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Page Views by Month for Each Year')
    ax.set_xticks(x + width * 6)  # Center the x-ticks
    ax.set_xticklabels(years)  # Year labels
    ax.legend(title='Months', loc='upper left', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


    ###### Save image and return fig (don't change this part) ######
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    ### Year Plot ###

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    sns.boxplot(df_box, x="year", y="value", hue="year", ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')


    ### Month Plot ###

    # create pseudo DF with null values for 
    d = {'date': {0: '2016-01-09 00:00:00',
        1: '2016-02-10 00:00:00',
        2: '2016-03-11 00:00:00',
        3: '2016-04-12 00:00:00'},
        'value': {0: np.nan, 1: np.nan, 2: np.nan, 3: np.nan},
        'year': {0: 2016, 1: 2016, 2: 2016, 3: 2016},
        'month': {0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr'}}

    df_zero = pd.DataFrame(data=d)
    # Parse the 'date' column to datetime
    df_zero['date'] = pd.to_datetime(df_zero['date'])

    # Concate to original DF
    df_complete = pd.concat([df_zero,df_box])

    # Create the box plot using the complete DataFrame
    sns.boxplot(data=df_complete, x="month", y="value", hue="month", ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')  # Change to 'Month' for clarity
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
