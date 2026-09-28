def test_parse_header_of_non_string_column(self):
    result = self.read_html('\n            <table>\n                <tr>\n                    <td>S</td>\n                    <td>I</td>\n                </tr>\n                <tr>\n                    <td>text</td>\n                    <td>1944</td>\n                </tr>\n            </table>\n        ', header=0)[0]
    expected = DataFrame([['text', 1944]], columns=('S', 'I'))
    tm.assert_frame_equal(result, expected)