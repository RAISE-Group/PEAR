@pytest.mark.parametrize('displayed_only,exp0,exp1', [(True, DataFrame(['foo']), None), (False, DataFrame(['foo  bar  baz  qux']), DataFrame(['foo']))])
def test_displayed_only(self, displayed_only, exp0, exp1):
    data = StringIO('<html>\n          <body>\n            <table>\n              <tr>\n                <td>\n                  foo\n                  <span style="display:none;text-align:center">bar</span>\n                  <span style="display:none">baz</span>\n                  <span style="display: none">qux</span>\n                </td>\n              </tr>\n            </table>\n            <table style="display: none">\n              <tr>\n                <td>foo</td>\n              </tr>\n            </table>\n          </body>\n        </html>')
    dfs = self.read_html(data, displayed_only=displayed_only)
    tm.assert_frame_equal(dfs[0], exp0)
    if exp1 is not None:
        tm.assert_frame_equal(dfs[1], exp1)
    else:
        assert len(dfs) == 1