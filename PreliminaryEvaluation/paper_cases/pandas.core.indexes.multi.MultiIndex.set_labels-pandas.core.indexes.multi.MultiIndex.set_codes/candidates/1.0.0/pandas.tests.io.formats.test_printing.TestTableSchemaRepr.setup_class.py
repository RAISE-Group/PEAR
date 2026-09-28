@classmethod
def setup_class(cls):
    pytest.importorskip('IPython')
    from IPython.core.interactiveshell import InteractiveShell
    cls.display_formatter = InteractiveShell.instance().display_formatter