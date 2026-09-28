def test_to_csv_path_is_none(self):
    s = Series([1, 2, 3])
    csv_str = s.to_csv(path_or_buf=None, header=False)
    assert isinstance(csv_str, str)