import threading
from datetime import datetime

from database import Database
import threading

query_insert_name = {
    "query_1": "insert into users values ('Bakhrom', 23)",
    "query_2": "insert into users values ('Nodir', 24)",
    "query_3": "insert into users values ('Salim', 22)",
    "query_4": "insert into users values ('Shahzod', 23)",
    "query_5": "insert into users values ('Shohnur', 24)",
    "query_6": "insert into users values ('Dilshod', 24)",
    "query_7": "insert into users values ('Sherbek', 23)",
    "query_8": "insert into users values ('Kamronbek', 19)",
    "query_9": "insert into users values ('Shohruh', 21)",
    "query_10": "insert into users values ('Diyorbek', 23)"
}


def insert_data(query, query_type):
    print(Database.connect(query, query_type))


def multhproces():
    query_1 = "insert into users values ('Bakhrom', 23)",
    query_2 = "insert into users values ('Nodir', 24)",
    query_3 = "insert into users values ('Salim', 22)",
    query_4 = "insert into users values ('Shahzod', 23)",
    query_5 = "insert into users values ('Shohnur', 24)",
    query_6 = "insert into users values ('Dilshod', 24)",
    query_7 = "insert into users values ('Sherbek', 23)",
    query_8 = "insert into users values ('Kamronbek', 19)",
    query_9 = "insert into users values ('Shohruh', 21)",
    query_10 = "insert into users values ('Diyorbek', 23)"

    query_type_1 = "insert"

    multhpoces_1 = threading.Thread(target=insert_data, args=(query_1, query_type_1))
    multhpoces_2 = threading.Thread(target=insert_data, args=(query_2, query_type_1))
    multhpoces_3 = threading.Thread(target=insert_data, args=(query_3, query_type_1))
    multhpoces_4 = threading.Thread(target=insert_data, args=(query_4, query_type_1))
    multhpoces_5 = threading.Thread(target=insert_data, args=(query_5, query_type_1))
    multhpoces_6 = threading.Thread(target=insert_data, args=(query_6, query_type_1))
    multhpoces_7 = threading.Thread(target=insert_data, args=(query_7, query_type_1))
    multhpoces_8 = threading.Thread(target=insert_data, args=(query_8, query_type_1))
    multhpoces_9 = threading.Thread(target=insert_data, args=(query_9, query_type_1))
    multhpoces_10 = threading.Thread(target=insert_data, args=(query_10, query_type_1))

    multhpoces_1.start()
    multhpoces_2.start()
    multhpoces_3.start()
    multhpoces_4.start()
    multhpoces_5.start()
    multhpoces_6.start()
    multhpoces_7.start()
    multhpoces_8.start()
    multhpoces_9.start()
    multhpoces_10.start()

    multhpoces_1.join()
    multhpoces_2.join()
    multhpoces_3.join()
    multhpoces_4.join()
    multhpoces_5.join()
    multhpoces_6.join()
    multhpoces_7.join()
    multhpoces_8.join()
    multhpoces_9.join()
    multhpoces_10.join()


if __name__ == '__main__':
    print(datetime.now())
    multhproces()
    print(datetime.now())
