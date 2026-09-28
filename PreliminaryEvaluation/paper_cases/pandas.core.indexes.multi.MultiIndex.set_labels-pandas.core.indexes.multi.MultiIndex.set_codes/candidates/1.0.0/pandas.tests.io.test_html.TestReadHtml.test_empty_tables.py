def test_empty_tables(self):
    """
        Make sure that read_html ignores empty tables.
        """
    html = '\n            <table>\n                <thead>\n                    <tr>\n                        <th>A</th>\n                        <th>B</th>\n                    </tr>\n                </thead>\n                <tbody>\n                    <tr>\n                        <td>1</td>\n                        <td>2</td>\n                    </tr>\n                </tbody>\n            </table>\n            <table>\n                <tbody>\n                </tbody>\n            </table>\n        '
    result = self.read_html(html)
    assert len(result) == 1