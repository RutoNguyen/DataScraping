from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
#from webdriver_manager.chrome import ChromeDriverManager
# Khởi tạo trình duyệt Selenium
chrome_service = ChromeService()
driver = webdriver.Chrome(service=chrome_service)
# driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())

# Mở trang web
url = 'https://www.hsx.vn/Modules/Rsde/Report/ForeignTradingReportIndex?fid=4eade9cd9f9b%20472ebdc235a0d4a6407e'
params ={
    'pageFieldValue2': '01.01.2021',
    'pageFieldValue3': '30.11.2023'
}

driver.get(url)
# Đợi cho trang web tải toàn bộ
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_element_located((By.ID, 'volumeGrid-grid')))

# Lấy mã nguồn HTML của trang web đã tải
html_source = driver.page_source
# Tạo đối tượng BeautifulSoup từ mã nguồn HTML
soup = BeautifulSoup(html_source, 'html.parser')

# Tìm div có class 'fegrid'
data_div = soup.find('div', class_='fegrid')
if data_div:
    print("Found div with class 'fegrid'")
    # Tìm table có id 'volumeGrid-grid'
    table_id = data_div.find('table', {'id': 'volumeGrid-grid'})
    if table_id:
        print("Found table with id 'volumeGrid-grid'")
        # Tìm tất cả các dòng trong tbody
        #rows = table_id.find('tbody').find_all('tr')
        rows = table_id.find('tbody').find('tr',{'id':'Mua'})
        print(rows)
        # # Lặp qua từng dòng và in dữ liệu
        # for row in rows:
        #     # Tìm tất cả các ô trong dòng
        #     cells = row.find_all('td')
            
        #     # # Lặp qua từng ô và in nội dung
        #     # for cell in cells:
        #     #     print(cell.get_text(), end='\t')
            
        #     # # Xuống dòng sau mỗi dòng
        #     # print()
        #     # Lấy giá trị ở vị trí mong muốn
        #     target_value = cells[2].get_text()  # Giả sử giá trị ở vị trí 2 (cột thứ 3)
            
        #     # In giá trị
        #     print(target_value)
        ###
        if rows:
            cells = rows.find_all('td')
            target_value = cells[2].get_text()  # giá trị ở vị trí 2 (cột thứ 3)
            print(target_value)
    else:
        print('Table with id "volumeGrid-grid" not found inside the "fegrid" div.')
else:
    print('Div with class "fegrid" not found.')

# Đóng trình duyệt sau khi đã hoàn thành
driver.quit()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# #from webdriver_manager.chrome import ChromeDriverManager
# # Khởi tạo trình duyệt Selenium
# chrome_service = ChromeService()
# driver = webdriver.Chrome(service=chrome_service)
# # driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())

# # Mở trang web
# url = 'https://www.hsx.vn/Modules/Rsde/Report/ForeignTradingReportIndex?fid=4eade9cd9f9b%20472ebdc235a0d4a6407e'
# params ={
#     'pageFieldValue2': '01.01.2021',
#     'pageFieldValue3': '30.11.2023'
# }
# driver.get(url)
# # # Đợi cho trang web tải toàn bộ

# # wait = WebDriverWait(driver, 10)
# # wait.until(EC.presence_of_element_located((By.ID, 'volumeGrid-grid')))
# # #wait.until(lambda driver: driver.execute_script("return document.getElementById('volumeGrid-grid') !== null;"))
# # wait.until(EC.presence_of_element_located((By.ID, 'valueGrid-grid')))
# # #wait.until(lambda driver: driver.execute_script("return document.getElementById('valueGrid-grid') !== null;"))

# # wait.until(EC.presence_of_element_located((By.ID, 'foreignTrading')))
# # #wait.until(lambda driver: driver.execute_script("return document.getElementById('foreignTrading') !== null;"))
# ##########
# def element_has_class(driver, element, class_name):
#     try:
#         # Kiểm tra xem phần tử có class_name không
#         return class_name in element.get_attribute("class")
#     except Exception as e:
#         return False

# # Đợi cho phần tử có ID là 'volumeGrid-grid' xuất hiện và có class 'ui-jqgrid-btable'
# wait = WebDriverWait(driver, 60)
# volumeGrid_grid = wait.until(
#     EC.presence_of_element_located((By.ID, 'volumeGrid-grid'))
# )

# # Đợi cho phần tử có ID là 'volumeGrid-grid' có class 'ui-jqgrid-btable'
# wait.until(
#     lambda driver: element_has_class(driver, volumeGrid_grid, 'ui-jqgrid-btable'),
#     "Timed out waiting for element to have class 'ui-jqgrid-btable'"
# )
# ##########################################
# #Đợi cho phần tử có ID là 'valueGrid-grid' xuất hiện và có class 'ui-jqgrid-btable'
# wait = WebDriverWait(driver, 60)
# valueGrid_grid = wait.until(
#     EC.presence_of_element_located((By.ID, 'valueGrid-grid'))
# )
# # Đợi cho phần tử có ID là 'valueGrid-grid' có class 'ui-jqgrid-btable'
# wait.until(
#     lambda driver: element_has_class(driver, valueGrid_grid, 'ui-jqgrid-btable'),
#     "Timed out waiting for element to have class 'ui-jqgrid-btable'"
# )
# ##########
# ###########
# # Lấy mã nguồn HTML của trang web đã tải
# html_source = driver.page_source
# # Tạo đối tượng BeautifulSoup từ mã nguồn HTML
# soup = BeautifulSoup(html_source, 'html.parser')
# table_KLGD = soup.find('table', {'id': 'volumeGrid-grid'})
# if table_KLGD:
#         # Tìm tất cả các dòng trong tbody
#         #rows = table_id.find('tbody').find_all('tr')
#         # Tìm tất cả các dòng trong tbody sau đó tìm tr có id là 'Mua'
#         rows = table_KLGD.find('tbody').find('tr',{'id':'Mua'})
#         if rows:
#             cells = rows.find_all('td')
#             target_value = cells[2].get_text()  # giá trị ở vị trí 2 (cột thứ 3)
#             print(target_value)
#         else:
#             print('The data has not finished loading volumeGrid-grid !!!')
# else:
#     print('Table with id "volumeGrid-grid" not found inside the "fegrid" div.')
# #########
# table_GTGD =soup.find('table',{'id':'valueGrid-grid'})
# if table_GTGD:
#         # Tìm tất cả các dòng trong tbody
#         #rows = table_id.find('tbody').find_all('tr')
#         # Tìm tất cả các dòng trong tbody sau đó tìm tr có id là 'Mua'
#         rows = table_GTGD.find('tbody').find('tr',{'id':'Mua'})
#         if rows:
#             cells = rows.find_all('td')
#             target_value = cells[2].get_text()  # giá trị ở vị trí 2 (cột thứ 3)
#             print(target_value)
#         else:
#             print('The data has not finished loading valueGrid-grid !!!')
# else:
#     print('Table with id "valueGrid-grid" not found inside the "fegrid" div.')

# # Đóng trình duyệt sau khi đã hoàn thành
# driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


chrome_service = ChromeService()
driver = webdriver.Chrome(service=chrome_service)

url = 'https://www.hsx.vn/Modules/Rsde/Report/ForeignTradingReportIndex?fid=4eade9cd9f9b%20472ebdc235a0d4a6407e'
params ={
    'pageFieldValue2': '01.01.2021',
    'pageFieldValue3': '30.11.2023'
}
def GetStockType(soup):
    StockType = soup.find("div",class_ ="filter-line")
    #start =StockType.find("()")
    checked_input = StockType.find('input', {'checked': 'checked'})

    if checked_input:
        value = checked_input.find_next('label')
    #     print(f'The value of the checked input is: {value}')
    # else:
    #     print('No input with checked="checked" found.')
    return value.text
# def get_stock_type(driver):
#     try:
#         stock_type_element = driver.find_element(By.CSS_SELECTOR, '.filter-line input[checked="checked"] + label')
#         return stock_type_element.text
#     except:
#         print('Error getting stock type.')
#         return None
def is_data_loaded(driver):
    try:
        return EC.presence_of_element_located((By.ID, 'volumeGrid-grid'))(driver) and EC.presence_of_element_located((By.ID, 'valueGrid-grid'))(driver) and EC.presence_of_element_located((By.ID, 'foreignTrading'))(driver)
    except:
        return False

def get_table_data(table_id, row_id):
    table = driver.find_element(By.ID, table_id)
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        if row.get_attribute('id') == row_id:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                return cells[2].text  # giá trị ở vị trí 2 (cột thứ 3)
    return None

# Số lần thử làm mới trang
max_refresh_attempts = 10

for attempt in range(max_refresh_attempts):
    driver.get(url)
    
    time.sleep(0.5)
    # wait = WebDriverWait(driver, 10)
    # wait.until(is_data_loaded)
##
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    stock_type = GetStockType(soup)
    #print(soup.get_text())   
##
    target_value_KLGD = get_table_data('volumeGrid-grid', 'Mua')
    target_value_GTGD = get_table_data('valueGrid-grid', 'Mua')
    
    if target_value_KLGD and target_value_GTGD:
        ###
        print("Loại cổ phiếu:", stock_type)    
        ###
        print("VolumeGrid-grid:", target_value_KLGD)
        print("ValueGrid-grid:", target_value_GTGD)
        break  # Thoát khỏi vòng lặp nếu dữ liệu đã được lấy thành công
    else:
        print(f'Attempt {attempt + 1}: The data has not finished loading. Refreshing the page...')

# Đóng trình duyệt sau khi đã hoàn thành
driver.quit()


