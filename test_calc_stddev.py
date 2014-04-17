from calc_stddev import stddev

def test_one():
    x = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.86]

    answer = stddev(x)
    answer = round(answer, 2)
    assert answer == 1.92, answer
