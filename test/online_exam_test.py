from src.exam import check_exam_status



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