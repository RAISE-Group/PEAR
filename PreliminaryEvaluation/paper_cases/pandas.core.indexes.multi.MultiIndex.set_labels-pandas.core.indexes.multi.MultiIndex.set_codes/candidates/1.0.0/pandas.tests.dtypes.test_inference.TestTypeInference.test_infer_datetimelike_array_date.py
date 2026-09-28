def test_infer_datetimelike_array_date(self):
    arr = [date(2017, 6, 12), date(2017, 3, 11)]
    assert lib.infer_datetimelike_array(arr) == 'date'