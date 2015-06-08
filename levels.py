#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from resources import *
from level_class import Level
#--Images Files:
images = None
#=======================================================================
class Level_One(Level):
    limit = (-2000,-500)
    background_color = (208,244,247)
    music_filename = "game_files/In The Forest.ogg"
    def __init__(self,imagesFiles,soundsFiles,player):
        Level.__init__(self,imagesFiles,soundsFiles,player)
        #========================
        global images
        images = imagesFiles
        #========================
        for i in range(0,70*8,70):
            platform = Block((i,430),images["grassMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Block((i,430),images["grassRight"])
        self.platform_list.add(platform)
        
        platform = Platform((280,290),images["grassLeft"])
        self.platform_list.add(platform)
        platform = Platform((350,290),images["grassMid"])
        self.platform_list.add(platform)
        platform = Platform((420,290),images["grassRight"])
        self.platform_list.add(platform)
        
        for i in range(0,210,70):
            platform = Platform((i,220),images["grassMid"])
            self.platform_list.add(platform)
        platform = Platform((210,220),images["grassRight"])
        self.platform_list.add(platform)
        
        platform = Platform((350,70),images["grassHalfLeft"])
        self.platform_list.add(platform)
        for i in range(420,980,70):
            platform = Platform((i,70),images["grassHalfMid"])
            self.platform_list.add(platform)
        platform = Platform((980,70),images["grassHalfRight"])
        self.platform_list.add(platform)
        
        platform = Platform((140,-70),images["grassCliff"])
        self.platform_list.add(platform)
        
        platform = Platform((2170,0),images["grassCliffAlt"])
        self.platform_list.add(platform)
        
        platform = Block((980,430),images["grassLeft"])
        self.platform_list.add(platform)
        
        for i in range(1050,2730,70):
            platform = Block((i,430),images["grassMid"])
            self.platform_list.add(platform)
            
        platform = Platform((1260,-70),images["grassHalfLeft"])
        self.platform_list.add(platform)
        for i in range(1330,1680,70):
            platform = Platform((i,-70),images["grassHalfMid"])
            self.platform_list.add(platform)
            
        platform = Platform((1680,-70),images["grassHalfRight"])
        self.platform_list.add(platform)
        
        movingPlatform = MovingPlatform((630,350),images["grassHalf"])
        movingPlatform.leftLimit = 630
        movingPlatform.rightLimit = 910
        movingPlatform.changeX = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
        
        movingPlatform = MovingPlatform((1130,210),images["grassHalf"])
        movingPlatform.bottomLimit = 280
        movingPlatform.topLimit = -140
        movingPlatform.changeY = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
        

        wall = Block((1610,360),images["brickWall"])
        self.block_list.add(wall)
        wall = Block((1610,290),images["brickWall"])
        self.block_list.add(wall)
        
        wall = Block((2170,360),images["brickWall"])
        self.block_list.add(wall)
        wall = Block((2170,290),images["brickWall"])
        self.block_list.add(wall)

        hud = Block((70,50),images["hud_coin"])
        self.hud_list.add(hud)
        hud = Block((770,190),images["hud_coin"])
        self.hud_list.add(hud)
        hud = Block((1610,70),images["hud_coin"])
        self.hud_list.add(hud)
        
        hud = Block((190,-140),images["hud_coin"])
        self.hud_list.add(hud)
        hud = Block((260,-140),images["hud_coin"])
        self.hud_list.add(hud)
        
        for i in range(560,980,70):
            hud = Block((i,-20),images["hud_coin"])
            self.hud_list.add(hud)
    
        block = MovableBlock((1260,210),images["boxCoin"],images["boxCoin_disabled"],player)
        block.level = self
        self.block_list.add(block)
        
        slime = AnimatedBlock((1190,430),images["slime"])
        slime.image1 = images["slime"]
        slime.image2 = images["slime2"]
        slime.leftLimit = 980
        slime.rightLimit = 1330
        slime.changeX = -2
        slime.level = self
        slime.player = player
        slime.dead_image = images["slimeDead"]
        self.block_list.add(slime)
        
        slime = AnimatedBlock((1330,-70),images["slime"])
        slime.image1 = images["slime"]
        slime.image2 = images["slime2"]
        slime.leftLimit = 1260
        slime.rightLimit = 1680
        slime.changeX = -2
        slime.level = self
        slime.player = player
        slime.dead_image = images["slimeDead"]
        self.block_list.add(slime)
        
        snail = AnimatedBlock((350,70),images["snailWalk1"])
        snail.image1 = images["snailWalk1"]
        snail.image2 = images["snailWalk2"]
        snail.leftLimit = 350
        snail.rightLimit = 980
        snail.changeX = -2
        snail.level = self
        snail.player = player
        snail.is_snail = True
        snail.dead_image = images["snailShell"]
        self.block_list.add(snail)
        
        fish = AnimatedBlock((1750,400),images["fishSwim1"])
        fish.image1 = images["fishSwim1"]
        fish.image2 = images["fishSwim2"]
        fish.leftLimit = 1680
        fish.rightLimit = 2100
        fish.changeX = -2
        fish.level = self
        fish.player = player
        fish.dead_image = images["fishDead"]
        self.block_list.add(fish)
        
        weight = Weight((1400,210),images["weightChained"],player,self.platform_list,self.items_list)
        self.block_list.add(weight)
        
        fly = Fly((630,210),images["fly1"],images["fly2"])
        self.block_list.add(fly)
        
        exit_sign = Block((2590,360),images["signExit"])
        self.items_list.add(exit_sign)
        
        spring = Spring((140,220),images["SpringDown"],player)
        self.block_list.add(spring)
        
        spring = Spring((2380,430),images["SpringDown"],player)
        self.block_list.add(spring)
        
        for i in range(0,490,70):
            item = Block((i,360),images["grassCenter"])
            self.items_list.add(item)
        for i in range(0,280,70):
            item = Block((i,290),images["grassCenter"])
            self.items_list.add(item)
            
        for i in range(1050,1330,58):
            item = Block((i,360),images["fence"])
            self.items_list.add(item)
            
        for i in range(630,980,70):
            water = AnimatedItem((i,430),images["liquidWaterTop_mid"],
                                pygame.transform.flip(images["liquidWaterTop_mid"],True,False))
            self.items_list.add(water)
        
        for i in range(1680,2170,70):
            water = Block((i,360),images["liquidWater"])
            self.items_list.add(water)
            
        for i in range(1680,2170,70):
            water = AnimatedItem((i,290),images["liquidWaterTop_mid"],
                                pygame.transform.flip(images["liquidWaterTop_mid"],True,False))
            self.items_list.add(water)
#=======================================================================            
class Level_Two(Level_One):
    background_color = (222,222,130)
    music_filename = "game_files/Mushroom Theme_0.ogg"
    def __init__(self,imagesFiles,soundsFiles,player):
        Level.__init__(self,imagesFiles,soundsFiles,player)
        #========================
        global images
        images = imagesFiles
        #========================
        for i in range(0,70*5,70):
            platform = Block((i,430),images["sandMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Block((i,430),images["sandRight"])
        self.platform_list.add(platform)
        
        platform = Block((1190,430),images["sandLeft"])
        self.platform_list.add(platform)
        for i in range(1260,2730,70):
            platform = Block((i,430),images["sandMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Block((i,430),images["sandRight"])
        self.platform_list.add(platform)
        
        for i in range(0,70*4,70):
            platform = Platform((i,70),images["sandHalfMid"])
            self.platform_list.add(platform)
        i += 70 
        platform = Platform((i,70),images["sandHalfRight"])
        self.platform_list.add(platform)
        
        lava = AnimatedItem((420,430),images["liquidLavaTop_mid"],
                                pygame.transform.flip(images["liquidLavaTop_mid"],True,False))
        self.items_list.add(lava)
        lava = AnimatedItem((490,430),images["liquidLavaTop_mid"],
                                pygame.transform.flip(images["liquidLavaTop_mid"],True,False))
        self.items_list.add(lava)
        
        platform = Block((560,430),images["sandLeft"])
        self.platform_list.add(platform)
        platform = Block((630,430),images["sandMid"])
        self.platform_list.add(platform)
        platform = Block((700,430),images["sandRight"])
        self.platform_list.add(platform)
        
        platform = Platform((770,70),images["sandHalfLeft"])
        self.platform_list.add(platform)
        platform = Platform((840,70),images["sandHalfMid"])
        self.platform_list.add(platform)
        platform = Platform((910,70),images["sandHalfMid"])
        self.platform_list.add(platform)
        platform = Platform((980,70),images["sandHalfRight"])
        self.platform_list.add(platform)
        
        for i in range(770,1190,70):
            lava = AnimatedItem((i,430),images["liquidLavaTop_mid"],
                                pygame.transform.flip(images["liquidLavaTop_mid"],True,False))
            self.items_list.add(lava)
            
        platform = Platform((280,290),images["sandHalf"])
        self.platform_list.add(platform)
        
        platform = Platform((420,220),images["sandHalf"])
        self.platform_list.add(platform)
        
        platform = Platform((560,70),images["sandHalf"])
        self.platform_list.add(platform)

        for i in range(70,280,70):
            hud = Block((i,-70),images["hud_coin"])
            self.hud_list.add(hud)
        
        hud = Block((560,-70),images["hud_coin"])
        self.hud_list.add(hud)
        
        hud = Block((420,0),images["hud_coin"])
        self.hud_list.add(hud)
            
        movingPlatform = MovingPlatform((840,280),images["sandHalf"])
        movingPlatform.leftLimit = 770
        movingPlatform.rightLimit = 1120
        movingPlatform.changeX = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
        
        snail = AnimatedBlock((1260,430),images["snailWalk1"])
        snail.image1 = images["snailWalk1"]
        snail.image2 = images["snailWalk2"]
        snail.leftLimit = 1190
        snail.rightLimit = 1540
        snail.changeX = -2
        snail.level = self
        snail.player = player
        snail.is_snail = True
        snail.dead_image = images["snailShell"]
        self.block_list.add(snail)
        
        slime = AnimatedBlock((630,430),images["slime"])
        slime.image1 = images["slime"]
        slime.image2 = images["slime2"]
        slime.leftLimit = 560
        slime.rightLimit = 700
        slime.changeX = -2
        slime.level = self
        slime.player = player
        slime.dead_image = images["slimeDead"]
        self.block_list.add(slime)
        
        for i in range(80,430,70):
            wall = Block((1610,i),images["brickWall"])
            self.block_list.add(wall)
        
        spring = Spring((1500,430),images["SpringDown"],player)
        self.block_list.add(spring)
        
        fly = Fly((700,-140),images["fly1"],images["fly2"])
        self.block_list.add(fly)
        
        exit_sign = Block((2590,360),images["signExit"])
        self.items_list.add(exit_sign)
