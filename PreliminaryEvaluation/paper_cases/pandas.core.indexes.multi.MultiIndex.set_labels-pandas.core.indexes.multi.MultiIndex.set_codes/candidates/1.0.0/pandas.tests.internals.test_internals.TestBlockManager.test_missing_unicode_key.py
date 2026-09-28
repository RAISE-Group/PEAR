def test_missing_unicode_key(self):
    df = DataFrame({'a': [1]})
    try:
        df.loc[:, 'א']
    except KeyError:
        pass