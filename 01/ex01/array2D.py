def slice_me(fam: list, start: int, end: int) -> list:
    """slice_me function"""
    assert isinstance(fam, list) and all(isinstance(i, list) for i in fam), "f\
            am is not 2Darray"
    assert isinstance(start, int) and isinstance(end, int), "start and end \
            aren't int"
    assert all(len(i) == len(fam[0]) for i in fam), "fam is not list \
            of lists of same size"
    assert start <= len(fam) or end <= len(fam), "start or end too big"
    if fam == []:
        print("My shape is : (0, 0)")
    else:
        print(f"My shape is : ({len(fam)}, {len(fam[0])})")
    slice_object = slice(start, end)
    new_fam = fam[slice_object]
    if new_fam == []:
        print("My new shape is : (0, 0)")
    else:
        print(f"My new shape is : ({len(new_fam)}, {len(new_fam[0])})")
    return new_fam
