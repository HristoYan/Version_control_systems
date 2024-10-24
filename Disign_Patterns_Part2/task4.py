class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}"

    def edit_student(self, new_name):
        self.name = new_name


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []  # List to hold students in the group

    # Add a student to the group
    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.group_name}.")

    # Remove a student from the group by student ID
    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        print(f"Student ID {student_id} removed from {self.group_name}.")

    # Edit a student's details in the group by student ID
    def edit_student(self, student_id, new_name):
        for student in self.students:
            if student.student_id == student_id:
                student.edit_student(new_name)
                print(f"Student ID {student_id} updated to Name: {new_name}.")
                return
        print(f"Student ID {student_id} not found.")


class GroupIterator:
    def __init__(self, students):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        else:
            raise StopIteration


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.group_name}.")

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        print(f"Student ID {student_id} removed from {self.group_name}.")

    def edit_student(self, student_id, new_name):
        for student in self.students:
            if student.student_id == student_id:
                student.edit_student(new_name)
                print(f"Student ID {student_id} updated to Name: {new_name}.")
                return
        print(f"Student ID {student_id} not found.")

    # Create an iterator for students
    def create_iterator(self):
        return GroupIterator(self.students)

    # Display all students in the group using the iterator
    def display_students(self):
        print(f"Displaying students in {self.group_name}:")
        iterator = self.create_iterator()
        for student in iterator:
            print(student)


class GroupManager:
    def __init__(self):
        self.groups = {}

    # Add a new group
    def add_group(self, group_name):
        if group_name in self.groups:
            print(f"Group {group_name} already exists.")
        else:
            self.groups[group_name] = Group(group_name)
            print(f"Group {group_name} added.")

    # Remove a group
    def remove_group(self, group_name):
        if group_name in self.groups:
            del self.groups[group_name]
            print(f"Group {group_name} removed.")
        else:
            print(f"Group {group_name} not found.")

    # Add a student to a group
    def add_student_to_group(self, group_name, student):
        if group_name in self.groups:
            self.groups[group_name].add_student(student)
        else:
            print(f"Group {group_name} not found.")

    # Remove a student from a group
    def remove_student_from_group(self, group_name, student_id):
        if group_name in self.groups:
            self.groups[group_name].remove_student(student_id)
        else:
            print(f"Group {group_name} not found.")

    # Edit a student's name in a group
    def edit_student_in_group(self, group_name, student_id, new_name):
        if group_name in self.groups:
            self.groups[group_name].edit_student(student_id, new_name)
        else:
            print(f"Group {group_name} not found.")

    # Display all students in a group
    def display_students_in_group(self, group_name):
        if group_name in self.groups:
            self.groups[group_name].display_students()
        else:
            print(f"Group {group_name} not found.")


if __name__ == "__main__":
    # Create a GroupManager instance
    group_manager = GroupManager()

    # Add groups
    group_manager.add_group("Group A")
    group_manager.add_group("Group B")

    # Add students to Group A
    group_manager.add_student_to_group("Group A", Student(1, "John Doe"))
    group_manager.add_student_to_group("Group A", Student(2, "Jane Smith"))

    # Add students to Group B
    group_manager.add_student_to_group("Group B", Student(3, "Alice Johnson"))
    group_manager.add_student_to_group("Group B", Student(4, "Bob Brown"))

    # Display students in Group A
    group_manager.display_students_in_group("Group A")

    # Edit a student in Group A
    group_manager.edit_student_in_group("Group A", 1, "Johnathan Doe")

    # Display students in Group A again
    group_manager.display_students_in_group("Group A")

    # Remove a student from Group B
    group_manager.remove_student_from_group("Group B", 3)

    # Display students in Group B
    group_manager.display_students_in_group("Group B")

    # Remove Group A
    group_manager.remove_group("Group A")

    # Try to display students from a removed group
    group_manager.display_students_in_group("Group A")
