def test_validate_median_initial(self):
    s = pd.Series([1, 2])
    msg = "the 'overwrite_input' parameter is not supported in the pandas implementation of median\\(\\)"
    with pytest.raises(ValueError, match=msg):
        s.median(overwrite_input=True)