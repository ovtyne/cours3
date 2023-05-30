from utils import *

data = read_json_data()
data = filter_data(data)
data = sort_data(data)
print_last_transactions(data, 5)
