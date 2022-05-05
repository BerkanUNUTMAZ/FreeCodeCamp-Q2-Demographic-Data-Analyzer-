import pandas as pd
def calculate_demographic_data(print_data=True):
  df = pd.read_csv('adult.data.csv')
  # 1- How many of each race are represented in this dataset?
  race_count = df['race'].value_counts()
  print("Number of each race:\n", race_count) 


  # 2- What is the average age of men?
  average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
  print("Average age of men:", average_age_men)

  # 3- What is the percentage of people who have a Bachelor's degree?
  total_bachelor = df[df['education'] == 'Bachelors'].shape[0]  # gives number of row count
  print(total_bachelor)
  total_people = df.shape[0] # total people in dataset
  print(total_people)
  percentange_of_bachelors = round((total_bachelor / total_people) * 100,1)
  print(f"Percentage with Bachelors degrees: {percentange_of_bachelors}%")

  # 4- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

  education_requirements = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
  salary_requirements = df['salary'] == '>50K'
  total_requirements = round((education_requirements &salary_requirements).sum() / education_requirements.sum() *100,1)
  print(f"Percentage with higher education that earn >50K: {total_requirements}%")

  # 5- What percentage of people without advanced education make more than 50K?
  low_education_high_salary = round((~education_requirements & salary_requirements).sum() /(~education_requirements).sum() *100,1 )
  print(low_education_high_salary)
  print(f"Percentage without higher education that earn >50K: {low_education_high_salary}%")

  # 6- What is the minimum number of hours a person works per week?  
  min_hours_per_week = df['hours-per-week'].min()
  print(min_hours_per_week)
  print(f"Min work time: {min_hours_per_week} hours/week")

  # 7- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
  min_hours_req = df['hours-per-week'] == min_hours_per_week
  percentage_minhours_salaryrich = round((min_hours_req & salary_requirements).sum() / min_hours_req.sum() *100,1 )
  print(f"Percentage of rich among those who work fewest hours: {percentage_minhours_salaryrich}%")

  # 8- What country has the highest percentage of people that earn >50K and what is that percentage?
  sorted_countries = (df[salary_requirements]['native-country'].value_counts() \
  / df['native-country'].value_counts() * 100).sort_values(ascending=False)
  highest_earning_country = sorted_countries.index[0]
  highest_earning_country_percentage = round(sorted_countries.iloc[0], 1)
  print("Country with highest percentage of rich:", highest_earning_country)
  print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")

  # 9- Identify the most popular occupation for those who earn >50K in India.
  most_popular_occupation =  df[salary_requirements & (df['native-country'] == "India")]["occupation"].value_counts().index[0]
  print("Top occupations in India:", most_popular_occupation)

  return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentange_of_bachelors,
        'higher_education_rich': total_requirements,
        'lower_education_rich': low_education_high_salary,
        'min_work_hours': min_hours_per_week,
        'rich_percentage': percentage_minhours_salaryrich,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': most_popular_occupation
    }