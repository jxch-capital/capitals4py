from capitals4py import container


def test_get_data_cn():
    container.qlib_service().qlib_data("cn")


def test_get_data_us():
    container.qlib_service().qlib_data("us")
