import pygame

import constants
import sprite_objects

class Area():
    """ This is a generic super-class used to define a area.
        Create a child class for each area with area-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all areas. --> Add or remove some?
        self.wall_list = None
        self.enemy_list = None
        self.tile_list = None


        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.area_limit = -1000
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this area
    def update(self):
        """ Update everything in this area."""
        self.wall_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this area. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth. --- More applicable to side-scroller?  ### MODIFY IF NEEDED ###
        screen.fill(constants.BLUE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.wall_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x, shift_y):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift = self.world_shift + shift_x + shift_y  ##### Probably wrong

        # Go through all the sprite lists and shift
        for wall in self.wall_list:
            wall.rect.x += shift_x
            wall.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            enemy.rect.y += shift_y


# Create tiles for the area?
class Area_01(area):  # Around Home        ### Create more areas as needed
    """ Definition for area 1. """

    def __init__(self, player):
        """ Create area 1. """

        # Call the parent constructor
        area.__init__(self, player)

        self.background = pygame.image.load("background/background_images/forrest_side_scroll_background_2.jpg").convert() ### Temp image. ### WILL BE REPLACED WITH TILE MAP LATER
        self.background.set_colorkey(constants.WHITE)
        self.area_limit = -2500

        # Array with type of wall, and x, y location of the wall.      ### Modify as needed
        area = [[sprite_objects.GRASS_LEFT, 500, 500],
                 [sprite_objects.GRASS_MIDDLE, 570, 500],
                 [sprite_objects.GRASS_RIGHT, 640, 500],
                 [sprite_objects.GRASS_LEFT, 800, 400],
                 [sprite_objects.GRASS_MIDDLE, 870, 400],
                 [sprite_objects.GRASS_RIGHT, 940, 400],
                 [sprite_objects.GRASS_LEFT, 1000, 500],
                 [sprite_objects.GRASS_MIDDLE, 1070, 500],
                 [sprite_objects.GRASS_RIGHT, 1140, 500],
                 [sprite_objects.STONE_PLATFORM_LEFT, 1120, 280],
                 [sprite_objects.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [sprite_objects.STONE_PLATFORM_RIGHT, 1260, 280],
                 ]

        # Go through the array above and add platforms
        for wall in area:
            wall = sprite_objects.Platform(wall[0])
            wall.rect.x = wall[1]
            wall.rect.y = wall[2]
            wall.player = self.player
            self.wall_list.add(wall)

        # Add a custom moving walls etc...
        wall = sprite_objects.MovingPlatform(sprite_objects.STONE_PLATFORM_MIDDLE)  ### Modify as needed
        wall.rect.x = 1350
        wall.rect.y = 280
        wall.boundary_left = 1350
        wall.boundary_right = 1600
        wall.change_x = 1
        wall.player = self.player
        wall.area = self
        self.wall_list.add(wall)


# Create platforms for the area
class Area_02(area): # Forest to "right" of home/ Area one.
    """ Definition for area 2. """

    def __init__(self, player):
        """ Create area 2. """

        # Call the parent constructor
        area.__init__(self, player)

        self.background = pygame.image.load("background/background_images/glad_forest_side_scroll_background2.jpg").convert()  ### WILL BE REPLACED WITH TILE MAP LATER
        self.background.set_colorkey(constants.WHITE)
        self.area_limit = -1000

        # Array with type of wall, and x, y location of the sprite
        area = [[platforms.STONE_PLATFORM_LEFT, 500, 550],
                 [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                 [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                 [platforms.GRASS_LEFT, 800, 400],
                 [platforms.GRASS_MIDDLE, 870, 400],
                 [platforms.GRASS_RIGHT, 940, 400],
                 [platforms.GRASS_LEFT, 1000, 500],
                 [platforms.GRASS_MIDDLE, 1070, 500],
                 [platforms.GRASS_RIGHT, 1140, 500],
                 [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                 [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                 ]

        # Go through the array above and add walls or trees, etc....
        for wall in area:
            wall = sprite_objects.Platform(SOME_SPRITE_LIST[0])  #### Needs to be modifies, Placeholder.
            wall.rect.x = wall[1]
            wall.rect.y = wall[2]
            wall.player = self.player
            self.wall_list.add(wall)

        # Add a custom moving wall etc.
        wall = sprite_objects.MovingPlatform(sprite_objects.SOME_SEGMENT)  ### Needs to be modified. Placeholder.
        wall.rect.x = 1500
        wall.rect.y = 300
        wall.boundary_top = 100
        wall.boundary_bottom = 550
        wall.change_y = -1
        wall.player = self.player
        wall.area = self
        self.wall_list.add(wall)

class Area_03(area):  # Base of Tree house. Up from Area_02
    pass
class Area_04(area): # second story of Tree house. Up from Area_03, Down from Area_05
    pass

class Area_05(area): # top of Tree hous. Up from Area_04
    pass

class Area_06(area): # Home interior. Only accessible via object (house) collision within Area_01
    pass

class Area_07(area): # Rocky area to the Left of Area_07.
    pass

class Area_08(area): # First segment of the dungeon. Up from Area_07
    pass

class Area_09(area): # Second segment of the dungeon. Up from Area_08 and Down from Area_10
    pass

class Area_10(area): # Deepest segment of the dungeon. Secondary area for games. Up from Area_09
    pass
class Area_11(area): # Possible mining area. Only accessible from Area_07 through colliding with object. Likely not an area.
    pass
