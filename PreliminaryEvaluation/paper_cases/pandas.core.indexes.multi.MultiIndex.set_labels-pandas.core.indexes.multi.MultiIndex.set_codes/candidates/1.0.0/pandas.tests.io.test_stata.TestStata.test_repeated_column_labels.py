def test_repeated_column_labels(self):
    msg = '\nValue labels for column ethnicsn are not unique. These cannot be converted to\npandas categoricals.\n\nEither read the file with `convert_categoricals` set to False or use the\nlow level interface in `StataReader` to separately read the values and the\nvalue_labels.\n\nThe repeated labels are:\n-+\nwolof\n'
    with pytest.raises(ValueError, match=msg):
        read_stata(self.dta23, convert_categoricals=True)