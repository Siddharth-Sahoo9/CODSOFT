def works():
    work=[] #An empty list to store the tasks given by the user.
    print("---WELCOME TO THE TO-DO-LIST APPLICATION---")
    x=int(input("Enter the number of tasks to be added to the list-\n"))
    for i in range(x):
        workName=input(f"Enter task {i+1} - ")
        work.append(workName)

    print("\nTasks to be done today are - ")
    for j in work:
        print(f"{work.index(j)+1}. {j} - undone")
    k=0
    status=["undone" for k in range(x)]    
    while True:
        try:
            mod=int(input("\nEnter the Number - \n1) To add a new task\n2) To update an existing task\n3) To delete a task\n4) To display all the tasks\n5) To change the status of a task\n6) To exit or stop the program.\n"))

            if mod==1:
                newTask=input("Enter the task to be added - \n")
                work.append(newTask)
                status.append("undone")
                print(f"\nYour task '{newTask}' has been successfully added.")
            elif mod==2:
                num=int(input("Enter the task number you want to update - "))
                if num<=len(work):
                    upTask=input("Enter the updated task - ")
                    work[num-1]=upTask
                    print(f"\nTask no. {num} has now been updated to '{upTask}'")
                else:
                    print("\nThe entered task number is not found.")
            elif mod==3:
                nums=int(input("Enter the task number you want to delete - "))
                if nums<=len(work):
                    del work[nums-1]
                    print(f"\nTask no. {nums} has now been deleted.")
                else:
                    print("\nThe entered task number is not found.")
            elif mod==4:
                print("The tasks are - \n")
                for j in work:
                    print(f"{work.index(j)+1}. {j} - {status[work.index(j)]}")
            elif mod==5:
                nums1=int(input("Enter the task number whose status needs to be changed - "))
                if nums1<=len(work):
                    y=int(input("Enter 0 to mark as undone and 1 to mark as done.\n"))
                    if(y==0):
                        status[nums1-1]="undone"
                    elif(y==1):
                        status[nums1-1]="done"
                    else:
                        print("Please enter a valid number, either 0 or 1.")
                    print(f"\nStatus of task no. {nums1} has now been changed to - '{status[nums1-1]}'.")
                else:
                    print("\nThe entered task number is not found.")
            elif mod==6:
                print("Closing the program...")
                break
            else:
                print("Invalid Input.\n You are requested to enter a number between 1 and 5.")
        
        except ValueError:
            print("Invalid Input\nPlease enter a valid number(1-5)")

works()