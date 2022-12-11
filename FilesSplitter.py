# import project libraries.
import wx
import webbrowser


# Create app with wx.
app= wx.App()

# Create Files splitter window with wx.
class FilesSplitter(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title = 'FilesSplitter', size=(300, 230))

		#make window in center.
		self.Center()

		#make window Minimum size.
		self.Maximize(False)
		self.EnableMaximizeButton(False)
		self.FileContent = ""
		self.encoding = ""


		# Creating panel
		self.Panel = wx.Panel(self)

		# Creating Buttons
		self.ImportFiles = wx.Button(self.Panel, -1, "Import a file", pos=(30,30), size=(100,30))
		wx.StaticText(self.Panel, -1, "Select the number of characters in each file:", pos=(20,70), size=(380, 30))
		self.PartsNumber  = wx.SpinCtrl(self.Panel, -1, "2500", min=100, max=10000000000, style=wx.SP_ARROW_KEYS, pos=(40, 100), size=(50, 20))
		self.SaveFiles = wx.Button(self.Panel, -1, "Save files", pos=(20,140), size=(70,30))
		self.more = wx.Button(self.Panel, -1, "more", pos=(10,140), size=(120,30))
		self.Close = wx.Button(self.Panel, -1, "Close", pos=(100,140), size=(60,30))

		# Show Main window
		self.Show()

		# events.
		self.ImportFiles.Bind(wx.EVT_BUTTON, self.OnOnOpwnFile)
		self.Close.Bind(wx.EVT_BUTTON, self.OnCloseProgram)
		self.SaveFiles.Bind(wx.EVT_BUTTON, self.OnSaveFiles)
		self.more.Bind(wx.EVT_BUTTON, self.OnMore)


	def OnMore(self, event):
		MoreMenu = wx.Menu()
		ContactMenu = wx.Menu()
		QaisMenu = wx.Menu()
		QaisEm = QaisMenu.Append(-1, "&E-mail")
		QaisTe =QaisMenu.Append(-1, "&Telegram")
		QaisWh =QaisMenu.Append(-1, "&Whats App")
		QaisTw =QaisMenu.Append(-1, "&Twitter")
		QaisFa =QaisMenu.Append(-1, "&Facebook")
		ContactMenu.AppendSubMenu(QaisMenu, "&Qais Alrefai")
		MahmoodMenu = wx.Menu()
		MahmoodEm =MahmoodMenu.Append(-1, "&E-mail")
		MahmoodTe =MahmoodMenu.Append(-1, "&Telegram")
		MahmoodWh =MahmoodMenu.Append(-1, "&Whats App")
		MahmoodTw =MahmoodMenu.Append(-1, "&Twitter")
		MahmoodFa =MahmoodMenu.Append(-1, "&Facebook")
		ContactMenu.AppendSubMenu(MahmoodMenu, "&Mahmood atef")
		MesterPerfectMenu = wx.Menu()
		MesterPerfectEm =MesterPerfectMenu.Append(-1, "&E-mail")
		MesterPerfectTe =MesterPerfectMenu.Append(-1, "&Telegram")
		MesterPerfectWh =MesterPerfectMenu.Append(-1, "&Whats App")
		MesterPerfectTw =MesterPerfectMenu.Append(-1, "&Twitter")
		MesterPerfectFa =MesterPerfectMenu.Append(-1, "&Facebook")
		ContactMenu.AppendSubMenu(MesterPerfectMenu, "&Ahmed Bakr")
		TecWindow=ContactMenu.Append(-1, "TecWindow on Telegram")
		MoreMenu.AppendSubMenu(ContactMenu, "&Contact us")
		self.AboutItem = MoreMenu.Append(-1, "About")
		self.CloseProgramItem = MoreMenu.Append(-1, "Close program")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("mailto:ww258148@gmail.com"), QaisEm)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/QaisAlrefai"), QaisTe)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/qais_Alrefai"), QaisTw)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/962792540394"), QaisWh)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/Qais1461"), QaisFa)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("mailto:mahmoud.atef.987123@gmail.com"), MahmoodEm)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/MahmoodAtef"), MahmoodTe)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/mahmoud_atef999"), MahmoodTw)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/201224660664"), MahmoodWh)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/mahmoud.atef.000"), MahmoodFa)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("mailto:AhmedBakr593@gmail.com"), MesterPerfectEm)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/MesterPerfect"), MesterPerfectTe)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/my_nvda"), MesterPerfectTw)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/201554240991"), MesterPerfectWh)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/my.nvda.1"), MesterPerfectFa)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/TecWindowProjects"), TecWindow)
		self.Bind(wx.EVT_MENU, self.OnAboutProgram, self.AboutItem)
		self.Bind(wx.EVT_MENU, self.OnCloseProgram, self.CloseProgramItem)
		self.PopupMenu(MoreMenu)


#creating OnAboutProgram function to show information about this program.
	def OnAboutProgram(self, event):
		AboutDialog = wx.MessageDialog(self, """ Files splitter.
Version: 1.0.
This simple tool allows you to split large text files into small files.
This tool was developed by:
Ahmed Bakr.
Qais Alrifai.
Mahmoud Atef.""", "About the program", style=wx.ICON_INFORMATION+wx.OK)
		AboutDialog.SetOKLabel("&Ok")
		AboutDialog.ShowModal()



	def OnOnOpwnFile(self, ev):
		if not self.FileContent == "":
			ConfirmReplace = wx.MessageDialog(self,"""You have already imported a file.
If you import another file, the new file will replace the old one.
Do you want to proceed?""", "Confirm", style=wx.YES_NO+wx.YES_DEFAULT+wx.ICON_WARNING+wx.ICON_QUESTION)
			ConfirmReplace.SetYesNoLabels("&Yes", "&No")
			if ConfirmReplace.ShowModal() == wx.ID_YES:
				OpenFile = wx.FileDialog(self, "Choose a file", "self.FilePath")
				OpenFile.Wildcard = "Text files (.txt)|*.txt"
				OpenFileResult = OpenFile.ShowModal()
				if OpenFileResult == wx.ID_OK:
					FilePath = OpenFile.Path
					FileName = OpenFile.Filename
					file = open(FilePath, "r")
					self.FileContent= file.read()
					file.close()
				else:
					return
		else:
			OpenFile = wx.FileDialog(self, "Choose a file", "self.FilePath")
			OpenFile.Wildcard = "Text files (.txt)|*.txt"
			OpenFileResult = OpenFile.ShowModal()
			if OpenFileResult == wx.ID_OK:
				FilePath = OpenFile.Path
				FileName = OpenFile.Filename
				file = open(FilePath, "r")
				self.FileContent= file.read()
				self.encoding = file.encoding
				file.close()
			else:
				return

	def OnSaveFiles(self, ev):
		if self.FileContent == "":
			wx.MessageBox("You need to import a file first.", "Error", style=wx.ICON_ERROR)
			return
		SaveFile = wx.FileDialog(self, "Save ", "self.FilePath", style=wx.FD_SAVE+wx.FD_OVERWRITE_PROMPT)
		SaveFile.Wildcard = "Text files (.txt)|*.txt"
		SaveFileResult = SaveFile.ShowModal()
		if SaveFileResult == wx.ID_OK:
			FilePath = SaveFile.Path
			FileName = SaveFile.Filename


		parts = self.split_text(self.FileContent, self.PartsNumber.Value)

		for number, part  in enumerate(parts):
			NewPath = FilePath[:-4] + str(number+1) + ".txt"
			with 			open(NewPath, "w", encoding=self.encoding) as f:
				f.write(part)

	def split_text(self, text: str, maxcharsnum:int = 10000):
		if len(text) <= maxcharsnum:
			return [text]
		rettxt = ""
		retlist = []
		for line in text.split("\n"):
			if len(f"{rettxt}\n{line}") <= maxcharsnum:
				if rettxt == "":
					rettxt = line
				else:
					rettxt += f"\n{line}"
				continue

			crtline = ""
			for word in line.split():
				txt_length = len(f"{rettxt}\n{crtline + ' ' + word}")
				if txt_length <= maxcharsnum:
					if crtline == "":
						crtline = word
					else:
						crtline += " " + word
				elif txt_length > maxcharsnum:
					retlist.append(f"{rettxt}\n{crtline}")
					rettxt = ""
					crtline = word

			if rettxt == "":
				rettxt = crtline
			else:
				rettxt += f"\n{crtline}"
				crtline = ""

		else:
			retlist.append(rettxt)
		return retlist

	def OnCloseProgram(self, event):
		wx.Exit()

FilesSplitter()
app.MainLoop()    