from src.exam import check_exam_status


def test_exam_canceled_for_holiday_with_accommodation():
    result = check_exam_status(
        120,
        True,
        0,
        10,
        True
    )

    assert result == "Exam Canceled"


def test_exam_canceled_for_holiday_without_accommodation():
    result = check_exam_status(
        120,
        False,
        0,
        10,
        True
    )

    assert result == "Exam Canceled"
    