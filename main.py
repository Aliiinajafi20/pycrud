from insert import *
from update import *
from delete import *
from select import *


def print_menu():
    print('1. show Customers')
    print('2. add a Customers')
    print('3. remove a Customers')
    print('4. update a Customers')
    print('5. Quit')
    print('1. press any key to show menu')
    print()

def insertcustomer():
    print("Add customer : ")
    Customername = input("FirstName: ")
    Customerfamily = input("LastName: ")
    nationalCode = input("NationalCode: ")
    insert(Customername,Customerfamily,nationalCode)

def selectcustomer():
    print("Customers are : ")
    select()

def updatecustomer():
    print("Update Customer : ")
    nationalcode = input("NationalCode : ")
    customername = input("Enter New Name : ")
    update(nationalcode, customername)

def deletCustomer():
    print("Delete Customer : ")
    nationalcode = input("Enter Customer NationalCode: ")
    delete(nationalcode)


menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = input("Type in a Number (1-5): ")

    if menu_choice == "1":
        selectcustomer()

    elif menu_choice == "2":
        insertcustomer()

    elif menu_choice == "3":
        deletCustomer()

    elif menu_choice == "4":
        updatecustomer()

    elif menu_choice == "5":
        break

    else:
        print_menu()
