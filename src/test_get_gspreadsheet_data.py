import copy
import datetime
import get_gspreadsheet_data


def test_filter_by_time():
    mock_data = [[u'\u6642\u9593\u6233\u8a18', u'\ufffd\u59d3\u540d\u6216\u66b1\u7a31', u'\u96fb\u5b50\u90f5\u4ef6', u'\u6240\u5728\u5730', u'\u5e6b\u52a9\u4f7f\u7528\u8005', u'\u54c1\u8cea\u6aa2\u6e2c', u'\u5beb\u7a0b\u5f0f', u'\u5354\u52a9\u5ba3\u50b3', u'\u5728\u5730\u5316\u8207\u7ffb\u8b6f', u'\u7db2\u9801\u958b\u767c', u'\u9644\u52a0\u5143\u4ef6', u'\u8996\u89ba\u8a2d\u8a08', u'\u64b0\u5beb\u6587\u4ef6', u'\u6559\u80b2', u'\u5176\u4ed6', u'\u6211\u6709\u95dc\u65bc Firefox \u7684\u5efa\u8b70\u6216\u554f\u984c', u'\u7559\u500b\u8a00\u7d66\u6211\u5011\uff0c\u8b93\u6211\u5011\u66f4\u52a0\u4e86\u89e3\u60a8\u7684\u6280\u80fd\u6216\u554f\u984c\u7d30\u7bc0'], [u'2016-09-09-13:15:46', 'asdfsdfdf', 'irvinf@gadfas.dsffa', u'\u6e2f\u6fb3', u'\u5e6b\u52a9\u4f7f\u7528\u8005', '', '', u'\u5354\u52a9\u5ba3\u50b3', '', '', '', u'\u8996\u89ba\u8a2d\u8a08', '', '', u'\u5176\u4ed6', '', 'dsafsdfdsfsfsfafsddfsdfa']]
    temp_row = copy.deepcopy(mock_data[1])
    temp_row[0] = "2014-01-01-11:00:00"
    mock_data.append(temp_row)
    expected = [mock_data[1]]

    output = get_gspreadsheet_data.filter_by_time(mock_data,
                                                  datetime.datetime(2015, 1, 1,
                                                                    0, 0))
    assert(len(expected) == len(output))
    assert(expected == output)
