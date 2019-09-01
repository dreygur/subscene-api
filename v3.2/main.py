from os import listdir, rename, remove, rmdir, system, path
import sys
from zipfile import ZipFile
from time import sleep
from datetime import datetime
from json import loads
import platform


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


print('Path: ' + resource_path(''))
sys.path.insert(1, resource_path('installHelper.py'))


from installHelper import install, run_as_admin


installer='python -m pip install wxPython requests beautifulsoup4'
installer2='python3 -m pip install wxPython requests beautifulsoup4'


try:
    from requests import get, post
    from bs4 import BeautifulSoup
    import wx
    import wx.adv
except:
    if platform.system()=='Windows':
        system(installer)
    elif platform.system()=='Linux':
        if sys.version.split('.')[0]==0:
            system(installer2)
        else:
            print('Supports python 3 only!')
            sys.exit()
    from requests import get, post
    from bs4 import BeautifulSoup
    import wx



class TransparentText(wx.StaticText):
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.TRANSPARENT_WINDOW, name=''):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.on_size)

    def on_paint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)

        font_face = self.GetFont()
        font_color = self.GetForegroundColour()

        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)

    def on_size(self, event):
        self.Refresh()
        event.Skip()


class MessageDialog(wx.Dialog):
    def __init__(self, message, title, textColor='WHITE'):
        wx.Dialog.__init__(self, None, -1, title,size=(300, 160))
        self.CenterOnScreen(wx.BOTH)
        self.SetBackgroundColour('BLACK')
        self.SetForegroundColour(textColor)
        text = wx.StaticText(self, -1, message)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(text, 1, wx.ALIGN_CENTER|wx.TOP, 10)
        self.SetSizer(vbox)


class SubScene(wx.Frame):

    def __init__(self, parent, id):
        print(sys.argv)
        self.link = 'https://subscene.com'
        self.version = '3.2'
        self.extList = ['mkv', 'mp4', '3gp', 'ogg', 'wmv', 'webm', 'flv', 'avi']
        self.install()
        try:
            if not (open(r'C:\Windows\Temp\infoFileDT', 'r').read())==str(datetime.now()).split()[0]:
                self.updateChecker('5742')
        except Exception as e:
            print('Line 66: ' + str(e))
            open(r'C:\Windows\Temp\infoFileDT', 'w').write('--')
            self.updateChecker('5742')
        if len(sys.argv)==1:
            wx.Frame.__init__(self, parent, id, (' '*74)+'Subtitle Finder V_{}'.format(self.version), style=wx.CAPTION, size=(600, 500))#350,280
            #self.SetBackgroundColour('BLACK') 
            self.CenterOnScreen(wx.BOTH)
            panel=wx.Panel(self)
            bmp1 = wx.Image(resource_path('bg.jpg'), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.bitmap1 = wx.StaticBitmap(panel, -1, bmp1, (-100, -100))

            h1 = TransparentText(self.bitmap1, -1, 'Subtitle Finder', (180, 120))
            hfont = wx.Font(55, wx.ROMAN, wx.ITALIC, wx.NORMAL)
            h1.SetFont(hfont)

            t=TransparentText(self.bitmap1, -1, 'Welcome! Please wait some time after clicking any button.', pos=(220,210))
            t.SetFont(wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL))

            try:
                ld=listdir(r"C:\Program Files\Subtitle Finder")
                for d in ld:
                    if d.startswith('Subtitle_Finder_V'):
                        b1=wx.Button(self.bitmap1, -1, 'Check For Update', pos=(205, 300), size=(180,30))
                        self.Bind(wx.EVT_BUTTON, self.updateChecker, b1)
                        break
                else:
                    b1=wx.Button(self.bitmap1, -1, 'Install The Software', pos=(205, 300), size=(180, 30))
                    self.Bind(wx.EVT_BUTTON, self.install, b1)
            except:
                b1=wx.Button(self.bitmap1, -1, 'Install The Software', pos=(205, 300), size=(180, 30))
                self.Bind(wx.EVT_BUTTON, self.install, b1)
            b2=wx.Button(self.bitmap1, -1, 'Search For Movies Subtitle', pos=(395, 335), size=(180, 30))
            b3=wx.Button(self.bitmap1, -1, 'Select Language', pos=(205, 370), size=(180, 30))
            b3.Disable()
            b4=wx.Button(self.bitmap1, -1, 'Search For Tv-Series Subtitle', pos=(395, 405), size=(180, 30))
            b4.Disable()
            b5=wx.Button(self.bitmap1, -1, 'About', pos=(205, 440), size=(180, 30))
            b6=wx.Button(self.bitmap1, -1, 'Exit', pos=(395, 475), size=(180, 30))
            self.Bind(wx.EVT_BUTTON, self.searchFromDirectiory, b2)
            #self.Bind(wx.EVT_BUTTON, self.aboutButton, b3)
            #self.Bind(wx.EVT_BUTTON, self.aboutButton, b4)
            self.Bind(wx.EVT_BUTTON, self.aboutButton, b5)
            self.Bind(wx.EVT_BUTTON, self.closeButton, b6)

            b=wx.Button(self.bitmap1, -1, '', pos=(386, 300), size=(8, 205))
            b.Disable()

            t2=TransparentText(self.bitmap1, -1, 'Made By: Xayed © 2019', pos=(330, 530), size=(160, 20))
            t2.SetForegroundColour('WHITE')

        elif len(sys.argv)==2:
            print('Single File Downloader')
            name=sys.argv[1].split('\\')[-1]
            if name[-1]=='"':name=name[:-1]
            try:
                print(name)
                print(listdir())
                self.searchFromDirectiory('', [name])
                sys.exit()
            except Exception as e:
                print(e)
                print('len2 1st exp')


    def install(self, e='1234'):
        if path.exists('installExt'):
            if install()==1:
                remove('installExt')
                mb=MessageDialog('\n\nSuccessfully Installed.\n\nRight Click on any video and \ndownload sub in your device.', 'WELCOME', 'GREEN')
                wx.CallLater(3000, mb.Destroy)
                mb.ShowModal()
            else:
                sys.exit()
        elif e!='1234':
            open('installExt', 'w').close()
            if install()==1:
                mb=MessageDialog('\n\nSuccessfully Installed.\n\nRight Click on any video and \ndownload sub in your device.', 'WELCOME', 'GREEN')
                wx.CallLater(3000, mb.Destroy)
                mb.ShowModal()
            else:
                sys.exit()
        else:
            pass

    def updater(self, l=''):
        fileName=l
        open('installExt', 'w').close()
        f=open('downloaderAndInstallerNewVersion.bat', 'w').write(resource_path('aria2c.exe')+' https://raw.githubusercontent.com/xaadu/subFinderReleases/master/{}\n{}'.format(fileName,fileName))
        system('downloaderAndInstallerNewVersion.bat')
        sys.exit()


    def updateChecker(self, e):
        uA={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        newName=get('https://sourceforge.net/projects/subtitle-finder/best_release.json', headers=uA).json()['release']['filename'][1:]
        print(newName)
        try:
            l=listdir(r"C:\Program Files\Subtitle Finder")
        except Exception as e:
            print(e)
            return
        print(l)
        v=float(newName.split('_')[-1][1:-4])
        print(v)
        vList=[]
        for i in l:
            if i.startswith('Subtitle_Finder_V'):
                vList.append(float(i.split('_')[-1][1:-4]))
        vList=sorted(vList)
        if vList[-1]<v:
            dlg = wx.MessageDialog(None, "A new version is available! \n\nDo you want to update?",'Updater',wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.updater('Subtitle_Finder_V{}.exe'.format(v))
            else:
                mb=MessageDialog("\n\nUpdater will check for \n\nUpdate tomorrow", 'Updater', 'RED')
                wx.CallLater(3000, mb.Destroy)
                mb.ShowModal()
        else:
            if e!='5742':
                mb=MessageDialog("\n\nYour Program Is \n\nUp To Date", 'Updater', 'GREEN')
                wx.CallLater(3000, mb.Destroy)
                mb.ShowModal()
            else:
                open(r'C:\Windows\Temp\infoFileDT', 'w').write(str(datetime.now()).split()[0])



    def closeButton(self, e):
        self.Destroy()
    

    def aboutButton(self, e):
        #x=About()
        description='''
        This is a free software which will help you finding subtitle.

        Usage:
        Run this software, click install, give this software 
        administrator right to install, then just close the program.
        Now right click on any file and click 'Download Subtitle' 
        to download the subtitle.

        OR

        Place this software at the movie folder/directory, Run 
        and Enjoy.
        

        This Software is developed By Xayed.

        Contact:

        Facebook: Abdullah Xayed (https://facebook.com/xayed42)
        Messenger: https://m.me/xayed42
        Email: xayed42@gmail.com
        Telegram: t.me/Xaadu
        
        Feel free to report any bug. Thanks!
        '''
        licence='Free Software'
        info = wx.adv.AboutDialogInfo()
        info.SetName('Subtitle Finder ')
        info.SetVersion(self.version)
        info.SetDescription(description)
        info.SetCopyright('© 2019 Xayed')
        info.SetWebSite('http://subtitle-finder.sourceforge.io/')
        info.SetLicence(licence)
        info.AddDeveloper('Xayed')
        wx.adv.AboutBox(info)

    
    def failed(self, na):
        mb=MessageDialog('Failed! Sorry. No subtitle found.\n\nPlease Perform Custom Search for\n\n'+na, 'Failed', 'RED')
        wx.CallLater(3000, mb.Destroy)
        mb.ShowModal()


    def getFileNameFromDirectory(self, di=''):
        if di!='':
            di = listdir(di)
        else:
            di = listdir()
        mvList = []
        for d in di:
            x=d.split('.')[-1]
            if x in self.extList:
                mvList.append(d)

        if len(mvList)>1:
            qt='\nWhat file do you want to download subtitle for?\n'
            at='All Movies from this list'
            mvList.append(at)
            m=wx.SingleChoiceDialog(None, qt, 'Choice', mvList)
            if m.ShowModal()==wx.ID_OK:
                if m.GetStringSelection()==at:
                    names=mvList[:-1]
                else:
                    names=[m.GetStringSelection()]
            else:
                sys.exit()
            m.Destroy()
        elif len(mvList)==1:
            names=[mvList[0]]
        else:
            return None        
        return names


    def getDetailsFromName(self, name=None):
        name=name.lower()
        if len(name.split())>2:
            print('Splitted By Space')
            exD = name.split()
        elif len(name.split('.'))>2:
            print('Splitted By Dot')
            exD = name.split('.')
        elif len(name.split('_'))>2:
            exD = name.split('_')
        elif len(name.split('-'))>2:
            exD = name.split('-')
        else:  
            print('Name couldn\'t be splitted. Please perform custom search at https://www.subscene.com.')
            return None
        print(exD)
        nameDone = False
        name2,year,p,pList='','','',['bluray','hc','hdrip','dvdrip','camrip','webdl','web-dl', 'webrip', 'brrip']
        p=''
        for x in exD:
            if len(x.split('.'))==2 and not nameDone:
                pass
            elif x=='-' or x==':':
                pass
            elif (x.isalpha() or x[:-1].isalpha() or x.replace(' ', '').isalpha() or (x.isnumeric() and len(x)<3)) and not nameDone:
                name2+=(' ' + x.title())
            else:
                nameDone = True
                if x.isnumeric() and len(x)==4:
                    year=x
                elif len(x)==6:
                    if (x[0]=='[' or x[0]=='(') and x[1:5].isnumeric() and (x[5]==']' or x[5]==')'):
                        year=x[1:5]
                elif x.isalpha() and x in pList:
                    p=x
                else:
                    for sp in pList:
                        if sp in name:
                            p=sp
                            break
        if p=='':
            m=wx.SingleChoiceDialog(None, 'Please select print for "{}": '.format(name2[1:]), 'Choice', pList)
            if m.ShowModal()==wx.ID_OK:
                p=m.GetStringSelection()
            else:
                return None
        data = {
            'name': name2[1:],
            'year': year,
            'print': p
        }
        print(data)
        return data


    def getFromFullChoice(self, h, l, details):
        try:
            links, names = [], []
            for sh, sl in zip(h, l):
                a = sl.findAll('a')
                for sa in a:
                    links.append(self.link+sa.get('href'))
                    if details.get('year') != '' and details.get('year') in sa.text:
                        flag=True
                        for sn in details['name'].split():
                            if sn not in sa.text:
                                flag=False
                                break
                        if flag:
                            return links[-1]
                        else:
                            names.append(sa.text)
                    else:
                        names.append(sa.text)
            links=list(dict.fromkeys(links))
            names=list(dict.fromkeys(names))
            m=wx.SingleChoiceDialog(None, 'Please Select Your Choice for "{}": '.format(details['name']), 'Choice', names)
            if m.ShowModal()==wx.ID_OK:
                 return links[names.index(m.GetStringSelection())]
            else:
                return None
        except Exception as e:
            print(e)
            return None


    def getSearchedMovieDefault(self, details):
        try:
            data = {
                'query': details['name']
            }
            while True:
                r=post(self.link+'/subtitles/searchbytitle', data=data)
                print(r.status_code)
                if r.status_code != 200:
                    sleep(3)
                else:
                    break
            soup = BeautifulSoup(r.text, 'html.parser')
            d = soup.find('div', {'class': 'search-result'})
            h = d.findAll('h2')
            l = d.findAll('ul')
            links,names = [],[]
            try:
                if h[0]['class'][0].title() == 'Exact':
                    if len(l[0].findAll('a'))>1:
                        for a in l[0].findAll('a'):
                            links.append(self.link+a.get('href'))
                            if details.get('year') != '' and details.get('year') in a.text:
                                return links[-1]
                        else:
                            return self.getFromFullChoice(h,l,details)
                    else:
                        if details.get('year') != '' and details.get('year') in l[0].find('a').text:
                            return self.link+l[0].find('a')['href']
                        else:
                            return self.getFromFullChoice(h,l,details)
                else:
                    return self.getFromFullChoice(h,l,details)
            except Exception as e:
                print(e)
                return None
        except Exception as e:
            print(e)
            return None
    

    def getPerfectSubtitleLink(self, link, lang, p):
        html=get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        l = soup.find('tbody').findAll('a')
        for a in l:
            al = a.findAll('span')
            try:
                language = al[0].text.strip()
                subName = al[1].text.strip()
                if language==lang: # and 'positive-icon' in a.span['class']
                    if p in subName.lower():
                        print('Subtitle name: '+subName)
                        print()
                        return self.link+a['href']
            except Exception as e:
                pass
        return None
    

    def getDownloadLink(self, link):
        html=get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        s=soup.find('div', {'class': 'download'})
        return self.link+s.a['href']


    def downloadAndFinish(self, link, name, na, di=''):
        try:
            with open(di+'temp.zip', 'wb') as temp:
                temp.write(get(link).content)
            with ZipFile(di+'temp.zip', 'r') as z:
                l=z.namelist()
                for n in l:
                    if n.endswith('.srt'):
                        z.extract(n, di+'temp')
                        break            
            name='.'.join(name.split('.')[:-1])+'.srt'
            try:
                rename(di+'temp/{}'.format(listdir(di+'temp')[0]), di+name)
            except FileExistsError:
                remove(di+name)
                rename(di+'temp/{}'.format(listdir(di+'temp')[0]), di+name)
            rmdir(di+'temp')
            remove(di+'temp.zip')

            ed='\nSubtitle for :\n\n"{}"\n\n has been downloaded successfully. :)\n'.format(na)
            mb=MessageDialog(ed, 'Complete One', 'GREEN')
            wx.CallLater(2000, mb.Destroy)
            mb.ShowModal()

        except:
            self.failed(na)
    

    def searchFromDirectiory(self, event, n=None, di=''):
        if n==None:
            dialog=wx.FileDialog(None, 'Select Movie Folder', '', '', 
                'Video Files (*.mp4;*.mkv;*3gp;*.avi;*.webm;*.ogg;*.flv)|*.mp4;*.mkv;*3gp;*.avi;*.webm;*.ogg;*.flv',
                style=wx.FD_MULTIPLE)

            try:
                if dialog.ShowModal() == wx.ID_CANCEL:
                    raise ValueError
                paths = dialog.GetPaths()
                print('Paths: ' + str(paths))
                names=[]
                for p in paths:
                    names.append(p.split('\\')[-1])
                print()
                di='\\'.join(paths[0].split('\\')[:-1])+'\\'
                print(di)
                print()
            except:
                names=None
        else:
            names=n
        print(names)
        if names:
            for name in names:
                details=self.getDetailsFromName(name)
                if details is not None:
                    ds=self.getSearchedMovieDefault(details)
                    if ds is not None:
                        link=self.getPerfectSubtitleLink(ds, 'English', details['print'])
                        if link is not None:
                            dl = self.getDownloadLink(link)
                            if dl is not None:
                                self.downloadAndFinish(dl, name, details['name'], di)
                            else:
                                self.failed(name)
                        else:
                            self.failed(name)
                    else:
                        self.failed(name)
                else:
                    self.failed(name)
            if len(names)>1:
                ed='\nYour chosen subtitle(s) \n\nhas been downloaded successfully. :)\n'
                mb=MessageDialog(ed, 'Complete All', 'GREEN')
                wx.CallLater(3000, mb.Destroy)
                mb.ShowModal()

        else:
            mb=MessageDialog("Empty Directory.\n\nPlease choose different directory.", 'Error', 'RED')
            wx.CallLater(3000, mb.Destroy)
            mb.ShowModal()



if __name__ == '__main__':
        app=wx.App()
        frame=SubScene(parent=None, id=-1)
        try:
            frame.Show()
        except:
            pass
        app.MainLoop()