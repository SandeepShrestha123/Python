"""
Example of multiple inheritance along with super
"""


class Student:

    def __init__(self, name, student_id, age, subject):
        print("Student constructor is called.")
        self.name = name
        self.student_id = student_id
        self.age = age
        self.subject = subject

    def displayStudent(self):
        print("\n----- Student Details -----")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Age        : {self.age}")
        print(f"Subject    : {self.subject}")

    def study(self):
        print(f"{self.name} is studying {self.subject}.")


class Sport:

    def __init__(self, sport_name, coach_name):
        print("Sport constructor is called.")

        self.sport_name = sport_name
        self.coach_name = coach_name

    def displaySport(self):
        print("\n----- Sport Details -----")
        print(f"Sport : {self.sport_name}")
        print(f"Coach : {self.coach_name}")

    def practice(self):
        print(f"{self.name} is practicing {self.sport_name}.")


class Athlete(Student, Sport):

    def __init__(self, name, student_id, age, subject,
                 sport_name, coach_name,
                 tournament, team_name):

        super().__init__(name, student_id, age, subject)
        Sport.__init__(self, sport_name, coach_name)
        self.tournament = tournament
        self.team_name = team_name

    def displayAthlete(self):

        self.displayStudent()
        self.displaySport()

        print("\n----- Athlete Details -----")
        print(f"Team       : {self.team_name}")
        print(f"Tournament : {self.tournament}")

    def participate(self):
        print(
            f"\n{self.name} is representing "
            f"{self.team_name} in the "
            f"{self.tournament}."
        )


a = Athlete(
    "Sandeep",
    101,
    21,
    "Python",
    "Football",
    "Mr. Sharma",
    "Furfuri Nagar Tournament",
    "Kathmandu Tigers"
)

a.displayAthlete()

a.study()

a.practice()

a.participate()
