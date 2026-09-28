def test_interp_raise_on_all_object_dtype(self):
    df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, dtype='object')
    msg = 'Cannot interpolate with all object-dtype columns in the DataFrame. Try setting at least one column to a numeric dtype.'
    with pytest.raises(TypeError, match=msg):
        df.interpolate()