
import re
from tkinter import *
import tkinter as tk
from tkinter.font import Font
import webbrowser
from tkinter import ttk
from tkinter import filedialog,messagebox
from PyPDF2 import PdfFileMerger,PdfFileReader, PdfFileWriter
import glob,string,os,sys,collections,time
import pandas as pd
from pandas import ExcelWriter
from random import *
import random

from sys import exit
x=''

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#main inherit classes
#----------------------------------------------------------------

win =tk.Tk()
main_menu=tk.Menu(win)
#-----------------main gui title-----------------
win.title("PyGems Office Utilites")


program_directory=sys.path[0]
win.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "ficon.png")))

#TABS SIZES
style = ttk.Style()

settings = {"TNotebook.Tab": {"configure": {"padding": [28,10], 
"background": "#fdd57e","font" : ('URW Gothic L', '11', 'bold') },
"TNotebook": {"configure": {"tabmargins": [1, 1, 1, 1] } },

 "map": {"background": [("selected", "#C70039"), ("active", "#fc9292")], 
 "foreground": [("selected", "#ffffff"), ("active", "#000000")] } } }


style.theme_create("mi_estilo", parent="alt", settings=settings) 
style.theme_use("mi_estilo")


tab_control = ttk.Notebook(win)

excel_m = ttk.Frame(tab_control)
excel_s = ttk.Frame(tab_control)
pdf_m = ttk.Frame(tab_control)
pdf_s = ttk.Frame(tab_control)
rename = ttk.Frame(tab_control)

 
tab_control.add(excel_m, text='Excel Merger')
tab_control.add(excel_s, text='Excel Spliter')
tab_control.add(pdf_m, text='Pdf Merger')
tab_control.add(pdf_s, text='Pdf Spliter')
tab_control.add(rename, text='File Renamer')
#---------Button for select directory-------------

statusbar =Label(win, text="Click here to visit : pygems.com ",
 bd=1,
  relief=SUNKEN,
   bg="#37474F",
   fg='#fcf9ec',
   height=2,
   font="Times 13",
   cursor="hand2"
   )

statusbar.bind("<Button-1>", lambda e: opnlink("https://pygems.com/"))
statusbar.pack(side=BOTTOM, fill=X)

###### Name conflict ###########

def name_merge():
	counter = 1
	filename = "Merged-{}.pdf"
	b=True
	while b:
		if os.path.isfile(filename.format(counter)):
			counter += 1
		else:
			filename = filename.format(counter)
			b=False
			return filename
def name_split():
	counter = 1
	filename = "Splited-{}.pdf"
	b=True
	while b:
		if os.path.isfile(filename.format(counter)):
			counter += 1
		else:
			filename = filename.format(counter)
			b=False
			return filename
def name_merge_e():
	counter = 1
	filename = "Merged-{}.xlsx"
	b=True
	while b:
		if os.path.isfile(filename.format(counter)):
			counter += 1
		else:
			filename = filename.format(counter)
			b=False
			return filename
def name_split_e():
	counter = 1
	filename = "Splited-{}.xlsx"
	b=True
	while b:
		if os.path.isfile(filename.format(counter)):
			counter += 1
		else:
			filename = filename.format(counter)
			b=False
			return filename

###############################################################


def opnlink(url):
    webbrowser.open_new(url)

#--------------------- wait Screen ------------------

#----------- Excel Merger Start ------------------


#----------- Excel Merger Start ------------------

def fileid():
	RNUM =randint(1,10000)
	return str(RNUM)


def daction():
	entry_d.delete(0, 'end')
	daction.folder_selected = filedialog.askdirectory(initialdir="/",title='Please select a directory')
	if not daction.folder_selected:
		daction.folder_selected=entry_d_var.get()
	else:
		entry_d.insert(0,daction.folder_selected)
	try:
		pp=os.chdir(str(daction.folder_selected))
	except:
		messagebox.showerror("Error", "Files are Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")


def mrgall():
	try:
		btn_txt.set("Merging...")
		button_m.configure(state=DISABLED)
		messagebox.showinfo("Excel Merger","Before Click OK ! \n Must Close All Opened Excel Files of Working Directory")

		d=entry_d_var.get()
		os.chdir(d)
		x=0
		name=name_merge_e()
		writer = ExcelWriter(str(name))
		for filename in glob.glob("*.xlsx"):
		    excel_file = pd.ExcelFile(filename)
		    (_, f_name) = os.path.split(filename)
		    (f_short_name, _) = os.path.splitext(f_name)
		    for sheet_name in excel_file.sheet_names:
		        df_excel = pd.read_excel(filename, sheet_name=sheet_name)
		        df_excel.to_excel(writer, sheet_name+"- "+str(x+1), index=False)
		        x=x+1
		writer.save()
		messagebox.showinfo("Information","Merge Complete")
		btn_txt.set("Merge")
		# progbar.destroy()
		path=os.getcwd()
		button_m.configure(state=NORMAL)
		webbrowser.open(path)
	except:
		messagebox.showerror("Error", "Files are Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")
		btn_txt.set("Merge")
		button_m.configure(state=NORMAL)



def defaultmrg():
	try:
		btn_txt.set("Merging...")
		button_m.configure(state=DISABLED)
		messagebox.showinfo("Excel Merger","Before Click OK ! \n Must Close All Opened Excel Files of Working Directory")
		# pattern ='*.xlsx'
		# xllis=glob.glob(pattern)
		

		d=entry_d_var.get()
		os.chdir(d)	
		pa=selct_typ1.get()
		name=name_merge_e()
		if pa==1:
			file_identifier = "*.xlsx"

			all_data = pd.DataFrame()
			for f in glob.glob(d + "/*" + file_identifier):
			    df = pd.read_excel(f,header=None)
			    all_data = all_data.append(df,ignore_index=True,sort=False)

			writer = pd.ExcelWriter(str(name), engine='xlsxwriter') 
			all_data.to_excel(writer, sheet_name='Sheet1',index=False,header=None)
			writer.save()


			messagebox.showinfo("Information","Merge Complete")
			btn_txt.set("Merge")
			path=os.getcwd()
			button_m.configure(state=NORMAL)
			webbrowser.open(path)
		elif pa==2:
			file_identifier = "*.xlsx"

			all_data = pd.DataFrame()
			for f in glob.glob(d + "/*" + file_identifier):
			    df = pd.read_excel(f)
			    all_data = all_data.append(df,ignore_index=True,sort=False)
			name=name_merge_e()
			writer = pd.ExcelWriter(str(name), engine='xlsxwriter') 
			all_data.to_excel(writer, sheet_name='Sheet1',index=False)
			writer.save()

			messagebox.showinfo("Information","Merge Complete")
			btn_txt.set("Merge")
			path=os.getcwd()
			button_m.configure(state=NORMAL)

	except:
		messagebox.showerror("Error", "Files are Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")
		btn_txt.set("Merge")
		button_m.configure(state=NORMAL)


def mainf():
	r=selct_typ1.get()
	if r==1 or r==2:
		defaultmrg()
	else:
		mrgall()



def daction():
	entry_d.delete(0, 'end')
	daction.folder_selected = filedialog.askdirectory(initialdir="/",title='Please select a directory')
	if not daction.folder_selected:
		daction.folder_selected=entry_d_var.get()
	else:
		entry_d.insert(0,daction.folder_selected)
	try:
		pp=os.chdir(str(daction.folder_selected))
	except:
		messagebox.showerror("Error", "Files are Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")

def empt():
	button_m.configure(state=DISABLED)
	

def pygems():
	messagebox.showinfo("Excel Merger","Merge Complete")


#---------sub Frame------------------------ 
excel_mframe=Frame(excel_m)
excel_sframe=Frame(excel_s)
pdf_mframe=Frame(pdf_m)
pdf_sframe=Frame(pdf_s)
file_rename=Frame(rename)


excel_mframe.pack()
excel_sframe.pack()
pdf_mframe.pack()
pdf_sframe.pack()
file_rename.pack()
#-------EXCEL MERGER --------

rframe=Frame(excel_m)
dframe=Frame(excel_m)
mframe=Frame(excel_m)

pframe=Frame(excel_m)


label_1=Label(excel_mframe,text="PyGems Excel Merger",
	bd=0,
	bg="#393e46",
	fg='#F4511E',
	font='Times 20',
	width=0,
	height=0	
	)
label_1.pack(fill=X,pady=20)




label_x=Label(pframe,text="Warning : Don't close the application if showing Not Responding, just minimize the application")
label_x.pack()

#-----------Radio Button All----------- 
selct_typ1=tk.IntVar()
selct_typ1.set(1)

#radiobtn1 = ttk.Radiobutton(rframe,text="Ignore Header" ,value=1,variable=selct_typ1)
radiobtn2 = ttk.Radiobutton(rframe,text="Default" ,value=1,variable=selct_typ1)
radiobtn3 = ttk.Radiobutton(rframe,text="Same Header" ,value=2,variable=selct_typ1)
radiobtn4 = ttk.Radiobutton(rframe,text="Sheet Wise" ,value=3,variable=selct_typ1)


#------------- directory entry------------
entry_d_var = StringVar()
entry_d=Entry(dframe,width=80,textvariable=entry_d_var,bg='#dedede')
entry_d_txt = entry_d_var.get()

#------------directory Button----------
button_d=tk.Button(dframe,relief=RAISED,font=('Times 10 bold'),text='Select Folder' ,fg='#fcf9ec',bg='#132238',command=daction)

#----------merge button-------------------
btn_txt=StringVar()
button_m=tk.Button(mframe,textvariable=btn_txt,command=mainf,relief=GROOVE,font=('Times 10 bold'),width=22,fg='#fcf9ec',bg='#132238')
btn_txt.set("Merge")

#radio pack
#radiobtn1.pack(side=LEFT,padx=20)
radiobtn2.pack(side=LEFT,padx=20)
radiobtn3.pack(side=LEFT,padx=20)
radiobtn4.pack(side=LEFT,padx=20)


entry_d.pack(ipady=4,side=LEFT,pady=13)
entry_d.focus()

button_d.pack(side=LEFT,padx=10,ipady=2,pady=13)
button_m.pack(pady=20)

#frame pack
#radio button pack
rframe.pack(pady=10)
#directory entry pack
dframe.pack(padx=0)
#merge button pack
mframe.pack(pady=0)
pframe.pack(pady=5)


excel_mframe.config(bg="#D9D9D9")
dframe.config(bg="#ffffff")
rframe.config(bg="#D9D9D9")
mframe.config(bg="#D9D9D9")



###############################################################
###############################################################

###############################################################
#-------------excel spliter -------------------################

sdframe=Frame(excel_sframe)
smframe=Frame(excel_sframe)
seframe=Frame(excel_sframe)
esrframe=Frame(excel_sframe)
pframe=Frame(excel_sframe)

#----- function ------
		

#---------Button for select directory-------------
def sdaction():
	sentry_d.delete(0, 'end')
	
	sdaction.file_selected = filedialog.askopenfilename(initialdir="/",title='Please Select The file',filetypes=(("Excel file","*.xlsx"),("all files","*.")))
		#os.chdir(chd)
	try:
		if not sdaction.file_selected:
			sdaction.file_selected=sentry_d_var.get()
		else:
			sentry_d.insert(0,sdaction.file_selected)
	except:
		messagebox.showerror("Error", "File is Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")
	
def cerrint():
	messagebox.showinfo("Excel Spliter", "Split Done !")

def smfunc():
	try:
		def xtaddt():
				xtaddt.nwin = Toplevel()
				wi_gui=250
				hi_gui=150

				wi_scr=xtaddt.nwin.winfo_screenwidth()
				hi_scr=xtaddt.nwin.winfo_screenheight()

				x=(wi_scr/2)-(wi_gui/2)
				y=(hi_scr/2)-(hi_gui/2)

				xtaddt.nwin.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))

				xtaddt.nwin.title("Row Wise Split")


				l=Label(xtaddt.nwin,text="Enter Number Of Files  : ")
				l.pack(pady=10)
				xtaddt.ed=StringVar()
				eadd=Entry(xtaddt.nwin,width=40,textvariable=xtaddt.ed)
				xtaddt.ed_txt=xtaddt.ed.get()
				eadd.pack(padx=30,pady=10)
				eadd.focus()

				b=Button(xtaddt.nwin,text="OK",command=esokb)
				b.pack(pady=10)


		def esokb():

			esokb.prc=xtaddt.ed.get()

			erwsplt()
			xtaddt.nwin.destroy()

		def erwsplt():
			try:

				sbtn_txt.set("Spliting...")
				sbutton_m.configure(state=DISABLED)
				messagebox.showinfo("Excel Merger","Before Click OK ! \n Must Close All Opened Excel Files \n Enable Macro Once (Trust access to the VBA project object model)  \n Close workbook named Book1 or Book2 if opened \n Don't close the auto opened Excel Files ")
				
				tto=sentry_d_var.get()
				(ro, f_name) = os.path.split(tto)
				os.chdir(ro)

				df = pd.read_excel(f_name)

				total_file =int(esokb.prc)
				#total_file=total_file-1

				sloop_max_range = len(df)//(total_file)

				nxt = sloop_max_range

				fracpart = int(len(df)%total_file)

				#for sloop initialization

				t=0
				# name=name_split_e()
				for x in range(0,total_file):
					df2 = pd.DataFrame()
					for y in range(t,sloop_max_range):
						df2=df2.append(df.iloc[[y,],:])
					writer = ExcelWriter('Splited File_wise'+'-'+str(x)+'.xlsx', engine='xlsxwriter') 
					df2.to_excel(writer,sheet_name='merged',index=False)
					writer.save()
					t=sloop_max_range
					sloop_max_range=nxt+t

					if sloop_max_range+fracpart==len(df):
						sloop_max_range=sloop_max_range+fracpart
					else:
						sloop_max_range=nxt+t
					df2.iloc[0:0]
				sbtn_txt.set("Split")
				sbutton_m.configure(state=NORMAL)

				messagebox.showinfo("Excel Spliter","Split Complete")


				
			except:
				sbtn_txt.set("Split")
				sbutton_m.configure(state=NORMAL)
				messagebox.showerror("Error", "File is Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")


		def eswplt():
			try:

				sbtn_txt.set("Spliting...")
				sbutton_m.configure(state=DISABLED)
				messagebox.showinfo("Excel Merger","Before Click OK ! \n Must Close All Opened Excel Files of Working Directory")

				to=sentry_d_var.get()
				(ro, f_name) = os.path.split(to)
				os.chdir(ro)
				x=0
				excel_file = pd.ExcelFile(f_name)
				(_, f_name) = os.path.split(f_name)
				(f_short_name, _) = os.path.splitext(f_name)
				for sheet_name in excel_file.sheet_names:
					df_excel = pd.read_excel(f_name, sheet_name=sheet_name)
					writer = ExcelWriter(sheet_name+"- "+str(x+1)+"-Splited Sheet_wise.xlsx")
					df_excel.to_excel(writer, sheet_name+"-"+str(x+1), index=False)
					x=x+1
					writer.save()
				sbtn_txt.set("Split")
				sbutton_m.configure(state=NORMAL)

				messagebox.showinfo("Excel Spliter","Split Complete")
			
			except:    
				sbtn_txt.set("Split")
				sbutton_m.configure(state=NORMAL)

				messagebox.showerror("Error", "File is Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")
				
		def xtaddt2():
				messagebox.showinfo("Excel Merger","Before Click OK ! \n Must Close All Opened Excel Files of Working Directory")
				xtaddt2.nwin = Toplevel()
				wi_gui=400
				hi_gui=350

				wi_scr=xtaddt2.nwin.winfo_screenwidth()
				hi_scr=xtaddt2.nwin.winfo_screenheight()

				x=(wi_scr/2)-(wi_gui/2)
				y=(hi_scr/2)-(hi_gui/2)

				xtaddt2.nwin.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))

				xtaddt2.nwin.title("Value Wise Split")

				ly=Label(xtaddt2.nwin,text="How many columns you want to filter ")
				ly.pack(pady=10)

				#-----------Radio Button All----------- 
				xtaddt2.selct_typ1=tk.IntVar()
				xtaddt2.selct_typ1.set(1)

				#radiobtn1 = ttk.Radiobutton(rframe,text="Ignore Header" ,value=1,variable=selct_typ1)
				radiobtn2 = ttk.Radiobutton(xtaddt2.nwin,text="1" ,value=1,variable=xtaddt2.selct_typ1)
				radiobtn3 = ttk.Radiobutton(xtaddt2.nwin,text="2" ,value=2,variable=xtaddt2.selct_typ1)
				radiobtn4 = ttk.Radiobutton(xtaddt2.nwin,text="3" ,value=3,variable=xtaddt2.selct_typ1)

				# xtaddt2.radiovalue=xtaddt2.selct_typ1.get()
				# print("from xtaddt2")
				# print(xtaddt2.radiovalue)

				radiobtn2.pack(pady=5)
				radiobtn3.pack(pady=5)
				radiobtn4.pack(pady=5)

				l=Label(xtaddt2.nwin,text="First Column Name  : ")
				l.pack(pady=5)

				xtaddt2.ed1=StringVar()
				eadd=Entry(xtaddt2.nwin,width=40,textvariable=xtaddt2.ed1)
				xtaddt2.ed_txt1=xtaddt2.ed1.get()
				
				eadd.pack(padx=30,pady=5)
				eadd.focus()

				l1=Label(xtaddt2.nwin,text="Second Column Name  : ")
				l1.pack(pady=5)
				xtaddt2.ed2=StringVar()
				eadd1=Entry(xtaddt2.nwin,width=40,textvariable=xtaddt2.ed2)
				xtaddt2.ed_txt2=xtaddt2.ed2.get()
				eadd1.pack(padx=30,pady=5)

				l2=Label(xtaddt2.nwin,text="Third Column Name  : ")
				l2.pack(pady=5)
				xtaddt2.ed3=StringVar()
				eadd2=Entry(xtaddt2.nwin,width=40,textvariable=xtaddt2.ed3)
				xtaddt2.ed_txt3=xtaddt2.ed3.get()
				eadd2.pack(padx=30,pady=5)

				b=Button(xtaddt2.nwin,text="OK",command=esokb2)
				b.pack(pady=10)

		def esokb2():

			esokb2.r1=xtaddt2.selct_typ1.get()

			esokb2.p1=xtaddt2.ed1.get()
			

			esokb2.p2=xtaddt2.ed2.get()
			

			esokb2.p3=xtaddt2.ed3.get()
			

			
			evwplt()

			xtaddt2.nwin.destroy()

			

		def evwplt():

			try:
				sbtn_txt.set("Spliting...")
				sbutton_m.configure(state=DISABLED)

				
				def fone():
					try:
						sbtn_txt.set("Spliting...")
						sbutton_m.configure(state=DISABLED)
						to=sentry_d_var.get()
						(ro, f_name) = os.path.split(to)
						os.chdir(ro)
						b=f_name
						a=esokb2.p1
						name=name_split_e()


						df=pd.read_excel(b)
						names = df[a].unique().tolist()
						

						writer = pd.ExcelWriter(str(name), engine='xlsxwriter')

						for name in names:
						    mydf=df[(df[a] ==name)]
						    mydf.to_excel(writer, sheet_name=str(name),index=False)
						writer.save()

						sbtn_txt.set("Split")
						sbutton_m.configure(state=NORMAL)
						messagebox.showinfo("Excel Spliter","Split Complete")
					except:
						sbtn_txt.set("Split")
						sbutton_m.configure(state=NORMAL)
						messagebox.showerror("Error", "Check columns name and close the excel file , try again ")
				
				def ftwo():
					try:
						sbtn_txt.set("Spliting...")
						sbutton_m.configure(state=DISABLED)

						to=sentry_d_var.get()
						(ro, f_name) = os.path.split(to)
						os.chdir(ro)
						b=f_name
						a=esokb2.p1
						c=esokb2.p2
						name=name_split_e()


						df=pd.read_excel(b)
						df = df.applymap(str)
						
						writer = pd.ExcelWriter(str(name), engine='xlsxwriter')

						df2 = df.drop_duplicates(subset=[a,c])

						for i in range(0,len(df2)):
								one=str(df2.iloc[i][a])
								two=str(df2.iloc[i][c])

								t=df[(df[a] == one)&(df[c]==two)]
								#t=df[(df['Depot'] ==depo_code)&(df['RSM Territory']==rsm_code)]
								t.to_excel(writer, sheet_name=one+"-"+two,index=False)
						writer.save()
						sbtn_txt.set("Split")
						sbutton_m.configure(state=NORMAL)
						messagebox.showinfo("Excel Spliter","Split Complete")
					except:
						sbtn_txt.set("Split")
						sbutton_m.configure(state=NORMAL)
						messagebox.showerror("Error", "Check columns name and close the excel file , try again ")
					


				def fthree():
					try:
						sbtn_txt.set("Spliting...")
						sbutton_m.configure(state=DISABLED)

						to=sentry_d_var.get()
						(ro, f_name) = os.path.split(to)
						os.chdir(ro)
						b=f_name

						a=esokb2.p1
						c=esokb2.p2
						d=esokb2.p3

						df=pd.read_excel(b)
						df = df.applymap(str)
						RNUM =randint(1000,10000)

						writer = pd.ExcelWriter(str(name), engine='xlsxwriter')

						df2 = df.drop_duplicates(subset=[a,c,d])

						for i in range(0,len(df2)):
								one=str(df2.iloc[i][a])
								two=str(df2.iloc[i][c])
								three=str(df2.iloc[i][d])

								t=df[(df[a] == one)&(df[c]==two)&(df[d]==three)]
								#t=df[(df['Depot'] ==depo_code)&(df['RSM Territory']==rsm_code)]
								t.to_excel(writer, sheet_name=one+"-"+two+"-"+three,index=False)
						writer.save()
						sbtn_txt.set("Split")
						sbutton_m.configure(state=NORMAL)
						messagebox.showinfo("Excel Spliter","Split Complete")

					except:
						sbtn_txt.set("Split")
						sbutton_m.configure(state=NORMAL)
						messagebox.showerror("Error", "Check columns name and close the excel file , try again ")
			except:
				sbtn_txt.set("Split")
				sbutton_m.configure(state=NORMAL)
				messagebox.showerror("Error", "Check columns name and close the excel file , try again ")
					


				
			h=int(esokb2.r1)
			

			if h==1:
				fone()
			elif h==2:
				ftwo()
			else:
				fthree()

		pa=esselct_typ1.get()
		
		if pa ==1:
			eswplt()
		elif pa==2:
			xtaddt()
		elif pa==3:
			xtaddt2()
	except:
		sbtn_txt.set("Split")
		sbutton_m.configure(state=NORMAL)

		messagebox.showerror("Error", "File is Read Only Or Wrong Directory !\n  Visit : pygems.com For Tutorial")

label_1=Label(excel_sframe,text="PyGems Excel Spliter",
	bd=0,
	bg="#393e46",
	fg='#F4511E',
	font='Times 20',
	width=0,
	height=0	
	)
label_1.pack(pady=20)

label_x=Label(pframe,text="Warning : Don't close the application if showing Not Responding, just minimize the application")
label_x.pack()




esselct_typ1=tk.IntVar()
esselct_typ1.set(1)

radiobtn1 = ttk.Radiobutton(esrframe,text="Sheet Wise Split",value=1,variable=esselct_typ1)
radiobtn2 = ttk.Radiobutton(esrframe,text="File Wise Split" ,value=2,variable=esselct_typ1)
radiobtn3 = ttk.Radiobutton(esrframe,text="Value Wise Split" ,value=3,variable=esselct_typ1)
#radiobtn4 = ttk.Radiobutton(esrframe,text="Random Num" ,value=4,variable=esselct_typ1)

#------------- directory entry------------
sentry_d_var = StringVar()
sentry_d=Entry(sdframe,width=80,textvariable=sentry_d_var,bg='#dedede')
sentry_d_txt = sentry_d_var.get()

#----------------entry box-----------


#------------directory Button----------
sbutton_d=tk.Button(sdframe,relief=RAISED,font=('Times 10 bold'),text='Select File' ,fg='#fcf9ec',bg='#132238',command=sdaction)

#----------merge button-------------------
sbtn_txt=StringVar()
sbutton_m=tk.Button(smframe,textvariable=sbtn_txt,command=smfunc,relief=GROOVE,font=('Times 10 bold'),width=22,fg='#fcf9ec',bg='#132238')
sbtn_txt.set("Split")







radiobtn1.pack(side=LEFT,padx=20)
radiobtn2.pack(side=LEFT,padx=20)
radiobtn3.pack(side=LEFT,padx=20)
#radiobtn3.pack(side=LEFT,padx=20)

sbutton_m.pack(pady=20)
#frame pack
esrframe.pack(pady=10)
#directory entry pack
sdframe.pack(padx=0)
#sentry pack
seframe.pack(pady=0)
#merge button pack
smframe.pack(pady=0)

pframe.pack(pady=5)

excel_sframe.config(bg="#D9D9D9")
smframe.config(bg="#D9D9D9")
sdframe.config(bg="#ffffff")
seframe.config(bg="#D9D9D9")
esrframe.config(bg="#D9D9D9")


#############################################################
#############################################################
##################### PDF MERGER ############################

prframe=Frame(pdf_m)
pdframe=Frame(pdf_m)
pmframe=Frame(pdf_m)

pddframe=Frame(pdf_m)
################ PDF MERGER ########################

def pdaction():
	pentry_d.delete(0, 'end')
	
	pfolder_selected = filedialog.askdirectory(initialdir="/",title='Please select a directory')
	if not pfolder_selected:
		pfolder_selected=pentry_d_var.get()
	else:
		pentry_d.insert(0,pfolder_selected)
	try:
		pp=os.chdir(str(pfolder_selected))
	except:
		messagebox.showerror("Error", "Empty or wrong Directory")

def pempt():
	pbutton_m.configure(state=DISABLED)

def pmfunc():
	try:
		pfolder_selected=pentry_d_var.get()
		os.chdir(pfolder_selected)
		pattern ='*.pdf'
		pdfs=glob.glob(pattern)
		
		if not pdfs:
			messagebox.showerror("Error", "Wrong directory or There is no Pdf file found")
			pbtn_txt.set("Merge")
		else:
			pbtn_txt.set("Merging...")
			pbutton_m.configure(state=DISABLED)
			pm2=pselct_typ1.get()
			if pm2==2:
				pempt()
				
				merger = PdfFileMerger()
				for pdf in pdfs:
				    merger.append(pdf)
				#for name conflict
				name=name_merge()

				#
				merger.write(str(name))
				pbutton_m.configure(state=NORMAL)
				# webbrowser.open(pfolder_selected)
			elif pm2==1:
				pempt()
				pattern ='*.pdf'
				pdfs=glob.glob(pattern)

				merger = PdfFileMerger()
				outPdf= PdfFileWriter()
				name=name_merge()
				for pdf in pdfs:
					b=open(pdf,'rb')
					rpdf = PdfFileReader(b)
					if rpdf.getNumPages() % 2 == 1:
						outPdf.appendPagesFromReader(rpdf)
						outPdf.addBlankPage()
					else:
						outPdf.appendPagesFromReader(rpdf)
					

					outStream=open(str(name),'wb')
					outPdf.write(outStream)
					outStream.close()

		pbutton_m.configure(state=NORMAL)
		pbtn_txt.set("Merge")

		ppygems()
		webbrowser.open(pfolder_selected)
	except:
		messagebox.showerror("Error", "Enter a Valid Directory or No pdf found")
def ppygems():
	messagebox.showinfo("Pdf Merger ","Merge Complete")

label_1=Label(pdf_m,text="PyGems Pdf Merger",
	bd=0,
	bg="#393e46",
	fg='#F4511E',
	font='Times 20',
	width=0,
	height=0	
	)
label_1.pack(pady=20)

label_x=Label(pddframe,text="Warning : Don't close the application if showing Not Responding, just minimize the application")
label_x.pack()


#-------------radio Button ----------------
pselct_typ1=tk.IntVar()
pselct_typ1.set(2)


pradiobtn1 = ttk.Radiobutton(prframe,text="Add A Blank Page For Odd Number Of Pages",value=1,variable=pselct_typ1)
pradiobtn2 = ttk.Radiobutton(prframe,text="Default" ,value=2,variable=pselct_typ1)


pradiobtn1.pack(side=LEFT,padx=20)
pradiobtn2.pack(side=LEFT,padx=20)

#------------- directory entry------------
pentry_d_var = StringVar()
pentry_d=Entry(pdframe,width=80,textvariable=pentry_d_var,bg='#dedede')
pentry_d_txt = pentry_d_var.get()

#------------directory Button----------
pbutton_d=tk.Button(pdframe,relief=RAISED,font=('Times 10 bold'),text='Select Folder' ,fg='#fcf9ec',bg='#132238',command=pdaction)

#----------merge button-------------------
pbtn_txt=StringVar()
pbutton_m=tk.Button(pmframe,textvariable=pbtn_txt,command=pmfunc,relief=GROOVE,font=('Times 10 bold'),width=22,fg='#fcf9ec',bg='#132238')
pbtn_txt.set("Merge")

pentry_d.pack(ipady=4,side=LEFT,pady=13)
pentry_d.focus()

pbutton_d.pack(side=LEFT,padx=10,ipady=2,pady=13)
pbutton_m.pack(pady=20)

#frame pack
prframe.pack(pady=5)
#directory entry pack
pdframe.pack(padx=0)

#merge button pack
pmframe.pack(pady=0)

pddframe.pack(pady=0)


pdf_mframe.config(bg="#D9D9D9")
prframe.config(bg="#D9D9D9")
pmframe.config(bg="#D9D9D9")

#####################################################################
################### Pdf Split #########################################
#####################################################################
#####################################################################

psdframe=Frame(pdf_s)
psmframe=Frame(pdf_s)
pseframe=Frame(pdf_s)
psrframe=Frame(pdf_s)

pddsrframe=Frame(pdf_s)



#----- function ------

#---------Button for select directory-------------
def psdaction():
	psentry_d.delete(0, 'end')
	psdaction.file_selected = filedialog.askopenfilename(initialdir="/",title='Please file',filetypes=(("Pdf file","*.pdf"),("all files","*.")))
	
	ass=psdaction.file_selected.split("/")
	chd="/".join(ass[:-1])
	os.chdir(chd)

	try:
		if not psdaction.file_selected:
			psdaction.file_selected=sentry_d_var.get()
		else:
			psentry_d.insert(0,psdaction.file_selected)
	except:
		messagebox.showerror("Error", "Empty or wrong Directory")

def sempt():
	psbutton_m.configure(state=DISABLED)

def errint():
	messagebox.showerror("Error", "Read-only or Damaged file !\n  Visit : pygems.com For Tutorial")
def cerrint():
	messagebox.showinfo("Pdf Spliter", "Split Done !")

def psmfunc():

	def splt():
		try:

			psdir=psentry_d_var.get()
			# od=psdir.split("/")
			# chd="/".join(od[:-1])
			# os.chdir(chd)
			inputpdf = PdfFileReader(open(psdaction.file_selected, "rb"))
			psbtn_txt.set("Spliting...")
			psbutton_m.configure(state=DISABLED)



			for i in range(inputpdf.numPages):
			    output = PdfFileWriter()
			    output.addPage(inputpdf.getPage(i))
			    with open("Splited-Document-page-%s.pdf" % i, "wb") as outputStream:
			        output.write(outputStream)
			cerrint()
			psbtn_txt.set("Split")
			psbutton_m.configure(state=NORMAL)
			
			#webbrowser.open(chd)
		except:
			errint()


	def prxtaddt():
		try:
			
			inputpdf = PdfFileReader(open(psdaction.file_selected, "rb"))

			prxtaddt.nwin = Toplevel()
			wi_gui=350
			hi_gui=160

			wi_scr=prxtaddt.nwin.winfo_screenwidth()
			hi_scr=prxtaddt.nwin.winfo_screenheight()

			x=(wi_scr/2)-(wi_gui/2)
			y=(hi_scr/2)-(hi_gui/2)

			prxtaddt.nwin.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))

			prxtaddt.nwin.title("Pdf Spliter")

			prl=Label(prxtaddt.nwin,text="Enter Sequential Page Number Separated By Comma E.g : 2,3,4 ")
			prl.pack(pady=10)
			prxtaddt.pred=StringVar()
			preadd=Entry(prxtaddt.nwin,width=40,textvariable=prxtaddt.pred)
			prxtaddt.pred_txt=prxtaddt.pred.get()
			preadd.pack(padx=15,pady=10)
			preadd.focus()

			prb=Button(prxtaddt.nwin,text="OK",command=prokb)
			prb.pack(pady=10)
		except:
			errint()

	def prokb():

		prc=prxtaddt.pred.get()
		#print("print from :",c)
		spltn()
		prxtaddt.nwin.destroy()


	def spltn():
		try:
			

			psdir=psentry_d_var.get()
			# od=psdir.split("/")
			# chd="/".join(od[:-1])
			# os.chdir(chd)
			inputpdf = PdfFileReader(open(psdaction.file_selected, "rb"),strict=False)
			psbtn_txt.set("Spliting...")
			psbutton_m.configure(state=DISABLED)

			s=prxtaddt.pred.get()
			pnum=s.split(",")

			merger = PdfFileMerger()
			outPdf= PdfFileWriter()
			rpdf = inputpdf
			name=name_split()
			for i in pnum:
				for j in range(inputpdf.numPages):

					if j==int(i)-1:
						outPdf.addPage(rpdf.getPage(j))
					#outPdf.addBlankPage()
			
			
			outStream=open(str(name),'wb')
			outPdf.write(outStream)
			outStream.close()

			psbtn_txt.set("Split")
			psbutton_m.configure(state=NORMAL)
			cerrint()
			#webbrowser.open(chd)
		except:
			psbtn_txt.set("Split")
			psbutton_m.configure(state=NORMAL)
			errint()

	a=psselct_typ1.get()

	if a==1:
		splt()
	elif a==2:
		prxtaddt()
	else:
		pass

pslabel_1=Label(pdf_s,text="PyGems Pdf Spliter",
	bd=0,
	bg="#393e46",
	fg='#F4511E',
	font='Times 20',
	width=0,
	height=0	
	)

pslabel_1.pack(pady=20)

label_x=Label(pddsrframe,text="Warning : Don't close the application if showing Not Responding, just minimize the application")
label_x.pack()

#------------- directory entry------------
psentry_d_var = StringVar()
psentry_d=Entry(psdframe,width=80,textvariable=psentry_d_var,bg='#dedede')
psentry_d_txt = psentry_d_var.get()

#------------- Radio Button ---------
psselct_typ1=tk.IntVar()
psselct_typ1.set(2)

psradiobtn1 = ttk.Radiobutton(psrframe,text="Spit All Pages",value=1,variable=psselct_typ1)
psradiobtn2 = ttk.Radiobutton(psrframe,text="Split By Page Numbers" ,value=2,variable=psselct_typ1)


psradiobtn1.pack(side=LEFT,padx=20)
psradiobtn2.pack(side=LEFT,padx=20)

#------------directory Button----------
psbutton_d=tk.Button(psdframe,relief=RAISED,font=('Times 10 bold'),text='Select File' ,fg='#fcf9ec',bg='#132238',command=psdaction)

#----------merge button-------------------
psbtn_txt=StringVar()
psbutton_m=tk.Button(psmframe,textvariable=psbtn_txt,command=psmfunc,relief=GROOVE,font=('Times 10 bold'),width=22,fg='#fcf9ec',bg='#132238')
psbtn_txt.set("Split")


psentry_d.pack(ipady=4,side=LEFT,pady=13)
psentry_d.focus()
psbutton_d.pack(side=LEFT,padx=10,ipady=2,pady=13)

psbutton_m.pack(pady=20)
#frame pack
psrframe.pack(pady=10)
#directory entry pack
psdframe.pack(padx=0)
#sentry pack


pseframe.pack(pady=0)
#merge button pack
psmframe.pack(pady=0)

pddsrframe.pack(pady=0)

excel_sframe.config(bg="#D9D9D9")
psmframe.config(bg="#D9D9D9")
psdframe.config(bg="#ffffff")
pseframe.config(bg="#D9D9D9")
psrframe.config(bg="#D9D9D9")

#############################################################
#############################################################
##################### Renamer ############################
############################################################
############################################################

rrrframe=Frame(rename)
rrdframe=Frame(rename)
rrmframe=Frame(rename)
rrcframe=Frame(rename)


def rrdaction():
	rrentry_d.delete(0, 'end')
	
	rrfolder_selected = filedialog.askdirectory(initialdir="/",title='Please select a directory')
	if not rrfolder_selected:
		rrfolder_selected=rrentry_d_var.get()
	else:
		rrentry_d.insert(0,rrfolder_selected)
	try:
		rrpp=os.chdir(str(rrfolder_selected))
	except:
		messagebox.showerror("Error", "Empty or wrong Directory")

c=''

def reerror():
	messagebox.showerror("Error","Checked All Or Mention File type \n Empty or wrong Directory")
def chkfiletyp():
	gftype=pcnumentry_d_var.get()

	if gftype=="":
		reerror()

def repygems():
	messagebox.showinfo("Batch Rename","Batch Rename Complete")

def rrmfunc():
	try:
		dd=rrentry_d_var.get()
		os.chdir(dd)
		rrbtn_txt.set("Renaiming...")
		rrbutton_m.configure(state=DISABLED)

		cboxvalue=cvar.get()
		ffftype=pcnumentry_d_var.get()
		bfiles = list(filter(lambda x: os.path.isfile(x), os.listdir()))

		tfiles=[]

		for file in glob.glob("*."+ffftype):
			tfiles.append(file)

		if cboxvalue==1 and ffftype=="":
			files=bfiles
		elif cboxvalue !=1 and ffftype:
			files=tfiles
		else:
			pass
		def SNrename():
			try:
				i=1
				for file in files:
					name,e = file.rsplit('.',1)
					os.rename(file,str(i)+'.'+e)
					i=i+1
				repygems()
			except:
				reerror()

		def RNrename():
			try:
				for file in files:
					name,e = file.rsplit('.',1)
					RNUM =randint(1000,10000)
					os.rename(file,str(RNUM)+'.'+e)
				repygems()
				#print("*** RENAME COMPLETED ***")
			except:
				reerror()

		def RSrename():
			try:
				letters = string.ascii_uppercase
				for file in files:
					name,e = file.rsplit('.',1)
					s=''.join(random.choice(letters) for i in range(5))
					os.rename(file,s+'.'+e)
				repygems()
			#print("*** RENAME COMPLETED ***")
			except:
				reerror()
		def ADDrename():
			#c=input("what do u want to Add :")
			try:
				d=xtaddt.ed.get()
				#print("value of d :",d)
				for file in files:
					name,e = file.rsplit('.',1)
					os.rename(file,name+d+'.'+e)
				repygems()
			except:
				reerror()
			#repygems()
			#print("*** RENAME COMPLETED ***")
		def RErename():
			#x=input('insert what u want to replace :')
			#y=input('insert BY what u want to replace :')
			try:
				x=xtaddtre.edr.get()
				y=xtaddtre.ed2.get()

				for file in files:
					name,e = file.rsplit('.',1)
					rep=name.replace(x,y,)
					os.rename(file,rep+'.'+e)
				repygems()
			except:
				reerror()

		a=rrselct_typ1.get()
		
		def xtaddt():
			xtaddt.nwin = Toplevel()
			wi_gui=250
			hi_gui=150

			wi_scr=xtaddt.nwin.winfo_screenwidth()
			hi_scr=xtaddt.nwin.winfo_screenheight()

			x=(wi_scr/2)-(wi_gui/2)
			y=(hi_scr/2)-(hi_gui/2)

			xtaddt.nwin.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))

			xtaddt.nwin.title("Renamer")


			l=Label(xtaddt.nwin,text="Enter what you want to add : ")
			l.pack(pady=10)
			xtaddt.ed=StringVar()
			eadd=Entry(xtaddt.nwin,width=40,textvariable=xtaddt.ed)
			xtaddt.ed_txt=xtaddt.ed.get()
			eadd.pack(padx=30,pady=10)
			eadd.focus()

			b=Button(xtaddt.nwin,text="OK",command=okb)
			b.pack(pady=10)


		def xtaddtre():
			xtaddtre.nwin = Toplevel()
			wi_gui=250
			hi_gui=220

			wi_scr=xtaddtre.nwin.winfo_screenwidth()
			hi_scr=xtaddtre.nwin.winfo_screenheight()

			x=(wi_scr/2)-(wi_gui/2)
			y=(hi_scr/2)-(hi_gui/2)

			xtaddtre.nwin.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))

			xtaddtre.nwin.title("Renamer")


			l=Label(xtaddtre.nwin,text="Find What")
			l.pack(pady=10)
			xtaddtre.edr=StringVar()
			eadd=Entry(xtaddtre.nwin,width=40,textvariable=xtaddtre.edr)
			xtaddtre.ed_txt=xtaddtre.edr.get()
			eadd.pack(padx=35,pady=10)

			l2=Label(xtaddtre.nwin,text="Replace With")
			l2.pack(pady=10)
			xtaddtre.ed2=StringVar()
			eadd2=Entry(xtaddtre.nwin,width=40,textvariable=xtaddtre.ed2)
			xtaddtre.ed_txt=xtaddtre.ed2.get()
			eadd2.pack(padx=35,pady=10)
			
			eadd.focus()

			b2=Button(xtaddtre.nwin,text="OK",command=okbre)
			b2.pack(pady=10)


		def okb():
			c=xtaddt.ed.get()
			#print("print from :",c)
			ADDrename()
			xtaddt.nwin.destroy()
		
		def okbre():

			r=xtaddtre.edr.get()
			r2=xtaddtre.ed2.get()
			#print("print from :",c)
			RErename()
			xtaddtre.nwin.destroy()

		rrbutton_m.configure(state=NORMAL)
		rrbtn_txt.set("Rename")

		#ftyp = input("Please insert the file extension u want to rename  or press enter to rename all type files : ")
		if a==3 :
			SNrename()
		elif a==4:
			RNrename()
		elif a==5:
			RSrename()
		elif a==2:
			xtaddt()
			
		elif a==1:
			xtaddtre()
		else:
			reerror()
	except:
		reerror()


label_1=Label(rename,text="PyGems Batch File Renamer",
	bd=0,
	bg="#393e46",
	fg='#F4511E',
	font='Times 20',
	width=0,
	height=0	
	)
label_1.pack(pady=20)

#-----------Radio Button All----------- 

rrselct_typ1=tk.IntVar()
rrselct_typ1.set(2)

radiobtn1 = ttk.Radiobutton(rrrframe,text="Replace" ,value=1,variable=rrselct_typ1)
radiobtn2 = ttk.Radiobutton(rrrframe,text="Add" ,value=2,variable=rrselct_typ1)
radiobtn3 = ttk.Radiobutton(rrrframe,text="Sequential Num" ,value=3,variable=rrselct_typ1)
radiobtn4 = ttk.Radiobutton(rrrframe,text="Random Num" ,value=4,variable=rrselct_typ1)
radiobtn5 = ttk.Radiobutton(rrrframe,text="Random Text" ,value=5,variable=rrselct_typ1)
#------- Check box --------------------------
cvar=tk.IntVar()
c1=Checkbutton(rrcframe,text="All",variable=cvar)

c1.pack(side=LEFT,padx=20)

#----------------entry box-----------
pc_label=Label(rrcframe,text="File Type E.g: pdf ")
pc_label.pack(pady=5,side=LEFT)

#----entry box--------
pcnumentry_d_var=StringVar()
pcsentry=tk.Entry(rrcframe,textvariable=pcnumentry_d_var)
pcsentry.pack(pady=5,side=LEFT)

#------------- directory entry------------
rrentry_d_var = StringVar()
rrentry_d=Entry(rrdframe,width=80,textvariable=rrentry_d_var,bg='#dedede')
rrentry_d_txt = rrentry_d_var.get()

#------------directory Button----------
rrbutton_d=tk.Button(rrdframe,relief=RAISED,font=('Times 10 bold'),text='Select Folder' ,fg='#fcf9ec',bg='#132238',command=rrdaction)

#----------merge button-------------------
rrbtn_txt=StringVar()
rrbutton_m=tk.Button(rrmframe,textvariable=rrbtn_txt,command=rrmfunc,relief=GROOVE,font=('Times 10 bold'),width=22,fg='#fcf9ec',bg='#132238')
rrbtn_txt.set("Rename")

#radio pack

radiobtn1.pack(side=LEFT,padx=20)
radiobtn2.pack(side=LEFT,padx=20)
radiobtn3.pack(side=LEFT,padx=20)
radiobtn4.pack(side=LEFT,padx=20)
radiobtn5.pack(side=LEFT,padx=20)

rrentry_d.pack(ipady=4,side=LEFT,pady=13)
rrentry_d.focus()

rrbutton_d.pack(side=LEFT,padx=10,ipady=2,pady=13)
rrbutton_m.pack(pady=20)

#frame pack
#radio button pack
rrrframe.pack(pady=15)

rrcframe.pack(pady=15)

#directory entry pack
rrdframe.pack(padx=0)

#merge button pack
rrmframe.pack(pady=0)


rrcframe.config(bg="#D9D9D9")
file_rename.config(bg="#D9D9D9")
rrrframe.config(bg="#D9D9D9")
rrmframe.config(bg="#D9D9D9")

tab_control.pack(expand=1, fill='both')

#main window size

wi_gui=730
hi_gui=400

wi_scr=win.winfo_screenwidth()
hi_scr=win.winfo_screenheight()

x=(wi_scr/2)-(wi_gui/2)
y=(hi_scr/2)-(hi_gui/2)

win.geometry('%dx%d+%d+%d'%(wi_gui,hi_gui,x,y))
#win.iconbitmap(r'C:\Users\Aristo\Desktop\Niloy\Excel_Merger-master\Excel_Merger-master\images\xlsx.ico')
win.resizable(False, False)
win.mainloop()