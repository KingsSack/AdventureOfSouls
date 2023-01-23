import pygame

attacking = "false"

idle_right_images = []
for i in range(12):
    idle_right_images.append(pygame.image.load(f'wizard/WizardIdle1-{i + 1}.png'))
idle_right_fps = 6
idle_right_index = 0

idle_left_images = []
for i in range(12):
    idle_left_images.append(pygame.image.load(f'wizard/WizardIdle2-{i + 1}.png'))
idle_left_fps = 6
idle_left_index = 0

hurt_right_images = []
for i in range(3):
    hurt_right_images.append(pygame.image.load(f'wizard/WizardHurt1-{i}.png'))
hurt_right_fps = 10
hurt_right_index = 0

hurt_left_images = []
for i in range(3):
    hurt_left_images.append(pygame.image.load(f'wizard/WizardHurt2-{i}.png'))
hurt_left_fps = 10
hurt_left_index = 0

death_right_images = []
for i in range(20):
    death_right_images.append(pygame.image.load(f'wizard/WizardDie1-{i}.png'))
death_right_fps = 5
death_right_index = 0

death_left_images = []
for i in range(20):
    death_left_images.append(pygame.image.load(f'wizard/WizardDie2-{i}.png'))
death_left_fps = 5
death_left_index = 0

walk_right_images = []
for i in range(4):
    walk_right_images.append(pygame.image.load(f'wizard/WizardWalk1-{i + 1}.png'))
walk_right_fps = 4
walk_right_index = 0

walk_left_images = []
for i in range(4):
    walk_left_images.append(pygame.image.load(f'wizard/WizardWalk2-{i + 1}.png'))
walk_left_fps = 4
walk_left_index = 0

wizard_bomb_right_images = []
for i in range(27):
    wizard_bomb_right_images.append(pygame.image.load(f'wizard/WizardFirebomb1-{i}.png'))
wizard_bomb_right_fps = 15
wizard_bomb_right_index = 0

wizard_bomb_left_images = []
for i in range(27):
    wizard_bomb_left_images.append(pygame.image.load(f'wizard/WizardFirebomb2-{i}.png'))
wizard_bomb_left_fps = 15
wizard_bomb_left_index = 0

wizard_thunder_right_images = []
for i in range(30):
    wizard_thunder_right_images.append(pygame.image.load(f'wizard/WizardThunder2-{i}.png'))
wizard_thunder_right_fps = 5
wizard_thunder_right_index = 0

wizard_thunder_left_images = []
for i in range(30):
    wizard_thunder_left_images.append(pygame.image.load(f'wizard/WizardThunder2-{i}.png'))
wizard_thunder_left_fps = 5
wizard_thunder_left_index = 0

wizard_shadow_right_images = []
for i in range(33):
    wizard_shadow_right_images.append(pygame.image.load(f'wizard/WizardShadow1-{i}.png'))
wizard_shadow_right_fps = 5
wizard_shadow_right_index = 0

wizard_shadow_left_images = []
for i in range(33):
    wizard_shadow_left_images.append(pygame.image.load(f'wizard/WizardShadow2-{i}.png'))
wizard_shadow_left_fps = 5
wizard_shadow_left_index = 0

wizard_sprint_right_images = []
for i in range(5):
    wizard_sprint_right_images.append(pygame.image.load(f'wizard/WizardSprint1-{i}.png'))
wizard_sprint_right_fps = 4
wizard_sprint_right_index = 0

wizard_sprint_left_images = []
for i in range(5):
    wizard_sprint_left_images.append(pygame.image.load(f'wizard/WizardSprint2-{i}.png'))
wizard_sprint_left_fps = 4
wizard_sprint_left_index = 0


slime_idle_images = []
for i in range(24):
    slime_idle_images.append(pygame.image.load("slime/SlimeIdle-0.png"))
for i in range(24):
    slime_idle_images.append(pygame.image.load("slime/SlimeIdle-1.png"))
slime_idle_index = 0

slime_hurt_images = []
for i in range(24):
    slime_hurt_images.append(pygame.image.load("slime/SlimeHurt-0.png"))
for i in range(24):
    slime_hurt_images.append(pygame.image.load("slime/SlimeHurt-1.png"))
for i in range(24):
    slime_hurt_images.append(pygame.image.load("slime/SlimeHurt-2.png"))
slime_hurt_index = 0

slime_jump_images = []
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-0.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-1.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-2.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-3.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-4.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-5.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-6.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-7.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-8.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-9.png"))
for i in range(5):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-10.png"))
slime_jump_index = 0


glow_images = []
for i in range(24):
    glow_images.append(pygame.image.load("menu/Sparkle1.png"))
for i in range(24):
    glow_images.append(pygame.image.load("menu/Sparkle2.png"))
for i in range(24):
    glow_images.append(pygame.image.load("menu/Sparkle3.png"))
glow_index = 0
