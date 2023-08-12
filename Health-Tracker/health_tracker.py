# PROGRAM STARTS HERE (PRACTICED OOP HERE)
import numpy as np


class ErrorChecker:
    def __init__(self, height, weight, age, gender, bodyfat, goal_weight, goal_time, goal_knowledge):
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.bodyfat = bodyfat
        self.goal_weight = goal_weight
        self.goal_time = goal_time
        self.goal_knowledge = goal_knowledge


    # STATIC METHOD FOR INPUT ERROR HANDLING OF NUMBER
    @staticmethod 
    def num(ask, first_num, last_num, parts):
        while True:
            try:
                variable = float(input(f"{ask}"))

                if variable in np.linspace(first_num, last_num, parts):
                    return variable
                else:        
                    print("Input seems a little unrealistic, please try again.")     
            except ValueError:
                print("The entered value is not a number. Please try again...")


    #STATIC METHOD FOR INPUT ERROR HANDLING OF Y/N INPUTS
    @staticmethod 
    def thisthat(ask, this, that):
        while True:
            variable = input(f"{ask}").lower()
            if variable in [this, that]:
                return variable
            else:        
                print("Your input seems invalid, please try again.")     
            

    #STATIC METHOD FOR INPUT ERROR HANDLING OF CHOICE
    @staticmethod
    def choice(ask, first_num, last_num, parts):
        while True:
            try:
                choice = int(input(f"{ask}"))

                list = np.linspace(first_num, last_num, parts)
                if choice in list:
                    return choice
                else:
                    print("Enter a valid choice, try again...")
            except ValueError:
                print("Your input seens invalid, please try again")


# FUNCTION TO CHOOSE FORMULA
    def choose_formula(self):
        if self.bodyfat != "":
            return ErrorChecker.choice("Enter your choice (default = 0): ", 0, 3, 4)
        else:
            return ErrorChecker.choice("Enter your choice (default = 0): ", 0, 2, 3)


# FUNCTION TO CALCULATE BMR
    def cal_bmr(self, choose_formula):
        match choose_formula:
            case 0 | 1: # MILFFLIN ST JEOR'S
                if self.gender == "m":
                    msj_bmr = ((10 * self.weight) + (6.25 * self.height * 100) - (5 * self.age) + 5)
                    return msj_bmr
                else:
                    msj_bmr = ((10 * self.weight) + (6.25 * self.height * 100) - (5 * self.age) - 161)
                    return msj_bmr
            case 2: # REVISED HARRIS BENEDICT'S
                if self.gender == "m":
                    rhb_bmr = ((13.397 * self.weight) + (4.799 * self.height * 100) - (5.677 * self.age) + 88.362)
                    return rhb_bmr
                else:
                    rhb_bmr = ((9.247 * self.weight) + (3.098 * self.height * 100) - (4.330 * self.age) + 447.593)
                    return rhb_bmr   
            case 3: # KATCH MCARDLE'S
                if self.gender in ("m", "f"):
                    km_bmr = (370 + 21.6 * (1 - (self.bodyfat/100)) * self.weight)
                    return km_bmr

    
    # FUNCTION TO RETURN BMR
    def return_bmr(self):
        choice_formula = self.choose_formula()
        return round(self.cal_bmr(choice_formula), 2)
        

    # FUNCTION TO CHOOSE LIFESTYLE          
    def choose_lifestyle(self):
        return ErrorChecker.choice("Enter your choice: ", 1, 6, 6)


    # FUNCTION TO CALCULATE DAILY CALORIE INTAKE
    def caloric_intake(self, bmr, chunav_lifestyle):   
        chunav = [bmr * 1.2, bmr * 1.375, bmr * 1.46, bmr * 1.55, bmr * 1.725, bmr * 1.9]
        return chunav[chunav_lifestyle - 1]
        

    # FUNCTION TO CALCULATE GOAL CALORIES IF USER KNOWS GOAL
    def set_fitness_goal(self, goal_time, goal_weight, normal_caloric_intake):
        if goal_weight > self.weight:
            return ((7700 * (goal_weight - self.weight)) / goal_time) + normal_caloric_intake
        elif goal_weight < self.weight:
            return normal_caloric_intake + ((goal_weight - self.weight) * 7700 / goal_time)
        else:   
            return normal_caloric_intake


    # FUNCTION TO CALCULATE RECOMMENDED CALORIES IF USER DOES'T KNOW GOAL
    def recommend_weight(self):
        if self.gender == "m":
            if self.age in range(17,20):
                return 22 * self.height * self.height
            if self.age in range(21,30):
                return 23 * self.height * self.height
            if self.age in range(31,40):
                return 24 * self.height * self.height
            if self.age in range(40,150):
                return 25 * self.height * self.height
        else:
            if self.age in range(17,20):
                return 20.5 * self.height * self.height
            if self.age in range(21,30):
                return 21.5 * self.height * self.height
            if self.age in range(31,40):
                return 22.5 * self.height * self.height
            if self.age in range(40,150):
                return 23.5 * self.height * self.height
 
                
# MAIN FUNCTION
def main():
    print("Welcome to Health Tracker!\n") 

    # INPUT FUNCTIONS
    age = get_age()
    gender = get_gender()
    weight = get_weight()
    height = get_height()
    bodyfat = get_bodyfatpercent()


    # OBJECT CREATED FOR BMR
    info = ErrorChecker(height, weight, age, gender, bodyfat, "", "", "") 


    # PRINT FORMULAE FOR BMR
    print("\nSelect preferred formula for calculation of BMR")
    print("1) Milfflin St Jeor's")
    print("2) Revised Harris-Benedict's")
    if bodyfat != "":
        print("3) Katch-McArdle's")
    

    # PRINT BMR ACCORDING TO CHOICE
    bmr = info.return_bmr()
    print(f"\nYour Basic Metabolic Rate[BMR] is: {round(bmr, 2)}\n")


    # ASK LIFESTYLE
    print("Let's get some information regarding your lifestyle.\nHow often do you exercise?\n")
    print("1) Sedentary [Little or no Exercise]\n2) Light Exercise [1 - 3 Days/Week]")
    print("3) Moderate Exercise [4 - 5 Days/Week]\n4) Daily Exercise or Intense Exercise [3 - 4 Days/Week]")
    print("5) Intense Exercise [6 - 7 Days/Week]\n6) Extreme Intense Exercise [All Days Heavy Workout]\n")

    choice_lifestyle = info.choose_lifestyle()

    # PRINT DAILY CALORIC INTAKE
    normal_calories_intake = info.caloric_intake(bmr, choice_lifestyle)
    print(f"Your daily caloric intake is: {normal_calories_intake} kcal.\n")

    # PRINT GOAL CALORIC INTAKE
    print("If you know your fitness goal i.e, your goal weight to reach in specific days, enter 'Y'.")
    print("If you're not sure about it don't worry I'll suggest something.\nIn that case, enter 'N'.")

    goal_gyan = goal_knowledge()

    if goal_gyan == "y":
        print("\nEnter your goals below.")
        goal_wajan = goal_weight()
        goal_samay = goal_time() 

        goal_caloric_intake = round(info.set_fitness_goal(normal_calories_intake), 2)

        if goal_wajan > weight:
            print(f"\nLooks like you want to gain your weight by {goal_wajan - weight} kgs.")
            print(f"No problems, your daily caloric intake should be: {goal_caloric_intake} kcal\n")
        elif goal_wajan < weight:
            print(f"\nLooks like you want to lose your weight by {weight - goal_wajan} kgs.")
            print(f"No problems, your daily caloric intake should be: {goal_caloric_intake} kcal\n")
        else:
            print("\nLooks like you want to maintain your weight.")
            print(f"You should continue with your normal caloric intake: {normal_calories_intake} kcal\n")
    
    else:
        print("\nYour goal will be calculated on the basis of your age, gender and height provided by yourself.")
        recommend_wajan = round(info.recommend_weight(), 2)
        print(f"Ideally your weight should be: {recommend_wajan} Kgs\n")

        goal_samay = goal_time()

        if recommend_wajan > weight:
            print(f"\nLooks like you need to gain your weight by {round((recommend_wajan - weight), 2)} kgs.", )
            print(f"No problems, your daily caloric intake should be: {round(info.set_fitness_goal(goal_samay, recommend_wajan, normal_calories_intake), 2)} kcal\n")
        elif recommend_wajan < weight:
            print(f"\nLooks like you need to lose your Weight by {round((weight - recommend_wajan), 2)} kgs.")
            print(f"No problems, your daily caloric intake should be: {round(info.set_fitness_goal(goal_samay, recommend_wajan, normal_calories_intake), 2)} kcal\n")
        else:
            print("\nLooks like you want to maintain your Weight.")
            print(f"You should continue with your normal caloric intake: {normal_calories_intake} kcal\n")

        print("Always remember, muscle mass must have the highest contribution in your overall weight.\n")


# INPUT FUNCTIONS

def get_age():
    return ErrorChecker.num("1) Enter your age: ", 0, 200, 201)


def get_gender():
    return ErrorChecker.thisthat("2) Enter your gender [M/F]: ", "m", "f")


def get_weight():
    return ErrorChecker.num("3) Enter your weight in kgs: ", 0, 500, 10001)


def get_height():
    return ErrorChecker.num("4) Enter your height in meters: ", 0, 3, 301)


def get_bodyfatpercent():
    bodyfat = ""
    while True:
        bodyfat = input("5) Tell me your body fat percentage (Optional): ")
        if bodyfat != "":
            try:
                bodyfat = float(bodyfat)
                if 0 < bodyfat <= 100:
                    return bodyfat
                else:
                    print("Get your liposuction done by contacting us. Try again...")
            except ValueError:
                break
        else:
            return bodyfat


def goal_weight():
    return ErrorChecker.num("Enter your goal weight in kgs: ", 0, 100, 1001)


def goal_time():
    return ErrorChecker.num("Enter your goal time in days: ", 0, 15000, 15001)


def goal_knowledge():
    return ErrorChecker.thisthat("Enter your preference [Y/N]: ", "y", "n")

    
if __name__ == "__main__":
    main()
    
