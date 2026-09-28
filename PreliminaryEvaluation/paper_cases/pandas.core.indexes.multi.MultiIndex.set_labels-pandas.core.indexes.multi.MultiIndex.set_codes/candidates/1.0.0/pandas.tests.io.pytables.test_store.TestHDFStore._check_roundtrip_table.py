def _check_roundtrip_table(self, obj, comparator, path, compression=False):
    options = {}
    if compression:
        options['complib'] = _default_compressor
    with ensure_clean_store(path, 'w', **options) as store:
        store.put('obj', obj, format='table')
        retrieved = store['obj']
        comparator(retrieved, obj)