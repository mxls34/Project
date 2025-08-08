def read_employees():
  filename = "employees.txt"
  with open(filename, "r") as file:
    employees = file.readlines()
    for i in range(len(employees)):
      employees[i] = employees[i].strip()
    return employees
  

def add_employee():
  filename = "employees.txt"
  with open(filename, "a") as file:
    id = input("Enter employee id: ")
    name = input("Enter employee name: ")
    sales = float(input("Enter sales: "))
    commission = float(input("Enter commission: "))
    file.write(f'{id},{name},{sales},{commission}\n')
  print("Employee added successfully")

def calculate_commission(employees):
  filename = "history.txt"
  with open(filename, "a") as file:
    id_emp = input("Enter employee id: ")
    for employee in employees:
      emp = employee.split(',')
      id = emp[0]
      name = emp[1]
      sales = float(emp[2])
      commission = float(emp[3])
      commissions = sales * (commission / 100)
      total_commissions = sales + commissions
      if id_emp == id:
        print(f'ID Employee : {id}, Name : {name}, Sales : {sales}, Percent Commission : {commission}, Commission {commissions}, Total {total_commissions}')
        file.write(f'ID Employee : {id}, Name : {name}, Sales : {sales}, Percent Commission : {commission}, Commission {commissions}, Total {total_commissions}\n')
        break
    else:
      print("Employee not found")    

def menu():
  while True:
    print("1. Add a new employee")
    print("2. Calculate commission")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
      add_employee()
    elif choice == '2':
      employees = read_employees()
      calculate_commission(employees)
    elif choice == '3':
      break
    

if __name__ == '__main__':
  menu()