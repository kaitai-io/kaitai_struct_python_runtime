

def test_cycle():
    from kaitaistruct import local_cycle
    data = dict(zip([1, 2, 3, 4, 5], local_cycle([1, 2, 3])))
    assert len(data) == 5
    assert data[5] == 2

    i = 0
    for x in local_cycle([]):
        i += 1
    assert i == 0
