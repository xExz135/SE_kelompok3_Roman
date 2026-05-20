def check_exam_status(exam_duration: int, accommodation_status: bool, disconnect_duration: int, login_time: int, is_public_holiday: bool) -> str:
    """
    Refactor : Mengecek status ujian berdasarkan berbagai parameter.
    """
    
    # 1. Validasi data type
    if not isinstance(login_time, int):
        raise TypeError("login_time harus berupa angka bulat (integer)")
        
    # 2. Validasi nilai tidak masuk akal
    if login_time < 0:
        raise ValueError("login_time tidak boleh bernilai negatif")
        
    # 3. Main business rule
    if login_time > 30:
        return "Login Rejected"
        
    return "Exam Accepted"