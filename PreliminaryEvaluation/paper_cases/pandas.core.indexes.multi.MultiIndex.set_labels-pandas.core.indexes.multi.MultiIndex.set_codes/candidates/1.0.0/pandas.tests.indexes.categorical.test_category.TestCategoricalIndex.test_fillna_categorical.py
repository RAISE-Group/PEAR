def test_fillna_categorical(self):
    idx = CategoricalIndex([1.0, np.nan, 3.0, 1.0], name='x')
    exp = CategoricalIndex([1.0, 1.0, 3.0, 1.0], name='x')
    tm.assert_index_equal(idx.fillna(1.0), exp)
    msg = 'fill value must be in categories'
    with pytest.raises(ValueError, match=msg):
        idx.fillna(2.0)