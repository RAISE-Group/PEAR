def test_converters(self):
    result = self.read_html('<table>\n                 <thead>\n                   <tr>\n                     <th>a</th>\n                    </tr>\n                 </thead>\n                 <tbody>\n                   <tr>\n                     <td> 0.763</td>\n                   </tr>\n                   <tr>\n                     <td> 0.244</td>\n                   </tr>\n                 </tbody>\n               </table>', converters={'a': str})[0]
    expected = DataFrame({'a': ['0.763', '0.244']})
    tm.assert_frame_equal(result, expected)