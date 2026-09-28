def test_comparison_different_length(self):
    a = Series(['a', 'b', 'c'])
    b = Series(['b', 'a'])
    with pytest.raises(ValueError):
        a < b
    a = Series([1, 2])
    b = Series([2, 3, 4])
    with pytest.raises(ValueError):
        a == b