def test_not_string(self):
    assert not is_string_dtype(PeriodDtype('D'))