@async_mark()
async def test_tab_complete_warning(self, ip):
    pytest.importorskip('IPython', minversion='6.0.0')
    from IPython.core.completer import provisionalcompleter
    code = 'import pandas as pd; s = pd.Series()'
    await ip.run_code(code)
    with tm.assert_produces_warning(None):
        with provisionalcompleter('ignore'):
            list(ip.Completer.completions('s.', 1))