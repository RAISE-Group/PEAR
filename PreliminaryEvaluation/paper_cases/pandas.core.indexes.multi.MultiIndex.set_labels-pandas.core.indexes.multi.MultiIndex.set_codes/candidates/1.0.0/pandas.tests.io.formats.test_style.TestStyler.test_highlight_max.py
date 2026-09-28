def test_highlight_max(self):
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    for max_ in [True, False]:
        if max_:
            attr = 'highlight_max'
        else:
            df = -df
            attr = 'highlight_min'
        result = getattr(df.style, attr)()._compute().ctx
        assert result[1, 1] == ['background-color: yellow']
        result = getattr(df.style, attr)(color='green')._compute().ctx
        assert result[1, 1] == ['background-color: green']
        result = getattr(df.style, attr)(subset='A')._compute().ctx
        assert result[1, 0] == ['background-color: yellow']
        result = getattr(df.style, attr)(axis=0)._compute().ctx
        expected = {(1, 0): ['background-color: yellow'], (1, 1): ['background-color: yellow'], (0, 1): [''], (0, 0): ['']}
        assert result == expected
        result = getattr(df.style, attr)(axis=1)._compute().ctx
        expected = {(0, 1): ['background-color: yellow'], (1, 1): ['background-color: yellow'], (0, 0): [''], (1, 0): ['']}
        assert result == expected
    df['C'] = ['a', 'b']
    result = df.style.highlight_max()._compute().ctx
    expected = {(1, 1): ['background-color: yellow']}
    result = df.style.highlight_min()._compute().ctx
    expected = {(0, 0): ['background-color: yellow']}