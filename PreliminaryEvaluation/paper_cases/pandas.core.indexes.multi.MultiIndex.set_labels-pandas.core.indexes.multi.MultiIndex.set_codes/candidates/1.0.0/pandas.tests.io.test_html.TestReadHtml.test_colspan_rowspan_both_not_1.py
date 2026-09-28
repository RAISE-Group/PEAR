def test_colspan_rowspan_both_not_1(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <td rowspan="2">A</td>\n                    <td rowspan="2" colspan="3">B</td>\n                    <td>C</td>\n                </tr>\n                <tr>\n                    <td>D</td>\n                </tr>\n            </table>\n        ', header=0)[0]
    expected = DataFrame(data=[['A', 'B', 'B', 'B', 'D']], columns=['A', 'B', 'B.1', 'B.2', 'C'])
    tm.assert_frame_equal(result, expected)