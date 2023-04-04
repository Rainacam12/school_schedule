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
    def __init__(self, name, grade, classes=None):
        self.name = name
        self.grade = grade
        # use a ternary. if there is arg passed for classes, set the classes attr to that value, if nothing passed then list will be empty
        self.classes = classes if classes else []

    def __str__(self):
        return f"Student {self.name}, {self.grade}, {self.classes}"

    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        self.display_each_class()
        return self.__str__()

    def display_each_class(self):
        for name in self.classes:
            print(name)
    
    