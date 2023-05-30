from src.utils import read_json_data


def test_read_json_data():
    data = read_json_data()
    print(data)
    assert isinstance(data, list)
    assert len(data) > 0


def test_filter_data(data):
    pass


def test_sort_data(data):
    pass


def test_transform_account(line):
    pass


def test_print_transaction(transaction):
    pass


def test_print_last_transactions(data, number):
    pass
