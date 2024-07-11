class Student:
    def _init_(self, name):
        self.name = name
        self.grades = {} 
         # Dictionary to hold subjects and grades

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)

    def _str_(self):
        return f"Student Name: {self.name}, Grades: {self.grades}"


class Classroom:
    def _init_(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    def get_student_average(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                avg_grade = student.get_average_grade()
                print(f"Average grade for {student.name}: {avg_grade}")
                return avg_grade
        print(f"No student found with the name {name}.")
        return None

    def get_class_average_for_subject(self, subject):
        total_grades = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades found for subject {subject}.")
            return None
        class_avg = total_grades / count
        print(f"Class average for {subject}: {class_avg}")
        return class_avg


def main():
    classroom = Classroom()

    while True:
        print("\nSchool Class Management System")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Get the average grade of a student")
        print("4. Get the class average for a subject")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student's name: ")
            student = Student(name)
            while True:
                subject = input("Enter subject (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                grade = float(input(f"Enter grade for {subject}: "))
                student.add_grade(subject, grade)
            classroom.add_student(student)
        elif choice == '2':
            classroom.display_students()
        elif choice == '3':
            name = input("Enter the name of the student: ")
            classroom.get_student_average(name)
        elif choice == '4':
            subject = input("Enter the subject: ")
            classroom.get_class_average_for_subject(subject)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()