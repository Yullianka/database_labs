from __future__ import annotations
from typing import Dict, Any
from app import db
from .user import User
from .solar_station import SolarStation


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
    
    @staticmethod
    def add_user_to_station(user_name: str, station_name: str) -> UserHasSolarStation:
        user = User.query.filter_by(name=user_name).first()
        if not user:
            raise ValueError("User not found")

        station = SolarStation.query.filter_by(name=station_name).first()
        if not station:
            raise ValueError("Station not found")

        user_has_station = UserHasSolarStation(users_id=user.id, solar_station_id=station.id)
        db.session.add(user_has_station)
        db.session.commit()
        return user_has_station
