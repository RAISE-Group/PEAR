def test_tfoot_read(self):
    """
        Make sure that read_html reads tfoot, containing td or th.
        Ignores empty tfoot
        """
    data_template = '<table>\n            <thead>\n                <tr>\n                    <th>A</th>\n                    <th>B</th>\n                </tr>\n            </thead>\n            <tbody>\n                <tr>\n                    <td>bodyA</td>\n                    <td>bodyB</td>\n                </tr>\n            </tbody>\n            <tfoot>\n                {footer}\n            </tfoot>\n        </table>'
    expected1 = DataFrame(data=[['bodyA', 'bodyB']], columns=['A', 'B'])
    expected2 = DataFrame(data=[['bodyA', 'bodyB'], ['footA', 'footB']], columns=['A', 'B'])
    data1 = data_template.format(footer='')
    data2 = data_template.format(footer='<tr><td>footA</td><th>footB</th></tr>')
    result1 = self.read_html(data1)[0]
    result2 = self.read_html(data2)[0]
    tm.assert_frame_equal(result1, expected1)
    tm.assert_frame_equal(result2, expected2)