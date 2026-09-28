@staticmethod
def _hash_categories(categories, ordered: Ordered=True) -> int:
    from pandas.core.util.hashing import hash_array, _combine_hash_arrays, hash_tuples
    from pandas.core.dtypes.common import is_datetime64tz_dtype, _NS_DTYPE
    if len(categories) and isinstance(categories[0], tuple):
        categories = list(categories)
        cat_array = hash_tuples(categories)
    else:
        if categories.dtype == 'O':
            if len({type(x) for x in categories}) != 1:
                hashed = hash((tuple(categories), ordered))
                return hashed
        if is_datetime64tz_dtype(categories.dtype):
            categories = categories.astype(_NS_DTYPE)
        cat_array = hash_array(np.asarray(categories), categorize=False)
    if ordered:
        cat_array = np.vstack([cat_array, np.arange(len(cat_array), dtype=cat_array.dtype)])
    else:
        cat_array = [cat_array]
    hashed = _combine_hash_arrays(iter(cat_array), num_items=len(cat_array))
    return np.bitwise_xor.reduce(hashed)