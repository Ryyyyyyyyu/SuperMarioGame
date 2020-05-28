import json
import os

import pygame
from .. import  constants as C
from .. import tools, setup


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_data()
        self.setup_states()
        self.setup_velocities()
        self.setup_timer()
        self.load_images()

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def load_data(self):
        file_name = self.name + '.json'
        file_path = os.path.join(r'F:\pyCharm projects\SuperMaryGame\source\data\player', file_name)
        with open(file_path) as f:
            self.play_date = json.load(f)

    def setup_states(self):
        self.state = 'walk'
        self.face_right = True
        self.deas = False
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timer(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['mario_bros']
        frame_rects = self.play_date['image_frames']

        self.right_small_normal_frames = []
        self.right_big_normal_frames = []
        self.right_big_fire_frames = []
        self.left_small_normal_frames = []
        self.left_big_normal_frames = []
        self.left_big_fire_frames = []

        self.small_normal_frames = [self.right_small_normal_frames, self.left_small_normal_frames]
        self.big_normal_frames = [self.right_big_normal_frames, self.left_big_normal_frames]
        self.big_fire_frames = [self.right_big_fire_frames, self.left_big_fire_frames]

        self.all_frames = [
            self.right_small_normal_frames,
            self.right_big_normal_frames,
            self.right_big_fire_frames,
            self.left_small_normal_frames,
            self.left_big_normal_frames,
            self.left_big_fire_frames
        ]
        self.right_frames = self.right_small_normal_frames
        self.left_frames= self.left_small_normal_frames

        for group,group_farme_rects in frame_rects.items():
            for frame_rect in group_farme_rects:
                right_image = tools.get_image(sheet, frame_rect['x'],frame_rect['y'], frame_rect['width'], frame_rect['height'], (0, 0, 0), C.PLAYER_MULTI)
                left_image = pygame.transform.flip(right_image, True, False)
                if group == 'right_small_normal':
                    self.right_small_normal_frames.append(right_image)
                    self.left_small_normal_frames.append(left_image)
                if group == 'right_big_normal':
                    self.right_big_normal_frames.append(right_image)
                    self.left_big_normal_frames.append(left_image)
                if group == 'right_big_fire':
                    self.right_big_fire_frames.append(right_image)
                    self.left_big_fire_frames.append(left_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.state = 'walk'
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        if keys[pygame.K_LEFT]:
            self.state = 'walk'
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames

        if self.state == 'walk':
            if self.current_time - self.walking_timer > 100:
                self.walking_timer = self.current_time
                self.frame_index += 1
                self.frame_index %= 4

        self.image = self.frames[self.frame_index]
