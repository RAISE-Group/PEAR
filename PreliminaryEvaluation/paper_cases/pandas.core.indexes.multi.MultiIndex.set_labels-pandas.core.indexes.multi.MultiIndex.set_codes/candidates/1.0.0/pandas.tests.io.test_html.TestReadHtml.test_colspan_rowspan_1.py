def test_colspan_rowspan_1(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <th>A</th>\n                    <th colspan="1">B</th>\n                    <th rowspan="1">C</th>\n                </tr>\n                <tr>\n                    <td>a</td>\n                    <td>b</td>\n                    <td>c</td>\n                </tr>\n            </table>\n        ')[0]
    expected = DataFrame([['a', 'b', 'c']], columns=['A', 'B', 'C'])
    tm.assert_frame_equal(result, expected)