from qlib.data import D
from app import container


def test_simple_data():
    container.qlib_service().qlib_init("us")

    df = D.features(
        ["AAPL"], ["$close", "EMA($close, 20)"],
        start_time="2010-09-01", end_time="2011-09-25"
    )

    print(df.head())
    assert not df.empty
