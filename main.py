import os

import wx

class MCME ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MCME", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.findmods()
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
	
		self.m_checkList1 = wx.CheckListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_checkList1Choices, 0 )
		bSizer2.Add( self.m_checkList1, 0, wx.ALL, 5 )
		self.m_checkList1.Bind( wx.EVT_CHECKLISTBOX, self.switch )
		
		self.checkmods()
		
		self.m_scrolledWindow1.SetSizer( bSizer2 )
		self.m_scrolledWindow1.Layout()
		bSizer2.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		
	def findmods(self):
			
		self.mypath=os.environ['USERPROFILE'] + "\AppData\Roaming\.minecraft\mods"
		self.onlyfiles = [ f for f in os.listdir(self.mypath) if os.path.isfile(os.path.join(self.mypath,f)) ]
		#self.m_checkList1Choices = self.onlyfiles
		
		index = 0
		newname=[]
		for name in self.onlyfiles:
			striped = name[:-4]
			#print striped
			newname.insert(index ,striped)
			index = index + 1
		self.m_checkList1Choices = newname
		#print 'list is ' + str(self.m_checkList1Choices)
	
	def checkmods(self):
		
		
		index = 0
		for i in self.onlyfiles:
			#print i
			if i.endswith('.zip') or i.endswith('.jar'):
				
				self.m_checkList1.Check(index, True)
				index = index + 1
			
			elif i.endswith('.not') or i.endswith('.noj'):
				
				self.m_checkList1.Check(index, False)
				index = index + 1
			
			
	def switch(self,event):
		
		files = [ f for f in os.listdir(self.mypath) if os.path.isfile(os.path.join(self.mypath,f)) ]
		place = event.GetSelection()
		if files[place].endswith('.not'):
			infilename = os.path.join(self.mypath,files[place])
			newname = infilename.replace('.not', '.zip')
			os.rename(infilename, newname)
			
		elif files[place].endswith('.zip'):
			infilename = os.path.join(self.mypath,files[place])
			newname = infilename.replace('.zip', '.not')
			os.rename(infilename, newname)
			
		elif files[place].endswith('.jar'):
			infilename = os.path.join(self.mypath,files[place])
			newname = infilename.replace('.jar', '.noj')
			os.rename(infilename, newname)
			
		elif files[place].endswith('.noj'):
			infilename = os.path.join(self.mypath,files[place])
			newname = infilename.replace('.noj', '.jar')
			os.rename(infilename, newname)
			
if __name__ == "__main__":
	app = wx.App(False) 
	frame = MCME(None)
	frame.Show(True)
	app.MainLoop()
