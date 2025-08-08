def read_file(filepath):
    file = open(filepath,'r')
    grade_data = [list(map(int, line.strip().split(','))) for line in file] 
    file.close()
    return grade_data

def total_grade(grade_data):
    result = []
    for grade in grade_data:
        together = sum(grade)
        print(together)
        result.append([grade[0],grade[1],grade[2],together,letter_grade(together)])
    return result

def avg_grade(totals):
    result = []
    total_hw = sum([s[0] for s in totals])
    total_midterm = sum([s[1] for s in totals])
    total_final = sum([s[2] for s in totals])
    total = sum([s[3] for s in totals])

    avg_hw = total_hw/len(totals)
    avg_midterm = total_midterm/len(totals)
    avg_final = total_final/len(totals)
    avg_total = total/len(totals)
    result.append([avg_hw,avg_midterm,avg_final,avg_total])
    return result
    # for n in totals:
    #     hw = sum(n[0])
    #     mid = n[1]
    #     final = n[2]
    #     total = n[3]
    #     print(hw)
    #     result.append([hw,mid,final,total])
    # return result

def letter_grade(total):
    if total >= 80:
        return'A'
    elif total >= 75:
        return'B+'
    elif total >= 70:
        return'B'
    elif total >= 65:
        return'C+'
    elif total >= 60:
        return'C'
    elif total >= 55:
        return'D+'
    elif total >= 50:
        return'D'
    else:
        return'F'
   
def window(data,totals,avg):
    header_row = f"| {'No.':^11} | {'HW(30)':^11} | {'MID(35)':^11} | {'FINAL':^11} | {'TOTAL ':^11} | {'Grade ':^9} |"
    separator = "-" * 83

    print(separator)
    print(header_row)
    print(separator)

    count = 0
    for n, total in zip(data, totals):  # ใช้ zip เพื่อรวม data และ totals เข้าด้วยกัน
        count += 1
        row_str = f"| {count:^11} | {n[0]:^11} | {n[1]:^11} | {n[2]:^11} | {total[3]:^11} | {total[4]:^9} |"
        print(row_str)
        print(separator)

    for e in avg:
        hw_avg = f"{e[0]:.2f}"
        mid_avg = f"{e[1]:.2f}"
        final_avg = f"{e[2]:.2f}"
        total_avg = f"{e[3]:.2f}"
        end_row = f"| {"AVG":^11} | {hw_avg:^11} | {mid_avg:^11} | {final_avg:^11} | {total_avg:^11} | {"":^9} |"
        print(end_row)
    print(separator)  


def main ():
    filepath = 'Text_grade/student.txt'
    data = read_file(filepath)
    
  
    totals = total_grade(data)
    avg = avg_grade(totals)
    window(data,totals,avg)






if __name__ == "__main__":
    main()