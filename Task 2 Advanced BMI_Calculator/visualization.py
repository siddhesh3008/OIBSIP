import matplotlib.pyplot as plt
import pandas as pd
from database import fetch_bmi_records

def plot_bmi_trend():
    # Fetch records from the database
    records = fetch_bmi_records()

    # Check if there are any records
    if not records:
        plt.figure(figsize=(6, 4))
        plt.text(0.5, 0.5, 'No Data Available for Visualization', 
                 horizontalalignment='center', 
                 verticalalignment='center', 
                 fontsize=12, 
                 color='red')
        plt.axis('off')
        plt.show()
        return

    # Convert records to a DataFrame for processing
    data = pd.DataFrame(records, columns=['ID', 'Name', 'Height', 'Weight', 'BMI', 'Category', 'Date'])

    # Convert Date to datetime and set as index
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Check if there are valid entries for plotting
    if data.empty or 'BMI' not in data.columns:
        plt.figure(figsize=(6, 4))
        plt.text(0.5, 0.5, 'No Valid BMI Data for Visualization', 
                 horizontalalignment='center', 
                 verticalalignment='center', 
                 fontsize=12, 
                 color='red')
        plt.axis('off')
        plt.show()
        return

    # Plot BMI trends for each user
    plt.figure(figsize=(10, 6))
    for name, group in data.groupby('Name'):
        if group['BMI'].notnull().any():
            plt.plot(group.index, group['BMI'], marker='o', label=name)

    # Add title, labels, legend, and grid
    plt.title("BMI Trend Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("BMI", fontsize=12)
    plt.legend(title='User', loc='upper left', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()

