def Status():
    print("----------------------------------------------------------------")
    print("Table:")
    for i in n:
        print(i,end = "\n")
    print()
    print("RHS:", rhs)
    print("----------------------------------------------------------------")

def pos_min(n = []):
    min = max(n)
    for i in range (len(n)):
        if n[i] < min and n[i] > 0:
            min = n[i]
    return min

def positive_check(n = []):     # Check if there are any elements in array that positive
    flag = False
    for i in range (len(n)):
        if n[i] > 0:
            flag = True
    return flag



col, row = map(int,input().split(" "))

n = []

for i in range(row+1):
    z = list(map(int, input().strip().split()))
    for j in range(i):
        z.append(0)
    z.append(1)
    for j in range(i+1,row+1):
        z.append(0)
    n.append(z)
n[0][2] = -1
rhs = [0] + list(map(int, input().strip().split()))



def Simplexify(flag):
    temp = n[0].index(max(n[0]))    # Column has maximum 

    e = [] #Expectation
    for i in range(row):
        e.append(rhs[i+1]/n[i+1][temp])
    
    if positive_check(e) == False:
        flag = 1
        return flag
    
    temp_2 = e.index(pos_min(e)) + 1    # Row that has minimun expectation

    m = n[temp_2][temp]
    for i in range(len(n[temp_2])):
        n[temp_2][i] /= m
    rhs[temp_2] /= m
    # Update data to make the number in the target cell become 1

    for i in range(row + 1):
        if i == temp_2:
            continue
        
        k = n[i][temp] / n[temp_2][temp]    
        for j in range(len(n[i])):
            n[i][j] = n[i][j] - k * n[temp_2][j]
        
        rhs[i] = rhs[i] - k * rhs[temp_2]

    if not positive_check(n[0]):
        print(-rhs[0])

    Status()

    return flag


for i in range(col):
    


flag = 0                
while positive_check(n[0]) and flag == 0:
    Simplexify(flag)
if flag == 1:
    print("UNBOUNDED")



