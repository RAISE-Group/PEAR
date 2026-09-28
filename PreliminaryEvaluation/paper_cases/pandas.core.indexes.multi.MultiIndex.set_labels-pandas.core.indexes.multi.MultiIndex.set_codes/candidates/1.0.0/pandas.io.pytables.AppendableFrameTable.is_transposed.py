@property
def is_transposed(self) -> bool:
    return self.index_axes[0].axis == 1