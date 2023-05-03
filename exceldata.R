library(readxl)
library(writexl)
library(dplyr)
library(lubridate)

# Read excel file
input_file <- "afm10.xlsx"
data <- read_excel(input_file)

# Convert "StartTime" column to Date type
data$StartTime <- as.Date(substr(data$StartTime, 1, 10))

# Initialize an empty data frame to store the processed data
processed_data <- data.frame(Week = character(), TotalDuration = numeric())

# Group data by week using "StartTime" column, 
# and calculate the sum of "IncidentDuration" for each week
data <- data %>% 
  mutate(Week = floor_date(StartTime, unit = "week")) %>% 
  group_by(Week) %>% 
  summarise(TotalDuration = sum(IncidentDuration, na.rm = TRUE))

# Write the result to a new Excel file
output_file <- "data_afm10.xlsx"
write_xlsx(data, output_file)

