def test_to_string_truncate_multilevel(self):
    arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
    df = DataFrame(index=arrays, columns=arrays)
    with option_context('display.max_rows', 7, 'display.max_columns', 7):
        assert has_doubly_truncated_repr(df)