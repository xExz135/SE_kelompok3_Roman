import pytest
from src.exam_duration import process_exam


# TC001
def test_exam_rejected():
    assert process_exam(
        exam_duration=120,
        accomodation_status=False,
        disconnect_duration=3,
        login_time=30,
        is_public_holiday=False
    ) == "Exam Rejected"


# TC002
def test_invalid_exam_duration_over_150_with_accommodation():
    assert process_exam(
        exam_duration=160,
        accomodation_status=True,
        disconnect_duration=3,
        login_time=30,
        is_public_holiday=False
    ) == "Invalid Exam"


# TC003
def test_invalid_exam_duration_over_150_without_accommodation():
    assert process_exam(
        exam_duration=160,
        accomodation_status=False,
        disconnect_duration=3,
        login_time=30,
        is_public_holiday=False
    ) == "Invalid Exam"


# TC004
def test_exam_accepted_with_accommodation():
    assert process_exam(
        exam_duration=130,
        accomodation_status=True,
        disconnect_duration=3,
        login_time=30,
        is_public_holiday=False
    ) == "Exam Accepted"


# TC005
def test_exam_accepted_without_accommodation():
    assert process_exam(
        exam_duration=110,
        accomodation_status=False,
        disconnect_duration=3,
        login_time=30,
        is_public_holiday=False
    ) == "Exam Accepted"
