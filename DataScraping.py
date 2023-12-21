import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def format_date(date_string):
    # Chuyển đổi định dạng ngày tháng
    return date_string.replace('.', '-')
def format_trading_value(value_string):
    # Loại bỏ dấu chấm và chuyển đổi thành số
    return float(value_string.replace('.', '').replace(',', '.'))
def choose_stock_type(driver, stock_type_value):
    # Định vị phần tử input để chọn Stock Type
    input_element = driver.find_element(By.ID, stock_type_value)
    # Thực hiện thao tác chọn
    input_element.click()
def enter_date_range(driver, start_date, end_date):
    # Định vị phần tử input để nhập ngày tháng bắt đầu và kết thúc
    start_date_input = driver.find_element(By.ID, 'dateFrom')
    end_date_input = driver.find_element(By.ID, 'dateTo')

    # Xóa giá trị hiện tại trong input (nếu có)
    start_date_input.clear()
    end_date_input.clear()

    # Nhập ngày bắt đầu và kết thúc
    start_date_input.send_keys(start_date)
    end_date_input.send_keys(end_date)

    # Chờ 1 giây để đảm bảo dữ liệu được cập nhật
    time.sleep(1)
    # Gửi phím Enter để tải dữ liệu
    end_date_input.send_keys(Keys.ENTER)
    # Chờ cho dữ liệu được cập nhật
    time.sleep(2)
def get_stock_type(driver):
    try:
        # Sử dụng JavaScript để kiểm tra trạng thái checked
        script = 'return document.querySelector(".filter-line input.criteria:checked + label").innerText;'
        return driver.execute_script(script)
    except:
        print('Error getting stock type.')
        return None
def get_table_data(driver,table_id, row_id):
    table = driver.find_element(By.ID, table_id)
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        if row.get_attribute('id') == row_id:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                return cells[2].text  # giá trị ở vị trí 2 (cột thứ 3)
    return None
def main(driver,start_date,end_date,stock_type):
    url = 'https://www.hsx.vn/Modules/Rsde/Report/ForeignTradingReportIndex?fid=4eade9cd9f9b%20472ebdc235a0d4a6407e'
    # Truy cập URL
    driver.get(url)
    # Chọn loại chứng khoán (Stock Type) - ví dụ chọn Cổ phiếu (value = 2)
    choose_stock_type(driver,stock_type)

    # Nhập ngày tháng bắt đầu và kết thúc
    enter_date_range(driver, start_date, end_date)
    # Lấy dữ liệu
    name_stock_type = get_stock_type(driver)
    target_value_KLGD = get_table_data(driver,'volumeGrid-grid', 'Mua')
    target_value_GTGD = get_table_data(driver,'valueGrid-grid', 'Mua')

    # In thông tin
    if target_value_KLGD and target_value_GTGD:

        # xuất ra màn hình
        print("Month - Year:", start_date, "-", end_date)
        print("Trading Vol of Total Market:", target_value_KLGD)
        print("Trading Val of Total Market:", target_value_GTGD)
        print("Stock Type:", name_stock_type)

        ### Xuất dữ liệu ra file CSV ###
        # Định dạng dữ liệu trước khi xuất ra file CSV
        formatted_data = {
            "Date": format_date(f"{start_date} - {end_date}"),
            "Trading Vol of Total Market": format_trading_value(target_value_KLGD),
            "Trading Val of Total Market": format_trading_value(target_value_GTGD),
            "Stock Type": str(name_stock_type)
        }
        # Đường dẫn lưu file
        csv_file_path = "./Data/DataScraping.csv"
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["Date", "Trading Vol of Total Market", "Trading Val of Total Market", "Stock Type"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(formatted_data)
        print(f"Data has been exported to {csv_file_path}")
    else:
        print('Error getting data.')
    # Đóng trình duyệt sau khi đã hoàn thành
    driver.quit()
if __name__ == "__main__":
    # Driver
    chrome_service = ChromeService()
    driver = webdriver.Chrome(service=chrome_service)
    # Ngày bắt đầu và kết thúc
    start_date = '01.01.2021'
    end_date = '30.11.2023'
    # Loại chứng khoán
    stock_type = 'symbol' # Cổ phiếu
    #stock_type = 'bond' # Trái phiếu
    #stock_type = 'invcer' # Chứng chỉ quỹ
    #stock_type = 'etf' # ETF
    #stock_type = 'cw' # CW
    #stock_type = 'all' # Tất cả
    main(driver,start_date,end_date,stock_type)