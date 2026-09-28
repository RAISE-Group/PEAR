def test_constructor_ordereddict(self):
    data = OrderedDict((('col{i}'.format(i=i), np.random.random()) for i in range(12)))
    series = Series(data)
    expected = Series(list(data.values()), list(data.keys()))
    tm.assert_series_equal(series, expected)

    class A(OrderedDict):
        pass
    series = Series(A(data))
    tm.assert_series_equal(series, expected)