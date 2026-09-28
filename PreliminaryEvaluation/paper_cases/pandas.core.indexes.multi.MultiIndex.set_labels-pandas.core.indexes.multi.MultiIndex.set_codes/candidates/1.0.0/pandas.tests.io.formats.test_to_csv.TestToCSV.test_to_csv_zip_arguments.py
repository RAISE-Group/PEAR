@pytest.mark.parametrize('compression', ['zip', 'infer'])
@pytest.mark.parametrize('archive_name', [None, 'test_to_csv.csv', 'test_to_csv.zip'])
def test_to_csv_zip_arguments(self, compression, archive_name):
    from zipfile import ZipFile
    df = DataFrame({'ABC': [1]})
    with tm.ensure_clean('to_csv_archive_name.zip') as path:
        df.to_csv(path, compression={'method': compression, 'archive_name': archive_name})
        zp = ZipFile(path)
        expected_arcname = path if archive_name is None else archive_name
        expected_arcname = os.path.basename(expected_arcname)
        assert len(zp.filelist) == 1
        archived_file = os.path.basename(zp.filelist[0].filename)
        assert archived_file == expected_arcname