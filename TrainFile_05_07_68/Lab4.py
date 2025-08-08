# Example Program : 4
total = 0.0
for n in range(1,6):
    score = float(input("Enter score value "+str(n)+" : "))
    total = total + score
    
print()
print("Total Score value : ", total)
print("Average score : ", total/5 )
