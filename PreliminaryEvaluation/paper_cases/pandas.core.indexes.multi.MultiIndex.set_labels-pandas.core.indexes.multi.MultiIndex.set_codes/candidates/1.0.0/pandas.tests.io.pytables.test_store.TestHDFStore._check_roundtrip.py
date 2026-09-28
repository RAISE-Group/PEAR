def _check_roundtrip(self, obj, comparator, path, compression=False, **kwargs):
    options = {}
    if compression:
        options['complib'] = _default_compressor
    with ensure_clean_store(path, 'w', **options) as store:
        store['obj'] = obj
        retrieved = store['obj']
        comparator(retrieved, obj, **kwargs)