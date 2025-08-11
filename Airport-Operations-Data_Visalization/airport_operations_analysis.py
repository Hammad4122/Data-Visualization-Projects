"""
Airport Operations Data Analysis Script

Processes and visualizes key airport metrics including:
- Flight schedules/status by airline
- Daily passenger traffic (domestic/international) 
- Baggage handling performance (checked-in/lost/delayed)
- Fuel consumption patterns and cost efficiency

Data Input:
    airport_data (dict): Nested dictionary containing:
        - flights: List of flight records
        - passenger_stats: Daily passenger counts 
        - baggage_handling: Baggage operation logs
        - fuel_consumption: Fuel usage records

Key Outputs:
    1. Visualizations:
        - Flight status pie charts
        - Passenger traffic line/bar charts  
        - Baggage handling stacked bars
        - Fuel cost scatter plots
    2. Terminal Prints:
        - Peak traffic days
        - Most delayed baggage dates
        - Fuel cost extremes

Note: All DataFrames are created internally from the source dictionary.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import msvcrt
# Ariport Operations DATA : 
airport_data = {
    "flights": [
        {"flight_id": "PK301", "airline": "PIA", "origin": "LHE", "destination": "ISB", "departure": "08:00", "arrival": "09:00", "status": "On Time"},
        {"flight_id": "PK301", "airline": "PIA", "origin": "LHE", "destination": "ISB", "departure": "08:00", "arrival": "09:00", "status": "On Time"},
        {"flight_id": "EK612", "airline": "Emirates", "origin": "DXB", "destination": "LHE", "departure": "11:00", "arrival": "15:00", "status": "Delayed"},
        {"flight_id": "QR620", "airline": "Qatar Airways", "origin": "DOH", "destination": "ISB", "departure": "13:00", "arrival": "17:00", "status": "On Time"},
        # Add ~20 more
    ],
    "passenger_stats": [
        {"date": "2024-06-01", "domestic": 5200, "international": 3400},
        {"date": "2024-06-02", "domestic": 6100, "international": 3200},
        {"date": "2024-06-03", "domestic": 5800, "international": 3600},
        # Add ~30 more days
    ],
    "baggage_handling" : [
        {"flight_id": "PK301", "date": "2025-07-01", "checked_in": 160, "loaded": 150, "lost": 1, "delayed": 5},
        {"flight_id": "EK612", "date": "2025-07-01", "checked_in": 220, "loaded": 210, "lost": 0, "delayed": 3},
        {"flight_id": "QR620", "date": "2025-07-01", "checked_in": 200, "loaded": 190, "lost": 2, "delayed": 6},
        {"flight_id": "PK301", "date": "2025-07-02", "checked_in": 165, "loaded": 155, "lost": 0, "delayed": 4},
        {"flight_id": "EK612", "date": "2025-07-02", "checked_in": 230, "loaded": 215, "lost": 1, "delayed": 2},
        {"flight_id": "QR620", "date": "2025-07-02", "checked_in": 205, "loaded": 195, "lost": 0, "delayed": 7},
        {"flight_id": "PK301", "date": "2025-07-03", "checked_in": 170, "loaded": 160, "lost": 2, "delayed": 3},
        {"flight_id": "EK612", "date": "2025-07-03", "checked_in": 240, "loaded": 220, "lost": 1, "delayed": 1},
        {"flight_id": "QR620", "date": "2025-07-03", "checked_in": 210, "loaded": 200, "lost": 3, "delayed": 4},
        # Add for other flights
    ],
    "fuel_consumption": [
        # ── Day 1 ───────────────────────────────────────────
        {"flight_id": "PK301", "date": "2025-07-01", "fuel_liters": 15000, "fuel_cost_usd": 12000},
        {"flight_id": "EK612", "date": "2025-07-01", "fuel_liters": 22000, "fuel_cost_usd": 18000},
        {"flight_id": "QR620", "date": "2025-07-01", "fuel_liters": 20000, "fuel_cost_usd": 17000},

        # ── Day 2 ───────────────────────────────────────────
        {"flight_id": "PK301", "date": "2025-07-02", "fuel_liters": 15500, "fuel_cost_usd": 12500},
        {"flight_id": "EK612", "date": "2025-07-02", "fuel_liters": 23000, "fuel_cost_usd": 18500},
        {"flight_id": "QR620", "date": "2025-07-02", "fuel_liters": 20500, "fuel_cost_usd": 17200},

        # ── Day 3 ───────────────────────────────────────────
        {"flight_id": "PK301", "date": "2025-07-03", "fuel_liters": 16000, "fuel_cost_usd": 13000},
        {"flight_id": "EK612", "date": "2025-07-03", "fuel_liters": 24000, "fuel_cost_usd": 19000},
        {"flight_id": "QR620", "date": "2025-07-03", "fuel_liters": 21000, "fuel_cost_usd": 17500},
    ],
    "employee_stats": [
        {"employee_id": "E101", "role": "Pilot", "hours_flown": 85, "rating": 4.8},
        {"employee_id": "E102", "role": "Technician", "hours_worked": 160, "rating": 4.2},
        {"employee_id": "E103", "role": "Ground Staff", "hours_worked": 170, "rating": 3.9},
        # Add more roles/stats
    ],
    "weather_conditions": [
        {"date": "2024-06-01", "visibility_km": 8.5, "temperature_c": 35, "wind_kph": 18},
        {"date": "2024-06-02", "visibility_km": 6.2, "temperature_c": 38, "wind_kph": 22},
        {"date": "2024-06-03", "visibility_km": 9.1, "temperature_c": 33, "wind_kph": 15},
        # Add for more days
    ]
}

# ✅ Initial Task 1: Flights Overview
# Convert the flights data into a DataFrame.
flights_data = pd.DataFrame(airport_data["flights"])
number_of_flights = flights_data["airline"].value_counts()
# Count the number of flights by airline.
# Plot a bar chart: Airlines vs. Number of Flights.
plt.bar(number_of_flights.index,number_of_flights.values,color='skyblue')
plt.title("Airlines vs Number of Flights")
plt.xlabel("Airlines")
plt.ylabel("Number of Flights")
plt.grid(axis='y')
plt.show()
# Plot a pie chart showing status distribution (On Time, Delayed, etc.).
flights_on_time = flights_data[flights_data["status"] == "On Time"]["status"].count()
flights_delayed = flights_data[flights_data["status"] == "Delayed"]["status"].count()
flights_status = np.array([flights_on_time,flights_delayed])
plt.pie(flights_status,startangle=90,labels=["On Time","Delayed"],explode=[0,0.1],shadow=True)
plt.title("Flights On Time vs Flights Delayed",color='Green')
plt.show()

# ✅ Task 2: Passenger Flow Analysis
# Now we’ll explore the passenger_stats section.
# Your Goals:
# Convert the passenger_stats list to a DataFrame.
passenger_data = pd.DataFrame(airport_data["passenger_stats"])
# Create a new column total_passengers = domestic + international.
passenger_data["Total_Passengers"]= passenger_data["domestic"] + passenger_data["international"]
# Plot a line chart:
plt.plot(passenger_data["date"],passenger_data["Total_Passengers"],marker = 'o')
plt.title("Number of Passengers on each Date.")
plt.xlabel("Date")
plt.ylabel("Total Passengers")
plt.grid()
plt.show()
# Plot a stacked bar chart showing:
# domestic and international passengers per day.
plt.bar(passenger_data["date"],passenger_data["domestic"],color = 'orange',label  ='Domestic')
plt.bar(passenger_data["date"],passenger_data["international"],color = 'skyblue',label = "International")
plt.legend()
plt.title("Domestic and International passengers per day.")
plt.xlabel("Date")
plt.grid(axis='y')
plt.show()
# Optional Bonus:
# Calculate and print:
# Average domestic passengers
avg_domestic_passengers = int(passenger_data["domestic"].mean())
print(f"\nAverage Domestic Passengers are : {avg_domestic_passengers}")
# Day with the highest total passengers
highest_passengers = passenger_data["Total_Passengers"].max()
highest_passengers_day = passenger_data.loc[passenger_data["Total_Passengers"] == highest_passengers, 'date'].values[0]
print(f"\nDay with the highest total passengers is : {highest_passengers_day}")

# ✅ Task 3: Baggage Handling Insights
# Now we'll work with the "baggage_handling" data.
# Your Goals:
# Convert the baggage_handling list into a DataFrame.
baggages_data = pd.DataFrame(airport_data["baggage_handling"])
# Add a new column total_baggage = checked_in + lost + delayed.
total_baggages = baggages_data["checked_in"] + baggages_data["delayed"] + baggages_data["lost"]
baggages_data["Total_Baggages"] = total_baggages
# Plot a bar chart:
sns.barplot(data=baggages_data,x="date",y=total_baggages,legend=False,hue="date",palette='Greys')
plt.title("Total Baggages across flights per day")
plt.xlabel("Date")
plt.ylabel("Total_Baggages")
plt.grid(axis='y')
plt.show()
# Plot a stacked bar chart:
sns.barplot(data=baggages_data,x="date",y="checked_in",label="Checked_In",color='skyblue')
sns.barplot(data=baggages_data,x="date",y="lost",label="Lost",color='red')
sns.barplot(data=baggages_data,x="date",y="delayed",label="Delayed",color='lightpink')
plt.title("Baggages Data per Day")
plt.xlabel("Date")
plt.ylabel("Baggages")
plt.grid(axis='y')
plt.legend()
plt.show()
# Optional Bonus:
# Highlight the day with the most delayed baggage.
grouped_delayed_baggages = baggages_data.groupby("date")["delayed"].sum().reset_index()
max_delayed_baggage = grouped_delayed_baggages["delayed"].max()
max_delayed_baggage_date = grouped_delayed_baggages.loc[grouped_delayed_baggages["delayed"] == max_delayed_baggage,'date'].values[0]
print(f"\nDay with the most delayed baggage : {max_delayed_baggage_date}")
# Calculate and print total lost baggage over all days.
total_lost_baggage = grouped_delayed_baggages["delayed"].sum()
print(f"\nTotal lost baggage over all days : {total_lost_baggage}")


# ✅ Task 4: Load and Explore the Data
# Load the "fuel_consumption" list into a Pandas DataFrame.
fuel_consumption_data = pd.DataFrame(airport_data["fuel_consumption"])
# Convert "date" to datetime type.
# fuel_consumption_data["date"]=pd.to_datetime(fuel_consumption_data["date"])
# Print basic stats: total entries, unique flights, date range.



# Add a column called cost_per_liter:
fuel_consumption_data["Cost_per_litre_USD"] = (fuel_consumption_data["fuel_cost_usd"]/fuel_consumption_data["fuel_liters"]).round(2)

# Daily Fuel Usage Visualization
# Plot a line chart showing fuel consumption per day for each flight.
sns.lineplot(data=fuel_consumption_data,x=fuel_consumption_data["date"],y=fuel_consumption_data["fuel_liters"],marker= 'o',color='red',hue="flight_id")
plt.title("Fuel Consumption per day for each Flight")
plt.grid()
plt.show()

# Fuel Cost per Flight (Bar Plot):
# Group by flight_id and sum fuel_cost_usd.
grouped_id_fuel_cost = fuel_consumption_data.groupby(["flight_id","date"])["fuel_cost_usd"].sum().reset_index()
# Create a bar chart to show total fuel cost for each flight.
sns.barplot(data=grouped_id_fuel_cost,x="flight_id",y="fuel_cost_usd",palette='coolwarm',legend=False,hue="flight_id")
plt.title("Fuel cost per flight")
plt.grid(axis='y')
plt.show()

# Identify Extremes (Text + Plot)
# Which flight had the highest total fuel consumption?
highest_fuel_consumtion = grouped_id_fuel_cost["fuel_cost_usd"].max()
highest_fuel_consumtion_flight_ID = grouped_id_fuel_cost.loc[grouped_id_fuel_cost["fuel_cost_usd"] == highest_fuel_consumtion,'flight_id'].values[0]
print(f"\nFlight which had the highest total fuel consumption is : {highest_fuel_consumtion_flight_ID}")
# Which date had the most fuel used overall?
highest_fuel_consumtion_date = grouped_id_fuel_cost.loc[grouped_id_fuel_cost["fuel_cost_usd"] == highest_fuel_consumtion,'date'].values[0]
print(f"\nDate which had the most fuel used overall : {highest_fuel_consumtion_date}")
# Which flight is the most expensive per liter on average?
grouped_id_avg_fuel_cost = fuel_consumption_data.groupby("flight_id")["Cost_per_litre_USD"].mean().round(2).reset_index()
avg_max_cost_perlitre = grouped_id_avg_fuel_cost["Cost_per_litre_USD"].max()
expensive_flight_ID = grouped_id_avg_fuel_cost.loc[grouped_id_avg_fuel_cost["Cost_per_litre_USD"] == avg_max_cost_perlitre,'flight_id'].values[0]
print(f"\nFlight which is the most expensive per liter on average : {expensive_flight_ID}")

# ✅ Bonus Task (Optional)
# Create a scatter plot:
# Helps visualize whether higher fuel usage always means higher cost.
sns.scatterplot(data=fuel_consumption_data,x="fuel_liters",y="fuel_cost_usd",s=100,hue="flight_id")
plt.title("Fuel usage per cost")
plt.grid()
plt.show()
print("\n\nPress any key to exit...")
msvcrt.getch()