@td.skip_if_no_scipy
@pytest.mark.parametrize('arg', ['median', 'kurt', 'skew'])
def test_agg_function_support(self, arg):
    df = pd.DataFrame({'A': np.arange(5)})
    roll = df.rolling(2, win_type='triang')
    msg = f"'{arg}' is not a valid function for 'Window' object"
    with pytest.raises(AttributeError, match=msg):
        roll.agg(arg)
    with pytest.raises(AttributeError, match=msg):
        roll.agg([arg])
    with pytest.raises(AttributeError, match=msg):
        roll.agg({'A': arg})