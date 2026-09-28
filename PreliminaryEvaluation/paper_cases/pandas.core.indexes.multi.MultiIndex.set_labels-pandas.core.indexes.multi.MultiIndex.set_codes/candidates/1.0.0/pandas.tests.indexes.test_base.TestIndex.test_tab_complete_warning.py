@async_mark()
async def test_tab_complete_warning(self, ip):
    pytest.importorskip('IPython', minversion='6.0.0')
    from IPython.core.completer import provisionalcompleter
    code = 'import pandas as pd; idx = pd.Index([1, 2])'
    await ip.run_code(code)
    import jedi
    if jedi.__version__ < '0.16.0':
        warning = tm.assert_produces_warning(None)
    else:
        warning = tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False)
    with warning:
        with provisionalcompleter('ignore'):
            list(ip.Completer.completions('idx.', 4))