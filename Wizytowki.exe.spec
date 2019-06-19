# -*- mode: python -*-

block_cipher = None


a = Analysis(['BUSINESS_CARD_GENERATOR.py'],
             pathex=['D:\\Projects\\WIZYTOWKI_GENERATOR\\WIZYTOWKI_GENERATOR'],
             binaries=[],
             datas=[],
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
          name='Wizytowki.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='ikona.ico')
