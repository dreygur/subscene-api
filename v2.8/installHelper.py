import winreg, os, time, ctypes, sys
from requests import get
from datetime import datetime


def contextAdderForVideoFiles(fileType, regestryTitle, command, title):
    reg=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, 'SystemFileAssociations', 0, winreg.KEY_SET_VALUE)
    k1=winreg.CreateKey(reg, fileType)
    k2=winreg.CreateKey(k1, 'shell')
    k3=winreg.CreateKey(k2, regestryTitle)
    k4=winreg.CreateKey(k3, 'command')
    winreg.SetValueEx(k3, None, 0, winreg.REG_SZ, title)
    winreg.SetValueEx(k4, None, 0, winreg.REG_SZ, command)
    winreg.CloseKey(k4)
    winreg.CloseKey(k3)
    winreg.CloseKey(k2)
    winreg.CloseKey(k1)
    winreg.CloseKey(reg)


def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        print('I\'m Admin')
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print('Command line: '+ executable+ argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        print('False')
        return False
    return None



def install(e=''):
    time.sleep(2)
    extList = ['.mkv', '.mp4', '.3gp', '.ogg', '.wmv', '.webm', '.flv', '.avi']

    c="\"C:\\Users\\Xayed\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe\" \"D:\\Pr0grammming\\Pyth0n\\ScrapingAPI\\SubScene\\ExecutableProject\\main.py\" \"%\"C:\\Users\\Xayed\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe\" \"D:\\Pr0grammming\\Pyth0n\\ScrapingAPI\\SubScene\\ExecutableProject\\main.py\" \"%1\"\""
    ct="\"C:\\Program Files\\Test Folder\\{}\" \"%1\"\""

    

    if run_as_admin() is True:
        name='Subtitle_Finder_V2.8.exe'
        rd1 = '\"C:\\Program Files\\Subtitle Finder\\{}\" \"%1\"\"'.format(name)
        rd2="C:\\Program Files\\Subtitle Finder"
        '''for e in extList:
            contextAdderForVideoFiles(e, 'Download Subtitle', c, 'Download Subtitle')'''
        os.system('md "{}"'.format(rd2))
        os.system('copy "{}" "{}\\" /y'.format(name, rd2))
        open(r'C:\Windows\Temp\infoFileDT', 'w').write(str(datetime.now()).split()[0])
        for e in extList:
                contextAdderForVideoFiles(e, 'Download Subtitle', rd1, 'Download Subtitle')
        if 'downloaderAndInstallerNewVersion.bat' in os.listdir():
            os.remove('downloaderAndInstallerNewVersion.bat')
        ld=os.listdir(r"C:\Program Files\Subtitle Finder")
        for d in ld:
            if d.startswith('Subtitle_Finder_V') and d != name:
                os.remove(r"C:\Program Files\Subtitle Finder\{}".format(d))
        ld=os.listdir()
        for d in ld:
            if d.startswith('Subtitle_Finder_V') and d != name:
                os.remove(d)
        print('Installation Done! Enjoy!')
        return 1
    else:
        return 0
