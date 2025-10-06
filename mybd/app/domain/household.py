from __future__ import annotations
from typing import Dict, Any
from app import db


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
