def onOffset(self, dt):
    warnings.warn('onOffset is a deprecated, use is_on_offset instead', FutureWarning, stacklevel=2)
    return self.is_on_offset(dt)