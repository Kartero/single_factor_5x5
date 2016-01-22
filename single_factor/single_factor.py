# -*- coding: utf-8 -*-

##############################################################################
class Person(object):

    def __init__(self):
        ## default values
        self.back_squat = 110
        self.bench_press = 95
        self.pendlay_row = 70
        self.dead_lift = 150
        self.military_press = 50

    def set_max_weights(self, squat, bench, pendlay, dead, military):
        self.back_squat = squat
        self.bench_press = bench
        self.pendlay_row = pendlay
        self.dead_lift = dead
        self.military_press = military

    def print_weights(self):
        all_max_weights = [self.back_squat, self.bench_press, self.pendlay_row,
                           self.dead_lift, self.military_press]
        for i in all_max_weights:
            print (i)

    def ask_max_weights(self):
        weights = {
            "Back Squat": 0,
            "Bench Press": 0,
            "Pendlay Row": 0,
            "Deadlift": 0,
            "Military Press": 0
            }
        for key in weights:
            while True:
                weight = input("{0}, five reps max: " .format(key))
                try:
                    weight = int(weight)
                    break
                except Exception:
                    continue
                
            weights[key] = weight
            
        self.set_max_weights(weights["Back Squat"], weights["Bench Press"],
                        weights["Pendlay Row"], weights["Deadlift"],
                        weights["Military Press"])

    def show_weights(self, day=1):
        max_weights = {}
        if day == 1:
            max_weights = {
                "Back Squat": self.back_squat,
                "Bench Press": self.bench_press,
                "Pendlay Row": self.pendlay_row
                }
        elif day == 2:
            max_weights = {
                "Back Squat": self.back_squat,
                "Deadlift": self.dead_lift,
                "Military Press": self.military_press
                }
        elif day == 3:           
            max_weights = {
                "Back Squat": self.back_squat,
                "Bench Press": self.bench_press,
                "Pendlay Row": self.pendlay_row
                }
        return max_weights
##############################################################################
##############################################################################
class Exercises(object):

    def __init__(self):
        self.person = None
        self.set_progression = 0.125
        self.week_progression = 2.5
        self.three_reps_progression = 2.5

    def set_person(self, person):
        ## Note! person is an object!!
        self.person = person
        print ("Current weights: ")
        print ("Back Squat: ", self.person.back_squat)
        print ("Bench Press: ", self.person.bench_press)
        print ("Dead Lift: ", self.person.dead_lift)
        print ("Pendlay Row: ", self.person.pendlay_row)
        print ("Military Press: ", self.person.military_press)
        prompt = input("Do you want to adjust defaults? ")
        if not prompt == "":
            self.person.ask_max_weights()


    def default_week_first(self, exercise):
        ## total 12 weeks, default is the fourth
        training_set = []
        set_count = 5
        for i in range(set_count):
            set_weight = exercise * (1 - self.set_progression * i)
            training_set.append(set_weight)

        training_set.reverse()
        return training_set
            
    def default_week_second(self, exercise):
        training_set = []
        if exercise == self.person.back_squat:
            training_set = [self.default_week_first(exercise)[0],
                            self.default_week_first(exercise)[1],
                            self.default_week_first(exercise)[2],
                            self.default_week_first(exercise)[2]]
        else:
            set_count = 4
            for i in range(set_count):
                set_weight = exercise * (1 - self.set_progression * i)
                training_set.append(set_weight)
            training_set.reverse()
            
        return training_set

    def default_week_third(self, exercise):
        training_set = [self.default_week_first(exercise)[0],
                        self.default_week_first(exercise)[1],
                        self.default_week_first(exercise)[2],
                        self.default_week_first(exercise)[3],
                        self.default_week_first(exercise)[4] +
                        self.three_reps_progression,
                        self.default_week_first(exercise)[2]]
        return training_set


    def create_12_weeks_program(self, training_set):
        # twelve_week_reps is actually a nested list [[]] 
        twelve_week_reps = []
        for i in range(3):
            temp_set = []
            for j in training_set:
                temp = j - self.week_progression * (i + 1)
                temp_set.append(self.myround(temp))
            twelve_week_reps.append(temp_set)
        twelve_week_reps.reverse()
            
        for i in range(9):
            temp_set = []
            for j in training_set:
                temp = j + self.week_progression * i
                temp_set.append(self.myround(temp))
            twelve_week_reps.append(temp_set)

        return twelve_week_reps
            

    def count_all_exercises(self, max_weights, day=1):
        print ("Week")
        weeks = ["{0:5}".format(x) for x in range(1,13)]
        print (">>", end="")      
        for i in weeks:
            print (i, end=" ")
        print ()
        
        if day == 1:
            print ("First exercise of a week (e.g. Monday)")
            for key, value in max_weights.items():
                training_set = self.default_week_first(value)
                twelve_week_reps = self.create_12_weeks_program(training_set)
                zipped_twelve = zip(*twelve_week_reps)
                print (key)
                for i in zipped_twelve:
                    print ("5x ", end="")
                    for j in i:
                        print ("{0:5}".format(j), end=" ")
                    print ()

        elif day == 2:
            print ("Second exercise of a week (e.g. Wednesday)")
            for key, value in max_weights.items():
                training_set = self.default_week_second(value)
                twelve_week_reps = self.create_12_weeks_program(training_set)
                zipped_twelve = zip(*twelve_week_reps)
                print (key)
                for i in zipped_twelve:
                    print ("5x ", end="")
                    for j in i:
                        print ("{0:5}".format(j), end=" ")
                    print ()
        if day == 3:
            print ("Third exercise of a week (e.g. Friday)")
            for key, value in max_weights.items():
                training_set = self.default_week_third(value)
                twelve_week_reps = self.create_12_weeks_program(training_set)
                zipped_twelve = zip(*twelve_week_reps)
                print (key)

                temp_count = 0
                for i in zipped_twelve:
                    if temp_count < 4:
                        print ("5x ", end="")
                    elif temp_count == 4:
                        print ("3x ", end="")
                    elif temp_count == 5:
                        print ("8x ", end="")
                    for j in i:
                        print ("{0:5}".format(j), end=" ")
                    print ()
                    temp_count += 1

    def print_exercise(self, training_list):
        for i in training_list:
            print (i)
            
    def myround(self, x, base=2.5):
        return round(base *round(x/base), 1)
##############################################################################    
##############################################################################  
 
class Program(object):

    def __init__(self, person, exercise):
        self.person = person
        self.exercise = exercise

    def logic(self):
        self.exercise.set_person(self.person)
        for i in range(1, 4):
            max_weights = self.person.show_weights(i)
            self.exercise.count_all_exercises(max_weights, i)
        
def main():
    person = Person()
    exercise = Exercises()
    program = Program(person, exercise)
    program.logic()
##    exercise.set_person(person)
##    # Logic comes after these
##
##    for i in range(1, 4):
##        max_weights = person.show_weights(i)
##        exercise.count_all_exercises(max_weights, i)

if __name__ == "__main__":
    main()









