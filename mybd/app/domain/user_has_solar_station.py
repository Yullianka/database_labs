from __future__ import annotations
from typing import Dict, Any
from app import db


class UserHasSolarStation(db.Model):
    __tablename__ = 'users_has_solar_station'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'), nullable=False)

    def __repr__(self) -> str:
        return (f"UserHasSolarStation(id='{self.id}', users_id='{self.users_id}', "
                f"solar_station_id='{self.solar_station_id}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'users_id': self.users_id,
            'solar_station_id': self.solar_station_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserHasSolarStation:
        user_has_solar_station = UserHasSolarStation(
            users_id=dto_dict.get('users_id'),
            solar_station_id=dto_dict.get('solar_station_id'),
        )
        return user_has_solar_station
