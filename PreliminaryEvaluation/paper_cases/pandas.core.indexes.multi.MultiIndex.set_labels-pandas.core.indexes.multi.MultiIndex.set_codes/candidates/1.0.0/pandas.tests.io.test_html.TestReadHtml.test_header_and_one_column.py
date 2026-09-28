def test_header_and_one_column(self):
    """
        Don't fail with bs4 when there is a header and only one column
        as described in issue #9178
        """
    result = self.read_html('<table>\n                <thead>\n                    <tr>\n                        <th>Header</th>\n                    </tr>\n                </thead>\n                <tbody>\n                    <tr>\n                        <td>first</td>\n                    </tr>\n                </tbody>\n            </table>')[0]
    expected = DataFrame(data={'Header': 'first'}, index=[0])
    tm.assert_frame_equal(result, expected)