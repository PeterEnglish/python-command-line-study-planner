import random

subjectsArray =['Tailwind\t\t 40 Mins',
                'Golang\t\t 1/2 Hour',
                'Golang Repos\t 1 Hour',
                'Vue\t\t 40 Mins', 'ChartJS\t\t 1/2 Hour',
                'Golang Libraries\t 1 Hour',
                'React Native \t 1 Hour',
                'AWS\t\t 40 Mins']

reasonsArray = ['You look more attractive to other people',
                'Chance of heart disease and lung cancer lowered hugely',
                'Better skin, teeth an hair',
                'Nice smelling clothes',
                'Be a good role model',
                'Improved air quality in your home',
                'Nobody around you get second hand smoke',
                'You save that dolla dolla'
]

morningRoutineArr= [       
                'Get out of bed',
                'Make Bed',
                'Have Breakfast',
                'Go for walk',
                'Have Coffee',
                'Begin Work',
                ]
def studyplan(subArray):
        jumbleArray(subArray)
        printStudyPlan(subArray)

def jumbleArray(arr):
        for i in range(len(arr)-1):
                rand = random.randint(0,  len(arr)-1)
                temp = arr[i]
                arr[i] = arr[rand]
                arr[rand] = temp
        
def printStudyPlan(arr):
        print("Your study plan for today is:")
        for i, d in enumerate(arr, start=0):
                print(" {} - {}".format(i+1, d)) 


def reasonToStayQuitted(reasonsArray):
        jumbleArray(reasonsArray)
        print("Todays reason to stay quitted:")
        print(reasonsArray[random.randint(0, len(reasonsArray)-1)])

def morningRoutine(morningArr):
        print("Morning Routine:")
        print("------------------------")
        for i in morningArr:
                print(i)
        print("------------------------")



studyplan(subjectsArray)
print("")
reasonToStayQuitted(reasonsArray)
print("")
morningRoutine(morningRoutineArr)