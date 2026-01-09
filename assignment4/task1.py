try:
    with open("assignment4/sample.txt", "r") as f:
        list = f.readlines()
        print("Reading the contents of the file: ")
        for index,i in enumerate(list):
            index+=1
            print(f"line{index}: {i.strip()}")
        print("We have reached the end of file.")
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

    