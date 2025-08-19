# Smart Home Energy Monitor

Smart Home Energy Monitor is a Python-based tool that simulates monitoring of household energy consumption. It logs appliance usage, generates charts, and exports daily PDF reports. This project demonstrates skills in Python, data visualization, and IoT concepts, and is portfolio-ready.

---

## Features

- Simulates multiple home appliances (Fridge, AC, TV, etc.)  
- Logs energy usage in real-time to SQLite database  
- Generates daily reports with tables and pie charts  
- Exports reports as PDF files  
- Can be extended for real IoT devices or web dashboard  

---

## Prerequisites

- Ubuntu or Linux-based OS  
- Python 3  
- Required Python packages:
  - `sqlite3` (usually included with Python)  
  - `matplotlib`  
  - `fpdf`  
  - `tabulate`  

---

## Installation

1. Update your system and install dependencies:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install matplotlib fpdf tabulate

```
Download the project files (ensure energy_monitor.py is in your working directory).

Usage

Run the script:

```
python3 energy_monitor.py
```

The script will:

Simulate energy usage for multiple appliances every 10 seconds

Log data in energy_usage.db

Press Ctrl + C to stop the simulation and generate a daily PDF report

The PDF report includes:

Table of total energy used per appliance

Pie chart visualizing energy distribution

Saved in the working directory with the format YYYY-MM-DD_energy_report.pdf

Customization

Appliances: Modify the appliances list in the script

Simulation interval: Change time.sleep(10) to adjust logging frequency

PDF and chart styles: Customize fonts, colors, and layout in the script
---
License

## This project is released under the MIT License.

Author

## Blessing Nyaberi Hamisi
