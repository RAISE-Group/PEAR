def test_cannot_cast_inf_to_int(self):
    idx = pd.Float64Index([1, 2, np.inf])
    msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'
    with pytest.raises(ValueError, match=msg):
        idx.astype(int)