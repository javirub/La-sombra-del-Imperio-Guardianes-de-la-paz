import os

# Get the absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Window dimensions, actually not changeable as the game is not responsive
WIDTH, HEIGHT = 1920, 1080

# Frame rate
FPS = 60

# Paths to assets
ICON_PATH = os.path.join(BASE_DIR, './assets/images/other/icon.png')
BACKGROUND_PATH = os.path.join(BASE_DIR, './assets/images/backgrounds/bgGame1.png')
BACKGROUND_INTRO = os.path.join(BASE_DIR, './assets/images/backgrounds/bgIntro.jpg')
BACKGROUND_MENU = os.path.join(BASE_DIR, './assets/images/backgrounds/bgMenu.jpg')

# Sprites
# Spaceships
TIE_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/tie.png')
XWING_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/xwing.png')
FALCON_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/millenium_falcon.png')
# Animations
EXPLOSION_SPRITE = os.path.join(BASE_DIR, './assets/images/explosion/explosion.png')
# Others
DEATHSTAR_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/deathstar.png')
EARTH_PLANET_SPRITE = os.path.join(BASE_DIR, './assets/images/other/earth.png')
# Satellites
SPY_SATELLITE_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/satellite.png')
GOLDEN_TRUMP_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/golden_trump.png')
TESLA_ROADSTER_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/tesla_roadster_space.png')
# Characters
ELON_MUSK_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/elon_musk.png')
LAUGHING_MUSK_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/laughing_musk.png')
KIM_JONG_ILL_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/kim_jong_ill.png')
DARTH_VADER_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/darth_vader.png')
DONALD_TRUMP_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/donald_trump.png')
HARRISON_FORD_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/harrison_ford.png')
CHEWBACCA_SPRITE = os.path.join(BASE_DIR, './assets/images/characters/chewbacca.png')
# Arcade spaceships
ARCADE_TIE_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/level 2/tie.png')
ARCADE_TESLA_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/level 2/tesla_spaceship.png')
TESLA_UPGRADED_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/level 4/roadster_armed.png')
KOREA_TANK_SPRITE = os.path.join(BASE_DIR, './assets/images/spaceships/level 4/korea_tank.png')
# Powerups
CADENCE_POWERUP_SPRITE = os.path.join(BASE_DIR, './assets/images/powerups/cadence.png')
HEALTH_POWERUP_SPRITE = os.path.join(BASE_DIR, './assets/images/powerups/health.png')
SPEED_POWERUP_SPRITE = os.path.join(BASE_DIR, './assets/images/powerups/speed.png')

# Sounds & songs
TIE_SOUND = os.path.join(BASE_DIR, './assets/sounds/tieblast.wav')
XWING_SOUND = os.path.join(BASE_DIR, './assets/sounds/xwingblast.wav')
TANK_SOUND = os.path.join(BASE_DIR, './assets/sounds/tank_shoot.wav')
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
WOOKIE_SOUND = os.path.join(BASE_DIR, './assets/sounds/wookie.wav')
# Narrator
LEVEL1_NARRATOR = os.path.join(BASE_DIR, './assets/sounds/narrator/level1.ogg')
LEVEL2_NARRATOR = os.path.join(BASE_DIR, './assets/sounds/narrator/level2.ogg')
LEVEL4_NARRATOR = os.path.join(BASE_DIR, './assets/sounds/narrator/level4.ogg')

# Videos
DEATHSTAR_SHOOT_VIDEO = os.path.join(BASE_DIR, './assets/videos/deathstarShoot.mp4')
DEATHSTAR_HIT_EARTH_VIDEO = os.path.join(BASE_DIR, './assets/videos/deathstarHitEarth.mp4')

# Fonts
FONT_PATH = os.path.join(BASE_DIR, './assets/fonts/gameFont.ttf')

# Game settings
LEVEL2_ENEMIES = 50
LEVEL4_ENEMIES = 100

# Codes
CODES = {
    "intro": "intro",
    "ElonMusk": "Deathstar",
    "intro2": "intro2",
    "Arcadedon": "Arcadedon",
    "Deathstar2": "Deathstar2",
    "intro3": "intro3",
    "Team Korea": "Arcadedon2",
    "Deathstar3": "Deathstar3",
    "Trigonometria": "MilleniumFalcon",
    "largavidaalimperio": "ImperiumWinner"
}
