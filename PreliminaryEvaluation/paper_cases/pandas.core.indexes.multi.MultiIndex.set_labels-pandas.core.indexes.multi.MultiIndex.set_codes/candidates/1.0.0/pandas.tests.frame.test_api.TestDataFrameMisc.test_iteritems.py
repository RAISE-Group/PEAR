def test_iteritems(self):
    df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'a', 'b'])
    for k, v in df.items():
        assert isinstance(v, DataFrame._constructor_sliced)