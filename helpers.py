import pygame
import math

AQUA = (0, 255, 255)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def lengthdir_x(length, angle):
    angle = angle * math.pi / 180
    return length * math.cos(angle)

def lengthdir_y(length, angle):
    angle = angle * math.pi / 180
    return length * -math.sin(angle)

def norm_angle(angle):
    angle = angle%360
    angle = angle if angle <= 180 else angle-360
    return angle

def point_direction(x1, y1, x2, y2):
    return math.atan2((y1-y2), (x2-x1)) * 180 / math.pi

def calc_corners(x, y, w, l, rot):
    theta = math.atan2((w//2), (l//2)) * 180 / math.pi
    length = math.sqrt((w//2)**2 + (l//2)**2)
    fl = (x+round(lengthdir_x(length, norm_angle(rot+theta)),2), y+round(lengthdir_y(length, norm_angle(rot+theta)),2))
    fr = (x+round(lengthdir_x(length, norm_angle(rot-theta)),2), y+round(lengthdir_y(length, norm_angle(rot-theta)),2))

    rot2 = norm_angle(rot+180)
    bl = (x+round(lengthdir_x(length, norm_angle(rot2-theta)),2), y+round(lengthdir_y(length, norm_angle(rot2-theta)),2))
    br = (x+round(lengthdir_x(length, norm_angle(rot2+theta)),2), y+round(lengthdir_y(length, norm_angle(rot2+theta)),2))
    return fl, fr, bl, br

def draw_box(win, box, color):
    p1, p2, p3, p4 = box
    pygame.draw.line(win, color, p1, p2, 1)
    pygame.draw.line(win, color, p2, p4, 1)
    pygame.draw.line(win, color, p4, p3, 1)
    pygame.draw.line(win, color, p3, p1, 1)
