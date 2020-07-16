def distance(strand_a, strand_b):
    length_a = len(strand_a)
    if length_a != len(strand_b):
        raise ValueError("strings must be equal")
    return len([1 for i in range(length_a) if strand_a[i] != strand_b[i]])
    pass
