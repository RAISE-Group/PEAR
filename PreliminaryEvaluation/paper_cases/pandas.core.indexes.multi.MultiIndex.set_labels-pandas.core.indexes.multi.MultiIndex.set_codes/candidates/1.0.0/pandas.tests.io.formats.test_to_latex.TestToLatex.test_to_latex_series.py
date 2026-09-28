def test_to_latex_series(self):
    s = Series(['a', 'b', 'c'])
    withindex_result = s.to_latex()
    withindex_expected = '\\begin{tabular}{ll}\n\\toprule\n{} &  0 \\\\\n\\midrule\n0 &  a \\\\\n1 &  b \\\\\n2 &  c \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withindex_result == withindex_expected