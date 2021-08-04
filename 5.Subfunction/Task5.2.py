# -- coding: cp1252 --
def second_power(value1):
    counting = value1**2
    return counting

def main():
    value1 = int(input("Enter numeric value: "))
    print("The second power is ", second_power(value1))

if __name__ == "__main__":
    main()