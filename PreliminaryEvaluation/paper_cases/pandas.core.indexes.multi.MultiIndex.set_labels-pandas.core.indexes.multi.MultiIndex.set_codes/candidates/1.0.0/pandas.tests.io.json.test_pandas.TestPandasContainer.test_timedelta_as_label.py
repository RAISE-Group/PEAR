@pytest.mark.parametrize('date_format,key', [('epoch', 86400000), ('iso', 'P1DT0H0M0S')])
def test_timedelta_as_label(self, date_format, key):
    df = pd.DataFrame([[1]], columns=[pd.Timedelta('1D')])
    expected = f'{{"{key}":{{"0":1}}}}'
    result = df.to_json(date_format=date_format)
    assert result == expected