def test_to_latex_non_string_index(self):
    observed = pd.DataFrame([[1, 2, 3]] * 2).set_index([0, 1]).to_latex()
    expected = '\\begin{tabular}{llr}\n\\toprule\n  &   &  2 \\\\\n0 & 1 &    \\\\\n\\midrule\n1 & 2 &  3 \\\\\n  & 2 &  3 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert observed == expected