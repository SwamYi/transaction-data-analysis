# transaction-data-analysis
Analyzing bakery transaction data for sales trends and insights

# Transaction Data Analysis for Bakery

## Overview

This project analyzes transaction data from a bakery to identify popular items, sales trends, and customer behavior. The goal is to clean the data, perform analysis, and visualize trends in sales over time, most popular items, and how sales differ by day and time of day.

### **Objective**

The objective of this project is to perform data cleaning, analyze the transaction dataset, and visualize insights that can help the bakery improve sales strategies, inventory management, and customer engagement.

---

## Data Description

The dataset contains transaction records with the following columns:

- **TransactionNo**: Unique identifier for each transaction.
- **Items**: The item purchased by the customer.
- **DateTime**: The date and time of the transaction.
- **DayPart**: The part of the day during which the transaction occurred (Morning, Afternoon, etc.).
- **DayType**: The type of the day (Weekday or Weekend).

### Example Data:

| TransactionNo | Items      | DateTime             | DayPart   | DayType  |
|---------------|------------|----------------------|-----------|----------|
| 1             | Bread      | 10/30/2016 10:00 AM  | Morning   | Weekend  |
| 2             | Coffee     | 10/30/2016 10:05 AM  | Morning   | Weekend  |
| 3             | Scandinavian | 10/30/2016 10:10 AM | Morning   | Weekend  |

---

## Data Cleaning

The raw transaction data underwent the following cleaning steps:

1. **Removing Duplicate Rows**: Duplicate rows where `TransactionNo`, `Items`, and `DateTime` were identical were removed to ensure each transaction is unique.
   
2. **Handling Missing Data**: After inspecting the dataset, no missing data was found.

3. **Data Transformation**: Several new columns were created to help with analysis:
   - **DayType_fixed**: Categorized the days into "Monday to Sunday" based on the original `DayType`.
   - **DayPart_fixed**: Categorized the time into "Morning to Night" based on the `DayPart` column.

---

## Analysis

### Key Insights

- **Popular Items**: The most popular items are identified based on transaction frequency.
  - Coffee and bread are the top-selling items.
  
- **Sales Trends**: The analysis shows a clear trend of increased sales during weekends and mornings, with peak sales on Saturday mornings.

### Visualizations

The following visualizations were created to help better understand the data:

1. **Bar Chart**: Sales by `DayType` (Weekend vs. Weekday).
   - This chart shows the distribution of sales across weekdays and weekends.

2. **Pie Chart**: Most popular items based on frequency of occurrence in transactions.
   - This chart visualizes which items are sold the most.

3. **Line Chart**: Sales trends over time (e.g., hourly, daily).
   - This chart shows how sales change throughout the day and week.

---

## Tools Used

- **Python**: Used for data cleaning and transformation.
- **Power BI**: Used for data visualization, creating interactive dashboards.
- **Pandas**: Used for handling and processing the data in Python.

---

## Conclusion

The analysis revealed valuable insights that can help the bakery improve its sales strategies:
- **Focus on weekends and mornings**: These are the peak times for sales.
- **Promote popular items**: Coffee and bread are the most popular and highest-selling items.

### **Next Steps**
- Further analyze sales data across different seasons and holidays.
- Expand analysis to include customer demographics, if available.

---

## Repository

You can access the full code, analysis, and visualizations in this repository.

- Python code for data cleaning: [Python Script](./data_cleaning.py)
- Power BI report file: [Transaction Report (PBIX)](./transaction_report.pbix)
- Project explanation and insights: [README.md](./README.md)

Feel free to explore, contribute, or use this project as a reference!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
