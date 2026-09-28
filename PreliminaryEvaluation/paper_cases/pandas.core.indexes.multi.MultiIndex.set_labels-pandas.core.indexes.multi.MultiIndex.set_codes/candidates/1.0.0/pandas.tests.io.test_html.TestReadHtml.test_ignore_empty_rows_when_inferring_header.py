def test_ignore_empty_rows_when_inferring_header(self):
    result = self.read_html('\n            <table>\n                <thead>\n                    <tr><th></th><th></tr>\n                    <tr><th>A</th><th>B</th></tr>\n                    <tr><th>a</th><th>b</th></tr>\n                </thead>\n                <tbody>\n                    <tr><td>1</td><td>2</td></tr>\n                </tbody>\n            </table>\n        ')[0]
    columns = MultiIndex(levels=[['A', 'B'], ['a', 'b']], codes=[[0, 1], [0, 1]])
    expected = DataFrame(data=[[1, 2]], columns=columns)
    tm.assert_frame_equal(result, expected)