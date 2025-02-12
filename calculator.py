# CLI calculator build in python
list_ops = [1,2,3,4]
def main():
    while True:
        print("1. Sum")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")

        inptr = int(input("Calculator:"))

        if inptr in list_ops:
            if inptr == 1:
                x = Fsum()
                print(f"The total of your sum is {x}")
            elif inptr == 2:
                y = Fsub()
                print(f"The total of your substraction is {y}")
            elif inptr == 3:
                mu = Fmul()
                print(f"The total of your substraction is {mu}")
            elif inptr == 4:
                g = Fdiv()
                print(f"The total of your division is {g}")

def Fsum():
    n_times = int(input("How many numbers u wanna sum"))
    j = 0
    total = 0
    while (j < n_times):
        total += int(input("Number: "))
        j += 1
    
    return total

def Fsub():
    m_times = int(input("X:"))
    mc_times = int(input("Y:"))
    sub_total = m_times - mc_times
    return sub_total

def Fmul():
    v_times = int(input("X:"))
    zc = int(input("Y:"))
    mul_total = zc * v_times
    return mul_total

def Fdiv():
    z_times = int(input("X:"))
    zi_times = int(input("Y:"))
    div_total = z_times / zi_times

    return div_total

if __name__ == "__main__":
    main()