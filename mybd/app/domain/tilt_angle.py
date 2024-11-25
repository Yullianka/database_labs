from __future__ import annotations
from typing import Dict, Any
from app import db


class TiltAngle(db.Model):
    __tablename__ = 'tilt_angles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.String(45), nullable=False)
    tilt_angle = db.Column(db.String(45), nullable=False)
    panel_id = db.Column(db.Integer, db.ForeignKey('panel.id'), nullable=False)

    def __repr__(self) -> str:
        return f"TiltAngle(id='{self.id}', timestamp='{self.timestamp}', tilt_angle='{self.tilt_angle}', panel_id='{self.panel_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'tilt_angle': self.tilt_angle,
            'panel_id': self.panel_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TiltAngle:
        return TiltAngle(
            timestamp=dto_dict.get('timestamp'),
            tilt_angle=dto_dict.get('tilt_angle'),
            panel_id=dto_dict.get('panel_id')
        )



