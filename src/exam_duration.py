def process_exam(
    exam_duration,
    accomodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):
    if exam_duration > 150:
        return "Invalid Exam"
    
    if accomodation_status == True:
        if exam_duration <= 150:
            return "Exam Accepted"
        
    if exam_duration < 120:
        return "Exam Accepted"
    
    if exam_duration >= 120:
        return "Exam Rejected"