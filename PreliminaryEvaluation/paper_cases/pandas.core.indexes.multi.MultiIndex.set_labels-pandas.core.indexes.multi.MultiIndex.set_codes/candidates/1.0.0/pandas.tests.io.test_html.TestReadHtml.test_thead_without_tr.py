def test_thead_without_tr(self):
    """
        Ensure parser adds <tr> within <thead> on malformed HTML.
        """
    result = self.read_html('<table>\n            <thead>\n                <tr>\n                    <th>Country</th>\n                    <th>Municipality</th>\n                    <th>Year</th>\n                </tr>\n            </thead>\n            <tbody>\n                <tr>\n                    <td>Ukraine</td>\n                    <th>Odessa</th>\n                    <td>1944</td>\n                </tr>\n            </tbody>\n        </table>')[0]
    expected = DataFrame(data=[['Ukraine', 'Odessa', 1944]], columns=['Country', 'Municipality', 'Year'])
    tm.assert_frame_equal(result, expected)