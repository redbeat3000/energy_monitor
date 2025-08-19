import sqlite3
import random
from datetime import datetime
import matplotlib.pyplot as plt
from fpdf import FPDF
from tabulate import tabulate
import time

# -----------------------------
# Database setup
# -----------------------------
conn = sqlite3.connect("energy_usage.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usage
             (id INTEGER PRIMARY KEY, timestamp TEXT, appliance TEXT, power REAL)''')
conn.commit()

# -----------------------------
# Simulate appliances
# -----------------------------
appliances = ["Fridge", "AC", "Washing Machine", "TV", "Computer"]

def simulate_usage():
    for appliance in appliances:
        power = round(random.uniform(50, 500), 2)  # watts
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO usage (timestamp, appliance, power) VALUES (?, ?, ?)",
                  (timestamp, appliance, power))
    conn.commit()

# -----------------------------
# Generate daily report
# -----------------------------
def generate_report():
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute("SELECT appliance, SUM(power) FROM usage WHERE timestamp LIKE ? GROUP BY appliance", (f"{today}%",))
    data = c.fetchall()
    
    if not data:
        print("No data for today.")
        return
    
    # Display table
    print("\n--- Today's Energy Usage ---")
    print(tabulate(data, headers=["Appliance", "Total Power (W)"]))
    
    # Pie chart
    appliances_list, power_list = zip(*data)
    plt.figure(figsize=(6,6))
    plt.pie(power_list, labels=appliances_list, autopct='%1.1f%%')
    plt.title(f"Energy Usage Breakdown for {today}")
    chart_file = f"{today}_energy.png"
    plt.savefig(chart_file)
    plt.close()
    
    # Export PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Smart Home Energy Report - {today}", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Energy Usage by Appliance:", ln=True)
    pdf.set_font("Arial", '', 12)
    for appliance, power in data:
        pdf.cell(0, 10, f"{appliance}: {power} W", ln=True)
    
    pdf.image(chart_file, x=30, y=80, w=150)
    pdf.output(f"{today}_energy_report.pdf")
    print(f"\nPDF report exported: {today}_energy_report.pdf")

# -----------------------------
# Main Program
# -----------------------------
def main():
    print("=== Smart Home Energy Monitor ===")
    try:
        while True:
            simulate_usage()
            print("Simulated appliance usage logged.")
            time.sleep(10)  # simulate every 10 seconds; adjust as needed
    except KeyboardInterrupt:
        print("\nSimulation stopped. Generating report...")
        generate_report()

if __name__ == "__main__":
    main()
