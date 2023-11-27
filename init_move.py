# -*- coding: utf-8 -*-

import math
window_width = 800
window_height = 500

# 隕石移動函數
def init_move(rect):
    
    x_diff = rect.centerx - window_width // 2 # 圖片中心位置和遊戲畫面中心差距(x)
    
    y_diff = rect.centery - window_height // 2 # 圖片中心位置和遊戲畫面中心差距(y)
    
    d = math.sqrt(x_diff ** 2 + y_diff ** 2)
          
    x_move = x_diff / d # 移動量(x)
        
    y_move = y_diff / d # 移動量(y)
        
    
    # 圖片rect上下左右目前位置
    image_right = rect.topright[0]
    image_top = rect.topright[1]
    image_left = rect.topleft[0]
    image_bottom = rect.bottomright[1]
    
    # 有任何一部分在邊界以外，就向遊戲畫面中心移動
    if (image_right> window_width) or (image_left < 0) \
       or (image_top < 0) or (image_bottom > window_height):
           
           rect.centerx = rect.centerx - x_move
           rect.centery = rect.centery - y_move
