def test_empty(self):
    df = pd.DataFrame({'A': [1, 0]})
    s = df.style
    s.ctx = {(0, 0): ['color: red'], (1, 0): ['']}
    result = s._translate()['cellstyle']
    expected = [{'props': [['color', ' red']], 'selector': 'row0_col0'}, {'props': [['', '']], 'selector': 'row1_col0'}]
    assert result == expected