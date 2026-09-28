@cache_readonly
def is_na(self):
    if self.block is None:
        return True
    if not self.block._can_hold_na:
        return False
    values = self.block.values
    if self.block.is_categorical:
        values_flat = values.categories
    elif is_sparse(self.block.values.dtype):
        return False
    elif self.block.is_extension:
        values_flat = values
    else:
        values_flat = values.ravel(order='K')
    total_len = values_flat.shape[0]
    chunk_len = max(total_len // 40, 1000)
    for i in range(0, total_len, chunk_len):
        if not isna(values_flat[i:i + chunk_len]).all():
            return False
    return True