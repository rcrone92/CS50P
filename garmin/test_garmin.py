import pytest
from garmin import Activity, FitnessDay

def main():
    test_init()
    test_attributes()
    test_setters()
    test_setters2()
    test_fitnessday()


def test_init():
    activity = Activity()

def test_attributes():
    activity = Activity()
    assert activity.activity_type == None
    assert activity.date == None
    assert activity.favorite == False
    assert activity.calories == None

def test_setters():
    activity = Activity(title='100', max_hr=100)
    assert activity.title == '100'
    assert activity.max_hr == 100
    with pytest.raises(ValueError):
        activity = Activity(title = 100)

def test_setters2():
    activity = Activity(activity_type="Running", title="Jogging")
    newActivityType = "Swimming"
    newTitle = "Morning Swim"
    activity.activity_type = newActivityType
    activity.title = newTitle
    assert activity.activity_type == "Swimming"
    assert activity.title == "Morning Swim"

def test_fitnessday():
    fitDay = FitnessDay()


if __name__ == "__main__":
    main()
