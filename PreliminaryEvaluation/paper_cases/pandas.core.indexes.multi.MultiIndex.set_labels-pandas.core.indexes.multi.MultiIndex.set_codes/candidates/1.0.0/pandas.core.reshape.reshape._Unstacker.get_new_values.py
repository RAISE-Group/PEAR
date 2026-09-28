def get_new_values(self):
    values = self.values
    length, width = self.full_shape
    stride = values.shape[1]
    result_width = width * stride
    result_shape = (length, result_width)
    mask = self.mask
    mask_all = mask.all()
    if mask_all and len(values):
        new_values = self.sorted_values.reshape(length, width, stride).swapaxes(1, 2).reshape(result_shape)
        new_mask = np.ones(result_shape, dtype=bool)
        return (new_values, new_mask)
    if mask_all:
        dtype = values.dtype
        new_values = np.empty(result_shape, dtype=dtype)
    else:
        dtype, fill_value = maybe_promote(values.dtype, self.fill_value)
        new_values = np.empty(result_shape, dtype=dtype)
        new_values.fill(fill_value)
    new_mask = np.zeros(result_shape, dtype=bool)
    name = np.dtype(dtype).name
    sorted_values = self.sorted_values
    if needs_i8_conversion(values):
        sorted_values = sorted_values.view('i8')
        new_values = new_values.view('i8')
    elif is_bool_dtype(values):
        sorted_values = sorted_values.astype('object')
        new_values = new_values.astype('object')
    else:
        sorted_values = sorted_values.astype(name, copy=False)
    libreshape.unstack(sorted_values, mask.view('u1'), stride, length, width, new_values, new_mask.view('u1'))
    if needs_i8_conversion(values):
        new_values = new_values.view(values.dtype)
    return (new_values, new_mask)