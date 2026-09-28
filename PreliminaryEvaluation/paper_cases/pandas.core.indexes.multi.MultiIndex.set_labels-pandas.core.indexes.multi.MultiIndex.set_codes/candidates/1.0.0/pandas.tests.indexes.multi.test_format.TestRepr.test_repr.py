def test_repr(self, idx):
    result = idx[:1].__repr__()
    expected = "MultiIndex([('foo', 'one')],\n           names=['first', 'second'])"
    assert result == expected
    result = idx.__repr__()
    expected = "MultiIndex([('foo', 'one'),\n            ('foo', 'two'),\n            ('bar', 'one'),\n            ('baz', 'two'),\n            ('qux', 'one'),\n            ('qux', 'two')],\n           names=['first', 'second'])"
    assert result == expected
    with pd.option_context('display.max_seq_items', 5):
        result = idx.__repr__()
        expected = "MultiIndex([('foo', 'one'),\n            ('foo', 'two'),\n            ...\n            ('qux', 'one'),\n            ('qux', 'two')],\n           names=['first', 'second'], length=6)"
        assert result == expected