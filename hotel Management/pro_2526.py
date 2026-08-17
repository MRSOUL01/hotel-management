import pandas as pd
import tkinter as tk
from tkinter import messagebox
 
main_heart = tk.Tk()

#main settings
main_heart.geometry("400x300")
main_heart.title("N&S HOTEL")
Button_width = 15

#admin button
def adminpage():
    admin = tk.Toplevel()
    admin.geometry("300x200")
    admin.title("ADMIN PASSWORD")

    frame = tk.Frame(admin, bg="lightgray", bd=2, relief="groove")
    frame.pack(padx=20, pady=20)

    pas1= tk.Label(frame, text="Password:")
    pas1.grid(row=1, column=0)

    ent=tk.Entry(frame, show="*")
    ent.grid(row=1, column=1)

    def login():
        if ent.get() == "N&S_HoteL":
            admin.destroy()
            
            admin_panel = tk.Toplevel()
            admin_panel.geometry("500x600")
            admin_panel.title("ADMIN PANEL")
            wel = tk.Label(admin_panel, text="WELCOME TO ADMIN PANEL OF N&S HOTEL")
            wel.pack()
            adframe = tk.Frame(admin_panel, bg="Lightgray", bd=2, relief="groove")
            adframe.pack(padx=40, pady=40)
            
            def guest():    # admin guest
                gt = tk.Toplevel()
                gt.geometry("600x300")
                gt.title("GUEST DETAILS")
                
                df = pd.read_csv("gtinfo.csv", index_col="booking_id")
                
                wel = tk.Label(gt, text="ADMIN - GUEST DETAILS")
                wel.pack()
                gtframe = tk.Frame(gt, bg="Lightgray", bd=2, relief="groove")
                gtframe.pack(padx=50, pady=50)
                
                def gt_s():     # admin guest search
                    sgt = tk.Toplevel()
                    sgt.geometry("500x500")
                    sgt.title("SEARCH BY")
                    
                    by = tk.Label(sgt, text="SEARCH BY:")
                    by.pack()
                    sframe = tk.Frame(sgt, bg="Lightgray", bd=2, relief="groove")
                    sframe.pack(padx=80, pady=60)
                    def bk_id():
                        book = tk.Toplevel()
                        book.title("BOOKING_ID")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="Booking_ID:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book )
                        rt.place(x=20, y=140, width=460, height=240)

                        def search_rt():
                            bid = ent.get()
                            if bid in df.index:
                                rt.delete("1.0", "end")
                                rt.insert("end",df.loc[bid].to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"Booking_ID '{bid}' not found")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                        
                    bk = tk.Button(sframe, text="BOOKING_ID", padx=16,command=bk_id)
                    bk.grid(row=0)
                    
                    def gt_g():
                        book = tk.Toplevel()
                        book.title("GUEST NAME")
                        book.geometry("500x500")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)
                        
                        bok = tk.Label(bkf, text="Guest Name:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book)
                        rt.place(x=20, y=140, width=460, height=240)

                        def search_rt():
                            bid = ent.get()
                            match = df[df["guest_name"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end", row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for guest name '{bid}'")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    gn = tk.Button(sframe, text="GUEST NAME", padx=14, command=gt_g)
                    gn.grid(row=1)
                    
                    def gt_ci():
                        ci = tk.Toplevel()
                        ci.title("CHECK-IN DATE")
                        ci.geometry("500x500")
                        cif = tk.Frame(ci, bg="lightgray", bd=2, relief="groove")
                        cif.pack(padx=20, pady=20)
                        
                        ct = tk.Label(cif, text="Check-in Date:")
                        ct.grid(row=0, column=0)
                        ent = tk.Entry(cif)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(ci)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["check-in_date"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end",row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for check-IN date '{bid}'")
                        et = tk.Button(cif, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(ci, text="CLOSE", command=ci.destroy)
                        close.pack()
                    
                    ci = tk.Button(sframe, text="CHECK-IN DATE", padx=6, command=gt_ci)
                    ci.grid(row=2)
                    
                    def gt_co():
                        co = tk.Toplevel()
                        co.title("CHECK-OUT DATE")
                        co.geometry("500x500")
                        cof = tk.Frame(co, bg="lightgray", bd=2, relief="groove")
                        cof.pack(padx=20, pady=20)
                        
                        ct = tk.Label(cof, text="Check-out Date:")
                        ct.grid(row=0, column=0)
                        ent = tk.Entry(cof)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(co)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["check-out_date"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end",row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for check-out date '{bid}'")
                        et = tk.Button(cof, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(co, text="CLOSE", command=co.destroy)
                        close.pack()
                    
                    co = tk.Button(sframe, text="CHECK-OUT DATE", command=gt_co)
                    co.grid(row=3)
                    
                    def gt_no():
                        no = tk.Toplevel()
                        no.title("NO: OF GUESTS")
                        no.geometry("500x500")
                        nof = tk.Frame(no, bg="lightgray", bd=2, relief="groove")
                        nof.pack(padx=20, pady=20)
                        
                        ct = tk.Label(nof, text="No: of Guests:")
                        ct.grid(row=0, column=0)
                        ent = tk.Entry(nof)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(no)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            try:
                                bid = int(ent.get())
                                match = df[df["number_of_guests"] == bid]
                                rt.delete("1.0", "end")
                                if not match.empty:
                                    row = match.iloc[0]
                                    rt.insert("end", row.to_string())
                                else:
                                    rt.insert("end", f"No match for Total Bill Amount '{bid}'")
                            except:
                                rt.delete("1.0", "end")
                                rt.insert("end", "Please enter a valid number.")
                                
                        et = tk.Button(nof, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                
                        close = tk.Button(no, text="CLOSE",command=no.destroy)
                        close.pack()
                    
                    gn = tk.Button(sframe, text="NO: OF GUESTS", padx=8, command=gt_no)
                    gn.grid(row=4)
                    
                    def gt_cn():
                        cn = tk.Toplevel()
                        cn.title("CONTACT NUMBER")
                        cn.geometry("500x500")
                        cnf = tk.Frame(cn, bg="lightgray", bd=2, relief="groove")
                        cnf.pack(padx=20, pady=20)
                        
                        ct = tk.Label(cnf, text="Contact Number:")
                        ct.grid(row=0, column=0)
                        ent = tk.Entry(cnf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(cn)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            try:
                                bid = int(ent.get())
                                match = df[df["contact_number"] == bid]
                                rt.delete("1.0", "end")
                                if not match.empty:
                                    row = match.iloc[0]
                                    rt.insert("end", row.to_string())
                                else:
                                    rt.insert("end", f"No match for Contact Number '{bid}'")
                            except:
                                rt.delete("1.0", "end")
                                rt.insert("end", "Please enter a valid number.")
                            
                        et = tk.Button(cnf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
            
                        close = tk.Button(cn, text="CLOSE",command=cn.destroy)
                        close.pack()
                        
                    cn = tk.Button(sframe, text="CONTACT NO:", padx=10,command=gt_cn)
                    cn.grid(row=5)
                    
                    ba = tk.Button(sframe, text="BACK", padx=35,command=sgt.destroy)
                    ba.grid(row=6)
                    
                search = tk.Button(gtframe, text="SEARCH", padx=16,command=gt_s)
                search.grid(row=0)
                
                def gt_ds():
                    ds = tk.Toplevel()
                    ds.title("DISPLAY")
                    ds.geometry("800x500")
                    
                    lb = tk.Label(ds, text="ALL THE GUEST DETAILS")
                    lb.pack()
                    
                    close = tk.Button(ds, text="CLOSE", command=ds.destroy)
                    close.pack()
                    
                    tx = tk.Text(ds)
                    tx.place(x=20, y=50, width=760, height=380)
                    pd.set_option("display.max_columns", None)
                    tx.insert("1.0", df)
                
                display = tk.Button(gtframe, text="DISPLAY", padx=15, command=gt_ds)
                display.grid(row=1)
                
                def gt_mo():
                    mo = tk.Toplevel()
                    mo.title("GUEST MODIFY")
                    mo.geometry("500x400")
                    mof = tk.Frame(mo, bg="lightgray", bd=2, relief="groove")
                    mof.pack(padx=20, pady=20)

                    bok = tk.Label(mof, text="Booking_ID:")
                    bok.grid(row=0, column=0)
                    ent = tk.Entry(mof)
                    ent.grid(row=0, column=1)
                    
                    def mo_s():
                        bid = ent.get()
                        if bid in df.index:
                            mo.destroy()
                            m_m = tk.Toplevel()
                            m_m.title("MAIN MODIFY")
                            m_m.geometry("800x500")
                            mt = tk.Label(m_m, text="MODIFY PANEL")
                            mt.place(x=350, y=5)
                            
                            gtn = tk.Label(m_m, text="GUEST NAME    :")
                            gtn.place(x=40, y=80)
                            cid = tk.Label(m_m, text="CHECK-IN DATE :")
                            cid.place(x=40, y=120)
                            cod = tk.Label(m_m, text="CHECK-OUT DATE:")
                            cod.place(x=40, y=160)
                            nog = tk.Label(m_m, text="NO: OF GUEST  :")  
                            nog.place(x=40, y=200)
                            con = tk.Label(m_m, text="CONTACT NUMBER:")
                            con.place(x=40, y=240)
                            
                            gte = tk.Entry(m_m)
                            gte.place(x=200, y=80, width=160)
                            cie = tk.Entry(m_m)
                            cie.place(x=200, y=120, width=160)
                            coe = tk.Entry(m_m)
                            coe.place(x=200, y=160, width=160)
                            noe = tk.Entry(m_m)
                            noe.place(x=200,y=200, width=160)
                            cne = tk.Entry(m_m)
                            cne.place(x=200, y=240, width=160)
                            
                            tx = tk.Text(m_m)
                            tx.place(x=400, y=80, width=370, height=300)
                            
                            tx.insert("1.0","THE CURRENT DETAILS:\n")
                            tx.insert("end",df.loc[bid].to_string())

                            
                            def modify_data():
                                proceed = messagebox.askyesno("Confirmation", "Do you want to modify?")
                                if not proceed:
                                    messagebox.showinfo("Cancelled", "Modification cancelled!")
                                    return
                                changes = []
                                
                                if gte.get():
                                    df.at[bid, "guest_name"] = gte.get()
                                    changes.append(f"GUEST NAME   {gte.get()}")
                                
                                if cie.get():
                                    df.at[bid, "check-in_date"] = cie.get()
                                    changes.append(f"CHECK-IN DATE   {cie.get()}")
                                    
                                if coe.get():
                                    df.at[bid, "check-out_date"] = coe.get()
                                    changes.append(f"CHECK-OUT DATE   {coe.get()}")
                                    
                                if noe.get():
                                    df.at[bid, "number_of_guests"] = int(noe.get())
                                    changes.append(f"NO OF GUEST   {noe.get()}")
                                    
                                if cne.get():
                                    df.at[bid, "contact_number"] = int(cne.get())
                                    changes.append(f"CONTACT NUMBER   {cne.get()}")
                                    
                                df.to_csv("gtinfo.csv")
                                tx.delete("1.0", "end")
                                
                                if changes:
                                    tx.insert("1.0", "\nUPDATED FIELDS:\n".join(changes))
                                else:
                                    tx.insert("1.0", "No fields were changed.\n")
                                    
                                tx.insert("end", "\nCURRENT DETAILS:\n")
                                tx.insert("end",df.loc[bid].to_string())
                                messagebox.showinfo("Success", "Guest details checked.")
                            
                            md = tk.Button(m_m, text="MODIFY", command=modify_data)
                            md.place(x=120, y=300, width=100)
                            cl = tk.Button(m_m, text="CLOSE", command=m_m.destroy)
                            cl.place(x=240, y=300, width=100)
                            
                        elif bid not in df.index:
                            mod = tk.Label(mo, text="PLEASE CHECK BOOKING_ID!", fg="Red")
                            mod.pack()
                                                                        
                    enter = tk.Button(mof, text="ENTER", command=mo_s)
                    enter.grid(row=1, columnspan=2)
                    
                    close = tk.Button(mo, text="CLOSE", command=mo.destroy)
                    close.pack()
                
                modify = tk.Button(gtframe, text="MODIFY", padx=16, command=gt_mo)
                modify.grid(row=2)
                
                def gt_dl():
                    dl = tk.Toplevel()
                    dl.title("DELETE")
                    dl.geometry("500x400")
                    dlf = tk.Frame(dl, bg="lightgray", bd=2, relief="groove")
                    dlf.pack(padx=20, pady=20)

                    dle = tk.Label(dlf, text= "Booking_ID:")
                    dle.grid(row=0, column=0)
                    ent = tk.Entry(dlf)
                    ent.grid(row=0, column=1)
                    rt = tk.Text(dl)
                    rt.place(x=20, y=150, width=460, height=240)

                    def ch_rdl():
                        bid = ent.get()
                        if bid in df.index:
                            rt.delete("1.0", "end")
                            rt.insert("end",f"booking details of'{bid}':\n")
                            rt.insert("end",df.loc[bid].to_string())
                        else:
                            rt.delete("1.0", "end")
                            rt.insert("end", f"Booking_ID '{bid}' not found")
                            
                    et = tk.Button(dlf, text="ENTER", command=ch_rdl)
                    et.grid(row=1, columnspan=2)
                    
                    def conf_delete():
                        bid = ent.get()
                        if bid in df.index:
                            ans = messagebox.askyesno("Delete confrimation", f"Do you want to delete '{bid}'?")
                            rt.delete("1.0", "end")
                            
                            if ans==True:
                                df.drop(index = bid, inplace = True)
                                df.to_csv("gtinfo.csv")
                                rt.insert("1.0",f"Booking_ID '{bid}' has been deleted successfully.")
                                messagebox.showinfo("Deleted", f"Booking_ID '{bid}' was successfully deleted.")
                                
                            else:
                                rt. insert("1.0", f"Deletion cancelled for booking_ID '{bid}'")
                                
                        else:
                            rt.insert("1.0", f"Booking_ID '{bid}' not found.")
                    
                    fdel = tk.Button(dl, text="DELETE", command=conf_delete)
                    fdel.pack()
                    
                    close = tk.Button(dl, text="CLOSE", command=dl.destroy)
                    close.pack()
                                    
                delete = tk.Button(gtframe, text="DELETE", padx=18, command=gt_dl)
                delete.grid(row=3)
                
                def gt_add():
                    gtad = tk.Toplevel()
                    gtad.title("ADD PANEL")
                    gtad.geometry("800x500")
                    adp = tk.Label(gtad, text="ADD NEW GUEST DETAILS")
                    adp.place(x=350, y=5)
                        
                    bkd = tk.Label(gtad, text="BOOKING_ID    :")
                    bkd.place(x=40, y=80)
                    gtn = tk.Label(gtad, text="GUEST NAME    :")
                    gtn.place(x=40, y=120)
                    cid = tk.Label(gtad, text="CHECK-IN DATE :")
                    cid.place(x=40, y=160)
                    cod = tk.Label(gtad, text="CHECK-OUT DATE:")  
                    cod.place(x=40, y=200)
                    nog = tk.Label(gtad, text="NO: OF GUEST  :")
                    nog.place(x=40, y=240)
                    con = tk.Label(gtad, text="CONTACT NUMBER:")
                    con.place(x=40, y=280)
                        
                    bke = tk.Entry(gtad)
                    bke.place(x=200, y=80, width=160)
                    gte = tk.Entry(gtad)
                    gte.place(x=200, y=120, width=160)
                    cie = tk.Entry(gtad)
                    cie.place(x=200, y=160, width=160)
                    coe = tk.Entry(gtad)
                    coe.place(x=200,y=200, width=160)
                    noe = tk.Entry(gtad)
                    noe.place(x=200, y=240, width=160)
                    cne = tk.Entry(gtad)
                    cne.place(x=200, y=280, width=160)
                    
                    tx = tk.Text(gtad)
                    tx.place(x=400, y=80, width=370, height=300)
                    
                    def add_data():
                        bid = bke.get().strip()
                        tx.delete("1.0", "end")

                        if not (bid and gte.get() and cie.get() and coe.get() and noe.get() and cne.get()):
                            messagebox.showwarning("Incomplete Details", "All fields must be filled to add a new guest.")
                            tx.insert("1.0", "All fields are required.\n")
                            return

                        elif bid in df.index:
                            messagebox.showwarning("Duplicate Entry", f"Booking_ID '{bid}' already exists.")
                            tx.insert("1.0", f"Booking_ID '{bid}' already exists.\n")
                            return

                        confirm = messagebox.askyesno("Confirm Add", f"Add guest with Booking_ID '{bid}'?")
                        if confirm==True:
                            df.loc[bid] = {
                                "guest_name": gte.get(),
                                "check-in_date": cie.get(),
                                "check-out_date": coe.get(),
                                "number_of_guests": int(noe.get()),
                                "contact_number": int(cne.get())}

                            df.to_csv("gtinfo.csv")

                            tx.insert("1.0", f"NEW DETAILS OF'{bid}'\n")
                            tx.insert("2.0",df.loc[bid].to_string() + "\n")
                            tx.insert("end", "NEW GUEST ADDED SUCCESSFULLY:\n")
                            messagebox.showinfo("Success", f"Guest with Booking_ID '{bid}' was added.")
                        else:
                            messagebox.showinfo("Cancelled", "Guest not added.")
                            tx.insert("1.0", f"Guest booking cancelled for Booking_ID '{bid}'.\n")
                    
                    ad = tk.Button(gtad, text="ADD",command=add_data)
                    ad.place(x=120, y=340, width=100)
                    cl = tk.Button(gtad, text="CLOSE", command=gtad.destroy)
                    cl.place(x=240, y=340, width=100)
                
                add = tk.Button(gtframe, text="ADD", padx=26, command=gt_add)
                add.grid(row=4)
                back = tk.Button(gtframe, text="BACK", padx=23, command=gt.destroy)
                back.grid(row=5)

            
            gtinfo = tk.Button(adframe, text="GUEST DETAILS", padx=1,command=guest)
            gtinfo.grid(row=0)
            
            def roominfo():    # admin room
                rt = tk.Toplevel()
                rt.geometry("600x300")
                rt.title("ROOM DETAILS")
                
                df = pd.read_csv("room.csv", index_col="booking_id")
                
                wel = tk.Label(rt, text="ADMIN - ROOM DETAILS")
                wel.pack()
                rtframe = tk.Frame(rt, bg="Lightgray", bd=2, relief="groove")
                rtframe.pack(padx=50, pady=50)
                
                def rm_s():     # admin room search
                    sgt = tk.Toplevel()
                    sgt.geometry("500x500")
                    sgt.title("SEARCH BY")
                    
                    by = tk.Label(sgt, text="SEARCH BY:")
                    by.pack()
                    sframe = tk.Frame(sgt, bg="Lightgray", bd=2, relief="groove")
                    sframe.pack(padx=80, pady=60)
                    
                    def bk_id():
                        book = tk.Toplevel()
                        book.title("BOOKING_ID")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="Booking_ID:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book )
                        rt.place(x=20, y=140, width=460, height=240)

                        def search_rt():
                            bid = ent.get()
                            if bid in df.index:
                                rt.delete("1.0", "end")
                                rt.insert("end",df.loc[bid].to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"Booking_ID '{bid}' not found")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                        
                    bk = tk.Button(sframe, text="BOOKING_ID", padx=16,command=bk_id)
                    bk.grid(row=0)
                    
                    def rt_r():
                        book = tk.Toplevel()
                        book.title("ROOM NO:")
                        book.geometry("500x500")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)
                        
                        bok = tk.Label(bkf, text="ROOM_NO:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book)
                        rt.place(x=20, y=140, width=460, height=240)

                        def search_rt():
                            bid = ent.get()
                            match = df[df["room_no"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end", row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for room no '{bid}'")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    gn = tk.Button(sframe, text="ROOM NO", padx=22, command=rt_r)
                    gn.grid(row=1)
                    
                    def rt_t():
                        rtt = tk.Toplevel()
                        rtt.title("ROOM TYPE")
                        rtt.geometry("500x500")
                        rtf = tk.Frame(rtt, bg="lightgray", bd=2, relief="groove")
                        rtf.pack(padx=20, pady=20)
                        
                        rmt = tk.Label(rtf, text="ROOM TYPE:")
                        rmt.grid(row=0, column=0)
                        ent = tk.Entry(rtf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(rtt)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["room_type"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end",row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for room type '{bid}'")
                        et = tk.Button(rtf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(rtt, text="CLOSE", command=rtt.destroy)
                        close.pack()
                    
                    ci = tk.Button(sframe, text="ROOM_TYPE", padx=16, command=rt_t)
                    ci.grid(row=2)
                    
                    def rt_f():
                        fr = tk.Toplevel()
                        fr.title("FLOOR_NO:")
                        fr.geometry("500x500")
                        frf = tk.Frame(fr, bg="lightgray", bd=2, relief="groove")
                        frf.pack(padx=20, pady=20)
                        
                        ct = tk.Label(frf, text="FLOOR NO:")
                        ct.grid(row=0, column=0)
                        ent = tk.Entry(frf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(fr)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            try:
                                bid = int(ent.get())
                                match = df[df["floor_no"] == bid]
                                rt.delete("1.0", "end")
                                if not match.empty:
                                    row = match.iloc[0]
                                    rt.insert("end", row.to_string())
                                else:
                                    rt.insert("end", f"No match for Floor Number '{bid}'")
                            except:
                                rt.delete("1.0", "end")
                                rt.insert("end", "Please enter a valid number.")
                            
                        et = tk.Button(frf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
            
                        close = tk.Button(fr, text="CLOSE",command=fr.destroy)
                        close.pack()
                    
                    frn = tk.Button(sframe, text="FLOOR_NO:", padx=19, command=rt_f)
                    frn.grid(row=3)
                    
                    def rt_b():
                        bd = tk.Toplevel()
                        bd.title("NO: OF BEDS")
                        bd.geometry("500x500")
                        bdf = tk.Frame(bd, bg="lightgray", bd=2, relief="groove")
                        bdf.pack(padx=20, pady=20)
                        
                        ct = tk.Label(bdf, text="NO OF BEDS:")
                        ct.grid(row=0, column=0)
                        ent = tk.Entry(bdf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(bd)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            try:
                                bid = int(ent.get())
                                match = df[df["no_of_beds"] == bid]
                                rt.delete("1.0", "end")
                                if not match.empty:
                                    row = match.iloc[0]
                                    rt.insert("end", row.to_string())
                                else:
                                    rt.insert("end", f"No match for No: of Beds '{bid}'")
                            except:
                                rt.delete("1.0", "end")
                                rt.insert("end", "Please enter a valid number.")
                            
                        et = tk.Button(bdf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
            
                        close = tk.Button(bd, text="CLOSE",command=bd.destroy)
                        close.pack()
                    
                    gn = tk.Button(sframe, text="NO_OF_BEDS", padx=16, command=rt_b)
                    gn.grid(row=4)
                    
                    ba = tk.Button(sframe, text="BACK", padx=35,command=sgt.destroy)
                    ba.grid(row=6)
                                    
                search = tk.Button(rtframe, text="SEARCH", padx=16, command=rm_s)
                search.grid(row=0)
                
                def rm_ds():
                    ds = tk.Toplevel()
                    ds.title("DISPLAY")
                    ds.geometry("800x500")
                    
                    lb = tk.Label(ds, text="ALL THE ROOM DETAILS")
                    lb.pack()
                    
                    close = tk.Button(ds, text="CLOSE", command=ds.destroy)
                    close.pack()
                    
                    tx = tk.Text(ds)
                    tx.place(x=20, y=50, width=760, height=380)
                    pd.set_option("display.max_columns", None)
                    tx.insert("1.0", df)
                
                display = tk.Button(rtframe, text="DISPLAY", padx=15, command=rm_ds)
                display.grid(row=1)
                
                def rm_mo():            #ROOM - MODIFY
                    mo = tk.Toplevel()
                    mo.title("ROOM MODIFY")
                    mo.geometry("500x400")
                    mof = tk.Frame(mo, bg="lightgray", bd=2, relief="groove")
                    mof.pack(padx=20, pady=20)

                    bok = tk.Label(mof, text="Booking_ID:")
                    bok.grid(row=0, column=0)
                    ent = tk.Entry(mof)
                    ent.grid(row=0, column=1)
                    
                    def mo_s():
                        bid = ent.get()
                        if bid in df.index:
                            mo.destroy()
                            m_m = tk.Toplevel()
                            m_m.title("MAIN MODIFY")
                            m_m.geometry("800x500")
                            mt = tk.Label(m_m, text="MODIFY PANEL")
                            mt.place(x=350, y=5)
                            
                            gtn = tk.Label(m_m, text="ROOM_NO       :")
                            gtn.place(x=40, y=80)
                            cid = tk.Label(m_m, text="ROOM TYPE     :")
                            cid.place(x=40, y=120)
                            cod = tk.Label(m_m, text="FLOOR_NO      :")
                            cod.place(x=40, y=160)
                            nog = tk.Label(m_m, text="NO: OF BEDS   :")  
                            nog.place(x=40, y=200)
                            
                            gte = tk.Entry(m_m)
                            gte.place(x=200, y=80, width=160)
                            cie = tk.Entry(m_m)
                            cie.place(x=200, y=120, width=160)
                            coe = tk.Entry(m_m)
                            coe.place(x=200, y=160, width=160)
                            noe = tk.Entry(m_m)
                            noe.place(x=200,y=200, width=160)
                            
                            tx = tk.Text(m_m)
                            tx.place(x=400, y=80, width=370, height=300)
                            
                            tx.insert("1.0","THE CURRENT DETAILS:\n")
                            tx.insert("end",df.loc[bid].to_string())

                            
                            def modify_data():
                                proceed = messagebox.askyesno("Confirmation", "Do you want to modify?")
                                if not proceed:
                                    messagebox.showinfo("Cancelled", "Modification cancelled!")
                                    return
                                changes = []
                                
                                if gte.get():
                                    df.at[bid, "room_no"] = gte.get()
                                    changes.append(f"ROOM NO   {gte.get()}")
                                
                                if cie.get():
                                    df.at[bid, "room_type"] = cie.get()
                                    changes.append(f"ROOM TYPE   {cie.get()}")
                                    
                                if coe.get():
                                    df.at[bid, "floor_no"] = int(coe.get())
                                    changes.append(f"FLOOR NO   {coe.get()}")
                                    
                                if noe.get():
                                    df.at[bid, "no_of_beds"] = int(noe.get())
                                    changes.append(f"NO OF BEDS   {noe.get()}")
                                    
                                df.to_csv("room.csv")
                                tx.delete("1.0", "end")
                                
                                if changes:
                                    tx.insert("1.0", "\nUPDATED FIELDS:\n".join(changes))
                                else:
                                    tx.insert("1.0", "No fields were changed.\n")
                                    
                                tx.insert("end", "\nCURRENT DETAILS:\n")
                                tx.insert("end",df.loc[bid].to_string())
                                messagebox.showinfo("Success", "room details checked.")
                            
                            md = tk.Button(m_m, text="MODIFY", command=modify_data)
                            md.place(x=120, y=300, width=100)
                            cl = tk.Button(m_m, text="CLOSE", command=m_m.destroy)
                            cl.place(x=240, y=300, width=100)
                            
                        elif bid not in df.index:
                            mod = tk.Label(mo, text="PLEASE CHECK BOOKING_ID!", fg="Red")
                            mod.pack()
                                                                        
                    enter = tk.Button(mof, text="ENTER", command=mo_s)
                    enter.grid(row=1, columnspan=2)
                    
                    close = tk.Button(mo, text="CLOSE", command=mo.destroy)
                    close.pack()
                
                modify = tk.Button(rtframe, text="MODIFY", padx=16, command=rm_mo)
                modify.grid(row=2)
                
                def gm_dl():
                    dl = tk.Toplevel()
                    dl.title("DELETE")
                    dl.geometry("500x400")
                    dlf = tk.Frame(dl, bg="lightgray", bd=2, relief="groove")
                    dlf.pack(padx=20, pady=20)

                    dle = tk.Label(dlf, text= "Booking_ID:")
                    dle.grid(row=0, column=0)
                    ent = tk.Entry(dlf)
                    ent.grid(row=0, column=1)
                    rt = tk.Text(dl)
                    rt.place(x=20, y=150, width=460, height=240)

                    def ch_rdl():
                        bid = ent.get()
                        if bid in df.index:
                            rt.delete("1.0", "end")
                            rt.insert("end",f"booking details of'{bid}':\n")
                            rt.insert("end",df.loc[bid].to_string())
                        else:
                            rt.delete("1.0", "end")
                            rt.insert("end", f"Booking_ID '{bid}' not found")
                            
                    et = tk.Button(dlf, text="ENTER", command=ch_rdl)
                    et.grid(row=1, columnspan=2)
                    
                    def conf_delete():
                        bid = ent.get()
                        if bid in df.index:
                            ans = messagebox.askyesno("Delete confrimation", f"Do you want to delete '{bid}'?")
                            rt.delete("1.0", "end")
                            
                            if ans==True:
                                df.drop(index = bid, inplace = True)
                                df.to_csv("room.csv")
                                rt.insert("1.0",f"Booking_ID '{bid}' has been deleted successfully.")
                                messagebox.showinfo("Deleted", f"Booking_ID '{bid}' was successfully deleted.")
                                
                            else:
                                rt. insert("1.0", f"Deletion cancelled for booking_ID '{bid}'")
                                
                        else:
                            rt.insert("1.0", f"Booking_ID '{bid}' not found.")
                    
                    fdel = tk.Button(dl, text="DELETE", command=conf_delete)
                    fdel.pack()
                    
                    close = tk.Button(dl, text="CLOSE", command=dl.destroy)
                    close.pack()
                
                delete = tk.Button(rtframe, text="DELETE", padx=18, command=gm_dl)
                delete.grid(row=3)
                
                def rm_add():           # ROOM - ADD
                    rmad = tk.Toplevel()
                    rmad.title("ADD PANEL")
                    rmad.geometry("800x500")
                    adp = tk.Label(rmad, text="ADD NEW ROOM DETAILS")
                    adp.place(x=350, y=5)
                        
                    bkd = tk.Label(rmad, text="BOOKING_ID    :")
                    bkd.place(x=40, y=80)
                    gtn = tk.Label(rmad, text="ROOM_NO       :")
                    gtn.place(x=40, y=120)
                    cid = tk.Label(rmad, text="ROOM_TYPE     :")
                    cid.place(x=40, y=160)
                    cod = tk.Label(rmad, text="FLOOR_NO      :")  
                    cod.place(x=40, y=200)
                    nog = tk.Label(rmad, text="NO_OF_BEDS    :")
                    nog.place(x=40, y=240)
                        
                    bke = tk.Entry(rmad)
                    bke.place(x=200, y=80, width=160)
                    gte = tk.Entry(rmad)
                    gte.place(x=200, y=120, width=160)
                    cie = tk.Entry(rmad)
                    cie.place(x=200, y=160, width=160)
                    coe = tk.Entry(rmad)
                    coe.place(x=200,y=200, width=160)
                    noe = tk.Entry(rmad)
                    noe.place(x=200, y=240, width=160)
                    
                    tx = tk.Text(rmad)
                    tx.place(x=400, y=80, width=370, height=300)
                    
                    def add_data():
                        bid = bke.get().strip()
                        tx.delete("1.0", "end")

                        if not (bid and gte.get() and cie.get() and coe.get() and noe.get()):
                            messagebox.showwarning("Incomplete Details", "All fields must be filled to add a new guest.")
                            tx.insert("1.0", "All fields are required.\n")
                            return

                        elif bid in df.index:
                            messagebox.showwarning("Duplicate Entry", f"Booking_ID '{bid}' already exists.")
                            tx.insert("1.0", f"Booking_ID '{bid}' already exists.\n")
                            return

                        confirm = messagebox.askyesno("Confirm Add", f"Add Room with Booking_ID '{bid}'?")
                        if confirm==True:
                            df.loc[bid] = {
                                "room_no": gte.get(),
                                "room_type": cie.get(),
                                "floor_no": coe.get(),
                                "no_of_beds": int(noe.get())}

                            df.to_csv("room.csv")

                            tx.insert("1.0", f"NEW DETAILS OF'{bid}'\n")
                            tx.insert("2.0",df.loc[bid].to_string() + "\n")
                            tx.insert("end", "NEW ROOM ADDED SUCCESSFULLY\n")
                            messagebox.showinfo("Success", f"Room with Booking_ID '{bid}' was added.")
                        else:
                            messagebox.showinfo("Cancelled", "Room not added.")
                            tx.insert("1.0", f"Room booking cancelled for Booking_ID '{bid}'.\n")
                    
                    ad = tk.Button(rmad, text="ADD",command=add_data)
                    ad.place(x=120, y=340, width=100)
                    cl = tk.Button(rmad, text="CLOSE", command=rmad.destroy)
                    cl.place(x=240, y=340, width=100)
                
                add = tk.Button(rtframe, text="ADD", padx=26, command=rm_add)
                add.grid(row=4)
                back = tk.Button(rtframe, text="BACK", padx=23, command=rt.destroy)
                back.grid(row=5)
            
            room = tk.Button(adframe, text="ROOM DETAILS",padx=1, command=roominfo)
            room.grid(row=1)
            
            def billsinfo():    # admin bills
                bs = tk.Toplevel()
                bs.geometry("600x300")
                bs.title("BILLS DETAILS")
                
                df = pd.read_csv("bills.csv", index_col="booking_id")
                
                wel = tk.Label(bs, text="ADMIN - BILLS DETAILS")
                wel.pack()
                rtframe = tk.Frame(bs, bg="Lightgray", bd=2, relief="groove")
                rtframe.pack(padx=50, pady=50)
                Button_width = 15
                
                def bs_s():     # admin bills search
                    bss = tk.Toplevel()
                    bss.geometry("500x500")
                    bss.title("SEARCH BY")
                    
                    by = tk.Label(bss, text="SEARCH BY FOR BILLS:")
                    by.pack()
                    sframe = tk.Frame(bss, bg="Lightgray", bd=2, relief="groove")
                    sframe.pack(padx=80, pady=60)
                    Button_width = 20
                    
                    def bk_id():
                        book = tk.Toplevel()
                        book.title("BOOKING_ID")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="Booking_ID:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book)
                        rt.place(x=20, y=140, width=460, height=240)

                        def search_rt():
                            bid = ent.get()
                            if bid in df.index:
                                rt.delete("1.0", "end")
                                rt.insert("end",df.loc[bid].to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"Booking_ID '{bid}' not found")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    bkd = tk.Button(sframe, text="BOOKING_ID", width=Button_width, command=bk_id)
                    bkd.grid(row=0)
                    
                    def bs_a():
                        book = tk.Toplevel()
                        book.title("TOTAL BILL AMOUNT:")
                        book.geometry("500x500")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)
                        
                        bok = tk.Label(bkf, text="Total Bill Amount:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book)
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            try:
                                bid = int(ent.get())
                                match = df[df["total_bill_amount"] == bid]
                                rt.delete("1.0", "end")
                                if not match.empty:
                                    row = match.iloc[0]
                                    rt.insert("end", row.to_string())
                                else:
                                    rt.insert("end", f"No match for Total Bill Amount '{bid}'")
                            except:
                                rt.delete("1.0", "end")
                                rt.insert("end", "Please enter a valid number.")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    tba = tk.Button(sframe, text="TOTAL BILL AMOUNT", width=Button_width, command=bs_a)
                    tba.grid(row=1)
                    
                    def bs_p():
                        book = tk.Toplevel()
                        book.title("PAYMENT METHOD")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="Payment Method:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book )
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["payment_method"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end", row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for Payment Method '{bid}'")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    pym = tk.Button(sframe, text="PAYMENT METHOD", width=Button_width, command=bs_p)
                    pym.grid(row=2)
                    
                    def bs_e():
                        book = tk.Toplevel()
                        book.title("EXTRA SERVICE")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="Payment Method:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book )
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["extra_service"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end", row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for Extra Service '{bid}'")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    ets = tk.Button(sframe, text="EXTRA SERVICE", width=Button_width, command=bs_e)
                    ets.grid(row=3)
                    
                    def bs_d():
                        book = tk.Toplevel()
                        book.title("DISCOUNT CODE")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="DISCOUNT CODE:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book )
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["discount_code"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end", row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for Discount Code '{bid}'")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    dsc = tk.Button(sframe, text="DISCOUNT CODE", width=Button_width, command=bs_d)
                    dsc.grid(row=4)
                    
                    def bs_ps():
                        book = tk.Toplevel()
                        book.title("PAYMENT STATUS")
                        book.geometry("500x400")
                        bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                        bkf.pack(padx=20, pady=20)

                        bok = tk.Label(bkf, text="Payment STATUS:")
                        bok.grid(row=0, column=0)
                        ent = tk.Entry(bkf)
                        ent.grid(row=0, column=1)
                        rt = tk.Text(book )
                        rt.place(x=20, y=140, width=460, height=240)
                        
                        def search_rt():
                            bid = ent.get()
                            match = df[df["payment_status"] == bid]
                            if not match.empty:
                                row = match.iloc[0]
                                rt.delete("1.0", "end")
                                rt.insert("end", row.to_string())
                            else:
                                rt.delete("1.0", "end")
                                rt.insert("end", f"No match for Payment Status '{bid}'")
                                
                        et = tk.Button(bkf, text="ENTER", command=search_rt)
                        et.grid(row=1, columnspan=2)
                        
                        close = tk.Button(book, text="CLOSE",command=book.destroy)
                        close.pack()
                    
                    pys = tk.Button(sframe, text="PAYMENT STATUS", width=Button_width, command=bs_ps)
                    pys.grid(row=5)
                    bak = tk.Button(sframe, text="BACK", width=Button_width, command=bss.destroy)
                    bak.grid(row=6)
                                   
                ser = tk.Button(rtframe, text="SEARCH", width=Button_width, command=bs_s)
                ser.grid(row=0)
                
                def bs_ds():
                    ds = tk.Toplevel()
                    ds.title("DISPLAY")
                    ds.geometry("800x500")
                    
                    lb = tk.Label(ds, text="ALL THE ROOM DETAILS")
                    lb.pack()
                    
                    close = tk.Button(ds, text="CLOSE", command=ds.destroy)
                    close.pack()
                    
                    tx = tk.Text(ds)
                    tx.place(x=20, y=50, width=760, height=380)
                    pd.set_option("display.max_columns", None)
                    tx.insert("1.0", df)
                
                dis = tk.Button(rtframe, text="DISPLAY", width=Button_width, command=bs_ds)
                dis.grid(row=1)
                
                def bss_mo():            #BILLS - MODIFY
                    mo = tk.Toplevel()
                    mo.title("BILLS MODIFY")
                    mo.geometry("500x400")
                    mof = tk.Frame(mo, bg="lightgray", bd=2, relief="groove")
                    mof.pack(padx=20, pady=20)

                    bok = tk.Label(mof, text="Booking_ID:")
                    bok.grid(row=0, column=0)
                    ent = tk.Entry(mof)
                    ent.grid(row=0, column=1)
                    
                    def mo_s():
                        bid = ent.get()
                        if bid in df.index:
                            mo.destroy()
                            m_m = tk.Toplevel()
                            m_m.title("MAIN MODIFY")
                            m_m.geometry("800x500")
                            mt = tk.Label(m_m, text="MODIFY PANEL")
                            mt.place(x=350, y=5)
                            
                            gtn = tk.Label(m_m, text="TOTAL BILL AMOUNT:")
                            gtn.place(x=40, y=80)
                            cid = tk.Label(m_m, text="PAYMENT METHOD   :")
                            cid.place(x=40, y=120)
                            cod = tk.Label(m_m, text="EXTRA SERVICE    :")
                            cod.place(x=40, y=160)
                            nog = tk.Label(m_m, text="DISCOUNT CODE    :")  
                            nog.place(x=40, y=200)
                            con = tk.Label(m_m, text="PAYMENT STATUS   :")
                            con.place(x=40, y=240)
                            
                            gte = tk.Entry(m_m)
                            gte.place(x=200, y=80, width=160)
                            cie = tk.Entry(m_m)
                            cie.place(x=200, y=120, width=160)
                            coe = tk.Entry(m_m)
                            coe.place(x=200, y=160, width=160)
                            noe = tk.Entry(m_m)
                            noe.place(x=200,y=200, width=160)
                            cne = tk.Entry(m_m)
                            cne.place(x=200, y=240, width=160)
                            
                            tx = tk.Text(m_m)
                            tx.place(x=400, y=80, width=370, height=300)
                            
                            tx.insert("1.0","THE CURRENT DETAILS:\n")
                            tx.insert("end",df.loc[bid].to_string())

                            
                            def modify_data():
                                proceed = messagebox.askyesno("Confirmation", "Do you want to modify?")
                                if not proceed:
                                    messagebox.showinfo("Cancelled", "Modification cancelled!")
                                    return
                                changes = []
                                
                                if gte.get():
                                    df.at[bid, "total_bill_amount"] = int(gte.get())
                                    changes.append(f"TOTAL BILL AMOUNT   {gte.get()}")
                                
                                if cie.get():
                                    df.at[bid, "payment_method"] = cie.get()
                                    changes.append(f"PAYMENT METHOD   {cie.get()}")
                                    
                                if coe.get():
                                    df.at[bid, "extra_service"] = coe.get()
                                    changes.append(f"EXTRA SERVICE   {coe.get()}")
                                    
                                if noe.get():
                                    df.at[bid, "discount_code"] = noe.get()
                                    changes.append(f"DISCOUNT CODE   {noe.get()}")
                                    
                                if cne.get():
                                    df.at[bid, "payment_status"] = cne.get()
                                    changes.append(f"PAYMENT STATUS   {cne.get()}")
                                    
                                df.to_csv("bills.csv")
                                tx.delete("1.0", "end")
                                
                                if changes:
                                    tx.insert("1.0", "\nUPDATED FIELDS:\n".join(changes))
                                else:
                                    tx.insert("1.0", "No fields were changed.\n")
                                    
                                tx.insert("end", "\nCURRENT DETAILS:\n")
                                tx.insert("end",df.loc[bid].to_string())
                                messagebox.showinfo("Success", "Bill details checked.")
                            
                            md = tk.Button(m_m, text="MODIFY", command=modify_data)
                            md.place(x=120, y=300, width=100)
                            cl = tk.Button(m_m, text="CLOSE", command=m_m.destroy)
                            cl.place(x=240, y=300, width=100)
                            
                        elif bid not in df.index:
                            mod = tk.Label(mo, text="PLEASE CHECK BOOKING_ID!", fg="Red")
                            mod.pack()
                                                                        
                    enter = tk.Button(mof, text="ENTER", command=mo_s)
                    enter.grid(row=1, columnspan=2)
                    
                    close = tk.Button(mo, text="CLOSE", command=mo.destroy)
                    close.pack()
                
                mod = tk.Button(rtframe, text="MODIFY", width=Button_width, command=bss_mo)
                mod.grid(row=2)
                
                def bss_dl():
                    dl = tk.Toplevel()
                    dl.title("DELETE")
                    dl.geometry("500x400")
                    dlf = tk.Frame(dl, bg="lightgray", bd=2, relief="groove")
                    dlf.pack(padx=20, pady=20)

                    dle = tk.Label(dlf, text= "Booking_ID:")
                    dle.grid(row=0, column=0)
                    ent = tk.Entry(dlf)
                    ent.grid(row=0, column=1)
                    rt = tk.Text(dl)
                    rt.place(x=20, y=150, width=460, height=240)

                    def ch_rdl():
                        bid = ent.get()
                        if bid in df.index:
                            rt.delete("1.0", "end")
                            rt.insert("end",f"booking details of'{bid}':\n")
                            rt.insert("end",df.loc[bid].to_string())
                        else:
                            rt.delete("1.0", "end")
                            rt.insert("end", f"Booking_ID '{bid}' not found")
                            
                    et = tk.Button(dlf, text="ENTER", command=ch_rdl)
                    et.grid(row=1, columnspan=2)
                    
                    def conf_delete():
                        bid = ent.get()
                        if bid in df.index:
                            ans = messagebox.askyesno("Delete confrimation", f"Do you want to delete '{bid}'?")
                            rt.delete("1.0", "end")
                            
                            if ans==True:
                                df.drop(index = bid, inplace = True)
                                df.to_csv("bills.csv")
                                rt.insert("1.0",f"Booking_ID '{bid}' has been deleted successfully.")
                                messagebox.showinfo("Deleted", f"Booking_ID '{bid}' was successfully deleted.")
                                
                            else:
                                rt. insert("1.0", f"Deletion cancelled for booking_ID '{bid}'")
                                
                        else:
                            rt.insert("1.0", f"Booking_ID '{bid}' not found.")
                    
                    fdel = tk.Button(dl, text="DELETE", command=conf_delete)
                    fdel.pack()
                    
                    close = tk.Button(dl, text="CLOSE", command=dl.destroy)
                    close.pack()
                
                dlt = tk.Button(rtframe, text="DELETE", width=Button_width, command=bss_dl)
                dlt.grid(row=3)
                
                def bss_add():
                    gtad = tk.Toplevel()
                    gtad.title("ADD PANEL")
                    gtad.geometry("800x500")
                    adp = tk.Label(gtad, text="ADD NEW BILLS DETAILS")
                    adp.place(x=350, y=5)
                        
                    bkd = tk.Label(gtad, text="BOOKING_ID       :")
                    bkd.place(x=40, y=80)
                    gtn = tk.Label(gtad, text="TOTAL BILL AMOUNT:")
                    gtn.place(x=40, y=120)
                    cid = tk.Label(gtad, text="PAYMENT METHOD   :")
                    cid.place(x=40, y=160)
                    cod = tk.Label(gtad, text="EXTRA SERVICE    :")  
                    cod.place(x=40, y=200)
                    nog = tk.Label(gtad, text="DISCOUNT CODE    :")
                    nog.place(x=40, y=240)
                    con = tk.Label(gtad, text="PAYMENT STATUS   :")
                    con.place(x=40, y=280)
                        
                    bke = tk.Entry(gtad)
                    bke.place(x=200, y=80, width=160)
                    gte = tk.Entry(gtad)
                    gte.place(x=200, y=120, width=160)
                    cie = tk.Entry(gtad)
                    cie.place(x=200, y=160, width=160)
                    coe = tk.Entry(gtad)
                    coe.place(x=200,y=200, width=160)
                    noe = tk.Entry(gtad)
                    noe.place(x=200, y=240, width=160)
                    cne = tk.Entry(gtad)
                    cne.place(x=200, y=280, width=160)
                    
                    tx = tk.Text(gtad)
                    tx.place(x=400, y=80, width=370, height=300)
                    
                    def add_data():
                        bid = bke.get().strip()
                        tx.delete("1.0", "end")

                        if not (bid and gte.get() and cie.get() and coe.get() and noe.get() and cne.get()):
                            messagebox.showwarning("Incomplete Details", "All fields must be filled to add a new bill.")
                            tx.insert("1.0", "All fields are required.\n")
                            return

                        elif bid in df.index:
                            messagebox.showwarning("Duplicate Entry", f"Booking_ID '{bid}' already exists.")
                            tx.insert("1.0", f"Booking_ID '{bid}' already exists.\n")
                            return

                        confirm = messagebox.askyesno("Confirm Add", f"Add bill with Booking_ID '{bid}'?")
                        if confirm==True:
                            df.loc[bid] = {
                                "total_bill_amount": int(gte.get()),
                                "payment_method": cie.get(),
                                "extra_service": coe.get(),
                                "discount_code": noe.get(),
                                "payment_status": cne.get()}

                            df.to_csv("bills.csv")

                            tx.insert("1.0", f"NEW DETAILS OF'{bid}'\n")
                            tx.insert("2.0",df.loc[bid].to_string() + "\n")
                            tx.insert("end", "NEW BILL ADDED SUCCESSFULLY:\n")
                            messagebox.showinfo("Success", f"Guest with Booking_ID '{bid}' was added.")
                        else:
                            messagebox.showinfo("Cancelled", "Guest not added.")
                            tx.insert("1.0", f"Bill booking cancelled for Booking_ID '{bid}'.\n")
                    
                    ad = tk.Button(gtad, text="ADD",command=add_data)
                    ad.place(x=120, y=340, width=100)
                    cl = tk.Button(gtad, text="CLOSE", command=gtad.destroy)
                    cl.place(x=240, y=340, width=100)
                
                add = tk.Button(rtframe, text="ADD", width=Button_width, command=bss_add)
                add.grid(row=4)
                bak = tk.Button(rtframe, text="BACK", width=Button_width, command=bs.destroy)
                bak.grid(row=6)
                
            bills = tk.Button(adframe, text="BILLS DETAILS", padx=5, command=billsinfo)
            bills.grid(row=2)
            closead = tk.Button(adframe, text="CLOSE", padx=25, command=admin_panel.destroy)
            closead.grid(row=3)
            
        elif ent.get() == "Cactus" :
            ca = tk.Toplevel()
            ca.title("Western egg")
            ca.geometry("500x400")
            
            tx0 = tk.Label(ca, text="this page is for all the singles")
            tx1 = tk.Label(ca, text="here you will get discount 100%")
            tx0.pack()
            tx1.pack()
            
        else:
            messagebox.showerror("Access Denied", "Wrong password. Please try again.")

    log = tk.Button(frame, text="Login", command=login)
    log.grid(row=2, columnspan=2)
    close_ap = tk.Button(admin, text="CLOSE", command=admin.destroy)
    close_ap.pack()

def user_heart():
    us = tk.Toplevel()
    us.title("USER")
    us.geometry("400x300")
    
    wl = tk.Label(us, text="WELCOME TO N&S HOTEL")
    wl.pack()
    
    usf = tk.Frame(us, bg="lightgray", bd=2, relief="groove")
    usf.pack(padx=20, pady=20)
    Button_width = 20
    
    def gt_u():
        gtu = tk.Toplevel()
        gtu.title("GUEST DETAILS")
        gtu.geometry("400x400")
        
        df = pd.read_csv("gtinfo.csv", index_col="booking_id")
        
        l1 = tk.Label(gtu, text="GUEST DETAILS")
        l1.pack()
        
        gtf = tk.Frame(gtu, bg="lightgray", bd=2, relief="groove")
        gtf.pack(padx=20, pady=20)
        Button_width = 15
        def gt_s():
            ss = tk.Toplevel()
            ss.title("SEARCH BY:")
            ss.geometry("400x300")
            
            l1 = tk.Label(ss, text="SEARCH BY:")
            l1.pack()
            
            ssf = tk.Frame(ss, bg="lightgray", bd=2, relief="groove")
            ssf.pack()
            Button_width = 20
            
            def bk_id():
                book = tk.Toplevel()
                book.title("BOOKING_ID")
                book.geometry("500x500")
                bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                bkf.pack(padx=20, pady=20)

                bok = tk.Label(bkf, text="Booking_ID:")
                bok.grid(row=0, column=0)
                ent = tk.Entry(bkf)
                ent.grid(row=0, column=1)
                rt = tk.Text(book )
                rt.place(x=20, y=140, width=460, height=240)
                l1 = tk.Label(book, text="THANK YOU FOR VISITING")
                l1.place(x=160,y=400)

                def search_rt():
                    bid = ent.get()
                    if bid in df.index:
                        rt.delete("1.0", "end")
                        rt.insert("end",df.loc[bid].to_string())
                    else:
                        rt.delete("1.0", "end")
                        rt.insert("end", f"Booking_ID '{bid}' not found")
                        
                et = tk.Button(bkf, text="ENTER", command=search_rt)
                et.grid(row=1, columnspan=2)
                
                close = tk.Button(book, text="CLOSE",command=book.destroy)
                close.pack()
            
            bkd = tk.Button(ssf, text="BOOKING_ID", width=Button_width, command=bk_id)
            bkd.grid(row=0)
            
            def gt_g():
                book = tk.Toplevel()
                book.title("GUEST NAME")
                book.geometry("500x500")
                bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                bkf.pack(padx=20, pady=20)
                
                bok = tk.Label(bkf, text="Guest Name:")
                bok.grid(row=0, column=0)
                ent = tk.Entry(bkf)
                ent.grid(row=0, column=1)
                rt = tk.Text(book)
                rt.place(x=20, y=140, width=460, height=240)
                l1 = tk.Label(book, text="THANK YOU FOR VISITING")
                l1.place(x=160,y=400)

                def search_rt():
                    bid = ent.get()
                    match = df[df["guest_name"] == bid]
                    if not match.empty:
                        row = match.iloc[0]
                        rt.delete("1.0", "end")
                        rt.insert("end", row.to_string())
                    else:
                        rt.delete("1.0", "end")
                        rt.insert("end", f"No match for guest name '{bid}'")
                        
                et = tk.Button(bkf, text="ENTER", command=search_rt)
                et.grid(row=1, columnspan=2)
                
                close = tk.Button(book, text="CLOSE",command=book.destroy)
                close.pack()
            
            gtn = tk.Button(ssf, text="GUEST NAME", width=Button_width, command=gt_g)
            gtn.grid(row=1)
            
            def gt_cn():
                cn = tk.Toplevel()
                cn.title("CONTACT NUMBER")
                cn.geometry("500x500")
                cnf = tk.Frame(cn, bg="lightgray", bd=2, relief="groove")
                cnf.pack(padx=20, pady=20)
                
                ct = tk.Label(cnf, text="Contact Number:")
                ct.grid(row=0, column=0)
                ent = tk.Entry(cnf)
                ent.grid(row=0, column=1)
                rt = tk.Text(cn)
                rt.place(x=20, y=140, width=460, height=240)
                l1 = tk.Label(cn, text="THANK YOU FOR VISITING")
                l1.place(x=160,y=400)
                
                def search_rt():
                    try:
                        bid = int(ent.get())
                        match = df[df["contact_number"] == bid]
                        rt.delete("1.0", "end")
                        if not match.empty:
                            row = match.iloc[0]
                            rt.insert("end", row.to_string())
                        else:
                            rt.insert("end", f"No match for Contact Number '{bid}'")
                    except:
                        rt.delete("1.0", "end")
                        rt.insert("end", "Please enter a valid number.")
                    
                et = tk.Button(cnf, text="ENTER", command=search_rt)
                et.grid(row=1, columnspan=2)
    
                close = tk.Button(cn, text="CLOSE",command=cn.destroy)
                close.pack()
            
            ctn = tk.Button(ssf, text="CONTACT NUMBER", width=Button_width, command=gt_cn)
            ctn.grid(row=2)
            bak = tk.Button(ssf, text="BACK", width=Button_width, command=ss.destroy)
            bak.grid(row=3)
            
            l1 = tk.Label(ss, text="FOR ANY INCONVENIENCE")
            l1.pack()
            l2 = tk.Label(ss, text="PLEASE CONTACT TO")
            l2.pack()
            l3 = tk.Label(ss, text="HOTEL MANAGEMENT STAFF.")
            l3.pack()
            l4 = tk.Label(ss, text="THANK YOU FOR YOUR PATIENCE")
            l4.pack()
            l5 = tk.Label(ss, text="THANK YOU FOR VISITING")
            l5.pack()
                   
        gts = tk.Button(gtf, text="SEARCH", width=Button_width, command=gt_s)
        gts.grid(row=0)
        
        def gt_m():
            gtmm = tk.Toplevel()
            gtmm.geometry("300x200")
            gtmm.title("MODIFY CHECK:")

            frame = tk.Frame(gtmm, bg="lightgray", bd=2, relief="groove")
            frame.pack(padx=20, pady=20)

            bkd = tk.Label(frame, text="Booking_ID:")
            bkd.grid(row=1, column=0)

            ent=tk.Entry(frame)
            ent.grid(row=1, column=1)
            
            def ft_mv():
                bid = ent.get()
                if bid in df.index:
                    gtmm.destroy()
                    
                    m_m = tk.Toplevel()
                    m_m.title("MAIN MODIFY")
                    m_m.geometry("800x500")
                    mt = tk.Label(m_m, text="MODIFY PANEL")
                    mt.place(x=350, y=5)
                    
                    gtn = tk.Label(m_m, text="GUEST NAME    :")
                    gtn.place(x=40, y=80)
                    cid = tk.Label(m_m, text="CHECK-IN DATE :")
                    cid.place(x=40, y=120)
                    cod = tk.Label(m_m, text="CHECK-OUT DATE:")
                    cod.place(x=40, y=160)
                    nog = tk.Label(m_m, text="NO: OF GUEST  :")  
                    nog.place(x=40, y=200)
                    con = tk.Label(m_m, text="CONTACT NUMBER:")
                    con.place(x=40, y=240)
                    
                    gte = tk.Entry(m_m)
                    gte.place(x=200, y=80, width=160)
                    cie = tk.Entry(m_m)
                    cie.place(x=200, y=120, width=160)
                    coe = tk.Entry(m_m)
                    coe.place(x=200, y=160, width=160)
                    noe = tk.Entry(m_m)
                    noe.place(x=200,y=200, width=160)
                    cne = tk.Entry(m_m)
                    cne.place(x=200, y=240, width=160)
                    
                    tx = tk.Text(m_m)
                    tx.place(x=400, y=80, width=370, height=300)
                    
                    tx.insert("1.0","THE CURRENT DETAILS:\n")
                    tx.insert("end",df.loc[bid].to_string())

                    
                    def modify_data():
                        proceed = messagebox.askyesno("Confirmation", "Do you want to modify?")
                        if not proceed:
                            messagebox.showinfo("Cancelled", "Modification cancelled!")
                            return
                        changes = []
                        
                        if gte.get():
                            df.at[bid, "guest_name"] = gte.get()
                            changes.append(f"GUEST NAME   {gte.get()}")
                        
                        if cie.get():
                            df.at[bid, "check-in_date"] = cie.get()
                            changes.append(f"CHECK-IN DATE   {cie.get()}")
                            
                        if coe.get():
                            df.at[bid, "check-out_date"] = coe.get()
                            changes.append(f"CHECK-OUT DATE   {coe.get()}")
                            
                        if noe.get():
                            df.at[bid, "number_of_guests"] = int(noe.get())
                            changes.append(f"NO OF GUEST   {noe.get()}")
                            
                        if cne.get():
                            df.at[bid, "contact_number"] = int(cne.get())
                            changes.append(f"CONTACT NUMBER   {cne.get()}")
                            
                        df.to_csv("gtinfo.csv")
                        tx.delete("1.0", "end")
                        
                        if changes:
                            tx.insert("1.0", "\nUPDATED FIELDS:\n".join(changes))
                        else:
                            tx.insert("1.0", "No fields were changed.\n")
                            
                        tx.insert("end", "\nCURRENT DETAILS:\n")
                        tx.insert("end",df.loc[bid].to_string())
                        messagebox.showinfo("Success", "Guest details checked.")
                    
                    md = tk.Button(m_m, text="MODIFY", command=modify_data)
                    md.place(x=120, y=300, width=100)
                    cl = tk.Button(m_m, text="CLOSE", command=m_m.destroy)
                    cl.place(x=240, y=300, width=100)
                                      
                else:
                    l1 = tk.Label(gtmm, text="PLEASE CHECK BOKKING_ID!!!", fg = "red")
                    l1.pack()
                    
            log = tk.Button(frame, text="VERIFY", command=ft_mv)
            log.grid(row=2, columnspan=2)
            close = tk.Button(gtmm, text="CLOSE", command=gtmm.destroy)
            close.pack()
        
        gtm = tk.Button(gtf, text="MODIFY", width=Button_width, command=gt_m)
        gtm.grid(row=1)
        gtb = tk.Button(gtf, text="BACK", width=Button_width, command=gtu.destroy)
        gtb.grid(row=2)
        
        l1 = tk.Label(gtu, text="FOR ANY INCONVENIENCE")
        l1.pack()
        l2 = tk.Label(gtu, text="PLEASE CONTACT TO")
        l2.pack()
        l3 = tk.Label(gtu, text="HOTEL MANAGEMENT STAFF.")
        l3.pack()
        l4 = tk.Label(gtu, text="THANK YOU FOR YOUR PATIENCE")
        l4.pack()
        l5 = tk.Label(gtu, text="THANK YOU FOR VISITING")
        l5.pack()
      
    gt = tk.Button(usf, text="GUEST DETAILS", width=Button_width, command=gt_u)
    gt.grid(row=0)
    
    def rm_u():
        rmu = tk.Toplevel()
        rmu.title("ROOM DETAILS")
        rmu.geometry("400x400")
        
        df = pd.read_csv("room.csv", index_col="booking_id")
        
        l1 = tk.Label(rmu, text="ROOM DETAILS")
        l1.pack()
        
        rmf = tk.Frame(rmu, bg="lightgray", bd=2, relief="groove")
        rmf.pack(padx=20, pady=20)
        Button_width = 15
        
        def rm_s():
            ss = tk.Toplevel()
            ss.title("SEARCH BY:")
            ss.geometry("400x300")
            
            l1 = tk.Label(ss, text="SEARCH BY:")
            l1.pack()
            
            ssf = tk.Frame(ss, bg="lightgray", bd=2, relief="groove")
            ssf.pack()
            Button_width = 20
            
            def bk_id():
                book = tk.Toplevel()
                book.title("BOOKING_ID")
                book.geometry("500x500")
                bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                bkf.pack(padx=20, pady=20)

                bok = tk.Label(bkf, text="Booking_ID:")
                bok.grid(row=0, column=0)
                ent = tk.Entry(bkf)
                ent.grid(row=0, column=1)
                rt = tk.Text(book )
                rt.place(x=20, y=140, width=460, height=240)
                l1 = tk.Label(book, text="THANK YOU FOR VISITING")
                l1.place(x=160,y=400)

                def search_rt():
                    bid = ent.get()
                    if bid in df.index:
                        rt.delete("1.0", "end")
                        rt.insert("end",df.loc[bid].to_string())
                    else:
                        rt.delete("1.0", "end")
                        rt.insert("end", f"Booking_ID '{bid}' not found")
                        
                et = tk.Button(bkf, text="ENTER", command=search_rt)
                et.grid(row=1, columnspan=2)
                
                close = tk.Button(book, text="CLOSE",command=book.destroy)
                close.pack()
            
            bkd = tk.Button(ssf, text="BOOKING_ID", width=Button_width, command=bk_id)
            bkd.grid(row=0)
            
            def rt_r():
                book = tk.Toplevel()
                book.title("ROOM NO:")
                book.geometry("500x500")
                bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
                bkf.pack(padx=20, pady=20)
                
                bok = tk.Label(bkf, text="ROOM_NO:")
                bok.grid(row=0, column=0)
                ent = tk.Entry(bkf)
                ent.grid(row=0, column=1)
                rt = tk.Text(book)
                rt.place(x=20, y=140, width=460, height=240)
                l1 = tk.Label(book, text="THANK YOU FOR VISITING")
                l1.pack()

                def search_rt():
                    bid = ent.get()
                    match = df[df["room_no"] == bid]
                    if not match.empty:
                        row = match.iloc[0]
                        rt.delete("1.0", "end")
                        rt.insert("end", row.to_string())
                    else:
                        rt.delete("1.0", "end")
                        rt.insert("end", f"No match for room no '{bid}'")
                        
                et = tk.Button(bkf, text="ENTER", command=search_rt)
                et.grid(row=1, columnspan=2)
                
                close = tk.Button(book, text="CLOSE",command=book.destroy)
                close.pack()
            
            rmn = tk.Button(ssf, text="ROOM_NO", width=Button_width, command=rt_r)
            rmn.grid(row=1)
            bak = tk.Button(ssf, text="BACK", width=Button_width, command=ss.destroy)
            bak.grid(row=2)
            
            l1 = tk.Label(ss, text="THANK YOU FOR VISITING")
            l1.pack()
            
        rms = tk.Button(rmf, text="SEARCH", width=Button_width, command=rm_s)
        rms.grid(row=0)
        rmb = tk.Button(rmf, text="BACK", width=Button_width, command=rmu.destroy)
        rmb.grid(row=1)
        
        l1 = tk.Label(rmu, text="FOR AFTER CHECK-IN UPGRADE")
        l1.pack()
        l2 = tk.Label(rmu, text="PLEASE CONTACT TO")
        l2.pack()
        l3 = tk.Label(rmu, text="HOTEL MANAGEMENT STAFF.")
        l3.pack()
        l4 = tk.Label(rmu, text="THANK YOU FOR VISITING")
        l4.pack()
        
    rm = tk.Button(usf, text="ROOM DETAILS", width=Button_width, command=rm_u)
    rm.grid(row=1)
    
    def bl_u():
        blu = tk.Toplevel()
        blu.title("BILL DETAILS")
        blu.geometry("400x400")
        
        df = pd.read_csv("room.csv", index_col="booking_id")
        
        l1 = tk.Label(blu, text="BILL DETAILS")
        l1.pack()
        
        blf = tk.Frame(blu, bg="lightgray", bd=2, relief="groove")
        blf.pack(padx=20, pady=20)
        Button_width = 15
        
        def bk_id():
            book = tk.Toplevel()
            book.title("BOOKING_ID")
            book.geometry("500x500")
            bkf = tk.Frame(book, bg="lightgray", bd=2, relief="groove")
            bkf.pack(padx=20, pady=20)

            bok = tk.Label(bkf, text="Booking_ID:")
            bok.grid(row=0, column=0)
            ent = tk.Entry(bkf)
            ent.grid(row=0, column=1)
            rt = tk.Text(book )
            rt.place(x=20, y=140, width=460, height=240)
            l1 = tk.Label(book, text="THANK YOU FOR VISITING")
            l1.place(x=160,y=400)

            def search_rt():
                bid = ent.get()
                if bid in df.index:
                    rt.delete("1.0", "end")
                    rt.insert("end",df.loc[bid].to_string())
                else:
                    rt.delete("1.0", "end")
                    rt.insert("end", f"Booking_ID '{bid}' not found")
                    
            et = tk.Button(bkf, text="ENTER", command=search_rt)
            et.grid(row=1, columnspan=2)
            
            close = tk.Button(book, text="CLOSE",command=book.destroy)
            close.pack()
            
        ss = tk.Button(blf, text="SEARCH", width=Button_width, command = bk_id)
        ss.grid(row=0)
        bk = tk.Button(blf, text="BACK", width=Button_width, command = blu.destroy)
        bk.grid(row=1)
        
        l1 = tk.Label(blu, text="FOR ANY INCONVENIENCE")
        l1.pack()
        l2 = tk.Label(blu, text="PLEASE CONTACT TO")
        l2.pack()
        l3 = tk.Label(blu, text="HOTEL MANAGEMENT STAFF.")
        l3.pack()
        l4 = tk.Label(blu, text="THANK YOU FOR YOUR PATIENCE")
        l4.pack()
        l5 = tk.Label(blu, text="THANK YOU FOR VISITING")
        l5.pack()
        
    bs = tk.Button(usf, text="BILL DETAILS", width=Button_width, command=bl_u)
    bs.grid(row=2)
    
    def show_about():
        about_win = tk.Toplevel()
        about_win.title("About N&S HOTEL")
        about_win.geometry("640x620")
        about_win.configure(bg="white")

        about_story = """
        N&S HOTEL began as a shared vision between two friends — 
        one from the vibrant heart of North India, the other from the soulful coasts of the 
        South.

        Their idea was simple yet profound: to create a space where India's cultural 
        richness could be experienced in harmony. 
        'N' stands for North. 'S' stands for South. Together, 
        
        they represent a fusion of contrasts — the serenity of the North with the spices of 
        the South, the grandeur of Mughal architecture with the grace of Dravidian 
        design.

        N&S is more than a hotel — it's a sanctuary where cultures converge, 
        stories unfold, and every guest feels at home.

        With branches across India and around the world, 
        N&S HOTEL is known not just for its exquisite luxury and world-class service, 
        but for its spirit — a celebration of unity in diversity.

        At N&S, we don’t see people as customers — we welcome them as guests, 
        with warmth and dignity. 
        
        Our philosophy is rooted in timeless values, inspired by the Hadith:

        “Whoever believes in Allah and the Last Day should honor his guest.”

            Welcome to N&S — where heritage meets harmony."""

        font_style = ("Georgia", 11)
        about_text = tk.Text(about_win, wrap="word", bg="white", fg="black", font=font_style)
        about_text.insert("1.0", about_story)
        about_text.config(state="disabled")
        about_text.pack(padx=30, pady=30, fill="both", expand=True)

        bcf = tk.Frame(about_win, bg="lightgray", bd=2, relief="groove")
        bcf.pack(pady=10)

        cl = tk.Button(bcf, text="CLOSE", command=about_win.destroy)
        cl.pack()

    ns = tk.Button(usf, text="ABOUT N&S HOTEL", width=Button_width, command=show_about)
    ns.grid(row=3)
    bk = tk.Button(usf, text="BACK", width=Button_width, command=us.destroy)
    bk.grid(row=4)
    ts = tk.Label(us, text="THANK YOU FOR VISITING", font=("Arial", 10))
    ts.pack()
    
#main interface
hotel1 = tk.Label(main_heart, text="Welcome to N&S HOTEL")
hotel1.pack()
admin1 = tk.Button(main_heart, text="ADMIN", width=Button_width, command=adminpage)
admin1.pack()
user = tk.Button(main_heart, text="USER", width=Button_width, command=user_heart)
user.pack()
close_main = tk.Button(main_heart, text="CLOSE", width=Button_width, command=main_heart.destroy)
close_main.pack()
ts2 = tk.Label(main_heart, text="THANK YOU FOR VISITING")
ts2.pack()

main_heart.mainloop()
