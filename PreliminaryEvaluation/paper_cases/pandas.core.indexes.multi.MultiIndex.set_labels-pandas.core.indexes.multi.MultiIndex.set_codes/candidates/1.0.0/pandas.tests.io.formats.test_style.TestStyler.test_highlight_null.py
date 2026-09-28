def test_highlight_null(self, null_color='red'):
    df = pd.DataFrame({'A': [0, np.nan]})
    result = df.style.highlight_null()._compute().ctx
    expected = {(0, 0): [''], (1, 0): ['background-color: red']}
    assert result == expected