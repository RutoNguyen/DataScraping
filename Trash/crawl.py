from bs4 import BeautifulSoup
import requests
import selenium

def GetStockType(soup):
    StockType = soup.find("div",class_ ="filter-line")
    #start =StockType.find("()")
    checked_input = StockType.find('input', {'checked': 'checked'})

    if checked_input:
        value = checked_input.find_next('label')
        print(f'The value of the checked input is: {value}')
    else:
        print('No input with checked="checked" found.')
    return value.text
def GetData(soup):
#     #table_id = soup.find('table', {'id': 'volumeGrid-grid'})
#     table_class = soup.find('div',class_="fegrid")
#     #print(table_class)
#     # if table_class:
#     #     # Tìm tất cả các dòng (tr) trong bảng
#     #     rows = table_class.find_all('tr')
#     #     # In thông tin từ mỗi dòng
#     #     for row in rows:
#     #         # Tìm tất cả các ô (td) trong dòng
#     #         cells = row.find_all(['th', 'td'])

#     #         # In nội dung từng ô
#     #         for cell in cells:
#     #             print(cell.text, end='\t')
#     #         print()  # Xuống dòng giữa các dòng
#     # else:
#     #     print('Table with class "fieldset" not found.')
# # Tìm thẻ input có name="chs"
#     input_chs = table_class.find('input', {'name': 'chs'})
#     if input_chs:
#         # Lấy giá trị của thuộc tính value
#         value = input_chs.get('value')

#         # Xử lý giá trị để lấy 'Toàn thị trường'
#         all_market = value.split("','")[2]
#         print(f"The value of 'Toàn thị trường' is: {all_market}")
#     else:
#         print("Input with name='chs' not found.")
#     return all_market

 # Get Data
    data_div = soup.find('div', class_='fegrid')
    if data_div:
        print("Found div with class 'fegrid'")
        
        table_id = data_div.find('table', {'id': 'volumeGrid-grid'})
        if table_id:
            print("Found table with id 'volumeGrid-grid'")
            print(table_id)
        else:
            print('Table with id "volumeGrid-grid" not found inside the "fegrid" div.')
    else:
        print('Div with class "fegrid" not found.')

def GetPageContent(url):
    page = requests.get(url,headers={"Acept-Language":"en-US"})
    return BeautifulSoup(page.text,"html.parser")
def CrawData():
    url = 'https://www.hsx.vn/Modules/Rsde/Report/ForeignTradingReportIndex?fid=4eade9cd9f9b%20472ebdc235a0d4a6407e'
    soup = GetPageContent(url)
    ### Stock Type
    StockType = GetStockType(soup)
    print(StockType)
    ### Get Data
    '''
    - Trading Vol of Total Market (Khối lượng toàn thị trường)
    - Trading Val of Total Market (Giá Trị Giao dịch toàn thị trường)
    '''
    #Data = GetData(soup)
    #print(Data)
CrawData()