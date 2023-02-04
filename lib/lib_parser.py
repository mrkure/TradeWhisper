# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:07:30 2023

@author: mrkure
"""
import re

class StringParser:
    def __init__(self):
        self.comp = re.compile(r'.+@From (.+): Hi, I would like to buy your (.+) for my (.+) in')

    def evaluate_string(self, string):
        string = re.sub('<.+> ', '', string)
        string = re.sub("I'd like to buy your", 'I would like to buy your', string)
        string = re.sub(" listed for ", ' for my ', string)        
        result = self.comp.findall(string)
        
        if result:           
            self.buyer = result[0][0]
            self.item  = result[0][1]
            self.price = result[0][2]
            return True
        return False
# =============================================================================
#     
# =============================================================================
if __name__ == '__main__':
    
    s2 = r'@From theallendance: Hi, I would like to buy your Damnation Slippers, Crusader Boots listed for 5 chaos in Sanctum (stash tab "~price 5 chaos"; position: left 1, top 6)'
    s2 = r"2022/12/14 16:56:33 3009395281 cffb0734 [INFO Client 26192] @From hehepitcca: Hi, I'd like to buy your 600 Wild Crystallised Lifeforce for my 10 Chaos Orb in Sanctum"
    # s2 = r"2023/01/11 17:14:06 680274312 cffb0734 [INFO Client 26536] @From <*PLS*> EatIchsCharlie: Hi, I'd like to buy your 500 Orb of Alteration for my 50 Chaos Orb in Sanctum"
    s2 = 'asdfs'

    parser = StringParser()
    result = parser.evaluate_string(s2)
    if result:    
        print(parser.buyer)
        print(parser.item)
        print(parser.price)
    else:
        print('not evaluated')





























