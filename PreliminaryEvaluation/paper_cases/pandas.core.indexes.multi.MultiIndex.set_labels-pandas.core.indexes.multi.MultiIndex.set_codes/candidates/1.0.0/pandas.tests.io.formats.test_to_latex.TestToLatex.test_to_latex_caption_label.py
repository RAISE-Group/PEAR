def test_to_latex_caption_label(self):
    the_caption = 'a table in a \\texttt{table/tabular} environment'
    the_label = 'tab:table_tabular'
    df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
    result_c = df.to_latex(caption=the_caption)
    expected_c = '\\begin{table}\n\\centering\n\\caption{a table in a \\texttt{table/tabular} environment}\n\\begin{tabular}{lrl}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'
    assert result_c == expected_c
    result_l = df.to_latex(label=the_label)
    expected_l = '\\begin{table}\n\\centering\n\\label{tab:table_tabular}\n\\begin{tabular}{lrl}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'
    assert result_l == expected_l
    result_cl = df.to_latex(caption=the_caption, label=the_label)
    expected_cl = '\\begin{table}\n\\centering\n\\caption{a table in a \\texttt{table/tabular} environment}\n\\label{tab:table_tabular}\n\\begin{tabular}{lrl}\n\\toprule\n{} &  a &   b \\\\\n\\midrule\n0 &  1 &  b1 \\\\\n1 &  2 &  b2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'
    assert result_cl == expected_cl