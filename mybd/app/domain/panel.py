from __future__ import annotations
from typing import Dict, Any
from app import db


class Panel(db.Model):
    __tablename__ = 'panel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(45))
    power = db.Column(db.String(45))
    installation_date = db.Column(db.String(45))
    tilt_angle = db.Column(db.String(45))
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'), nullable=False)

    tilt_angle = db.relationship('TiltAngle', backref='panel')


    def __repr__(self) -> str:
        return f"Panel({self.id}, type='{self.type}', power='{self.power}')"

    def put_into_dto(self) -> Dict[str, Any]:
        tilt_angle = [tilt_angle.put_into_dto() for tilt_angle in self.tilt_angle]


        return {
            'id': self.id,
            'type': self.type,
            'power': self.power,
            'installation_date': self.installation_date,
            'tilt_angle': self.tilt_angle,
            'solar_station_id': self.solar_station_id,
            'tilt_angle': tilt_angle if tilt_angle else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Panel:
        return Panel(
            type=dto_dict.get('type'),
            power=dto_dict.get('power'),
            installation_date=dto_dict.get('installation_date'),
            tilt_angle=dto_dict.get('tilt_angle'),
            solar_station_id=dto_dict.get('solar_station_id'),
        )
