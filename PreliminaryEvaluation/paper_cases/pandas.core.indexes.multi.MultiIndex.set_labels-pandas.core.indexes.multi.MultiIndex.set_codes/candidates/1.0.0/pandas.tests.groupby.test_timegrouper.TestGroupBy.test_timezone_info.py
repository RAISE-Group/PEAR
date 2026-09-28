def test_timezone_info(self):
    df = pd.DataFrame({'a': [1], 'b': [datetime.now(pytz.utc)]})
    assert df['b'][0].tzinfo == pytz.utc
    df = pd.DataFrame({'a': [1, 2, 3]})
    df['b'] = datetime.now(pytz.utc)
    assert df['b'][0].tzinfo == pytz.utc