def test_to_latex_longtable_caption_label(self):
    the_caption = 'a table in a \\texttt{longtable} environment'
    the_label = 'tab:longtable'
    df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    result_c = df.to_latex(longtable=True, caption=the_caption)
    expected_c = '\\begin{longtable}{lrl}\n\\caption{a table in a \\texttt{longtable} environment}\\\\\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n\\endhead\n\\midrule\n\\multicolumn{3}{r}{{Continued on next page}} \\\\\n\\midrule\n\\endfoot\n\n\\bottomrule\n\\endlastfoot\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\end{longtable}\n'
    assert result_c == expected_c
    result_l = df.to_latex(longtable=True, label=the_label)
    expected_l = '\\begin{longtable}{lrl}\n\\label{tab:longtable}\\\\\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n\\endhead\n\\midrule\n\\multicolumn{3}{r}{{Continued on next page}} \\\\\n\\midrule\n\\endfoot\n\n\\bottomrule\n\\endlastfoot\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\end{longtable}\n'
    assert result_l == expected_l
    result_cl = df.to_latex(longtable=True, caption=the_caption, label=the_label)
    expected_cl = '\\begin{longtable}{lrl}\n\\caption{a table in a \\texttt{longtable} environment}\\label{tab:longtable}\\\\\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n\\endhead\n\\midrule\n\\multicolumn{3}{r}{{Continued on next page}} \\\\\n\\midrule\n\\endfoot\n\n\\bottomrule\n\\endlastfoot\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\end{longtable}\n'
    assert result_cl == expected_cl