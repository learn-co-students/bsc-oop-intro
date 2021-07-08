class EveryWeekDay:
    
    def __init__(self):
        self.wake_up = '7:30am'
        self.bed_time = '11:00pm'
        self.lunch = '12:00pm'
        self.other_tasks = None
        self.morning_tasks = ['brush teeth', 'shower', 'caffeine', 'drive to work', 'say hi to class', 'release checkpoint']
        self.evening_tasks = ['record warmdown video', 'eat dinner', 'play smash brothers', 'do dishes', 'brush teeth']
        
    def print_schedule(self):
        print('====== Morning ======')
        print('Alarm:', self.wake_up)
        for task in self.morning_tasks:
            print('    -', task)
        print('=====================')
        print('Lunch time:', self.lunch)
        print('=====================')
        print()
        if self.other_tasks:
            print('==== Other Tasks ====')
            for task in self.other_tasks:
                print('    -', task)
            print('=====================')
        print()
        print('====== Evening ======')
        for task in self.evening_tasks:
            print('    -', task)
        print('=====================')
        print()
        print('Bed time:', self.bed_time)
        
class Wednesday(EveryWeekDay):
    
    def __init__(self, morning_message):
        EveryWeekDay.__init__(self)
        self.evening_tasks.append('go to gym')
        self.morning_message = morning_message
        
    def print_schedule(self):
        print('Hi!')
        
class Thursday(EveryWeekDay):
    
    def __init__(self):
        EveryWeekDay.__init__(self)
        self.bed_time = '12:00am'
        
class EndOfPhaseFriday(EveryWeekDay):
    
    def __init__(self):
        EveryWeekDay.__init__(self)
        self.morning_tasks.remove('release checkpoint')
        self.morning_tasks.append('release code challenge')
        self.other_tasks = ['create project groups']