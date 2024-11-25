from __future__ import annotations
from typing import Dict, Any
from app import db


class BatteryCharge(db.Model):
    __tablename__ = 'battery_charge'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.String(45))
    charge_level_per_hour = db.Column(db.String(45))
    date = db.Column(db.String(45))
    time = db.Column(db.String(45))
    battery_id = db.Column(db.Integer, db.ForeignKey('battery.id'), nullable=False)

    def __repr__(self) -> str:
        return f"BatteryCharge({self.id}, timestamp='{self.timestamp}', charge_level='{self.charge_level_per_hour}', date='{self.date}', time='{self.time}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'charge_level_per_hour': self.charge_level_per_hour,
            'date': self.date,
            'time': self.time,
            'battery_id': self.battery_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BatteryCharge:
        return BatteryCharge(
            timestamp=dto_dict.get('timestamp'),
            charge_level_per_hour=dto_dict.get('charge_level_per_hour'),
            date=dto_dict.get('date'),
            time=dto_dict.get('time'),
            battery_id=dto_dict.get('battery_id'),
        )



