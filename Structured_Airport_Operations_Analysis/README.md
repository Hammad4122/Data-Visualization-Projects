# 🛫 Airport Data Visualization Project

This project performs **data analysis and visualization** on airport operational datasets.  
It uses **Python**, **Pandas**, **Matplotlib**, and **Seaborn** to explore and visualize different aspects of airport operations, including flight status, passenger trends, fuel consumption, baggage handling, and weather impact.

---

## 📌 Features

- **Data Loading**: Reads JSON files containing multiple datasets:
  - Flights
  - Passenger statistics
  - Baggage handling
  - Fuel consumption
  - Employee stats
  - Weather conditions
- **Data Cleaning**: Removes duplicate rows and resets indices.
- **Analysis Functions**:
  - Count on-time vs delayed flights.
  - Calculate average domestic & international passengers per day.
  - Compute total fuel cost per airline.
  - Correlate weather conditions with passenger numbers.
  - Compare fuel consumption to lost baggage.
- **Visualizations**:
  - Bar charts for flight status and baggage handling.
  - Line charts for passenger trends and fuel consumption.
  - scatterplots for deeper insights.

---

## 📂 Project Structure

Data_Visualization_Projects/\n
│
├── assets/
│ ├── airport_data.json # Airport dataset in JSON format
│ ├── airport_data_all.csv # (Optional) Combined dataset in CSV format
│
├── scripts/
│ ├── main.py # Main entry point for analysis
│
├── README.md # Project documentation


---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Hammad4122/Data-Visualization-Projects.git
   cd Data-Visualization-Projects
   
2. Install dependencies:
    pip install pandas matplotlib seaborn
   
3. 🚀 Usage
Run the main script:
python scripts/main.py

The script will:
  1. Load and clean the datasets.
  2. Perform statistical analysis.
  3. Display multiple visualizations in sequence.
---

.

## 📊 Example Visualizations
The project generates:

• Flight Status: Bar chart of on-time vs delayed flights.
  <img width="475" height="407" alt="image" src="https://github.com/user-attachments/assets/47d2ee44-3dba-408e-b303-0c337b59435f" />

• Passenger Trends: Line chart comparing domestic & international passengers over time.
  <img width="906" height="457" alt="image" src="https://github.com/user-attachments/assets/d55d0c8f-4e41-435c-9cf4-5b034ba48c84" />

• Fuel Consumption: Multi-line chart showing per-flight fuel usage.
  <img width="912" height="451" alt="image" src="https://github.com/user-attachments/assets/1d2fc432-b489-4653-8620-c3c612d01337" />

• Baggage Handling: Efficiency comparisons and lost baggage distribution.
  <img width="875" height="449" alt="image" src="https://github.com/user-attachments/assets/08c36417-87d1-42d3-99a4-650e29b8adc8" />
  <img width="473" height="382" alt="image" src="https://github.com/user-attachments/assets/37d42bec-fd3a-4567-a0da-c9e095974049" />

• Weather Correlation: Scatterplot of visibility vs passenger counts.
  <img width="474" height="379" alt="image" src="https://github.com/user-attachments/assets/51693363-1a8a-4742-aa4f-2e16b2a9172c" />

• Advanced Analysis: Fuel usage vs lost baggage relationship.
  <img width="473" height="385" alt="image" src="https://github.com/user-attachments/assets/d42bffb3-c029-4178-a2af-6a90619711da" />

---

⚠ Notes
• Ensure your airport_data.json file is in the correct assets/ directory.

• The script is written to work with the dataset's existing column names; modifying the dataset structure may require code changes.

---

📌 Requirements
• Python 3.7+
• pandas
• matplotlib
• seaborn
