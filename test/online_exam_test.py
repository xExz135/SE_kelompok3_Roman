import pytest
from src.exam import evaluate_exam

# test case
def test_exam_rejected_duration_above_120_without_accommodation():
    assert evaluate_exam(
        exam_duration=130,
        accommodation_status=False,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=False
    ) == "Exam Rejected"


def test_invalid_exam_duration_above_150_with_accommodation():
    assert evaluate_exam(
        exam_duration=151,
        accommodation_status=True,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=False
    ) == "Invalid Exam"


def test_invalid_exam_duration_above_150_without_accommodation():
    assert evaluate_exam(
        exam_duration=151,
        accommodation_status=False,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=False
    ) == "Invalid Exam"


def test_exam_accepted_duration_120_to_150_with_accommodation():
    assert evaluate_exam(
        exam_duration=140,
        accommodation_status=True,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=False
    ) == "Exam Accepted"


def test_exam_accepted_duration_below_120_without_accommodation():
    assert evaluate_exam(
        exam_duration=100,
        accommodation_status=False,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=False
    ) == "Exam Accepted"


def test_auto_submit_with_accommodation():
    assert evaluate_exam(
        exam_duration=120,
        accommodation_status=True,
        disconnect_duration=6,
        login_time=30,
        is_public_holiday=False
    ) == "Auto Submit Exam"


def test_auto_submit_without_accommodation():
    assert evaluate_exam(
        exam_duration=120,
        accommodation_status=False,
        disconnect_duration=6,
        login_time=30,
        is_public_holiday=False
    ) == "Auto Submit Exam"


def test_login_rejected_with_accommodation():
    assert evaluate_exam(
        exam_duration=120,
        accommodation_status=True,
        disconnect_duration=4,
        login_time=31,
        is_public_holiday=False
    ) == "Login Rejected"


def test_login_rejected_without_accommodation():
    assert evaluate_exam(
        exam_duration=120,
        accommodation_status=False,
        disconnect_duration=4,
        login_time=31,
        is_public_holiday=False
    ) == "Login Rejected"


def test_exam_canceled_with_accommodation_on_public_holiday():
    assert evaluate_exam(
        exam_duration=120,
        accommodation_status=True,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=True
    ) == "Exam Canceled"


def test_exam_canceled_without_accommodation_on_public_holiday():
    assert evaluate_exam(
        exam_duration=120,
        accommodation_status=False,
        disconnect_duration=4,
        login_time=30,
        is_public_holiday=True
    ) == "Exam Canceled"


def test_invalid_negative_exam_duration():
    with pytest.raises(ValueError):
        evaluate_exam(
            exam_duration=-1,
            accommodation_status=False,
            disconnect_duration=4,
            login_time=30,
            is_public_holiday=False
        )