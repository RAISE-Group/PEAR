def validate_attr(self, append: bool):
    if append:
        existing_kind = getattr(self.attrs, self.kind_attr, None)
        if existing_kind is not None and existing_kind != self.kind:
            raise TypeError(f'incompatible kind in col [{existing_kind} - {self.kind}]')