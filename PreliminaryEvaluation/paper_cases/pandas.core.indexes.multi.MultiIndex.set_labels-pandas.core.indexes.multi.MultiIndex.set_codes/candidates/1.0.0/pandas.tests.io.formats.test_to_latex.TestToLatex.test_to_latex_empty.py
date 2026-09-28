def test_to_latex_empty(self):
    df = DataFrame()
    result = df.to_latex()
    expected = "\\begin{tabular}{l}\n\\toprule\nEmpty DataFrame\nColumns: Index([], dtype='object')\nIndex: Index([], dtype='object') \\\\\n\\bottomrule\n\\end{tabular}\n"
    assert result == expected
    result = df.to_latex(longtable=True)
    expected = "\\begin{longtable}{l}\n\\toprule\nEmpty DataFrame\nColumns: Index([], dtype='object')\nIndex: Index([], dtype='object') \\\\\n\\end{longtable}\n"
    assert result == expected