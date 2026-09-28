def test_to_latex_with_formatters(self):
    df = DataFrame({'datetime64': [datetime(2016, 1, 1), datetime(2016, 2, 5), datetime(2016, 3, 3)], 'float': [1.0, 2.0, 3.0], 'int': [1, 2, 3], 'object': [(1, 2), True, False]})
    formatters = {'datetime64': lambda x: x.strftime('%Y-%m'), 'float': lambda x: '[{x: 4.1f}]'.format(x=x), 'int': lambda x: '0x{x:x}'.format(x=x), 'object': lambda x: '-{x!s}-'.format(x=x), '__index__': lambda x: 'index: {x}'.format(x=x)}
    result = df.to_latex(formatters=dict(formatters))
    expected = '\\begin{tabular}{llrrl}\n\\toprule\n{} & datetime64 &  float & int &    object \\\\\n\\midrule\nindex: 0 &    2016-01 & [ 1.0] & 0x1 &  -(1, 2)- \\\\\nindex: 1 &    2016-02 & [ 2.0] & 0x2 &    -True- \\\\\nindex: 2 &    2016-03 & [ 3.0] & 0x3 &   -False- \\\\\n\\bottomrule\n\\end{tabular}\n'
    assert result == expected