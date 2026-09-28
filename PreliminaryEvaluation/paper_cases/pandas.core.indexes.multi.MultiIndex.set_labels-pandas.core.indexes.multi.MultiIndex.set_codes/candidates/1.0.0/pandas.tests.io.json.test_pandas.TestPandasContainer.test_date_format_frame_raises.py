def test_date_format_frame_raises(self):
    df = self.tsframe.copy()
    msg = "Invalid value 'foo' for option 'date_unit'"
    with pytest.raises(ValueError, match=msg):
        df.to_json(date_format='iso', date_unit='foo')