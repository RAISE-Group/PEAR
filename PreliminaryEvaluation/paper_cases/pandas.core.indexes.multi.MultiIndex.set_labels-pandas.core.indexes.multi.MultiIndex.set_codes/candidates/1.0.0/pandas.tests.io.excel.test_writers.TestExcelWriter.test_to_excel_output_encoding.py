def test_to_excel_output_encoding(self, ext):
    df = DataFrame([['ƒ', 'Ɠ', 'Ɣ'], ['ƕ', 'Ɩ', 'Ɨ']], index=['Aƒ', 'B'], columns=['XƓ', 'Y', 'Z'])
    with tm.ensure_clean('__tmp_to_excel_float_format__.' + ext) as filename:
        df.to_excel(filename, sheet_name='TestSheet', encoding='utf8')
        result = pd.read_excel(filename, 'TestSheet', encoding='utf8', index_col=0)
        tm.assert_frame_equal(result, df)