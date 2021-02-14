from tkinter import*
import PyPDF2
from tkinter import filedialog

pdf_list =[]


def UploadAction(event=None):
    UploadAction.counter += 2
    filename = filedialog.askopenfilename()
    pdf_list.append(filename)
    file = filename.split('/')
    lengh = len(file)
    label = Label(root, text=file[lengh - 1])
    label.grid(row=0, column=UploadAction.counter, padx=40, pady=20)
    print('Selected:', filename)

UploadAction.counter = -1

def merge_pdfs():
    merger = PyPDF2.PdfFileMerger()  # object combine pdfs
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('pdf_merger.pdf')


root = Tk()

root. geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title('pdf merger')

pdf_one = Button(text= "First pdf",command=UploadAction,pady=10,padx=10,font=('helvetica',16))
pdf_one.grid(row=0,column=1,padx=40,pady=50)

pdf_two = Button(text= "Second pdf",command=UploadAction,pady=10,padx=10,font=('helvetica',16))
pdf_two.grid(row=0,column=3)

merge_button = Button(text= "Merge the pdfs",command= merge_pdfs,pady=10,padx=10,font=('helvetica',16),bg='green')
merge_button.grid(row=3,column=2,pady=40)



root.mainloop()