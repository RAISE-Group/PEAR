@td.skip_if_no('openpyxl')
@td.skip_if_no('xlwt')
def test_set_column_names_in_parameter(self, ext):
    refdf = pd.DataFrame([[1, 'foo'], [2, 'bar'], [3, 'baz']], columns=['a', 'b'])
    with tm.ensure_clean(ext) as pth:
        with ExcelWriter(pth) as writer:
            refdf.to_excel(writer, 'Data_no_head', header=False, index=False)
            refdf.to_excel(writer, 'Data_with_head', index=False)
        refdf.columns = ['A', 'B']
        with ExcelFile(pth) as reader:
            xlsdf_no_head = pd.read_excel(reader, 'Data_no_head', header=None, names=['A', 'B'])
            xlsdf_with_head = pd.read_excel(reader, 'Data_with_head', index_col=None, names=['A', 'B'])
        tm.assert_frame_equal(xlsdf_no_head, refdf)
        tm.assert_frame_equal(xlsdf_with_head, refdf)