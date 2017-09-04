import wx

wildcard="Excel 97-2003 Workbook (*.xls)|*.xls|Excel Workbook (*.xlsx)|*.xlsx"

def filelisttodict(filelist):
    i=len(filelist)
    j=0
    filedict={}
    for element in filelist:
        filedict[j]=element
        j+=1
    return filedict

class filelistctrl(wx.ListCtrl):
    def __init__(self, parent, ID, pos, size, style):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

class panelup(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1)


        self.SetBackgroundColour("red")
        b=wx.Button(self,-1,"Add File",(10,10))
        self.Bind(wx.EVT_BUTTON,self.OnButton,b)
        filelistctrl=wx.ListCtrl(self,)
#        lc=wx.LayoutConstraints()
#        lc.top.SameAs(self,wx.Top,10)
#        lc.left.SameAs(self,wx.Left,10)
#        lc.right.SameAs(self,wx.Right,10)
#        lc.bottom.PercentOf(self,wx.Bottom,30)
#        self.SetConstraints(lc)

    def OnButton(self,evt):
        openfile_dlg=wx.FileDialog(self,message="choose file",wildcard=wildcard,style=wx.FD_OPEN | wx.FD_MULTIPLE|wx.FD_CHANGE_DIR|wx.FD_FILE_MUST_EXIST)
        if openfile_dlg.ShowModal()==wx.ID_OK:
            paths=openfile_dlg.GetPaths()
            data=filelisttodict(paths)
            filelist=filelistctrl(self,pos=(20,10),ID=-1,style=wx.LC_REPORT,size=(30,20))
            filelist.InsertColumn(0,paths)
        openfile_dlg.Destroy()









app=wx.App()
frm=wx.Frame(None,-1,title="Excel File Compare")
pnl=panelup(frm)

frm.Show()
app.MainLoop()
