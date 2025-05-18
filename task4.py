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
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет курсов"
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.get_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.get_average_grade():.1f}")
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


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
    
    def __str__(self):
        return super().__str__()


student1 = Student('Иван', 'Иванов', 'мужской')
student1.courses_in_progress = ['Python', 'Java']
student1.finished_courses = ['Основы тестирования']

student2 = Student('Петр', 'Петров', 'мужской')
student2.courses_in_progress = ['Python', 'JavaScript']
student2.finished_courses = ['Java']

lecturer1 = Lecturer('Алексей', 'Алексеев')
lecturer1.courses_attached = ['Python', 'Java']

lecturer2 = Lecturer('Сергей', 'Сергеев')
lecturer2.courses_attached = ['Python', 'JavaScript']

reviewer1 = Reviewer('Андрей', 'Андреев')
reviewer1.courses_attached = ['Python', 'Java']

reviewer2 = Reviewer('Денис', 'Денисов')
reviewer2.courses_attached = ['JavaScript', 'Python']

reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Java', 6)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'JavaScript', 8)

student1.rate_lecturer(lecturer1, 'Python', 3)
student1.rate_lecturer(lecturer1, 'Java', 4)

student2.rate_lecturer(lecturer2, 'Python', 5)
student2.rate_lecturer(lecturer2, 'JavaScript', 6)


print(student1)
print(student2)
print(f"student1 < student2: {student1 < student2}")
print(f"student1 <= student2: {student1 <= student2}")
print(f"student1 == student2: {student1 == student2}")

print(lecturer1)
print(lecturer2)
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 <= lecturer2: {lecturer1 <= lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

print(reviewer1)
print(reviewer2)

def get_avg_student_grade_by_course(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0

def get_avg_lecturer_grade_by_course(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count > 0 else 0

python_students_avg = get_avg_student_grade_by_course([student1, student2], 'Python')
print(f"Средняя оценка за домашние задания по курсу Python: {python_students_avg:.1f}")

python_lecturers_avg = get_avg_lecturer_grade_by_course([lecturer1, lecturer2], 'Python')
print(f"Средняя оценка за лекции всех лекторов по курсу Python: {python_lecturers_avg:.1f}")