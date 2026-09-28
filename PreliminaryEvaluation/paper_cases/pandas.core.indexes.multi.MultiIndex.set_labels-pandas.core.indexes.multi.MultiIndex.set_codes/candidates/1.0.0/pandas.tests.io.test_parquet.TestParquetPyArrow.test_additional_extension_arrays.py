@td.skip_if_no('pyarrow', min_version='0.15.0')
def test_additional_extension_arrays(self, pa):
    df = pd.DataFrame({'a': pd.Series([1, 2, 3], dtype='Int64'), 'b': pd.Series(['a', None, 'c'], dtype='string')})
    if LooseVersion(pyarrow.__version__) >= LooseVersion('0.15.1.dev'):
        expected = df
    else:
        expected = df.assign(a=df.a.astype('int64'), b=df.b.astype('object'))
    check_round_trip(df, pa, expected=expected)
    df = pd.DataFrame({'a': pd.Series([1, 2, 3, None], dtype='Int64')})
    if LooseVersion(pyarrow.__version__) >= LooseVersion('0.15.1.dev'):
        expected = df
    else:
        expected = df.assign(a=df.a.astype('float64'))
    check_round_trip(df, pa, expected=expected)