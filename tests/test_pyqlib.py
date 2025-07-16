import qlib
from qlib.data import D

def test_simple_data():
    qlib.init(provider_uri=r"D:\jxch-capital\capitals4py\data\qlib\data\us", region="us")
    # 取有数据的时间区间
    df = D.features(
        ["AAPL"], ["$close", "EMA($close, 20)"],
        start_time="2010-09-01", end_time="2011-09-25"
    )
    print(df.head())
    assert not df.empty
