def test_apply_bad_return(self):

    def f(x):
        return ''
    df = pd.DataFrame([[1, 2], [3, 4]])
    with pytest.raises(TypeError):
        df.style._apply(f, axis=None)