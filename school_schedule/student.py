class Student:
    """
attributes:
    - name -str
    - grade -str 
    - class - list
methods: 
    - add_class, param: STR
    - get_num_classes
    - summary
    - pretty_print_each_class()
"""
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def __str__(self):
        return f"Student {self.name}, {self.grade}, {self.classes}"

    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes

    def get_num_classes(self):
        pass   

    def summary(self):
        pass

    def display_each_class(self):
        pass
    pass
    