import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = { pg.K_UP:(0, -5),
                pg.K_DOWN:(0, 5),
                pg.K_LEFT:(-5, 0),
                pg.K_RIGHT:(5, 0)
    }

def check_bound(obj_rct: pg.Rect):
    """
    引数:こうかとんRectかばくだんRect
    戻り値:タプル(横判定効果,縦判定効果))
    """
    yoko = True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: #横方向判定
        yoko = False
    
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    #こうかとん
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900,400) #こうかとんの初期座標

    clock = pg.time.Clock()
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    enn_width = 800
    enn_height = 450
    vx,vy = 5,5
    tmr = 0

    #こうかとん移動量の辞書
    kk_width = 900
    kk_height = 450
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, [0,0])

        #こうかとん移動
        key_list = pg.key.get_pressed()
        sum_mv = [0,0] 
        for key, mv in delta.items():
            if key_list[key]:
                sum_mv[0] += mv[0] #横方向の合計移動量
                sum_mv[1] += mv[1] #縦方向の合計移動量
        kk_rct.move_ip(sum_mv[0],sum_mv[1])
        screen.blit(kk_img,kk_rct)
        #爆弾
        screen.blit(enn, [enn_width, enn_height])
        pg.display.update()
        enn_width += vx
        enn_height += vy
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()