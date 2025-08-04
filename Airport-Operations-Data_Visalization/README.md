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
<img width="478" height="409" alt="image" src="https://github.com/user-attachments/assets/eec8b000-9a02-4b77-a37c-95f4838869cc" />
* Pie chart of flight statuses
<img width="479" height="403" alt="image" src="https://github.com/user-attachments/assets/79b47784-4d05-4996-b5c3-e9736c33de64" />
* Passenger traffic line chart
<img width="478" height="404" alt="image" src="https://github.com/user-attachments/assets/241213bd-3e2b-4bd7-8250-e86f0e3484f8" />
* Domestic and International Passengers Stacked Bar chart
<img width="477" height="408" alt="image" src="https://github.com/user-attachments/assets/ae8bb616-c7e0-4c8b-b6a1-840f073bb149" />
* Total Baggage across Flights
<img width="476" height="407" alt="image" src="https://github.com/user-attachments/assets/ab4b0e15-9e76-4ee0-84fa-ca1f8c804b2c" />
* Baggage delay bar and stacked visualizations
<img width="477" height="407" alt="image" src="https://github.com/user-attachments/assets/ce9cedc2-7769-47b2-994d-6206b5a66ab4" />
* Fuel usage trends and cost analysis plots
<img width="476" height="407" alt="image" src="https://github.com/user-attachments/assets/5113683b-9cf6-4f61-aa27-e1b14dad56e5" />
<img width="476" height="406" alt="image" src="https://github.com/user-attachments/assets/6fa2c3f9-70c6-4547-8671-6c34b8c2b3ed" />
<img width="476" height="403" alt="image" src="https://github.com/user-attachments/assets/ff1a04f5-58b7-44d1-9d2a-9bdb99de0fb7" />

---

### ✅ To Do

* Integrate weather and employee stats into analysis
* Add more real-world variability or connect to live/CSV datasets
* Export visualizations to files




