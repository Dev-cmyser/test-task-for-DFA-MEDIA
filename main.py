import sqlalchemy
from sqlalchemy import create_engine
from models import engine
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.orm import Session
from middlewar import add_data_to_db, parse_exel


def main():

    csv_gen = parse_exel()
    for data in csv_gen:
        print(f"Добавляю следущую запись: {data}")
        add_data_to_db(data)


if __name__ == "__main__":
    main()
