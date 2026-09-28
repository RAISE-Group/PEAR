def test_convert_no_arg_error(self):
    s = Series(['1.0', '2'])
    msg = 'At least one of datetime, numeric or timedelta must be True\\.'
    with pytest.raises(ValueError, match=msg):
        s._convert()