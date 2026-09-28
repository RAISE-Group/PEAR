def test_rowspan_only_rows(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <td rowspan="3">A</td>\n                    <td rowspan="3">B</td>\n                </tr>\n            </table>\n        ', header=0)[0]
    expected = DataFrame(data=[['A', 'B'], ['A', 'B']], columns=['A', 'B'])
    tm.assert_frame_equal(result, expected)