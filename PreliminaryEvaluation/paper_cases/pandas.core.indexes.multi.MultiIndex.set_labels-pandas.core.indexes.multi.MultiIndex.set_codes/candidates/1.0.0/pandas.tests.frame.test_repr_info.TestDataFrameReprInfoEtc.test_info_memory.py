def test_info_memory(self):
    df = pd.DataFrame({'a': pd.Series([1, 2], dtype='i8')})
    buf = StringIO()
    df.info(buf=buf)
    result = buf.getvalue()
    bytes = float(df.memory_usage().sum())
    expected = textwrap.dedent("        <class 'pandas.core.frame.DataFrame'>\n        RangeIndex: 2 entries, 0 to 1\n        Data columns (total 1 columns):\n         #   Column  Non-Null Count  Dtype\n        ---  ------  --------------  -----\n         0   a       2 non-null      int64\n        dtypes: int64(1)\n        memory usage: {} bytes\n        ".format(bytes))
    assert result == expected