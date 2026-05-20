def evaluate_exam(
    exam_duration,
    accomodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):
    if disconnect_duration > 5:
        return "Auto Submit Exam"

    return "Exam Accepted"