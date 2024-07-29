"""Starting Strength weight lifting tracker. made by (soon-2-b CS student) Matthew Johnson as his first python project
You can contact him at mattjohnson2002@icloud.com"""
import json
# data storage
from os.path import exists as file_exists
# checks if files exists


class Trainee():
    def __init__(self):
        # Dictionary of trainee lifts. Lists used to track progress 
        self.liftsDict = {
        'Benchpress 3x5': [],
        'Press 3x5': [],
        'Squat 3x5': [],
        'Deadlift 1x5': []
        }

    def appendLift(self, lift, weight):
        with open('user.json', 'r') as f:
            jsonData = json.load(f)
            liftsDict = jsonData['liftsDict']       
        if lift in liftsDict:
            liftsDict[lift].append(weight)
            print(f'\n{lift} set to {weight}')

        with open('user.json', 'w') as f:
            json.dump(jsonData, f, indent=4)

    def show(self):
        # Debugging
        print(f'Current lifts: {self.liftsDict}')
    
    def toJSON(self):
        # Save instance data to JSON file
        with open('user.json', 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    def setup(self):
        # Setup after downloading
        print('Setting up new user file...\n'
        'Please fill in the following:\n')              
        for key in self.liftsDict.keys():
            try:
                value = int(input(f'{key}: '))
                self.liftsDict[key].append(value)
            except ValueError:
                print('That is not a number')
                return
        user.toJSON()

# Math functions
def difference(num1, num2):
    difference = abs(num1 - num2)
    return difference

def percent_difference(num1, num2):
    difference = abs(num1 - num2)
    average = (num1 + num2) / 2
    percent_diff = (difference / average) * 100
    return round(percent_diff, 2)

# Main logic
user = Trainee()
while not file_exists('user.json'):
    user.setup()

flag = True
while flag:
    message = """\nStarting Strength Tracker:
    Make a selection by entering a number:
    [1]Update working set
    [2]Delete working set
    [3]Progress report
    [4]Exit
    : """
    reply = input(message)

    if reply == '1':
        message = """Which lifts would you like to update?
    [0]Benchpress 3x5
    [1]Press 3x5
    [2]Squat 3x5
    [3]Deadlift 1x5
    [4]All
    [5]Back
    : """
        reply = input(message)
        if reply in ['0', '1', '2', '3']:
            # Looks convoluted but works. Takes user input from 0-3 which equates to the index of list(liftsDict)[0-3]
            # Uses way less code than if/else statements
            with open('user.json', 'r') as f:
                jsonData = json.load(f)
                liftsDict = jsonData['liftsDict']
    
                try:
                    reply = int(reply)
                except ValueError:
                    print(f'{reply} is not a number')
                    break
                key = list(liftsDict)[reply]
                message = f'Enter new {key} weight: '
                reply = input(message)
                try:
                    value = int(reply)
                except ValueError:
                    print(f'{reply} is not a number')
                    break
                user.appendLift(key, value)
       
        # Append all lifts 
        elif reply == '4':
            with open('user.json', 'r') as f:
                jsonData = json.load(f)
                liftsDict = jsonData['liftsDict']
    
                try:
                    value = int(reply)
                except ValueError:
                    print(f'{reply} is not a number')
                    break

                for key, value in liftsDict.items():
                    value = input(f'\nEnter new {key} weight: ')
         
                    try:
                        value = int(value)
                    except ValueError:
                        print(f'{value} is not a number')
                        break 
                    user.appendLift(key, value)
    
    elif reply == '2':
        message = """Which lifts would you like to delete an entry from?
    [0]Benchpress 3x5
    [1]Press 3x5
    [2]Squat 3x5
    [3]Deadlift 1x5
    [4]Back
    : """
        reply = input(message)
        if reply in ['0', '1', '2', '3']:
            with open('user.json', 'r') as f:
                jsonData = json.load(f)
                liftsDict = jsonData['liftsDict']
                value = int(reply)
                index = list(liftsDict.values())[value]
                print(index)
                message = input('\nPlease enter which entry you want to delete: ')
                entry = int(message)
                index.remove(entry)
                with open('user.json', 'w') as f:
                    json.dump(jsonData, f, indent=4)

    elif reply == '3':
        with open('user.json', 'r') as f:
            jsonData = json.load(f)
            liftsDict = jsonData['liftsDict']
            print('Progress Report...')
            for key, value in liftsDict.items():
                print(key, value)
            try:
                for key, values in liftsDict.items():
                    print(f"""\nYour {key} went from {values[-2]} to {values[-1]}. 
a difference of {difference(values[-2], values[-1])}, or {percent_difference(values[-2], values[-1])}%""")
            except IndexError:
                print('\nOnce you add more entries, you can generate more info in your progress report')
            continue

    elif reply == '4':
        flag = False
