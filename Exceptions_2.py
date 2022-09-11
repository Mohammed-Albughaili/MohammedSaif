i = 0
tries = 0
while i <= 25:
    try:
        input1 = int(input("Please guss a number: "))
        if input1 not in [1,2,3]:
            raise RuntimeError
    except RuntimeError:
            print("Input out of range")
    except ValueError:
        print("This was not a number")
    else:
        i += 1
        print(i)
    finally:
        tries += 1
print(tries)
