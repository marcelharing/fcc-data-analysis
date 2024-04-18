import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men =  round(df['age'].loc[df['sex'] == 'Male'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.loc[df['education'] == 'Bachelors'].shape[0]  / df['education'].shape[0] * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # High Education Mask
    mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')

    # percentage with salary >50K
    df_hig_edu = df.loc[mask] 
    higher_education_rich = round((df_hig_edu.loc[df_hig_edu['salary'] == '>50K'].shape[0] / df_hig_edu.shape[0] * 100), 1)
  
    df_low_edu = df.loc[~mask] 
    lower_education_rich = round((df_low_edu.loc[df_low_edu['salary'] == '>50K'].shape[0] / df_low_edu.shape[0] * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_hrs = df.loc[df['hours-per-week'] == df['hours-per-week'].min()]
    rich_percentage = round((df_min_hrs.loc[df_min_hrs['salary'] == '>50K'].shape[0] / df_min_hrs.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].unique()

    countries_s = pd.Series()
    for country in countries:
        country_df = df.loc[df['native-country'] == country]
        countries_s[country] = country_df.loc[country_df['salary'] == '>50K'].shape[0] / country_df.shape[0] * 100

    countries_s.sort_values(ascending=False).index[0]

    highest_earning_country = countries_s.sort_values(ascending=False).index[0]
    highest_earning_country_percentage = round(countries_s.sort_values(ascending=False)[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df['occupation'].loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
