def test_header_inferred_from_rows_with_only_th(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <th>A</th>\n                    <th>B</th>\n                </tr>\n                <tr>\n                    <th>a</th>\n                    <th>b</th>\n                </tr>\n                <tr>\n                    <td>1</td>\n                    <td>2</td>\n                </tr>\n            </table>\n        ')[0]
    columns = MultiIndex(levels=[['A', 'B'], ['a', 'b']], codes=[[0, 1], [0, 1]])
    expected = DataFrame(data=[[1, 2]], columns=columns)
    tm.assert_frame_equal(result, expected)