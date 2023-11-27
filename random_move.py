# -*- coding: utf-8 -*-

import random
import math
window_width = 800
window_height = 500

# 隕石隨機移動函數
def random_move(meteorite, current_direct=None, r=1, r_dir=(0, 360)):
    
    if current_direct == None:
        
        theda = random.uniform(*r_dir) # 角度
        movex, movey = r * math.cos(theda), r * math.sin(theda)
    
    else:
        
        movex, movey = current_direct # 現在方向
        
        d = math.sqrt(movex ** 2 + movey ** 2) # 移動距離
        
        if d != 0:
            movex, movey = movex / d * r, movey / d * r
            
        else:
            movex, movey = 0, 0
        

    right_over = (movex > 0) and (meteorite.rect.right + movex > window_width)
    left_over = (movex < 0) and (meteorite.rect.left + movex < 0)
    up_over = (movey < 0) and (meteorite.rect.top + movey < 0)
    down_over = (movey > 0) and (meteorite.rect.bottom + movey > window_height)
    
    if (not right_over) and (not left_over):
        meteorite.rect.x = meteorite.rect.x + movex
        signx = 1
    
    elif left_over or right_over:
        meteorite.rect.x = meteorite.rect.x - movex
        signx = -1
        

    if (not up_over) and (not down_over): 
        meteorite.rect.y = meteorite.rect.y + movey
        signy = 1
        
    elif up_over or down_over:
        meteorite.rect.y = meteorite.rect.y - movey
        signy = -1
        
    return signx * movex, signy * movey
