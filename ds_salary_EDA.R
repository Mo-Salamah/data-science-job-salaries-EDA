
library(reticulate)
library(tidyverse)
library(ggplot2)
library(GGally)

use_miniconda("r-reticulate", required=TRUE)

source_python('data_science_salary_EDA.py')

py_to_r(salary)

head(salary)

# measures of central tendancy
salary %>% 
  summarise("Avg. Salary" = mean(salary_in_usd),
            "median salary" = median(salary_in_usd),
            "trimmed mean salary" = mean(salary_in_usd, trim=0.1),
            "trimmed median" = median(salary_in_usd, trim=0.1)
            )


# measures of variability
salary %>% 
  summarise('std' = sd(salary_in_usd),
            'range' = diff(range(salary_in_usd)),
            'IQR' = IQR(salary_in_usd),
            'median absolute deviation' = mad(salary_in_usd), # only robust metric
            'trimmed range' = diff(quantile(salary_in_usd, c(0.1, 0.9))))


ggplot(salary, aes(salary_in_usd)) +
  geom_histogram() +
  # title("salary distribution")
  NULL

salary$job_title <- toString(salary$job_title)

salary %>% 
  select(work_year, experience_level, employment_type, remote_ratio, company_size) -> salary_categorical

ggpairs(salary_categorical)



# frequency table

breaks <- seq(from=min(salary$salary_k), to=max(salary$salary_k), length=11)

salary_freq <- cut(salary$salary_k, breaks = breaks, include.lowest = TRUE, right = TRUE)

table(salary_freq)


# percentiles table

percentiles <- quantile(salary$salary_k, (seq(0, 100, length=11)/100))

salary_freq_quantiles <- cut(salary$salary_k, breaks = percentiles, include.lowest = TRUE, right = TRUE)

table(salary_freq_quantiles, salary$experience_level)









