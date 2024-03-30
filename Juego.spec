# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['src/main.py'],
             pathex=[r'C:\Users\javi_\PycharmProjects\Juego'],  # Updated path here
             binaries=[],
             datas=[('assets/images', 'assets/images'),
                    ('assets/sounds', 'assets/sounds'),
                    ('assets/music', 'assets/music'),
                    ('assets/videos', 'assets/videos'),
                    ('assets/fonts', 'assets/fonts')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='La sombra del Imperio',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,  # Set to True if you want a console window, otherwise False for GUI applications
          icon='assets/images/other/icon.ico')  # Change this if your icon has a different path
