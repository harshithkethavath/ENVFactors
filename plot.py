import pandas as pd
import matplotlib.pyplot as plt


# Reading and Merging Sensor Data
env_data_1 = pd.read_csv('Data_Plot_Dec4/11-08-2024/Run_1/ENV Factors Sensor.csv')
env_data_2 = pd.read_csv('Data_Plot_Dec4/11-08-2024/Run_2/ENV Factors Sensor.csv')
env_data_3 = pd.read_csv('Data_Plot_Dec4/11-10-2024/ENV Factors Sensor.csv')
env_data_4 = pd.read_csv('Data_Plot_Dec4/11-11-2024/ENV Factors Sensor.csv')
env_data_5 = pd.read_csv('Data_Plot_Dec4/11-13-2024/ENV Factors Sensor.csv')
env_data_6 = pd.read_csv('Data_Plot_Dec4/11-18-2024/ENV Factors Sensor.csv')
env_data_7 = pd.read_csv('Data_Plot_Dec4/11-19-2024/ENV Factors Sensor.csv')
env_data_8 = pd.read_csv('Data_Plot_Dec4/11-22-2024/ENV Factors Sensor.csv')

merged_env_data = pd.concat([env_data_1, env_data_2, env_data_3, env_data_4, env_data_5, env_data_6, env_data_7, env_data_8])


# Reading and Merging Temperature Gun Data
temp_data_1 = pd.read_excel('Data_Plot_Dec4/11-08-2024/Run_1/Temperature Gun.xlsx')
temp_data_2 = pd.read_excel('Data_Plot_Dec4/11-08-2024/Run_2/Temperature Gun.xlsx')
temp_data_3 = pd.read_excel('Data_Plot_Dec4/11-10-2024/Temperature Gun.xlsx')
temp_data_4 = pd.read_excel('Data_Plot_Dec4/11-11-2024/Temperature Gun.xlsx')
temp_data_5 = pd.read_excel('Data_Plot_Dec4/11-13-2024/Temperature Gun.xlsx')
temp_data_6 = pd.read_excel('Data_Plot_Dec4/11-18-2024/Temperature Gun.xlsx')
temp_data_7 = pd.read_excel('Data_Plot_Dec4/11-19-2024/Temperature Gun.xlsx')
temp_data_8 = pd.read_excel('Data_Plot_Dec4/11-22-2024/Temperature Gun.xlsx')

merged_temp_data = pd.concat([temp_data_1, temp_data_2, temp_data_3, temp_data_4, temp_data_5, temp_data_6, temp_data_7, temp_data_8])


# Splitting Timestamp into Date and Time in Sensor Data
merged_env_data['Timestamp'] = pd.to_datetime(merged_env_data['Timestamp'])

merged_env_data['Date'] = merged_env_data['Timestamp'].dt.date
merged_env_data['Time'] = merged_env_data['Timestamp'].dt.time


# Creating a Timestamp column in Temperature Gun Data
merged_temp_data['Date'] = pd.to_datetime(merged_temp_data['Date'])
merged_temp_data['Time'] = pd.to_datetime(merged_temp_data['Time'], format='%H:%M:%S').dt.time

merged_temp_data['Timestamp'] = pd.to_datetime(merged_temp_data['Date'].astype(str) + ' ' + merged_temp_data['Time'].astype(str))


# Converting °F to °C in Temperature Gun Data
merged_temp_data['Temperature (°C)'] = (merged_temp_data['Temperature (°F)'] - 32) * 5/9


# Merging Temperature Data into a single Data holder
temp_readings = pd.merge( merged_temp_data, merged_env_data, on='Timestamp', suffixes=('_Gun', '_Sensor'))


# # Printing Data after Manipulation
# print(merged_env_data.head())
# print(merged_temp_data.head())
# print(temp_readings.head())


# Plotting Graph
plt.figure(figsize=(12, 6))

plt.plot(temp_readings['Temperature (°C)_Gun'], label='Temperature (°C) Gun', marker='o')
plt.plot(temp_readings['Temperature (°C)_Sensor'], label='Temperature (°C) Sensor', marker='o')

plt.xlabel('Index')
plt.ylabel('Temperature (°C)')
plt.title('Sensor vs Temprature Gun Readings')
plt.legend()
plt.grid(True)


# Show the plot
plt.tight_layout()
plt.show()