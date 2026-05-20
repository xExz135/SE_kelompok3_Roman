def check_exam_status(exam_duration, accommodation_status, disconnect_duration, login_time, is_public_holiday):
    
    # Tolak jika login lebih dari 30 menit
    if login_time > 30:
        return "Login Rejected"
        
    return "Exam Accepted"