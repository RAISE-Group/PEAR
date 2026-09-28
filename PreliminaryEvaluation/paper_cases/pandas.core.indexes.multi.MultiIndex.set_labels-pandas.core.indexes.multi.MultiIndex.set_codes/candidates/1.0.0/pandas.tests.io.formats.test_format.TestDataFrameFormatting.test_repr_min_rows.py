def test_repr_min_rows(self):
    df = pd.DataFrame({'a': range(20)})
    assert '..' not in repr(df)
    assert '..' not in df._repr_html_()
    df = pd.DataFrame({'a': range(61)})
    assert '..' in repr(df)
    assert '..' in df._repr_html_()
    with option_context('display.max_rows', 10, 'display.min_rows', 4):
        assert '..' in repr(df)
        assert '2  ' not in repr(df)
        assert '...' in df._repr_html_()
        assert '<td>2</td>' not in df._repr_html_()
    with option_context('display.max_rows', 12, 'display.min_rows', None):
        assert '5    5' in repr(df)
        assert '<td>5</td>' in df._repr_html_()
    with option_context('display.max_rows', 10, 'display.min_rows', 12):
        assert '5    5' not in repr(df)
        assert '<td>5</td>' not in df._repr_html_()
    with option_context('display.max_rows', None, 'display.min_rows', 12):
        assert '..' not in repr(df)
        assert '..' not in df._repr_html_()