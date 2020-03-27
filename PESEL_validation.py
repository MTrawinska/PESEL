pesel = input("Please insert PESEL number to check if it is valid:")


def sprawdzPesel(pesel):
    try:
        return (int(pesel[10]) == (
                    100000 - sum(x * int(y) for x, y in zip([1, 3, 7, 9, 1, 3, 7, 9, 1, 3], pesel))) % 10)
    except IndexError:
        print("Error, it is not valid PESEL")


print(sprawdzPesel(pesel))
