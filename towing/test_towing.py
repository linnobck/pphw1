from towing import top_days, day_summary


def test_day_summary_length():
    assert len(day_summary()) == 91


def test_day_summary_ordering():
    summary = day_summary()
    assert summary[0][0] == "07/01/2022"
    assert summary[1][0] == "07/02/2022"
    assert summary[40][0] == "08/10/2022"
    assert summary[-2][0] == "09/28/2022"
    assert summary[-1][0] == "09/29/2022"


def test_say_summary_values():
    summary = day_summary()
    assert summary[0][1] == 5
    assert summary[1][1] == 30
    assert summary[40][1] == 16
    assert summary[-2][1] == 116
    assert summary[-1][1] == 76


def test_top_n3():
    assert top_days(3) == [
        ("09/17/2022", 128),
        ("09/28/2022", 116),
        ("09/24/2022", 94),
    ]


def test_top_n10():
    top10 = top_days(10)
    assert top10 == [
        ("09/17/2022", 128),
        ("09/28/2022", 116),
        ("09/24/2022", 94),
        ("09/08/2022", 89),
        ("09/11/2022", 85),
        ("09/27/2022", 80),
        ("09/07/2022", 78),
        ("09/29/2022", 76),
        ("08/20/2022", 76),
        ("09/16/2022", 74),
    ] or top10 == [
        ("09/17/2022", 128),
        ("09/28/2022", 116),
        ("09/24/2022", 94),
        ("09/08/2022", 89),
        ("09/11/2022", 85),
        ("09/27/2022", 80),
        ("09/07/2022", 78),
        ("08/20/2022", 76),
        ("09/29/2022", 76),
        ("09/16/2022", 74),
    ]
