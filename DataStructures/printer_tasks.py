"""
Simulation: printing tasks

"""
import random
import time
from queue import Queue

#Printer Implementation

class Printer:

    def __init__(self,task = None):
        self.task = task 
        self.availability = True

    def isBusy(self):
        return self.availability

    def print(self):
        
        self.availability = False

        pages = self.task.total
        while pages > 0 and not self.isBusy():
            
            if pages % 3 == 0:
                time.sleep(2)
            pages -=1

        self.availability = True
        self.task.status = True


    def remainingPages(self):
        return self.task.total

    def taskCompleted(self):
        return self.task.status



#task implemetation

class Task:

    def __init__(self):
        self.total = random.randrange(1,21) #pages 
        self.status = False


class Student:
    
    def __init__(self,st_id):
        self.id = st_id
        self.tasks = []

    def getID(self):
        return self.id

    def getTasks(self):
        return self.tasks

    def addTasks(self,alist):
        for task in alist:
            self.tasks.append(task)

def QueueStatus(printing_queue,printerDetails):
    
    tasks = printing_queue
    total_pages  = []
    for task in tasks:
        pages = task.tasks[0].total + task.tasks[1].total
        total_pages.append(pages)
    
    seconds = float(sum(total_pages)) / float(1/6)
    minutes = seconds/float(60)
    return (minutes,printerDetails.remainingPages())




def main():
    
    students = [Student(student_id) for student_id in range(1,10)]

    print_queue = Queue()

    print("\n\t\tPrinter Initiated")

    for student in students:
        tasks_list = [Task(), Task()]
        student.addTasks(tasks_list)
        print_queue.add(student)
    
    while not bool(print_queue):

        student_tasks = print_queue.remove()
        tasks = student_tasks.tasks
        for task in range(len(tasks)):

            
            printer = Printer()
            
            print("\n\t---PRINTING!!--")
            if printer.isBusy():
                printer.task = tasks[task]
                printer.print()
                current_status = QueueStatus(print_queue,printer)
                print("Printing Student {0} task:{1}".format(student_tasks.id,task+1))
                print("Total pages: ",current_status[1])
                print("Average waiting time {0} min".format(current_status[0]))
                if printer.taskCompleted():
                    print("Current Task Print Completed")

            else: 
                print("Printer is busy, will update you the status very shortly ")
            

    print("ALL TASKS HAVE PRINTED")




if __name__ == "__main__":
    main()



            


