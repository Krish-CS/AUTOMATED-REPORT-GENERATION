# AUTOMATED-REPORT-GENERATION

**"COMPANY":** CODTECH IT SOLUTIONS

**"NAME":** KRISHKANTH K

**"INTERN ID":** CT08TUV

**"DOMAIN":** PYTHON PROGRAMMING

**"DURATION":** 4 WEEKS

**"MENTOR":** NEELA SANTHOSH KUMAR

**Automated Report Generation**

**Overview**

This project is a Python script that automates the process of reading a CSV file, analyzing its data, generating statistical summaries, creating visualizations, and compiling everything into a formatted PDF report.

**Features**

Reads data from a CSV file.

Performs statistical analysis (mean, median, standard deviation, etc.).

Generates histograms for numerical columns.

Creates a formatted PDF report with analysis and visualizations.

Automatically clears old reports and plots before generating new ones.

**Requirements**

Ensure you have the following Python libraries installed:

pip install pandas matplotlib fpdf

**Usage**

Place your dataset as data.csv in the same directory.

Run the script:

python automated_report.py

The generated report will be saved as report.pdf in the same directory.

**File Structure**

├── automated_report.py  # Main script
├── data.csv             # Input data file
├── report.pdf           # Generated PDF report
├── plots/               # Directory containing generated plots
└── README.md            # Documentation

**Customization**

Modify file_path in main() to specify a different input file.

Adjust the visualization settings in generate_plots() if needed.

**OUTPUT**
