def is_disconnected_too_long(disconnect_duration):
    return disconnect_duration > 5


def evaluate_exam(
    exam_duration,
    accomodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):
    if is_disconnected_too_long(disconnect_duration):
        return "Auto Submit Exam"

    return "Exam Accepted"