def test_to_latex_longtable(self):
    df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    withindex_result = df.to_latex(longtable=True)
    withindex_expected = '\\begin{longtable}{lrl}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n\\endhead\n\\midrule\n\\multicolumn{3}{r}{{Continued on next page}} \\\\\n\\midrule\n\\endfoot\n\n\\bottomrule\n\\endlastfoot\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\end{longtable}\n'
    assert withindex_result == withindex_expected
    withoutindex_result = df.to_latex(index=False, longtable=True)
    withoutindex_expected = '\\begin{longtable}{rl}\n\\toprule\n a &   b \\\\\n\\midrule\n\\endhead\n\\midrule\n\\multicolumn{2}{r}{{Continued on next page}} \\\\\n\\midrule\n\\endfoot\n\n\\bottomrule\n\\endlastfoot\n 1 &  b1 \\\\\n 2 &  b2 \\\\\n\\end{longtable}\n'
    assert withoutindex_result == withoutindex_expected
    df = DataFrame({'a': [1, 2]})
    with1column_result = df.to_latex(index=False, longtable=True)
    assert '\\multicolumn{1}' in with1column_result
    df = DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
    with3columns_result = df.to_latex(index=False, longtable=True)
    assert '\\multicolumn{3}' in with3columns_result