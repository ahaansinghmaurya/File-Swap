def SwapFiles():
    fileName1 = input("Enter the file name 1 to be swapped: ")
    fileName2 = input("Enter the file name 2 to be swapped: ")
    with open(fileName1, 'r') as a:
        data_a = a.read()

    with open(fileName2, 'r') as b:
        data_b = b.read()

    with open(fileName1, 'w') as a:
        a.write(data_b)

    with open(fileName2, 'w') as b:
        b.write(data_a)

    print("Abracadabra ! the magic has been done the files content have been swapped.")


SwapFiles()
