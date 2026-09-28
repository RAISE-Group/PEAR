def test_keep_default_na(self):
    html_data = '<table>\n                        <thead>\n                            <tr>\n                            <th>a</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                            <tr>\n                            <td> N/A</td>\n                            </tr>\n                            <tr>\n                            <td> NA</td>\n                            </tr>\n                        </tbody>\n                    </table>'
    expected_df = DataFrame({'a': ['N/A', 'NA']})
    html_df = self.read_html(html_data, keep_default_na=False)[0]
    tm.assert_frame_equal(expected_df, html_df)
    expected_df = DataFrame({'a': [np.nan, np.nan]})
    html_df = self.read_html(html_data, keep_default_na=True)[0]
    tm.assert_frame_equal(expected_df, html_df)