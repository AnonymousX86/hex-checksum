# -*- coding: utf-8 -*-
def calculate_checksum(filename: str) -> str:
    with open(filename, 'rb') as f:
        data = f.read()
    
    byte_sum = sum(data)
    hex_sum = hex(byte_sum)[2:]
    
    while len(hex_sum) < 4:
        hex_sum = '0' + hex_sum
    
    return hex_sum.upper()
