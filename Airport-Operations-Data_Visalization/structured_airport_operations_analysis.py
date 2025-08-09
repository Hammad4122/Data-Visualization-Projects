import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Loading json file
def loading_data(path):
    with open(path) as file :
        data = json.load(file)
    flights_df = pd.DataFrame(data["flights"])
    passenger_stats_df = pd.DataFrame(data["passenger_stats"])
    baggage_handling_df = pd.DataFrame(data["baggage_handling"])
    fuel_consumption_df = pd.DataFrame(data["fuel_consumption"])
    employee_stats_df = pd.DataFrame(data["employee_stats"])
    weather_conditions_df = pd.DataFrame(data["weather_conditions"])
    return flights_df,passenger_stats_df,baggage_handling_df,fuel_consumption_df,employee_stats_df,weather_conditions_df

# Removing the duplicate rows
def cleaning_df(df):
    # Removing the duplicate rows
    df = df.drop_duplicates().reset_index(drop = True)
    return df

# Counting Flights on-time and delayed
def flights_ontime_delayed(flights_status):
    on_time = flights_status[flights_status == "On Time"].count()
    delayed = flights_status[flights_status == "Delayed"].count()
    return on_time,delayed

# Avg Domestic and international passengers per day
def avg_dom_inter_passenger(df):                              # dom = Domestic , inter  = international
    avg_dom_passenger = df.groupby('date')["domestic"].mean()
    avg_inter_passenger = df.groupby('date')["international"].mean()
    return avg_dom_passenger,avg_inter_passenger

def fuel_cost(df):                # Total fuel cost for each airline
    fuel_cost_per_airline = df.groupby('flight_id')["fuel_cost_usd"].sum()
    return fuel_cost_per_airline

# Bar chart of flight status counts (On Time, Delayed) 
def flight_status(on_time,delayed):
    plt.bar("Delayed",delayed,label = "Delayed", color = 'skyblue')
    plt.bar("On-Time",on_time,label = "On-Time", color = 'lightpink')
    plt.title("Flights On-Time and Flights Delayed")
    plt.legend()
    plt.xlabel("Status");plt.ylabel("Counts")
    plt.show()

# Line chart of domestic vs international passengers over time.
def plot_passenger_trend(df):
    plt.plot(df["date"],df["domestic"],label = "Domestic")
    plt.plot(df["date"],df["international"], label = "International")
    plt.title("Domestic vs International passengers over time.")
    plt.legend()
    plt.xlabel("Date");plt.ylabel("Number of passengers")
    plt.xticks(df["date"],rotation = 90)
    plt.grid(axis='y')
    plt.show()

# fuel consumption (fuel_liters) per day for each flight on the same line chart.
def fuel_consumption(df):
    sns.lineplot(data=df,x='date',y='fuel_liters',hue='flight_id')
    plt.title("Fuel Consumption per Day")
    plt.xlabel("Date");plt.ylabel("Fuel in Liters")
    plt.xticks(rotation = 25)
    plt.grid()
    plt.show()

# Baggage Handling Efficiency
# Comparing checked_in vs loaded bags per flight.
def baggage_analysis(df):

    sns.barplot(data=df,x="checked_in",y="loaded",hue="flight_id",palette="coolwarm")
    plt.title("Checked_in vs Loaded bags per flight.",color = "blue")
    plt.xlabel("Checked_in");plt.ylabel("Loaded")
    plt.xticks(rotation = 90)
    plt.show()

# Lost & Delayed Bags Distribution
# boxplot of lost bags grouped by flight.
def lost_bags(df):
    grouped_data = df.groupby("flight_id")["lost"].sum().reset_index()
    sns.barplot(data=grouped_data,x="flight_id",y="lost")
    plt.title("Lost bags grouped by flight")
    plt.xlabel("Flight_id");plt.ylabel("Lost Baggages")
    plt.show()
    
# Weather & Passenger Correlation
def weather_passenger_correlation(weather_df,passenger_df):
    merged_df = weather_df.merge(passenger_df,how='inner')
    # Creating a scatterplot of visibility_km vs domestic passengers.
    sns.scatterplot(data=merged_df,x="visibility_km", y="domestic")
    plt.title("visibility_km vs domestic passengers.")
    plt.xlabel("Visibility_km");plt.ylabel("Domestic Passengers")
    plt.show()

## Advance Analysis
#Fuel cost vs lost baggage
def fuel_vs_lostBaggage(fuel_df,baggage_df):
    # Merge fuel consumption with baggage handling by flight_id & date.
    merged_df = fuel_df.merge(baggage_df,how="inner",on =["flight_id","date"])
    # scatterplot to see if higher fuel usage days have more lost baggage.
    sns.scatterplot(data=merged_df,x="fuel_liters",y="lost")
    plt.title("scatterplot to see if higher fuel usage days have more lost baggage.")
    plt.xlabel("Fuel (liters)");plt.ylabel("Lost_baggage")
    plt.show()

# main function()
def main():
    # Loading data from Json file
    flights_df, passenger_stats_df, baggage_handling_df, fuel_consumption_df, employee_stats_df, weather_conditions_df = loading_data(
    r"Data_Visualization_Projects/assets/airport_data.json")
    # Cleaning Data
    flights_df = cleaning_df(flights_df)
    passenger_stats_df = cleaning_df(passenger_stats_df)
    baggage_handling_df = cleaning_df(baggage_handling_df)
    fuel_consumption_df = cleaning_df(fuel_consumption_df)
    employee_stats_df = cleaning_df(employee_stats_df)
    weather_conditions_df = cleaning_df(weather_conditions_df)


    ## Data Analyzation
    # Counting Number of flights on-time and delayed
    ON_Time,Delayed = flights_ontime_delayed(flights_df["status"])
    # Average Domestic and international people per day
    avg_dom_passengers,avg_inter_passengers= avg_dom_inter_passenger(passenger_stats_df)
    # Total fuel cost for each airline
    FUEL_COST_OF_AIRLINEs = fuel_cost(fuel_consumption_df)


    ## Data Visualization
    # Bar chart of flight status counts (On Time, Delayed) 
    flight_status(ON_Time,Delayed)
    # Line chart of domestic vs international passengers over time.
    plot_passenger_trend(passenger_stats_df)
    # fuel consumption (fuel_liters) per day for each flight on the same line chart.
    fuel_consumption(fuel_consumption_df)
    # Baggage Handling Efficiency
    baggage_analysis(baggage_handling_df)
    # Lost & Delayed Bags Distribution
    lost_bags(baggage_handling_df)
    # Weather & Passenger Correlation
    weather_passenger_correlation(weather_conditions_df,passenger_stats_df)


    ## Advanced Analysis
    # Fuel Cost vs Lost Baggage
    fuel_vs_lostBaggage(fuel_consumption_df,baggage_handling_df)

if __name__ == "__main__":
    main()