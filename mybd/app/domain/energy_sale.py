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
    
def insert_energy_sales(n):
    energy_sales = [
        EnergySale(
            timestamp=f"2024-11-{20 + i} 10:00:00",
            energy_sold=f"{100 + i * 10} kWh",
            price_per_kw=f"{0.15 + i * 0.01} USD",
            energy_selected=f"{90 + i * 5} kWh",
            solar_station_id=1  
        )
        for i in range(n)
    ]

    try:
        db.session.bulk_save_objects(energy_sales)
        db.session.commit()
        return energy_sales
    except Exception as e:
        db.session.rollback()
        print(f"Error inserting energy sales: {e}")
        return -1
