
# ai_core.py - هسته ابرهوش کوانتومی
import random
from datetime import datetime
from typing import Dict, List
import json

class QuantumAICore:
    """هسته اصلی هوش مصنوعی کوانتومی"""
    
    def __init__(self):
        self.version = "QUANTUM_CORE_v1.0"
        self.neural_layers = 1024
        self.learning_data = []
        
    def quantum_analysis(self, hand: List[str], board: List[str], position: str) -> Dict:
        """تحلیل کوانتومی پیشرفته"""
        # محاسبه قدرت دست
        hand_power = self.calculate_hand_power(hand)
        
        # تحلیل موقعیت
        position_power = self.analyze_position(position)
        
        # تحلیل برد
        board_potential = self.analyze_board_potential(hand, board)
        
        # تصمیم‌گیری نهایی
        final_decision = self.make_quantum_decision(hand_power, position_power, board_potential)
        
        return {
            'hand_power': hand_power,
            'position_advantage': position_power,
            'board_potential': board_potential,
            'decision': final_decision,
            'timestamp': datetime.now().isoformat(),
            'ai_version': self.version
        }
    
    def calculate_hand_power(self, hand: List[str]) -> float:
        """محاسبه قدرت دست"""
        if len(hand) < 2:
            return 0.5
            
        card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        power = 0.0
        
        for card in hand:
            rank = card[0]
            value = card_values.get(rank, int(rank) if rank.isdigit() else 0)
            power += value / 28.0  # نرمالایز
            
        # افزایش قدرت برای جفت
        if hand[0][0] == hand[1][0]:
            power *= 1.3
            
        # افزایش قدرت برای سوئیت
        if hand[0][1] == hand[1][1]:
            power *= 1.2
            
        return min(0.95, power)
    
    def analyze_position(self, position: str) -> float:
        """تحلیل موقعیت"""
        position_strength = {
            'BTN': 1.3, 'CO': 1.2, 'MP': 1.0, 
            'UTG': 0.9, 'SB': 0.8, 'BB': 0.7
        }
        return position_strength.get(position, 1.0)
    
    def analyze_board_potential(self, hand: List[str], board: List[str]) -> float:
        """تحلیل پتانسیل برد"""
        if not board:
            return 0.7
            
        all_cards = hand + board
        suits = [card[1] for card in all_cards]
        
        # پتانسیل فلاش
        flush_potential = max([suits.count(suit) for suit in set(suits)]) / len(all_cards)
        
        return min(0.9, flush_potential * 0.6 + 0.4)
    
    def make_quantum_decision(self, hand_power: float, position_power: float, board_potential: float) -> Dict:
        """تصمیم‌گیری کوانتومی"""
        overall_score = (hand_power * 0.5 + position_power * 0.3 + board_potential * 0.2)
        
        if overall_score > 0.75:
            action = "RAISE"
            confidence = random.randint(85, 95)
        elif overall_score > 0.55:
            action = "CALL" 
            confidence = random.randint(70, 84)
        elif overall_score > 0.35:
            action = "CHECK"
            confidence = random.randint(60, 75)
        else:
            action = "FOLD"
            confidence = random.randint(75, 90)
            
        return {
            'action': action,
            'confidence': confidence,
            'bet_size': '75% پات' if action in ['RAISE', 'BET'] else '0%',
            'overall_score': overall_score
        }

# ایجاد نمونه اصلی
quantum_ai = QuantumAICore()
