

def parse_list_output(stream):
    stream = iter(stream.splitlines())
    header_ = next(stream)
    header = header_.split()
    info = [(x, header_.index(x)) for x in header]
    i1 = iter(info + [(None, None)])
    i2 = iter(info)
    next(i1)  # To offset the lists.
    split = zip(i2, i1)

    for entry in stream:
        entries = {}
        for fro, to in split:
            name, start = fro
            _, end = to
            if end is None:
                entries[name] = entry[start]
            else:
                entries[name] = entry[start:end]
            entries[name] = entries[name].strip()
        yield entries
