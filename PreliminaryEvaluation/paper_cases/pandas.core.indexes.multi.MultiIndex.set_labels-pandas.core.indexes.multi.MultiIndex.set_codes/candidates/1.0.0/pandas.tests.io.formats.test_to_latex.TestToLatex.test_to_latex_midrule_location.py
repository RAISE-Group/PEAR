def test_to_latex_midrule_location(self):
    df = pd.DataFrame({'a': [1, 2]})
    df.index.name = 'foo'
    observed = df.to_latex(index_names=False)
    expected = '\\begin{tabular}{lr}\n\\toprule\n{} &  a \\\\\n\\midrule\n0 &  1 \\\\\n1 &  2 \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert observed == expected