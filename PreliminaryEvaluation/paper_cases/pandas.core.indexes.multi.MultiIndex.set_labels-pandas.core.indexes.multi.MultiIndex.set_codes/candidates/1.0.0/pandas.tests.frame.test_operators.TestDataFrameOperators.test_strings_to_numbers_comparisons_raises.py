def test_strings_to_numbers_comparisons_raises(self, compare_operators_no_eq_ne):
    df = DataFrame({x: {'x': 'foo', 'y': 'bar', 'z': 'baz'} for x in ['a', 'b', 'c']})
    f = getattr(operator, compare_operators_no_eq_ne)
    with pytest.raises(TypeError):
        f(df, 0)