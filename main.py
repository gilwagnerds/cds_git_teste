def gether_data():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))

    returno n1, n2


def main():
    n1, n2 = gether_data()

    print(n1**n2)

    return None


if __name__ == "__main__":
    main()