from openpyxl import Workbook
from scheduler import scheduler

#grab workbook from working directory
wb = Workbook()

ws = wb.active

employees = [
    'chris', 'kamy', 'owen', 'ethan', 'sdr', 'james', 'eric',
    'zach', 'serge', 'george', 'jason', 'oscar', 'joey', 'wilfredo',
] 

rotations = int(input("How many rotations? 10 is 2 teams per day. "))

def scheduler():
    current_schedule = employees.copy()
    sliced_names = current_schedule[0:5]
    wb=Workbook()
    ws = wb.active

    while True:
        print(f"\nCurrent: {current_schedule}")

        global user_input
        user_input = input("How many to rotate? (Enter to quit): ")
        if not user_input:
            break
            
        try:
            num = int(user_input)
            for _ in range(rotations):
                current_schedule = current_schedule[num:] + current_schedule[:num]
                sliced_names = current_schedule[0:5]
                print(f"New top 5: {sliced_names}")
                ws.append(sliced_names)
                wb.save("Book1.xlsx")
        except ValueError:
            print("Please enter a number")

scheduler()
