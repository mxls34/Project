def read_day_data(file_data):
    file = open(file_data, 'r')
    sales_data = [list(map(int, line.strip().split(','))) for line in file]
    file.close()
    return sales_data

def total_branch(sales_data):
    numbers = []
    
    for i in sales_data:
        number = (sum(i))
        numbers.append(number)
    return numbers

def total_day(sales_data,branch,day):
    numbers = []

    for i in range(day):
        number = 0
        for n in range(branch):
            number += sales_data[n][i]
        numbers.append(number)
    return numbers
        
def total_sum_branch(total_branch1):
    return(sum(total_branch1))

def report_day(sales_data,total_branch1,total_day1,total_sum_branch1):
    heder = f"| {'No.':^9} | {'Day 1':^9} | {'Day 2':^9} | {'Day 3':^9} | {'Day 4':^9} | {'Day 5':^9} | {'Day 6':^9} | {'Day 7':^9} | {'Total':^9} |"
    sep = '-'*109
    
    print(sep)
    print(heder)
    print(sep)

    num = 0
    
    for data,branch in zip(sales_data,total_branch1,):
        num += 1
        self = f"| {num:^9} | {data[0]:^9} | {data[1]:^9} | {data[2]:^9} | {data[3]:^9} | {data[4]:^9} | {data[5]:^9} | {data[6]:^9} | {branch:^9} |"
        print(self)
        print(sep)

    self =  f"| {"Total":^9} | {total_day1[0]:^9} | {total_day1[1]:^9} | {total_day1[2]:^9} | {total_day1[3]:^9} | {total_day1[4]:^9} | {total_day1[5]:^9} | {total_day1[6]:^9} | {total_sum_branch1:^9} |"
    print(self)
    print(sep)




def main():
    day = 7
    branch = 2
    file_data = "Text_Sales/data_sales.txt"
    sales_data = read_day_data(file_data)
    total_branch1 = total_branch(sales_data)
    total_day1 = total_day(sales_data,branch,day)
    total_sum_branch1 = total_sum_branch(total_branch1)
    report_day(sales_data,total_branch1,total_day1,total_sum_branch1)

    
    



if __name__ == "__main__":
    main()
    