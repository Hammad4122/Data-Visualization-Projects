## ✈️ Airport Operations Data Analysis

This project analyzes and visualizes key operational metrics from an airport’s daily records. It leverages **Pandas**, **Matplotlib**, and **Seaborn** to extract insights from structured datasets related to flights, passengers, baggage handling, and fuel consumption.

---

### 📊 Features

The script processes synthetic airport data to provide:

* **Flight Operations**

  * Airline frequency counts
  * Flight status distribution (On Time vs Delayed)

* **Passenger Statistics**

  * Daily domestic and international passenger traffic
  * Line and stacked bar charts
  * Peak traffic day detection

* **Baggage Handling Insights**

  * Total baggage per flight and per day
  * Breakdown of checked-in, delayed, and lost bags
  * Highlights most delayed baggage day and total lost baggage

* **Fuel Consumption Analysis**

  * Fuel usage trends per flight
  * Cost efficiency (cost per liter)
  * Most fuel-consuming flights and expensive routes

---

### 📁 Data Sources

All data is internally defined using a nested Python dictionary with the following sections:

* `flights`
* `passenger_stats`
* `baggage_handling`
* `fuel_consumption`
* `employee_stats` *(defined but unused)*
* `weather_conditions` *(defined but unused)*

---

### 🛠 Technologies Used

* Python 3.x
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* `msvcrt` (for Windows-based keypress handling)

---

### 📌 How to Run

1. Ensure you have Python installed with the required libraries:

   ```bash
   pip install pandas matplotlib seaborn
   ```

2. Run the script:

   ```bash
   python airport_analysis.py
   ```

3. Follow the terminal output and view the generated charts.

---

### 📈 Sample Outputs

* Airline flight frequency bar chart
* Pie chart of flight statuses
* Passenger traffic line chart
* Baggage delay bar and stacked visualizations
* Fuel usage trends and cost analysis plots

---

### ✅ To Do

* Integrate weather and employee stats into analysis
* Add more real-world variability or connect to live/CSV datasets
* Export visualizations to files

### Graphs
<img width="478" height="409" alt="image" src="https://github.com/user-attachments/assets/eec8b000-9a02-4b77-a37c-95f4838869cc" />

