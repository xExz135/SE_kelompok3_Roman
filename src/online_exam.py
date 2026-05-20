def evaluate_exam(
    exam_duration,
    accommodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):
    if exam_duration < 0:
        raise ValueError("exam_duration cannot be negative")

    if disconnect_duration < 0:
        raise ValueError("disconnect_duration cannot be negative")
    
    if disconnect_duration > 5:
        return "Auto Submit Exam"

    if login_time < 0:
        raise ValueError("login_time cannot be negative")

    if is_public_holiday:
        return "Exam Canceled"

    if login_time > 30:
        return "Login Rejected"

    if disconnect_duration > 5:
        return "Auto Submit Exam"

    if exam_duration > 150:
        return "Invalid Exam"

    if exam_duration > 120 and accommodation_status is False:
        return "Exam Rejected"

    return "Exam Accepted"