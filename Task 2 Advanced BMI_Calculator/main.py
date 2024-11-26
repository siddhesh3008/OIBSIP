import tkinter as tk
from tkinter import messagebox
from database import create_database, save_bmi_record, fetch_bmi_records, delete_bmi_record
import visualization

def calculate_bmi():
    try:
        name = entry_name.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            raise ValueError("Height and Weight must be positive numbers.")

        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi} ({category})")
        save_bmi_record(name, height, weight, bmi, category)
        messagebox.showinfo("Success", "BMI record saved successfully!")

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

def view_history():
    records = fetch_bmi_records()
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    
    tk.Label(history_window, text="ID").grid(row=0, column=0)
    tk.Label(history_window, text="Name").grid(row=0, column=1)
    tk.Label(history_window, text="Height").grid(row=0, column=2)
    tk.Label(history_window, text="Weight").grid(row=0, column=3)
    tk.Label(history_window, text="BMI").grid(row=0, column=4)
    tk.Label(history_window, text="Category").grid(row=0, column=5)
    tk.Label(history_window, text="Date").grid(row=0, column=6)
    tk.Label(history_window, text="Action").grid(row=0, column=7)

    for idx, record in enumerate(records, start=1):
        for col, value in enumerate(record):
            tk.Label(history_window, text=value).grid(row=idx, column=col)
        
        delete_button = tk.Button(
            history_window, 
            text="Delete", 
            command=lambda r_id=record[0]: delete_record_and_refresh(r_id, history_window)
        )
        delete_button.grid(row=idx, column=7)

def delete_record_and_refresh(record_id, window):
    delete_bmi_record(record_id)
    messagebox.showinfo("Success", "Record deleted successfully!")
    window.destroy()  # Close the current history window
    view_history()  # Reopen it to reflect updated data

def show_trend():
    visualization.plot_bmi_trend()

# Initialize database
create_database()

# Main GUI
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Height (m):").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

tk.Label(root, text="Weight (kg):").grid(row=2, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=2, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="View History", command=view_history).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Show BMI Trend", command=show_trend).grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
