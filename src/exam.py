def check_exam_status(
    exam_duration,
    accommodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):
    EXAM_CANCELED = "Exam Canceled"
    EXAM_ACCEPTED = "Exam Accepted"
    
    if is_public_holiday:
        return EXAM_CANCELED
    return EXAM_ACCEPTED