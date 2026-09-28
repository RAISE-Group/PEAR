@pytest.mark.parametrize('one_row', [True, False])
def test_to_latex_multiindex_nans(self, one_row):
    df = pd.DataFrame({'a': [None, 1], 'b': [2, 3], 'c': [4, 5]})
    if one_row:
        df = df.iloc[[0]]
    observed = df.set_index(['a', 'b']).to_latex()
    expected = '\\begin{tabular}{llr}\n\\toprule\n    &   &  c \\\\\na & b &    \\\\\n\\midrule\nNaN & 2 &  4 \\\\\n'
    if not one_row:
        expected += '1.0 & 3 &  5 \\\\\n'
    expected += '\\bottomrule\n\\end{tabular}\n'
    assert observed == expected