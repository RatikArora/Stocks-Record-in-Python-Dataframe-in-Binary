import pickle
import os
# appending or adding the data to the file without replacing it

def append():
    print('-'*50)
    file = open('stockmain.dat', 'ab')
    a = []
    print('Enter the following details : ')
    code = int(input("Enter the code of the stock : "))
    name = input("Enter the name of the stock : ")
    price = int(input("Enter the price of the stock : "))
    quantity = int(input("Enter the quantity of the stock : "))
    total = price*quantity
    a = [code, name, price, quantity, total]
    pickle.dump(a, file)
    file.close()
    print('-'*50)


# printing tht file stockmain.dat
def show():
    file = open('stockmain.dat', 'rb')
    print('-'*100, '\nThe Data in the File is : \n')
    print('Code\t Name\t Price\t Quantity\t Total (₹) ')
    try:
        while True:
            # print("true")
            record = pickle.load(file)
            print(record[0], '\t', record[1],
                  '\t ₹', record[2], '\t', record[3], '\t\t₹', record[4])
            # print('yes')

    except Exception:
        file.close()
        print('-'*50)


def update():
    # print('-'*50)

    try:
        file = open("stockmain.dat", "rb+")
        found = False
        rec = []
        x = int(input("Enter Stock Code : "))
        y = int(input("1. Price\n2. Quantity\nEnter your input : "))
        while True:
            position = file.tell()
            stu = pickle.load(file)
            if stu[0] == x:
                if y == 2:
                    new = int(input("Enter New Quantity : "))
                    stu[3] = new
                    stu[4] = new*stu[2]
                    file.seek(position)
                    pickle.dump(stu, file)
                    found = True
                    break
                if y == 1:
                    new = int(input("Enter New Price : ₹"))
                    stu[2] = new
                    stu[4] = new*stu[3]
                    file.seek(position)
                    pickle.dump(stu, file)
                    found = True
                    break

    except Exception:
        file.close()
    if found == True:
        print("Done!")
    else:
        print("No stock found of such code")
    print('-'*50)


def sell():
    # print('-'*50)

    try:
        file = open("stockmain.dat", "rb+")
        found = False
        rec = []
        x = int(input("Enter Stock Code : "))
        while True:
            position = file.tell()
            stu = pickle.load(file)
            if stu[0] == x:
                selling = int(
                    input("Enter the quantity which you want to sell : "))
                if selling <= stu[3]:
                    stu[3] = stu[3]-selling
                    stu[4] = stu[2]*stu[3]
                    file.seek(position)
                    pickle.dump(stu, file)
                    found = True
                    Bill = selling*stu[2]
                    print("The bill of the sold stocks is : ₹", Bill)
                    break
                else:
                    print("You dont have enough to sell!\nChoose within the limit")

    except Exception:
        file.close()
    if found == True:
        print("Done!")
    else:
        print("No stock found of such code")
    print('-'*50)


def find():
    print('-'*50)
    file = open('stockmain.dat', 'rb')
    find = int(input("Enter the code of the stock you wish to find : "))
    z = False
    try:
        while True:
            record = pickle.load(file)
            if find == record[0]:
                print("\nyes stock is present ")
                z = True
    except Exception:
        if z == False:
            print("\nstock not found")
        print('-'*50)
        file.close()


def deletestock():
    print('-'*50)
    file = open("stockmain.dat", "rb")
    data = []
    found = False
    x = int(input("Enter the code of the stock you wish to delete : "))
    file2 = open("stockmain2.dat", "wb")
    try:
        while True:
            found = False
            rpos = file.tell()
            stu = pickle.load(file)
            if stu[0] == x:
                found = True
            if found == False:
                # data = [stu[0],stu[1],stu[2],stu[3]]
                pickle.dump(stu, file2)

    except Exception:
        file.close()
        file2.close()
        renamethefile()


def renamethefile():
    source = 'stockmain2.dat'
    dest = 'stockmain.dat'
    print('-'*50)
    if os.path.isfile(dest):
        os.remove(dest)
        # print("File has been deleted")

        # print("File not found")
    os.rename(source, dest)
    # print("Rename Successfull")


print('-'*50)
while True:
    print("\n--- Stocks Record ---\n")
    a = int(input("1. Add a stock\n2. Show the record\n3. Buy more \n4. Sell the stock\n5. Update the price  \n6. Find the Stock\n7. Delete the stock\n8. Exit\n\nEnter the input : "))
    print('-'*50)
    if a == 1:
        append()
    elif a == 2:
        show()
    elif a == 3 or a == 5:
        update()
        show()
    elif a == 4:
        sell()
    elif a == 6:
        find()
    elif a == 7:
        deletestock()
        show()
    elif a == 8:
        print("Open to suggestions \nGOODBYE")
        print('-'*50)
        break
    else:
        print("Invalid Syntax")

# # main
# # append()
# # append()
# show()
# # find()
# # update()
# deletestock()
# show()
