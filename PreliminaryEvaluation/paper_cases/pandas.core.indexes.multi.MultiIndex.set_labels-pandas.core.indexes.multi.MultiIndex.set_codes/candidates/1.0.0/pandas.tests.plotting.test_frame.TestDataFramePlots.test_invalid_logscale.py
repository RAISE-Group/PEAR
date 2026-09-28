@pytest.mark.parametrize('input_param', ['logx', 'logy', 'loglog'])
def test_invalid_logscale(self, input_param):
    df = DataFrame({'a': np.arange(100)}, index=np.arange(100))
    msg = "Boolean, None and 'sym' are valid options, 'sm' is given."
    with pytest.raises(ValueError, match=msg):
        df.plot(**{input_param: 'sm'})