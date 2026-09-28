def test_to_latex_specified_header(self):
    df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    withindex_result = df.to_latex(header=['AA', 'BB'])
    withindex_expected = '\\begin{tabular}{lrl}\n\\toprule\n{} & AA &  BB \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withindex_result == withindex_expected
    withoutindex_result = df.to_latex(header=['AA', 'BB'], index=False)
    withoutindex_expected = '\\begin{tabular}{rl}\n\\toprule\nAA &  BB \\\\\n\\midrule\n 1 &  b1 \\\\\n 2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withoutindex_result == withoutindex_expected
    withoutescape_result = df.to_latex(header=['$A$', '$B$'], escape=False)
    withoutescape_expected = '\\begin{tabular}{lrl}\n\\toprule\n{} & $A$ & $B$ \\\\\n\\midrule\n0 &   1 &  b1 \\\\\n1 &   2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert withoutescape_result == withoutescape_expected
    with pytest.raises(ValueError):
        df.to_latex(header=['A'])