def test_truncate_with_different_dtypes_multiindex(self):
    df = DataFrame({'Vals': range(100)})
    frame = pd.concat([df], keys=['Sweep'], names=['Sweep', 'Index'])
    result = repr(frame)
    result2 = repr(frame.iloc[:5])
    assert result.startswith(result2)