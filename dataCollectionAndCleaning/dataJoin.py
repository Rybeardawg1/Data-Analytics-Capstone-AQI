#This file will join the AQI and Weather Data by time to create one mega, super awesome, computer crashing csv file
import pandas as pd

def joinFiles(air_quality_data, weather_data):
    #initial cleanup
    weather_data = weather_data.dropna(subset=['time','year', 'month', 'day'])
    air_quality_data = air_quality_data.dropna(subset=['time','year', 'month', 'day'])
    weather_data['time'] = weather_data['time'].str.slice(0, 5)
    
    merged_data = pd.merge(weather_data, air_quality_data, on=['time','day', 'month', 'year'], how='inner')
    #final cleanup
    merged_data.drop_duplicates(inplace=True)
    merged_data.drop(columns=['lat', 'lon','dt'], inplace=True)
    merged_data.to_csv("csv/merged_data.csv", index=False)
    print('finished merging')
    return merged_data
    

if __name__ == "__main__":
    weather_data = pd.read_csv("csv/weather_data_Boston_processed.csv", nrows=1000000)
    air_quality_data = pd.read_csv("csv/aqi_cleaned_Boston.csv", nrows=1000000)
    merged_data = joinFiles(air_quality_data, weather_data)