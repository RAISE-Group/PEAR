def test_non_sparse_raises(self):
    ser = pd.Series([1, 2, 3])
    with pytest.raises(AttributeError, match='.sparse'):
        ser.sparse.density