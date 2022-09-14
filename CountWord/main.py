import myfun
import pandas as pd
import datetime
from tkinter import *

data_file = pd.DataFrame(columns=['File Name', 'Read/Not Read'])
data_word = pd.DataFrame(columns=['Word', 'Quantity'])


def main(catalogname):
    global data_file, data_word
    all_files = myfun.get_file_name(catalogname, chk_txt.get(), chk_doc.get(), chk_pdf.get(), chk_pptx.get(),
                                    chk_xlsx.get())
    for filename in all_files:
        data_file = myfun.create_files_tatus_table(data_file, filename, myfun.opening_file(filename, catalogname),
                                                   mylist)
        if myfun.opening_file(filename, catalogname):
            if filename.endswith(".txt"):
                words = myfun.get_words(str(myfun.read_txt((catalogname + '\\' + filename))))
                words_dict = myfun.get_words_dict(words)
            if filename.endswith(".pdf"):
                words = myfun.get_words(str(myfun.read_pdf((catalogname + '\\' + filename))))
                words_dict = myfun.get_words_dict(words)
            if filename.endswith(".docx") or filename.endswith(".doc"):
                words = myfun.get_words(str(myfun.read_docx((catalogname + '\\' + filename))))
                words_dict = myfun.get_words_dict(words)
            if filename.endswith(".xlsx") or filename.endswith(".xls"):
                words = myfun.get_words(str(myfun.read_xlsx((catalogname + '\\' + filename))))
                words_dict = myfun.get_words_dict(words)
            if filename.endswith(".pptx"):
                words = myfun.get_words(str(myfun.read_pptx((catalogname + '\\' + filename))))
                words_dict = myfun.get_words_dict(words)

            for word in words_dict:
                if len(word) > 3:
                    data_word = myfun.create_word_quantity_table(data_word, word, words_dict[word])
    data_word = data_word.groupby('Word').sum().reset_index()
    data_word = data_word.sort_values(by='Quantity', ascending=False)
    new_row = pd.DataFrame([[str(datetime.datetime.now())[:11], str(datetime.datetime.now())[11:19]]],
                           columns=['File Name', 'Read/Not Read'])
    data_file = pd.concat([data_file, new_row], ignore_index=True)
    myfun.saving_report(data_word, data_file, catalogname)
    mylist.insert(END, "Saved in:")
    mylist.insert(END, catalogname + myfun.REPORT.replace("/", "\\"))


def clicked():
    main(txt.get())


window = Tk()

window.title("Word Counter")
window.geometry('330x450')
window['background'] = '#C6F6FE'
lbl = Label(window, text="Enter directory with files", font=("System", 20), bg='#C6F6FE', fg='#0C123B')
lbl.grid(column=1, row=0, columnspan=5)
txt = Entry(window, width=40)
txt.grid(column=1, row=1, columnspan=5)

btn = Button(window, text="Ok", command=clicked, font=("System", 10))
btn.grid(column=3, row=4)

mylist = Listbox(window, height=14, width=30, font=("System", 10))
mylist.grid(column=1, row=5, columnspan=5)

chk_txt = BooleanVar()
chk_doc = BooleanVar()
chk_pdf = BooleanVar()
chk_xlsx = BooleanVar()
chk_pptx = BooleanVar()
chk_txt.set(True)
chk_doc.set(True)
chk_pdf.set(True)
chk_xlsx.set(True)
chk_pptx.set(True)

chk1 = Checkbutton(window, text='.txt', variable=chk_txt, bg='#C6F6FE')
chk1.grid(column=1, row=3, padx=10)

chk2 = Checkbutton(window, text='.doc', variable=chk_doc, bg='#C6F6FE')
chk2.grid(column=2, row=3)

chk3 = Checkbutton(window, text='.pdf', variable=chk_pdf, bg='#C6F6FE')
chk3.grid(column=3, row=3)

chk4 = Checkbutton(window, text='.xlsx', variable=chk_xlsx, bg='#C6F6FE')
chk4.grid(column=4, row=3)

chk5 = Checkbutton(window, text='.pptx', variable=chk_pptx, bg='#C6F6FE')
chk5.grid(column=5, row=3)
window.mainloop()

a = 1 + 2
