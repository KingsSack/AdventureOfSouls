import pygame

attacking = "false"

idle_right_images = []
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-1.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-2.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-3.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-4.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-5.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-6.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-7.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-8.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-9.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-10.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-11.png"))
for i in range(24):
    idle_right_images.append(pygame.image.load("wizard/WizardIdle1-12.png"))
idle_right_index = 0

idle_left_images = []
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-1.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-2.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-3.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-4.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-5.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-6.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-7.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-8.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-9.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-10.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-11.png"))
for i in range(24):
    idle_left_images.append(pygame.image.load("wizard/WizardIdle2-12.png"))
idle_left_index = 0

hurt_right_images = []
for i in range(20):
    hurt_right_images.append(pygame.image.load("wizard/WizardHurt1-0.png"))
for i in range(20):
    hurt_right_images.append(pygame.image.load("wizard/WizardHurt1-1.png"))
for i in range(20):
    hurt_right_images.append(pygame.image.load("wizard/WizardHurt1-2.png"))
hurt_right_index = 0

hurt_left_images = []
for i in range(20):
    idle_left_images.append(pygame.image.load("wizard/WizardHurt2-0.png"))
for i in range(20):
    idle_left_images.append(pygame.image.load("wizard/WizardHurt2-1.png"))
for i in range(20):
    idle_left_images.append(pygame.image.load("wizard/WizardHurt2-2.png"))
hurt_left_index = 0

death_right_images = []
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-0.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-1.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-2.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-3.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-4.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-5.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-6.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-7.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-8.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-9.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-10.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-11.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-12.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-13.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-14.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-15.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-16.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-17.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-18.png"))
for i in range(14):
    death_right_images.append(pygame.image.load("wizard/WizardDie1-19.png"))
death_right_index = 0

death_left_images = []
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-0.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-1.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-2.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-3.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-4.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-5.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-6.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-7.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-8.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-9.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-10.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-11.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-12.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-13.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-14.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-15.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-16.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-17.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-18.png"))
for i in range(14):
    death_left_images.append(pygame.image.load("wizard/WizardDie2-19.png"))
death_left_index = 0

walk_right_images = []
for i in range(24):
    walk_right_images.append(pygame.image.load("wizard/WizardWalk1-1.png"))
for i in range(24):
    walk_right_images.append(pygame.image.load("wizard/WizardWalk1-2.png"))
for i in range(24):
    walk_right_images.append(pygame.image.load("wizard/WizardWalk1-3.png"))
for i in range(24):
    walk_right_images.append(pygame.image.load("wizard/WizardWalk1-4.png"))
walk_right_index = 0

walk_left_images = []
for i in range(24):
    walk_left_images.append(pygame.image.load("wizard/WizardWalk2-1.png"))
for i in range(24):
    walk_left_images.append(pygame.image.load("wizard/WizardWalk2-2.png"))
for i in range(24):
    walk_left_images.append(pygame.image.load("wizard/WizardWalk2-3.png"))
for i in range(24):
    walk_left_images.append(pygame.image.load("wizard/WizardWalk2-4.png"))
walk_left_index = 0

wizard_bomb_right_images = []
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-0.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-1.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-2.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-3.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-4.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-5.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-6.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-7.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-8.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-9.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-10.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-11.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-12.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-13.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-14.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-15.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-16.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-17.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-18.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-19.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-20.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-21.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-22.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-23.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-24.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-25.png"))
for i in range(12):
    wizard_bomb_right_images.append(pygame.image.load("wizard/WizardFirebomb1-26.png"))
wizard_bomb_right_index = 0

wizard_bomb_left_images = []
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-0.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-1.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-2.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-3.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-4.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-5.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-6.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-7.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-8.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-9.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-10.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-11.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-12.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-13.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-14.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-15.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-16.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-17.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-18.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-19.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-20.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-21.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-22.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-23.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-24.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-25.png"))
for i in range(12):
    wizard_bomb_left_images.append(pygame.image.load("wizard/WizardFirebomb2-26.png"))
wizard_bomb_left_index = 0

wizard_thunder_right_images = []
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-0.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-1.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-2.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-3.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-4.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-5.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-6.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-7.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-8.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-9.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-10.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-11.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-12.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-13.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-14.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-15.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-16.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-17.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-18.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-19.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-20.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-21.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-22.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-23.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-24.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-25.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-26.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-27.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-28.png"))
for i in range(12):
    wizard_thunder_right_images.append(pygame.image.load("wizard/WizardThunder2-29.png"))
wizard_thunder_right_index = 0

wizard_thunder_left_images = []
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-0.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-1.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-2.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-3.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-4.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-5.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-6.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-7.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-8.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-9.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-10.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-11.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-12.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-13.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-14.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-15.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-16.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-17.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-18.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-19.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-20.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-21.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-22.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-23.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-24.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-25.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-26.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-27.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-28.png"))
for i in range(12):
    wizard_thunder_left_images.append(pygame.image.load("wizard/WizardThunder2-29.png"))
wizard_thunder_left_index = 0

wizard_shadow_right_images = []
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-0.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-1.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-2.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-3.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-4.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-5.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-6.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-7.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-8.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-9.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-10.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-11.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-12.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-13.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-14.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-15.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-16.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-17.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-18.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-19.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-20.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-21.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-22.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-23.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-24.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-25.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-26.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-27.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-28.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-29.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-30.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-31.png"))
for i in range(12):
    wizard_shadow_right_images.append(pygame.image.load("wizard/WizardShadow1-32.png"))
wizard_shadow_right_index = 0

wizard_shadow_left_images = []
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-0.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-1.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-2.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-3.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-4.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-5.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-6.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-7.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-8.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-9.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-10.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-11.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-12.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-13.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-14.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-15.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-16.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-17.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-18.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-19.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-20.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-21.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-22.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-23.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-24.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-25.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-26.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-27.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-28.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-29.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-30.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-31.png"))
for i in range(12):
    wizard_shadow_left_images.append(pygame.image.load("wizard/WizardShadow2-32.png"))
wizard_shadow_left_index = 0

wizard_sprint_right_images = []
for i in range(15):
    wizard_sprint_right_images.append(pygame.image.load("wizard/WizardSprint1-0.png"))
for i in range(15):
    wizard_sprint_right_images.append(pygame.image.load("wizard/WizardSprint1-1.png"))
for i in range(15):
    wizard_sprint_right_images.append(pygame.image.load("wizard/WizardSprint1-2.png"))
for i in range(15):
    wizard_sprint_right_images.append(pygame.image.load("wizard/WizardSprint1-3.png"))
for i in range(15):
    wizard_sprint_right_images.append(pygame.image.load("wizard/WizardSprint1-4.png"))
wizard_sprint_right_index = 0

wizard_sprint_left_images = []
for i in range(15):
    wizard_sprint_left_images.append(pygame.image.load("wizard/WizardSprint2-0.png"))
for i in range(15):
    wizard_sprint_left_images.append(pygame.image.load("wizard/WizardSprint2-1.png"))
for i in range(15):
    wizard_sprint_left_images.append(pygame.image.load("wizard/WizardSprint2-2.png"))
for i in range(15):
    wizard_sprint_left_images.append(pygame.image.load("wizard/WizardSprint2-3.png"))
for i in range(15):
    wizard_sprint_left_images.append(pygame.image.load("wizard/WizardSprint2-4.png"))
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
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-0.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-1.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-2.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-3.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-4.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-5.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-6.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-7.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-8.png"))
for i in range(8):
    slime_jump_images.append(pygame.image.load("slime/SlimeJump-9.png"))
for i in range(8):
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
