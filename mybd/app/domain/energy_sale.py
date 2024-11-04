from __future__ import annotations
from typing import Dict, Any
from app import db


class EnergySale(db.Model):
    __tablename__ = 'energy_sales'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.String(45))
    energy_sold = db.Column(db.String(45))
    price_per_kw = db.Column(db.String(45))
    energy_selected = db.Column(db.String(45))
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'), nullable=False)
    

    def __repr__(self) -> str:
        return f"EnergySale({self.id}, timestamp='{self.timestamp}', energy_sold='{self.energy_sold}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'energy_sold': self.energy_sold,
            'price_per_kw': self.price_per_kw,
            'energy_selected': self.energy_selected,
            'solar_station_id': self.solar_station_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EnergySale:
        return EnergySale(
            timestamp=dto_dict.get('timestamp'),
            energy_sold=dto_dict.get('energy_sold'),
            price_per_kw=dto_dict.get('price_per_kw'),
            energy_selected=dto_dict.get('energy_selected'),
            solar_station_id=dto_dict.get('solar_station_id'),
        )
