<<<<<<< HEAD
from online_exam import check_exam_status



def test_exam_canceled_when_public_holiday_and_accommodation_true():
    result = check_exam_status(
        120,
        True,
        0,
        10,
        True
    )

    assert result == "Exam Canceled"


def test_exam_canceled_when_public_holiday_and_accommodation_false():
    result = check_exam_status(
        120,
        False,
        0,
        10,
        True
    )

    assert result == "Exam Canceled"
=======
from src.online_exam import evaluate_exam

def test_auto_submit_when_disconnect_more_than_5_with_accommodation():
    result = evaluate_exam(
        exam_duration=120,
        accomodation_status=True,
        disconnect_duration=6,
        login_time=30,
        is_public_holiday=False
    )

    assert result == "Auto Submit Exam"


def test_auto_submit_when_disconnect_more_than_5_without_accommodation():
    result = evaluate_exam(
        exam_duration=120,
        accomodation_status=False,
        disconnect_duration=6,
        login_time=30,
        is_public_holiday=False
    )

    assert result == "Auto Submit Exam"
>>>>>>> 3d4d036b74542a842e1e462bff9096f2b2df459f
