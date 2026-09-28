def __repr__(self) -> str:
    prepr = f"[{','.join(map(pprint_thing, self))}]"
    return f'{type(self).__name__}({prepr})'