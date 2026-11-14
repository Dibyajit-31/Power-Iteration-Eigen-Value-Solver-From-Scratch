def make_matrix(n):
    '''This is a function that would let you make a nxn matrix'''
    m = []
    for i in range(n):
        # l = []
        # for j in range(n):
        #     num = int(input(f"Enter an integer for the position {i+1},{j+1}: "))
        #     l.append(num)
        # m.append(l)
        row = list(map(int, input(f"Enter {i+1} row: ").split()))
        m.append(row)
    return m

def eigen_value(m,n):
    '''Repeatedly multiply the given matrix m with a simple nx1 matrix'''
    step = 0
    err = False
    a = []
    l = []
    eigen = 1
    old_eigen = 0
    a.append(1)
    for i in range(n-1):
        a.append(0)
    num = 20
    l = a.copy()
    try:
        while (abs(eigen-old_eigen)/abs(eigen))>0.00000001:
            l.clear()
            for row in m:
                num = 0
                for j in range(n):
                    num += (row[j] * a[j])
                l.append(num)
            a = l.copy()
            try:
                old_eigen = eigen
            except:
                old_eigen = max(a,key=abs)
            eigen = max(a,key=abs)
            for j in range(n):
                a[j]/=eigen
            step+=1
            if step == 1000:
                err = True
                break
    except ZeroDivisionError:
        return 0
    if err == False:
        return eigen
    else:
        return "Fatal Error... Use another method"

def main():
    n = int(input("Enter the order of matrix nxn: "))
    matrix = make_matrix(n)
    res = eigen_value(matrix,n)
    return res

if __name__ == "__main__":
    result = main()
    print(result)