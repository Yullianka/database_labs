from __future__ import annotations
from typing import Dict, Any
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    contact_info = db.Column(db.String(45), unique=True)
    amount_of_station = db.Column(db.Integer)
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'), nullable=False)
    user_station = db.relationship('SolarStation', secondary='users_has_solar_station', back_populates='users')

    def __repr__(self) -> str:
        return f"User({self.id}, name='{self.name}', contact_info='{self.contact_info}')"


    def put_into_dto(self) -> Dict[str, Any]:
        user_station =[user_station.put_into_dto() for user_station in self.user_station ]
        return {
            'id': self.id,
            'name': self.name,
            'contact_info': self.contact_info,
            'amount_of_station': self.amount_of_station,
            'solar_station_id': self.solar_station_id,
            'user_station': user_station if user_station else None

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        return User(
            name=dto_dict.get('name'),
            contact_info=dto_dict.get('contact_info'),
            amount_of_station=dto_dict.get('amount_of_station'),
            solar_station_id=dto_dict.get('solar_station_id'),
        )
    

