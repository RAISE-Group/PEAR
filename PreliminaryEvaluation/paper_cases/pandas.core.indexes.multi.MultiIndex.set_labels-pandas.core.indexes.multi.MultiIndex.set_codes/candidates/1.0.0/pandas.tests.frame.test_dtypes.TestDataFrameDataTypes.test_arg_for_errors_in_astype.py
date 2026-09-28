def test_arg_for_errors_in_astype(self):
    df = DataFrame([1, 2, 3])
    with pytest.raises(ValueError):
        df.astype(np.float64, errors=True)
    df.astype(np.int8, errors='ignore')