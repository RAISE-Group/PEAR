def test_frame_to_json_except(self):
    df = DataFrame([1, 2, 3])
    msg = "Invalid value 'garbage' for option 'orient'"
    with pytest.raises(ValueError, match=msg):
        df.to_json(orient='garbage')