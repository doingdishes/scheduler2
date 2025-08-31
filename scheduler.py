employees = [
    'chris', 'kamy', 'owen', 'ethan', 'sdr', 'james', 'eric',
    'zach', 'serge', 'george', 'jason', 'oscar', 'joey', 'wilfredo',
] 

def scheduler():
    current_schedule = employees.copy()

    while True:
        print(f"\nCurrent: {current_schedule}")
        
        user_input = input("How many to rotate? (Enter to quit): ")
        if not user_input:
            break
            
        try:
            num = int(user_input)
            current_schedule = current_schedule[num:] + current_schedule[:num]
            print(f"Updated: {current_schedule}")
        except ValueError:
            print("Please enter a number")

'''
names = ['A', 'B', 'C', 'D', 'E']

# Rotate 1 position
names[1:] + names[:1]  # ['B', 'C', 'D', 'E', 'A']

# Rotate 3 positions  
names[3:] + names[:3]  # ['D', 'E', 'A', 'B', 'C']

# Rotate 0 positions (no change)
names[0:] + names[:0]  # ['A', 'B', 'C', 'D', 'E']
'''