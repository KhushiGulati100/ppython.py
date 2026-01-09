with open("assignment4/output.txt","a") as f:
    message = input("enter text to write into the file: ")
    f.write(f"{message}\n")
    print('Data successfully written to \'output.txt\'')
    message2 = input("enter data to append: ")
    f.write(f"{message2}\n")
    print("final contents of the file: ")
with open("assignment4/output.txt","r") as f:
    list = f.readlines()
    for i in list:
        print(i.strip())