from tkinter import messagebox
 
res = messagebox.askquestion('Gender testing','Are u gay')
print(res)
res = messagebox.askyesno('Gender testing','Are u sure')
print(res)
res = messagebox.askyesnocancel('Gender testing','No way YOU GAY')
print(res)
res = messagebox.askokcancel('Gender testing','If u click No, YOU GAY')
print(res)
res = messagebox.askretrycancel('Final verdict','Why are YOU GAY')
print(res)
