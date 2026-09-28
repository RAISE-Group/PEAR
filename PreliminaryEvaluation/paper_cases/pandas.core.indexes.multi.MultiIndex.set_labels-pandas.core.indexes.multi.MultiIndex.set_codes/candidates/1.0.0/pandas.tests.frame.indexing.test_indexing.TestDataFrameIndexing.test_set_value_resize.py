def test_set_value_resize(self, float_frame):
    res = float_frame._set_value('foobar', 'B', 0)
    assert res is float_frame
    assert res.index[-1] == 'foobar'
    assert res._get_value('foobar', 'B') == 0
    float_frame.loc['foobar', 'qux'] = 0
    assert float_frame._get_value('foobar', 'qux') == 0
    res = float_frame.copy()
    res3 = res._set_value('foobar', 'baz', 'sam')
    assert res3['baz'].dtype == np.object_
    res = float_frame.copy()
    res3 = res._set_value('foobar', 'baz', True)
    assert res3['baz'].dtype == np.object_
    res = float_frame.copy()
    res3 = res._set_value('foobar', 'baz', 5)
    assert is_float_dtype(res3['baz'])
    assert isna(res3['baz'].drop(['foobar'])).all()
    msg = "could not convert string to float: 'sam'"
    with pytest.raises(ValueError, match=msg):
        res3._set_value('foobar', 'baz', 'sam')