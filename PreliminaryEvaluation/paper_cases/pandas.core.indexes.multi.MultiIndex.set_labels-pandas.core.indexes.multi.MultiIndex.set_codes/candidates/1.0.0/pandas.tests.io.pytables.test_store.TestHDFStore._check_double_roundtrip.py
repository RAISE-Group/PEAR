def _check_double_roundtrip(self, obj, comparator, path, compression=False, **kwargs):
    options = {}
    if compression:
        options['complib'] = compression or _default_compressor
    with ensure_clean_store(path, 'w', **options) as store:
        store['obj'] = obj
        retrieved = store['obj']
        comparator(retrieved, obj, **kwargs)
        store['obj'] = retrieved
        again = store['obj']
        comparator(again, obj, **kwargs)