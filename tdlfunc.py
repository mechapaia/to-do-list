import csv
import time
from tabulate import tabulate

def createFile():

    # creating file
    with open(r"data.csv","w",newline="") as myfile:

        # assigning the headers of the file
        writer = csv.DictWriter(myfile,fieldnames=["Title","Description"])
        writer.writeheader()

        print("\nFile created successfully!")
        time.sleep(1)


def viewTasks():

    # opening file in read mode
    with open(r"data.csv","r",newline="") as myfile:

        # loading data and converting to list
        d=csv.reader(myfile)
        data=list(d)

        # printing data into tabular format
        print('\n',tabulate(data[1:], headers=data[0], tablefmt="grid"),sep="")
        time.sleep(1)


def addTask():

    # opening file in append mode
    with open(r"data.csv","a",newline="") as myfile:
        
        # taking input from user
        title=input("\nEnter Title: ")
        desc=input("Enter Task Description: ")

        # pushing the data into the file
        d={"Title":title,"Description":desc}
        writer = csv.DictWriter(myfile,fieldnames=["Title","Description"])
        writer.writerow(d)

        print("Task added successfully!")
        time.sleep(1)


def removeTask():

    # opening file in append and read mode
    flag=False
    with open(r"data.csv","a+",newline="") as myfile:

        # taking input from user
        find=input("\nEnter Title of Task to be Removed: ")

        # adjusting pointer to beginning of the file
        myfile.seek(0)

        # loading data
        d=csv.reader(myfile)
        data=list(d)

        # searching through data matching with input then removing it
        for pair in data[1:]:
            if pair[0].lower()==find.lower():
                data.remove(pair)
                flag=True
                break
    
    # updating file when matched
    if flag==True:
        # overwriting old data with modified one
        with open(r"data.csv","w",newline="") as myfile:
            writer = csv.DictWriter(myfile,fieldnames=["Title","Description"])
            writer.writeheader()
            for item in data[1:]:
                writer.writerow({"Title":item[0],"Description":item[1]})

        print("Task removed successfully!")
    else:
        print("Task not found.")
    time.sleep(1)
        
