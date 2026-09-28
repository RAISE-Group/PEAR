def test_series_to_json_except(self):
    s = Series([1, 2, 3])
    msg = "Invalid value 'garbage' for option 'orient'"
    with pytest.raises(ValueError, match=msg):
        s.to_json(orient='garbage')