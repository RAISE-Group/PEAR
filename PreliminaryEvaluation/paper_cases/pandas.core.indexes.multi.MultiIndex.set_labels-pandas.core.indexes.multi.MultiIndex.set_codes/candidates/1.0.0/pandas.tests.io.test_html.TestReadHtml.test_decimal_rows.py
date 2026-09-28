def test_decimal_rows(self):
    result = self.read_html('<html>\n            <body>\n             <table>\n                <thead>\n                    <tr>\n                        <th>Header</th>\n                    </tr>\n                </thead>\n                <tbody>\n                    <tr>\n                        <td>1100#101</td>\n                    </tr>\n                </tbody>\n            </table>\n            </body>\n        </html>', decimal='#')[0]
    expected = DataFrame(data={'Header': 1100.101}, index=[0])
    assert result['Header'].dtype == np.dtype('float64')
    tm.assert_frame_equal(result, expected)