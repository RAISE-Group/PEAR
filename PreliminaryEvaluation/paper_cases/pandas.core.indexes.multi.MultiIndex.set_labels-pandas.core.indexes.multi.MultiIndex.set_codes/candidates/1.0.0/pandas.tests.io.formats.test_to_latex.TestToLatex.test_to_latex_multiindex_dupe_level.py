def test_to_latex_multiindex_dupe_level(self):
    df = pd.DataFrame(index=pd.MultiIndex.from_tuples([('A', 'c'), ('B', 'c')]), columns=['col'])
    result = df.to_latex()
    expected = '\\begin{tabular}{lll}\n\\toprule\n  &   &  col \\\\\n\\midrule\nA & c &  NaN \\\\\nB & c &  NaN \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected