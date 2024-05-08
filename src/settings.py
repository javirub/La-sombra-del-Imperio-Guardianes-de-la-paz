import os

# Get the absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Window dimensions
WIDTH, HEIGHT = 1920, 1080

# Frame rate
FPS = 60

# Paths to assets
ICON_PATH = os.path.join(BASE_DIR, './assets/images/other/icon.png')
BACKGROUND_PATH = os.path.join(BASE_DIR, './assets/images/backgrounds/bgGame1.png')
BACKGROUND_INTRO = os.path.join(BASE_DIR, './assets/images/backgrounds/bgIntro.jpg')
BACKGROUND_MENU = os.path.join(BASE_DIR, './assets/images/backgrounds/bgMenu.jpg')

# Sprites
TIE_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/tie.png')
XWING_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/xwing.png')
EXPLOSION_SPRITE = os.path.join(BASE_DIR, './assets/images/explosion/explosion.png')
DEATHSTAR_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/deathstar.png')
SPY_SATELLITE_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/satellite.png')
GOLDEN_TRUMP_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/golden_trump.png')
EARTH_PLANET_SPRITE = os.path.join(BASE_DIR, './assets/images/other/earth.png')
TESLA_ROADSTER_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/tesla_roadster_space.png')
ELON_MUSK_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/elon_musk.png')
LAUGHING_MUSK_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/laughing_musk.png')
KIM_JONG_ILL_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/kim_jong_ill.png')
DARTH_VADER_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/darth_vader.png')
ARCADE_TIE_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/level 2/tie.png')
ARCADE_TESLA_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/level 2/tesla_spaceship.png')
CADENCE_POWERUP_SPRITE = os.path.join(BASE_DIR, './assets/images/powerups/cadence.png')
HEALTH_POWERUP_SPRITE = os.path.join(BASE_DIR, './assets/images/powerups/health.png')
SPEED_POWERUP_SPRITE = os.path.join(BASE_DIR, './assets/images/powerups/speed.png')
# Sounds & songs
TIE_SOUND = os.path.join(BASE_DIR, './assets/sounds/tieblast.wav')
XWING_SOUND = os.path.join(BASE_DIR, './assets/sounds/xwingblast.wav')
EXPLOSION_SOUND = os.path.join(BASE_DIR, './assets/sounds/explosion.wav')
TIE_FUNNY_SOUND = os.path.join(BASE_DIR, './assets/sounds/piu.wav')
XWING_FUNNY_SOUND = os.path.join(BASE_DIR, './assets/sounds/piu.wav')
EXPLOSION_FUNNY_SOUND = os.path.join(BASE_DIR, './assets/sounds/boom.wav')
DEATHSTAR_SOUND = os.path.join(BASE_DIR, './assets/sounds/deathstarShoot.wav')
MENU_SOUND = os.path.join(BASE_DIR, './assets/sounds/menu_sound.wav')
INTRO_SONG_PATH = os.path.join(BASE_DIR, './assets/music/intro_song.ogg')
MENU_SONG_PATH = os.path.join(BASE_DIR, './assets/music/menu_song.ogg')
GAME_SONG_PATH = os.path.join(BASE_DIR, './assets/music/game_song.ogg')
IMPERIUM_WINNER_SONG_PATH = os.path.join(BASE_DIR, './assets/music/menu_song.ogg')
REBEL_WINNER_SONG_PATH = os.path.join(BASE_DIR, './assets/music/intro_song.ogg')
EPIC_SONG_PATH = os.path.join(BASE_DIR, './assets/music/O Fortuna.ogg')

# Narrator
LEVEL1_NARRATOR = os.path.join(BASE_DIR, './assets/sounds/narrator/level1.ogg')
LEVEL2_NARRATOR = os.path.join(BASE_DIR, './assets/sounds/narrator/level2.ogg')

# Videos
DEATHSTAR_SHOOT_VIDEO = os.path.join(BASE_DIR, './assets/videos/deathstarShoot.mp4')

# Fonts
FONT_PATH = os.path.join(BASE_DIR, './assets/fonts/gameFont.ttf')

# Game settings
LEVEL2_ENEMIES = 50
LEVEL4_ENEMIES = 50

# Codes
CODES = {
    "estomereceun10": "intro", # Cambiar a final
    "prueba": "localMP",
    "largavidaalimperio": "ImperiumWinner",
    "ElonMusk": "Deathstar",
    "Arcadedon": "Arcadedon"
}