def test_where_new_category_raises(self):
    ser = pd.Series(Categorical(['a', 'b', 'c']))
    msg = 'Cannot setitem on a Categorical with a new category'
    with pytest.raises(ValueError, match=msg):
        ser.where([True, False, True], 'd')