def test_python_engine(self, python_engine):
    from pandas.io.parsers import _python_unsupported as py_unsupported
    data = '1,2,3,,\n1,2,3,4,\n1,2,3,4,5\n1,2,,,\n1,2,3,4,'
    for default in py_unsupported:
        msg = f'The {repr(default)} option is not supported with the {repr(python_engine)} engine'
        kwargs = {default: object()}
        with pytest.raises(ValueError, match=msg):
            read_csv(StringIO(data), engine=python_engine, **kwargs)