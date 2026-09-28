def test_to_dict_wide(self):
    df = DataFrame({'A_{:d}'.format(i): [i] for i in range(256)})
    result = df.to_dict('records')[0]
    expected = {'A_{:d}'.format(i): i for i in range(256)}
    assert result == expected