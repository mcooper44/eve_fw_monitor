from dataclasses import dataclass

@dataclass
class zkill_km:
    __slots__ = ['killmail_id', 'locationID', 'hash', 'fittedValue',
                 'totalValue', 'points', 'npc', 'solo', 'awox']
    killmail_id: int
    locationID: int
    hash: str
    fittedValue: float
    totalValue: float
    points: int
    npc: str
    solo: str
    awox: str

