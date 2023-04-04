from school_schedule.student import Student

def test_class_added_to_class_list():
    # arrange
    beyonce = Student("beyonce", "senior", ["PHD in music"])
    class_name = "PHD in Dance"

    # act
    result = beyonce.add_class(class_name)

    # assert
    result == ["PHD in music", "PHD in Dance"]
