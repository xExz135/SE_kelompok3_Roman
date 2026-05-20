from src.exam import check_exam_status

def test_login_rejected_with_accommodation():
    # Berdasarkan TC008: login_time > 30 (misal 31), expected = "Login Rejected"
    result = check_exam_status(
        exam_duration=120, 
        accommodation_status=True, 
        disconnect_duration=4, 
        login_time=31, 
        is_public_holiday=False
    )
    assert result == "Login Rejected"

def test_login_rejected_without_accommodation():
    # Berdasarkan TC009: login_time > 30 (misal 35), expected = "Login Rejected"
    result = check_exam_status(
        exam_duration=120, 
        accommodation_status=False, 
        disconnect_duration=2, 
        login_time=35, 
        is_public_holiday=False
    )
    assert result == "Login Rejected"

def test_login_time_must_be_integer():
    # reject jika login_time diisi teks/string ("30")
    with pytest.raises(TypeError):
        check_exam_status(
            exam_duration=120, 
            accommodation_status=False, 
            disconnect_duration=0, 
            login_time="30", 
            is_public_holiday=False
        )

def test_login_time_cannot_be_negative():
    # reject jika login_time diisi angka minus
    with pytest.raises(ValueError):
        check_exam_status(
            exam_duration=120, 
            accommodation_status=False, 
            disconnect_duration=0, 
            login_time=-5, 
            is_public_holiday=False
        )