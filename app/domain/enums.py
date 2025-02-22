from enum import Enum

class MovieFormat(str, Enum):
    TWO_D = '2D'
    THREE_D = '3D'
    IMAX = 'IMAX'
    FOUR_DX = '4DX'

class SeatType(str, Enum):
    STANDARD = 'Standard'
    PREMIUM = 'Premium'
    VIP = 'VIP'
    COUPLE = 'Couple'
    ACCESSIBLE = 'Accessible'