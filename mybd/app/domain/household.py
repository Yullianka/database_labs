from __future__ import annotations
from typing import Dict, Any
from app import db
from random import randint, choice
from time import time
from sqlalchemy import text


class Household(db.Model):
    __tablename__ = 'households'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(45), unique=True)
    users_id = db.Column(db.Integer)
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Household({self.id}, address='{self.address}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'address': self.address,
            'users_id': self.users_id,
            'solar_station_id': self.solar_station_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Household:
        return Household(
            address=dto_dict.get('address'),
            users_id=dto_dict.get('users_id'),
            solar_station_id=dto_dict.get('solar_station_id'),
        )
    
def create_dynamic_tables_from_household():
    household = Household.query.all()
    if not household:
        return "No leagues found in the database."

    table_count = randint(1, 9)
    created_tables = []

    for household in household[:table_count]:
        household_address = household.address.replace(" ", "_")
        table_name = f"{household_address}_{int(time())}"

        column_defs = []
        for i in range(randint(1, 9)):
            column_address = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_address} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {column_defs_str});")

        db.session.execute(create_table_sql)
        db.session.commit()
        created_tables.append(table_name)

    return created_tables
