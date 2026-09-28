def test_constructor_no_data_index_order(self):
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        result = pd.Series(index=['b', 'a', 'c'])
    assert result.index.tolist() == ['b', 'a', 'c']