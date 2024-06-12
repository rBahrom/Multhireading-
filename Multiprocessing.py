from datetime import datetime

from database import Database
import multiprocessing

query_insert = {
    "query_1": "insert into car2 values ('Malibu', '2019')",
    "query_2": "insert into car2 values ('Spark', '2022')",
    "query_3": "insert into car2 values ('epica', '2019')",
    "query_4": "insert into car2 values ('nexia', '2012')",
    "query_5": "insert into car2 values ('lacetti', '2015')",
    "query_6": "insert into car2 values ('nexia 3', '2018')",
    "query_7": "insert into car2 values ('captiva', '2017')",
    "query_8": "insert into car2 values ('onix', '2023')",
    "query_9": "insert into car2 values ('matiz', '2010')",
    "query_10": "insert into car2 values ('jigule', '2007')"
}

def insert_data(query, query_type):
    print(Database.connect(query, query_type))


def multreading():
    query_1 = "insert into car2 values ('Malibu', '2019')"
    query_2 = "insert into car2 values ('Spark', '2022')"
    query_3 = "insert into car2 values ('epica', '2019')"
    query_4 = "insert into car2 values ('nexia', '2012')"
    query_5 = "insert into car2 values ('lacetti', '2015')"
    query_6 = "insert into car2 values ('nexia 3', '2018')"
    query_7 = "insert into car2 values ('captiva', '2017')"
    query_8 = "insert into car2 values ('onix', '2023')"
    query_9 = "insert into car2 values ('matiz', '2010')"
    query_10 = "insert into car2 values ('jigule', '2007')"
    query_type_1 = "insert"
    multreading_1 = multiprocessing.Process(target=insert_data, args=(query_1, query_type_1))
    multreading_2 = multiprocessing.Process(target=insert_data, args=(query_2, query_type_1))
    multreading_3 = multiprocessing.Process(target=insert_data, args=(query_3, query_type_1))
    multreading_4 = multiprocessing.Process(target=insert_data, args=(query_4, query_type_1))
    multreading_5 = multiprocessing.Process(target=insert_data, args=(query_5, query_type_1))
    multreading_6 = multiprocessing.Process(target=insert_data, args=(query_6, query_type_1))
    multreading_7 = multiprocessing.Process(target=insert_data, args=(query_7, query_type_1))
    multreading_8 = multiprocessing.Process(target=insert_data, args=(query_8, query_type_1))
    multreading_9 = multiprocessing.Process(target=insert_data, args=(query_9, query_type_1))
    multreading_10 = multiprocessing.Process(target=insert_data, args=(query_10, query_type_1))

    # projectga start berish
    multreading_1.start()
    multreading_2.start()
    multreading_3.start()
    multreading_4.start()
    multreading_5.start()
    multreading_6.start()
    multreading_7.start()
    multreading_8.start()
    multreading_9.start()
    multreading_10.start()

    multreading_1.join()
    multreading_2.join()
    multreading_3.join()
    multreading_4.join()
    multreading_5.join()
    multreading_6.join()
    multreading_7.join()
    multreading_8.join()
    multreading_9.join()
    multreading_10.join()


if __name__ == '__main__':
    print(datetime.now())
    multreading()
    print(datetime.now())

