def test_pad_fillchar(self):
    values = Series(['a', 'b', np.nan, 'c', np.nan, 'eeeeee'])
    result = values.str.pad(5, side='left', fillchar='X')
    exp = Series(['XXXXa', 'XXXXb', np.nan, 'XXXXc', np.nan, 'eeeeee'])
    tm.assert_almost_equal(result, exp)
    result = values.str.pad(5, side='right', fillchar='X')
    exp = Series(['aXXXX', 'bXXXX', np.nan, 'cXXXX', np.nan, 'eeeeee'])
    tm.assert_almost_equal(result, exp)
    result = values.str.pad(5, side='both', fillchar='X')
    exp = Series(['XXaXX', 'XXbXX', np.nan, 'XXcXX', np.nan, 'eeeeee'])
    tm.assert_almost_equal(result, exp)
    msg = 'fillchar must be a character, not str'
    with pytest.raises(TypeError, match=msg):
        result = values.str.pad(5, fillchar='XY')
    msg = 'fillchar must be a character, not int'
    with pytest.raises(TypeError, match=msg):
        result = values.str.pad(5, fillchar=5)