def test_rowspan_at_end_of_row(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <td>A</td>\n                    <td rowspan="2">B</td>\n                </tr>\n                <tr>\n                    <td>C</td>\n                </tr>\n            </table>\n        ', header=0)[0]
    expected = DataFrame(data=[['C', 'B']], columns=['A', 'B'])
    tm.assert_frame_equal(result, expected)