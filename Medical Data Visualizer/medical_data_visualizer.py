import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("Medical Data Visualizer/medical_examination.csv")

# Add 'overweight' column
bmi = (df['weight'] / (df['height'] / 100)**2)
df['overweight']  = bmi.apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']  = df['cholesterol'].apply(lambda x: 1 if x == 1 else 0)
df['gluc']  = df['gluc'].apply(lambda x: 1 if x == 1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars=["cardio"], value_vars=["active","alco","cholesterol","gluc","overweight","smoke"])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat2 = df_cat.groupby(["cardio","variable","value"]).size().to_frame("counts").reset_index()


    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat2, x="variable", y="counts", kind="bar", hue='value', col="cardio")

    # Get the figure for the output
    fig = sns.catplot(data=df_cat2, x="variable", y="counts", kind="bar", hue='value', col="cardio")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
