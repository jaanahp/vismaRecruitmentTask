## ------- Main program ------- ##
from vismaUriValidatorClass import UriValidator
answer = ""
uriInput = ""

while answer != "Q":
    
    print("Pick action to be validated: ")
    print("1 = Login")
    print("2 = Confirm payments")
    print("3 = Sign documents")
    print("4 = Other")
    choice = input()

    if choice == "1":
        uriInput = "visma-identity://login?source=severa"
    elif choice == "2":
        paymentnumber = input("Enter payment number (numbers only): ")
        uriInput = "visma-identity://confirm?source=netvisor&paymentnumber="+paymentnumber
        #print(uriInput) #print for debugging purposes
    elif choice == "3":
        documentid = input("Enter document Id: ")
        uriInput = "visma-identity://sign?source=vismasign&documentid="+documentid
        #print(uriInput) #print for debugging purposes
#possibility for entering incorrect uri for testing purposes
    elif choice == "4":
        uriInput = input("Enter uri address: ")
        #print(uriInput) #print for debugging purposes
    else:
        print("Choice not valid")
        continue

    newUri = UriValidator(uriInput)
    newUri.validateUri(newUri.uri)

    values = newUri.returnValues()
    print(values)
    answer = input("If you wish to quit, press Q, else press some other key ").upper()