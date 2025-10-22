def read_employees():
    try:
      filename = "employees.txt"
      with open(filename, "r") as file:
        employees = file.readlines()
        if len(employees) != 0:
          for i in range(len(employees)):
            employees[i] = employees[i].strip()
          return employees
    except FileNotFoundError:
        print("Employee file not found. Please add employee information first.\n")

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
  if employees is not None:
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
          print("="*82)
          print("|  ID Employee |   Name  |   Sales | Percent Commission | Commission  |   Total  |")
          print("="*82)
          print(f'|{id:14}|{name:9}|{sales:9}|{commission:20}|{commissions:13}|{total_commissions:10}|')
          print("-"*82)
          file.write(f'ID Employee : {id}, Name : {name}, Sales : {sales}, Percent Commission : {commission}, Commission {commissions}, Total {total_commissions}\n')
          break
        else:
          print("Employee not found")

def menu():
  while True:

    print("\n"+"1. Add a new employee")
    print("2. Calculate commission")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
      add_employee()
    elif choice == '2':
      employees = read_employees()
      calculate_commission(employees)
    elif choice == '3':
      print("\n"+".........Exiting the program............\n")
      break
    else:
      print("Invalid choice. Please try again.")
    

if __name__ == '__main__':
  menu()