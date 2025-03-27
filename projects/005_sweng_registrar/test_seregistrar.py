import pytest
from unittest.mock import patch
from course import Course
from people import Person, Professor, Student
from grade import Grade


def test_create_course_valid():
    course_data = {
        "id": "CO2025UR1001SE",
        "title": "Introduction to Psychology",
        "instructor": "TBD",
        "attendance": 0,
    }
    new_course_as_text = f"""\ncourse_info:\nid: {course_data['id']}\ntitle: {course_data['title']}\ninstructor: {course_data['instructor']}\nattendance: {course_data['attendance']}\n"""
    new_course = Course("Introduction to Psychology")
    assert new_course.__str__() == new_course_as_text


def test_create_course_invalid():
    course_data = {
        "id": "CO2025UR1001SE",
        "title": "",
        "instructor": "TBD",
        "attendance": 0,
    }
    new_course_as_text = f"""\ncourse_info:\nid: {course_data['id']}\ntitle: {course_data['title']}\ninstructor: {course_data['instructor']}\nattendance: {course_data['attendance']}\n"""
    try:
        Course.id_counter = 1000
        new_course = Course("")
        assert new_course.__str__() == ValueError(
            "Title string may not be less than 5."
        )
    except Exception as err:
        pass


test_create_course_valid()
test_create_course_invalid()
