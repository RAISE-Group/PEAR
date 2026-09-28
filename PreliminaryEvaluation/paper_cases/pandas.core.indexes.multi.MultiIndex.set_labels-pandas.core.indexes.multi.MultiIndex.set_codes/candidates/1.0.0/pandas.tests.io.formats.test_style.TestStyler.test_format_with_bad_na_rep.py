def test_format_with_bad_na_rep(self):
    df = pd.DataFrame([[None, None], [1.1, 1.2]], columns=['A', 'B'])
    with pytest.raises(TypeError):
        df.style.format(None, na_rep=-1)