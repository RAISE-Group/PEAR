def test_preserve_empty_rows(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <th>A</th>\n                    <th>B</th>\n                </tr>\n                <tr>\n                    <td>a</td>\n                    <td>b</td>\n                </tr>\n                <tr>\n                    <td></td>\n                    <td></td>\n                </tr>\n            </table>\n        ')[0]
    expected = DataFrame(data=[['a', 'b'], [np.nan, np.nan]], columns=['A', 'B'])
    tm.assert_frame_equal(result, expected)