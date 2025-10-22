import datetime
from utils import read_file

SALES_FILE = "sales.txt"

def report_daily_sales():
  sales = read_file(SALES_FILE)
  today = datetime.date.today()
  total_sales = 0

  for sale in sales:
    date = sale.split(",")[-1].split()[0]
    if date == str(today):
      total_sales += float(sale.split(",")[4])
  
  title = ": Sales separated by product :".center(36)+'\n'
  head = "\n|  Product Name  |  Total Product  |\n"
  separate = ('=' * 36)
  print(title+separate+head+separate)
  products = {}
  for sale in sales:
    date = sale.split(",")[-1].split()[0]
    if date == str(today):
      product_name = sale.split(",")[2]
      price = float(sale.split(",")[4])
      if product_name in products:
        products[product_name] += price
      else:
        products[product_name] = price
  for product, price in products.items():
    print(f"|{product:^16} | {price:^9} bath |")
  print(separate)
  print(f"Total sales for {today}: {total_sales} bath")

def report_sales_by_employee():
  sales = read_file(SALES_FILE)
  
  employees = {}
  for sale, employee in zip(sales, read_file("employees.txt")):
    employee_id = employee.split(",")[0]
    employee_name = employee.split(",")[1]
    if employee_id in employees:
      employees[employee_id]["sales"] += float(sale.split(",")[4])
    else:
      employees[employee_id] = {"name": employee_name, "sales": float(sale.split(",")[4])}
  title = "Report Number Product".center(37)+'\n'
  head = "\n|  Employee Name  |   Total Price   |\n"
  separate = ('=' * 37)
  print(title+separate+head+separate)
  for employee_id, data in employees.items():
    print(f"|{data['name']:^16} | {data['sales']:^15} |")
  print(separate)

def report_total_sales():
  sales = read_file(SALES_FILE)
  total_sales = sum([float(sale.split(",")[4]) for sale in sales])
  print(f"Total sales: {total_sales} bath")

def report_employee():
  employee = read_file("employees.txt")
  title = "Report Employee".center(40)+'\n'
  head = "\n| No. |  Employee Name  |  commission  |\n"
  separate = ('=' * 40)
  print(title+separate+head+separate)
  for emp in employee:
    employee_id = emp.split(",")[0]
    employee_name = emp.split(",")[1]
    commission = float(emp.split(",")[2])
    print(f'|{employee_id:^5}| {employee_name:^16}| {commission:^13}|')
  print(separate+'\n')

def report_product():
  product = read_file("products.txt")
  title = "Report Product".center(40)+'\n'
  head = "\n| No. |   Product Name  |     price    |\n"
  separate = ('=' * 40)
  print(title+separate+head+separate)
  for prod in product:
    product_id = prod.split(",")[0]
    product_name = prod.split(",")[1]
    price = float(prod.split(",")[2])
    print(f'|{product_id:^5}| {product_name:^16}| {price:^13}|')
  print(separate+'\n')

def calculate_commission():
  sales = read_file(SALES_FILE)
  employees = read_file("employees.txt")
  
  employee_sales = {}
  title = "Report Commission".center(54)+'\n'
  head = "\n| Employee Name |  total sales  |  total commission  |\n"
  separate = ('=' * 54)
  print(title+separate+head+separate)
    
  for sale in sales:
    employee_id = sale.split(",")[0]
    price = float(sale.split(",")[4])
    if employee_id in employee_sales:
      employee_sales[employee_id] += price
    else:
      employee_sales[employee_id] = price
      
  for employee in employees:
    employee_id = employee.split(",")[0]
    employee_name = employee.split(",")[1]
    commission = float(employee.split(",")[2])    
    if employee_id in employee_sales:
      total_sales = employee_sales[employee_id]
      total_commission = total_sales * commission / 100
      print(f"|{employee_name:^15}| {total_sales:^13} | {total_commission:^18} |")
  print(separate)