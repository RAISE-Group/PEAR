def test_to_latex_no_bold_rows(self):
    df = pd.DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    observed = df.to_latex(bold_rows=False)
    expected = '\\begin{tabular}{lrl}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert observed == expected