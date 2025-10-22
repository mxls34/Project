from employees import *
from products import *
from sales import *
from report import *

def menu():
    while True:
        print("1. Add a new employee")
        print("2. Add a new product")
        print("3. Show Product")
        print("4. Buy a product")
        print("5. Report")
        print("0. exit")
        
        choice = input("Enter your choice : ")
        if choice == '1':
            print()
            print("<<<<< A D D   E M P L O  E E >>>>>")
            print()
            add_employee()
            print()
        elif choice == '2':
            print()
            print("<<<<< A D D   P R O D U C T >>>>>")
            print()
            add_product()
            print()
        elif choice == '3':
            print()
            print("......S H O W   P R O D U C T......")
            report_product()
            print()
        elif choice == '4':
            print()
            print("<<<<< B U Y   P R O D U C T >>>>>")
            print()
            buy_product()
            print()
        elif choice == '5':
            print()
            print("<<<<< R E P O R T >>>>>")
            while True:
                print()
                head = "===== Menu =====\n"
                head += "E  = employee\n"+"P  = product\n"+"DS = daily sales\n"+"SE = sales by employee\n"+"T  = total sales\n"+"C  = commision\n"+"0  = back "
                print(head)
                msg = str(input("Enter (E/P/DS/SE/T/C) : ")).upper()
                print()
                if msg == 'E':
                    report_employee()
                    print()
                elif msg == 'P':
                    report_product()
                    print()
                elif msg == 'DS':
                    report_daily_sales()
                    print()
                elif msg == 'SE':
                    report_sales_by_employee()
                    print()
                elif msg == 'T':
                    report_total_sales()
                    print()
                elif msg == 'C':
                    calculate_commission()
                    print()    
                elif msg =='0':
                    break
                else:
                    print("YOUR ENTER ISN'T CORRECT TRY AGAIN")        
        elif choice == '0':
            break
        else:
            print("YOUR ENTER ISN'T CORRECT TRY AGAIN")
            print()
        
if __name__ == '__main__':
    menu()