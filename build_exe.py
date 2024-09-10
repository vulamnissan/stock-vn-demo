import PyInstaller.__main__
import PyInstaller.config
import os

distpath ="--distpath=" + str(os.getcwd()) +  "\\builder"
workpath = "--workpath=" + str(os.getcwd()) +  "\\builder" + "\\tempo"
# PyInstaller.config.CONF['distpath'] = path
PyInstaller.__main__.run([
    # 'GUI v0.5.py',
    '--onedir',
    # '--onefile',
    # '-n Update-Database',
    # # '--hidden-import=pya2l.cgen',
    # '--windowed',

    r'C:\Users\KNT21819\Downloads\Meter2\src\Meter_demo.py',
    # '--onefile',
    '-n MeterConfigTool',
    # '--hidden-import=pya2l.cgen',
    '--windowed',

    #'--disable-windowed-traceback'
    distpath,
    workpath,
    '--clean',
    '-y'
])
