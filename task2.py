class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Ошибка: Это не лектор"
        if course not in self.courses_in_progress:
            return "Ошибка: Студент не изучает данный курс"
        if course not in lecturer.courses_attached:
            return "Ошибка: Лектор не прикреплен к этому курсу"
        if not (1 <= grade <= 10):
            return "Ошибка: Оценка должна быть от 1 до 10"
        
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return "Оценка успешно добавлена"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"