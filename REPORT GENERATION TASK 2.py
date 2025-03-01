import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
import shutil

# Read data from CSV file
def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Analyze data
def analyze_data(df):
    summary = df.describe()  # Basic statistical summary
    return summary

# Generate visualizations
def generate_plots(df, output_dir):
    # Clear previous plots if the directory exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    for column in df.select_dtypes(include=['number']).columns:
        plt.figure()
        df[column].hist(bins=20, edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plot_path = os.path.join(output_dir, f"{column}.png")
        plt.savefig(plot_path)
        plt.close()
    return output_dir

# Generate PDF report
def generate_pdf(summary, output_file, plot_dir):
    # Ensure previous report is removed
    if os.path.exists(output_file):
        os.remove(output_file)
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Automated Data Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Statistical Summary:", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "", 10)
    
    # Add table with statistics
    for column in summary.columns:
        pdf.cell(0, 10, f"Column: {column}", ln=True, align='L')
        for index, value in summary[column].items():
            pdf.cell(0, 10, f"{index}: {value:.2f}", ln=True, align='L')
        pdf.ln(5)
    
    # Add visualizations
    for image_file in os.listdir(plot_dir):
        pdf.add_page()
        pdf.cell(200, 10, f"Visualization: {image_file.split('.')[0]}", ln=True)
        pdf.image(os.path.join(plot_dir, image_file), x=10, y=30, w=180)
        pdf.ln(100)
    
    pdf.output(output_file)

# Main function
def main():
    file_path = input("Enter the file path: ")
    output_file = "report.pdf"
    plot_dir = "plots"
    
    df = read_data(file_path)
    summary = analyze_data(df)
    plot_dir = generate_plots(df, plot_dir)
    generate_pdf(summary, output_file, plot_dir)
    print("Report generated successfully: report.pdf")

if __name__ == "__main__":
    main()
