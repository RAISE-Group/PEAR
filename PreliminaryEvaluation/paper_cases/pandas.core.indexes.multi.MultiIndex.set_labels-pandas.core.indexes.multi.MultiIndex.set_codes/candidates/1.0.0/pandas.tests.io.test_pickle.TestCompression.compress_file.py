def compress_file(self, src_path, dest_path, compression):
    if compression is None:
        shutil.copyfile(src_path, dest_path)
        return
    if compression == 'gzip':
        f = gzip.open(dest_path, 'w')
    elif compression == 'bz2':
        f = bz2.BZ2File(dest_path, 'w')
    elif compression == 'zip':
        with zipfile.ZipFile(dest_path, 'w', compression=zipfile.ZIP_DEFLATED) as f:
            f.write(src_path, os.path.basename(src_path))
    elif compression == 'xz':
        f = _get_lzma_file(lzma)(dest_path, 'w')
    else:
        msg = 'Unrecognized compression type: {}'.format(compression)
        raise ValueError(msg)
    if compression != 'zip':
        with open(src_path, 'rb') as fh, f:
            f.write(fh.read())