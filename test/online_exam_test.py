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