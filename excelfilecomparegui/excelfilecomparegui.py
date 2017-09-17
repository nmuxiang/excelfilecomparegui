import wx

wildcard="Excel 97-2003 Workbook (*.xls)|*.xls|Excel Workbook (*.xlsx)|*.xlsx"

def filelisttoitem(filelist):
    i=len(filelist)
    j=0
    filelistitem=[]
    item=()
    for element in filelist:
        item[0]=j
        item[1]=element
        filelistitem.append(item)
        j+=1
    return filedictitem

class filelistctrl(wx.ListCtrl):
    def __init__(self, parent, ID, pos, size, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        self.InsertColumn(0,"ID")
        self.InsertColumn(1,"File")
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,self.OnRightClick)

    def OnRightClick(self,event):
        self.currentItem=event.Index
        if not hasattr(self,'popupID1'):
            self.popupID1=wx.NewId()
            self.Bind(wx.EVT_MENU,self.OnPopupOne,id=self.popupID1)
        menu=wx.Menu()
        menu.Append(self.popupID1,"Delete Selected Items")
        self.PopupMenu(menu)
        menu.Destroy()

    def OnPopupOne(self,event):
        '''First get id of selected items,storge in list n,
        Second iterate n by reverse order,delete each element,'''
        n=[]
        item=self.GetFirstSelected()
        while item !=-1:            
            n.append(item)
            item=self.GetNextSelected(item)
        for iter in range(len(n)-1,-1,-1) :
            self.DeleteItem(iter)

class panelup(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1)


        self.SetBackgroundColour("red")
        b=wx.Button(self,-1,"Add File",(10,10))
        self.Bind(wx.EVT_BUTTON,self.OnButton,b)
        self.filelist=filelistctrl(self,style=wx.LC_REPORT,size=(300,100),pos=(50,50),ID=wx.ID_ANY)
#        lc=wx.LayoutConstraints()
#        lc.top.SameAs(self,wx.Top,10)
#        lc.left.SameAs(self,wx.Left,10)
#        lc.right.SameAs(self,wx.Right,10)
#        lc.bottom.PercentOf(self,wx.Bottom,30)
#        self.SetConstraints(lc)

    def OnButton(self,evt):
        openfile_dlg=wx.FileDialog(self,message="choose file",wildcard=wildcard,style=wx.FD_OPEN | wx.FD_MULTIPLE|wx.FD_CHANGE_DIR|wx.FD_FILE_MUST_EXIST)
        if openfile_dlg.ShowModal()==wx.ID_OK:
            data=openfile_dlg.GetPaths()
            for item in data:
                a=self.filelist.GetItemCount()
                a+=1
                index=self.filelist.InsertItem(self.filelist.GetItemCount(),a)
                self.filelist.SetItem(index,1,item)
                self.filelist.SetItem(index,0,str(a))
                self.filelist.SetItemData(index,index)
                
        openfile_dlg.Destroy()







class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,wx.ID_ANY,"Excel File Compare")
        panelA=panelup(self)

app=wx.App()
frm=MyForm()
frm.Show()
app.MainLoop()
