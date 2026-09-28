@td.skip_if_np_lt('1.15')
def test_validate_sum_initial(self):
    s = pd.Series([1, 2])
    msg = "the 'initial' parameter is not supported in the pandas implementation of sum\\(\\)"
    with pytest.raises(ValueError, match=msg):
        np.sum(s, initial=10)