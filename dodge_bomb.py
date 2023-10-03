import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    enn_width = 800
    enn_height = 450
    vx = 5
    vy = 5
    tmr = 0
    total_move = [0,0]
    key_lst = {"up":(0, -5),"down":(0,5),"left":(-5,0),"right":(5,0)}
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        pg.K_UP 

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(enn, [enn_width, enn_height])
        pg.display.update()
        enn_width += vx
        enn_height += vy
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()