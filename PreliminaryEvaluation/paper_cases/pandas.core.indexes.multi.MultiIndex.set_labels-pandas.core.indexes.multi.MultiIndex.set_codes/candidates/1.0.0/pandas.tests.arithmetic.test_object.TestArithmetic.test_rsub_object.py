def test_rsub_object(self):
    index = pd.Index([Decimal(1), Decimal(2)])
    expected = pd.Index([Decimal(1), Decimal(0)])
    result = Decimal(2) - index
    tm.assert_index_equal(result, expected)
    result = np.array([Decimal(2), Decimal(2)]) - index
    tm.assert_index_equal(result, expected)
    with pytest.raises(TypeError):
        'foo' - index
    with pytest.raises(TypeError):
        np.array([True, pd.Timestamp.now()]) - index