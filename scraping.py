import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_data(start_month, start_year, end_month, end_year):
    url = "https://www.hsx.vn/Modules/Rsde/Report/ForeignTradingReportIndex?fid=4eade9cd9f9b472ebdc235a0d4a6407e"
    params = {
        'startMonth': start_month,
        'startYear': start_year,
        'endMonth': end_month,
        'endYear': end_year
    }
    # Initialize a Selenium WebDriver (make sure to have the appropriate driver installed)
    driver = webdriver.Chrome()

    try:
        # Open the URL
        driver.get(url)

        # Perform actions to select date range or any other necessary steps

        # Wait for the JavaScript to load and modify the DOM
        # You may need to add some explicit waits here based on the behavior of the website

        # Get the modified page source
        page_source = driver.page_source

        # Close the WebDriver
        driver.quit()

        # Use BeautifulSoup to parse the modified HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract data from the modified HTML
        f_div = soup.find('div', class_='fegrid')

        if f_div:
            rows = f_div.find_all('tr')
            
            # Extracted data
            data = []

            for row in rows:
                columns = row.find_all('td')
                row_data = [column.text.strip() for column in columns]
                data.append(row_data)

            # Save data to CSV file
            with open('trading_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                
                # Write header
                csv_writer.writerow(["Month-Year", "Trading Vol of Total Market", "Trading Val of Total Market", "Stock Type"])
                
                # Write data
                for row_data in data:
                    csv_writer.writerow(row_data)

            print("Data extracted and saved successfully to 'trading_data.csv'")
        else:
            print("Table not found.")

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()

# Example usage: Get data from January 2021 to November 2023
get_data(1, 2021, 11, 2023)