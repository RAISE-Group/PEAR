def test_where_ordered_differs_rasies(self):
    ser = pd.Series(Categorical(['a', 'b', 'c'], categories=['d', 'c', 'b', 'a'], ordered=True))
    other = Categorical(['b', 'c', 'a'], categories=['a', 'c', 'b', 'd'], ordered=True)
    with pytest.raises(ValueError, match='without identical categories'):
        ser.where([True, False, True], other)