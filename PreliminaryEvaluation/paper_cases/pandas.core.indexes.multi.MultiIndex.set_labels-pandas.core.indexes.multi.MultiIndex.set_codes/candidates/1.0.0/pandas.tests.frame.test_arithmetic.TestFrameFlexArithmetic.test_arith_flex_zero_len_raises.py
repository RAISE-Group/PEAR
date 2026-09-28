def test_arith_flex_zero_len_raises(self):
    ser_len0 = pd.Series([], dtype=object)
    df_len0 = pd.DataFrame(columns=['A', 'B'])
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    with pytest.raises(NotImplementedError, match='fill_value'):
        df.add(ser_len0, fill_value='E')
    with pytest.raises(NotImplementedError, match='fill_value'):
        df_len0.sub(df['A'], axis=None, fill_value=3)