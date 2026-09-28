def test_flex_comparison_nat(self):
    df = pd.DataFrame([pd.NaT])
    result = df == pd.NaT
    assert result.iloc[0, 0].item() is False
    result = df.eq(pd.NaT)
    assert result.iloc[0, 0].item() is False
    result = df != pd.NaT
    assert result.iloc[0, 0].item() is True
    result = df.ne(pd.NaT)
    assert result.iloc[0, 0].item() is True