def test_is_null_datetimelike(self):
    for value in na_vals:
        assert is_null_datetimelike(value)
        assert is_null_datetimelike(value, False)
    for value in inf_vals:
        assert not is_null_datetimelike(value)
        assert not is_null_datetimelike(value, False)
    for value in int_na_vals:
        assert is_null_datetimelike(value)
        assert not is_null_datetimelike(value, False)
    for value in sometimes_na_vals:
        assert not is_null_datetimelike(value)
        assert not is_null_datetimelike(value, False)
    for value in never_na_vals:
        assert not is_null_datetimelike(value)