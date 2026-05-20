def check_exam_status(
    exam_duration,
    accommodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):

    if is_public_holiday:
        return "Exam Canceled"

    return "Exam Accepted"