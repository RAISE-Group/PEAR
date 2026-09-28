def test_parser_error_on_empty_header_row(self):
    msg = 'Passed header=\\[0,1\\] are too many rows for this multi_index of columns'
    with pytest.raises(ParserError, match=msg):
        self.read_html('\n                <table>\n                    <thead>\n                        <tr><th></th><th></tr>\n                        <tr><th>A</th><th>B</th></tr>\n                    </thead>\n                    <tbody>\n                        <tr><td>a</td><td>b</td></tr>\n                    </tbody>\n                </table>\n            ', header=[0, 1])