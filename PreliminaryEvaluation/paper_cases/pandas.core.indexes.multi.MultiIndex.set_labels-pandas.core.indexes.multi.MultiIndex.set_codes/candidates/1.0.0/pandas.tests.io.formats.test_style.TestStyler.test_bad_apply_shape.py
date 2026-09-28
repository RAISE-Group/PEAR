def test_bad_apply_shape(self):
    df = pd.DataFrame([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        df.style._apply(lambda x: 'x', subset=pd.IndexSlice[[0, 1], :])
    with pytest.raises(ValueError):
        df.style._apply(lambda x: [''], subset=pd.IndexSlice[[0, 1], :])
    with pytest.raises(ValueError):
        df.style._apply(lambda x: ['', '', '', ''])
    with pytest.raises(ValueError):
        df.style._apply(lambda x: ['', '', ''], subset=1)
    with pytest.raises(ValueError):
        df.style._apply(lambda x: ['', '', ''], axis=1)