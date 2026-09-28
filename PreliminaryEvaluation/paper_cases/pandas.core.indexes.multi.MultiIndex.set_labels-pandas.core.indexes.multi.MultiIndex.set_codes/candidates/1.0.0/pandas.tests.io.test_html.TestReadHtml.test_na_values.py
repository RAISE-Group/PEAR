def test_na_values(self):
    result = self.read_html('<table>\n                 <thead>\n                   <tr>\n                     <th>a</th>\n                   </tr>\n                 </thead>\n                 <tbody>\n                   <tr>\n                     <td> 0.763</td>\n                   </tr>\n                   <tr>\n                     <td> 0.244</td>\n                   </tr>\n                 </tbody>\n               </table>', na_values=[0.244])[0]
    expected = DataFrame({'a': [0.763, np.nan]})
    tm.assert_frame_equal(result, expected)