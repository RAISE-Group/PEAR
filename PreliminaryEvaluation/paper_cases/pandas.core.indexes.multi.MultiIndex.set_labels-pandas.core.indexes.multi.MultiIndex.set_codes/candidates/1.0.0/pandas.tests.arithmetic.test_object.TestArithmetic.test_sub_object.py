def test_sub_object(self):
    index = pd.Index([Decimal(1), Decimal(2)])
    expected = pd.Index([Decimal(0), Decimal(1)])
    result = index - Decimal(1)
    tm.assert_index_equal(result, expected)
    result = index - pd.Index([Decimal(1), Decimal(1)])
    tm.assert_index_equal(result, expected)
    with pytest.raises(TypeError):
        index - 'foo'
    with pytest.raises(TypeError):
        index - np.array([2, 'foo'])