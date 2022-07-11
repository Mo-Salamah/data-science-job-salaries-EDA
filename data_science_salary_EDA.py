#%%
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Column	Description
# work_year	The year the salary was paid.
# experience_level	The experience level in the
#       job during the year with the following possible values: EN Entry-level 
#       / Junior MI Mid-level / Intermediate SE Senior-level /
#       Expert EX Executive-level / Director
# employment_type	The type of employement for the role: PT Part-time FT Full-time
#       CT Contract FL Freelance
# job_title	The role worked in during the year.
# salary	The total gross salary amount paid.
# salary_currency	The currency of the salary 
#   paid as an ISO 4217 currency code.
# salaryinusd	The salary in USD (FX rate divided by avg. 
#       USD rate for the respective year via fxdata.foorilla.com).
# employee_residence	Employee's primary country of residence in 
#                       during the work year as an ISO 3166 country code.
# remote_ratio	The overall amount of work done remotely, 
#               possible values are as follows: 0 No remote work (less than 20%) 
#               50 Partially remote 100 Fully remote (more than 80%)
# company_location	The country of the employer's main office or contracting branch 
#           as an ISO 3166 country code.
# company_size	The average number of people that worked for the company during the year: 
#           S less than 50 employees (small) M 50 to 250 employees (medium) L more than 250
#           employees (large)

#%%
salary = pd.read_csv('ds_salaries.csv')

#----------------------------------------------------------------
# Data Cleaning
#----------------------------------------------------------------
#%%
# salary.head()
salary.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

#%% 
salary.info()

#%% 
# changing type of categorical columns
salary['work_year'] = pd.Categorical(salary['work_year'].astype(str), categories=['2020', '2021', '2022'], ordered=True)
salary['experience_level'] = pd.Categorical(salary['experience_level'], categories=['EN', 'MI', 'SE', 'EX'], ordered=True)
salary['employment_type'] = pd.Categorical(salary['employment_type'], categories=['FL', 'CT', 'PT', 'FT'], ordered=True)
salary['job_title'] = pd.Categorical(salary['job_title'], categories=pd.Series(salary.job_title.value_counts().index), ordered=False)
salary['salary_currency'] = salary['salary_currency'].astype('category')
salary['employee_residence'] = pd.Categorical(salary['employee_residence'].astype('category'))
salary['remote_ratio'] = pd.Categorical(salary['remote_ratio'].astype(str), categories=['0', '50', '100'], ordered=True)
salary['company_location'] = salary['company_location'].astype('category')
salary['company_size'] = pd.Categorical(salary['company_size'], categories=['S', 'M', 'L'], ordered=True)





#%%
salary.info()

#%%
salary.describe()

#%%
# drop duplicated rows
salary.drop_duplicates(ignore_index=True, inplace=True)

#%%
salary.to_csv('ds_salaries_cleaned.csv')


#----------------------------------------------------------------
# Analysis
#----------------------------------------------------------------


# %%



