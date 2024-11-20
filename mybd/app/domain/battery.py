from __future__ import annotations
from typing import Dict, Any
from app import db


class Battery(db.Model):
    __tablename__ = 'battery'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.Integer)
    capacity = db.Column(db.String(45))
    usage_duration = db.Column(db.String(45))
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'))

    battery_charges = db.relationship('BatteryCharge', backref='battery')

    def __repr__(self) -> str:
        return f"Battery({self.id}, capacity='{self.capacity}', usage_duration='{self.usage_duration}')"

    def put_into_dto(self) -> Dict[str, Any]:
        battery_charges = [battery_charges.put_into_dto() for battery_charges in self.battery_charges]
        return {
            'id': self.id,
            'station_id': self.station_id,
            'capacity': self.capacity,
            'usage_duration': self.usage_duration,
            'solar_station_id': self.solar_station_id,
            'battery_charges': battery_charges if battery_charges else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Battery:
        return Battery(
            station_id=dto_dict.get('station_id'),
            capacity=dto_dict.get('capacity'),
            usage_duration=dto_dict.get('usage_duration'),
            solar_station_id=dto_dict.get('solar_station_id'),
        )
