def test_logical_nan_raises(self, all_logical_operators):
    op_name = all_logical_operators
    a = pd.array([True, False, None], dtype='boolean')
    msg = 'Got float instead'
    with pytest.raises(TypeError, match=msg):
        getattr(a, op_name)(np.nan)