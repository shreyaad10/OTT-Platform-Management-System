import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
from datetime import date, timedelta
import os

# ─── CONFIG ───────────────────────────────────────────────────────────────────
BASE_PATH = "D:\\OTT Platform Management\\"

BG        = "#0d0d1a"
PANEL     = "#13132b"
ACCENT    = "#e040fb"
ACCENT2   = "#7c4dff"
TEXT      = "#e8e8ff"
SUBTEXT   = "#888aaa"
ENTRY_BG  = "#1e1e3a"
BTN_BG    = "#1e1e3a"
BTN_ACT   = "#2a2a50"
DANGER    = "#ff4f6d"
SUCCESS   = "#00e5a0"

FONT_HEAD  = ("Segoe UI", 22, "bold")
FONT_SUB   = ("Segoe UI", 12)
FONT_BTN   = ("Segoe UI", 11, "bold")
FONT_LABEL = ("Segoe UI", 10)
FONT_ENTRY = ("Consolas", 10)

plan_data = {
    'TYPE':        ['A',      'B',    'C'],
    'PLAN':        ['SILVER', 'GOLD', 'PLATINUM'],
    'PRICE':       [199,       699,    1669],
    'PLAN PERIOD': ['30 DAYS','180 DAYS','365 DAYS']
}
plan_df = pd.DataFrame(plan_data)

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def fp(filename):
    return os.path.join(BASE_PATH, filename)

def styled_btn(parent, text, command, color=ACCENT, width=22):
    btn = tk.Button(
        parent, text=text, command=command,
        bg=BTN_BG, fg=color, activebackground=BTN_ACT,
        activeforeground=color, relief="flat", bd=0,
        font=FONT_BTN, cursor="hand2", width=width,
        highlightthickness=1, highlightbackground=color
    )
    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_ACT))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG))
    return btn

def make_label(parent, text, fg=TEXT, font=FONT_LABEL):
    return tk.Label(parent, text=text, bg=PANEL, fg=fg, font=font)

def make_entry(parent, width=30):
    e = tk.Entry(parent, bg=ENTRY_BG, fg=TEXT, insertbackground=ACCENT,
                 relief="flat", font=FONT_ENTRY, width=width,
                 highlightthickness=1, highlightbackground=ACCENT2)
    return e

def show_table(parent, df):
    """Render a DataFrame in a scrollable Treeview inside parent frame."""
    for w in parent.winfo_children():
        w.destroy()
    cols = list(df.columns)
    tree = ttk.Treeview(parent, columns=cols, show="headings", height=18)
    vsb = ttk.Scrollbar(parent, orient="vertical",   command=tree.yview)
    hsb = ttk.Scrollbar(parent, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
        background=ENTRY_BG, foreground=TEXT,
        fieldbackground=ENTRY_BG, rowheight=26,
        font=FONT_LABEL)
    style.configure("Treeview.Heading",
        background=PANEL, foreground=ACCENT, font=("Segoe UI", 10, "bold"))
    style.map("Treeview", background=[("selected", ACCENT2)])

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=max(100, len(str(c))*10), anchor="center")

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)

def form_dialog(parent, title, fields):
    """Generic form popup. Returns dict of values or None if cancelled."""
    dlg = tk.Toplevel(parent)
    dlg.title(title)
    dlg.configure(bg=PANEL)
    dlg.grab_set()
    dlg.resizable(False, False)

    tk.Label(dlg, text=title, bg=PANEL, fg=ACCENT,
             font=("Segoe UI", 14, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(16,10), padx=20)

    entries = {}
    for i, (label, default) in enumerate(fields.items(), start=1):
        tk.Label(dlg, text=label, bg=PANEL, fg=TEXT,
                 font=FONT_LABEL).grid(row=i, column=0, sticky="w",
                                       padx=20, pady=4)
        e = make_entry(dlg, width=28)
        if default:
            e.insert(0, str(default))
        e.grid(row=i, column=1, padx=20, pady=4)
        entries[label] = e

    result = {}

    def on_ok():
        for k, e in entries.items():
            result[k] = e.get()
        dlg.destroy()

    def on_cancel():
        dlg.destroy()

    bf = tk.Frame(dlg, bg=PANEL)
    bf.grid(row=len(fields)+1, column=0, columnspan=2, pady=14)
    styled_btn(bf, "✔  Confirm", on_ok, color=SUCCESS, width=14).pack(side="left", padx=8)
    styled_btn(bf, "✖  Cancel", on_cancel, color=DANGER, width=14).pack(side="left", padx=8)

    parent.wait_window(dlg)
    return result if result else None

# ─── MAIN APP ─────────────────────────────────────────────────────────────────
class OTTApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YOLO — OTT Platform Management")
        self.geometry("1280x760")
        self.configure(bg=BG)
        self.resizable(True, True)
        self._build_ui()

    def _build_ui(self):
        # ── Sidebar ──
        sidebar = tk.Frame(self, bg=PANEL, width=210)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="🎬 YOLO", bg=PANEL, fg=ACCENT,
                 font=("Segoe UI", 18, "bold")).pack(pady=(28, 4))
        tk.Label(sidebar, text="OTT Management", bg=PANEL, fg=SUBTEXT,
                 font=("Segoe UI", 9)).pack(pady=(0, 24))

        ttk.Separator(sidebar, orient="horizontal").pack(fill="x", padx=16)

        nav_items = [
            ("🎥  Movies",       self.show_movies),
            ("📺  Series",       self.show_series),
            ("👥  Workforce",    self.show_workforce),
            ("🪪  Membership",   self.show_membership),
            ("💳  Transactions", self.show_transactions),
            ("📊  Analytics",    self.show_analytics),
            ("📈  Visualisation",self.show_visualisation),
        ]

        for label, cmd in nav_items:
            b = tk.Button(
                sidebar, text=label, command=cmd,
                bg=PANEL, fg=TEXT, activebackground=BTN_ACT,
                activeforeground=ACCENT, relief="flat", bd=0,
                font=("Segoe UI", 11), anchor="w", padx=18,
                cursor="hand2", width=22
            )
            b.pack(fill="x", pady=2)
            b.bind("<Enter>", lambda e, btn=b: btn.config(bg=BTN_ACT, fg=ACCENT))
            b.bind("<Leave>", lambda e, btn=b: btn.config(bg=PANEL,   fg=TEXT))

        ttk.Separator(sidebar, orient="horizontal").pack(fill="x", padx=16, pady=12)
        styled_btn(sidebar, "⏻  Exit", self.destroy, color=DANGER, width=20).pack(pady=4)

        # ── Main content ──
        self.content = tk.Frame(self, bg=BG)
        self.content.pack(side="left", fill="both", expand=True)

        self.show_home()

    def clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def page_header(self, title, subtitle=""):
        h = tk.Frame(self.content, bg=BG)
        h.pack(fill="x", padx=32, pady=(24, 8))
        tk.Label(h, text=title, bg=BG, fg=ACCENT, font=FONT_HEAD).pack(anchor="w")
        if subtitle:
            tk.Label(h, text=subtitle, bg=BG, fg=SUBTEXT, font=FONT_SUB).pack(anchor="w")
        ttk.Separator(self.content, orient="horizontal").pack(fill="x", padx=32, pady=(0,12))

    # ── Home ──────────────────────────────────────────────────────────────────
    def show_home(self):
        self.clear_content()
        self.page_header("Welcome to YOLO", "Your complete OTT platform management suite")
        cards = [
            ("🎥", "Movies",       "Manage your movie library",     self.show_movies),
            ("📺", "Series",       "Manage your series catalog",    self.show_series),
            ("👥", "Workforce",    "Manage employees & staff",      self.show_workforce),
            ("🪪", "Membership",   "View & update memberships",     self.show_membership),
            ("💳", "Transactions", "Apply / cancel memberships",    self.show_transactions),
            ("📊", "Analytics",    "Deep-dive data analytics",      self.show_analytics),
            ("📈", "Visualisation","Charts & graphs",               self.show_visualisation),
        ]
        grid = tk.Frame(self.content, bg=BG)
        grid.pack(padx=32, pady=8, fill="both", expand=True)
        for idx, (icon, title, desc, cmd) in enumerate(cards):
            card = tk.Frame(grid, bg=PANEL, bd=0, relief="flat",
                            highlightthickness=1, highlightbackground=ACCENT2,
                            cursor="hand2")
            card.grid(row=idx//4, column=idx%4, padx=10, pady=10,
                      ipadx=10, ipady=12, sticky="nsew")
            tk.Label(card, text=icon, bg=PANEL, font=("Segoe UI",26)).pack(pady=(10,2))
            tk.Label(card, text=title, bg=PANEL, fg=ACCENT,
                     font=("Segoe UI",12,"bold")).pack()
            tk.Label(card, text=desc, bg=PANEL, fg=SUBTEXT,
                     font=("Segoe UI",9), wraplength=140).pack(pady=(2,10))
            card.bind("<Button-1>", lambda e, c=cmd: c())
            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, c=cmd: c())
        for c in range(4):
            grid.columnconfigure(c, weight=1)

    # ── MOVIES ────────────────────────────────────────────────────────────────
    def show_movies(self):
        self.clear_content()
        self.page_header("🎥 Movies", "Browse, add, edit and delete movie records")

        btn_row = tk.Frame(self.content, bg=BG)
        btn_row.pack(padx=32, pady=(0,10), fill="x")
        styled_btn(btn_row, "⟳ Refresh",    lambda: self._load_table(table_frame, fp("MOVIES.csv")), color=ACCENT, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "+ Add Movie",   self._add_movie,    color=SUCCESS, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "✎ Update",      self._update_movie, color=ACCENT2, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "✖ Delete",      self._delete_movie, color=DANGER,  width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "🔍 Search",     self._search_movie, color=ACCENT,  width=14).pack(side="left", padx=4)

        table_frame = tk.Frame(self.content, bg=BG)
        table_frame.pack(padx=32, fill="both", expand=True)
        self._load_table(table_frame, fp("MOVIES.csv"))

    def _load_table(self, frame, csv_path):
        try:
            df = pd.read_csv(csv_path)
            show_table(frame, df)
        except FileNotFoundError:
            for w in frame.winfo_children(): w.destroy()
            tk.Label(frame, text=f"⚠  File not found:\n{csv_path}",
                     bg=BG, fg=DANGER, font=FONT_SUB).pack(pady=40)

    def _add_movie(self):
        fields = {"Title":"","Release Date":"","Language":"","Producer":"",
                  "Certificate":"","Country":"","Genre":"","Duration":"",
                  "Runtime":"","IMDB Rating":"","Gross":""}
        data = form_dialog(self, "Add New Movie", fields)
        if not data: return
        try:
            mov = pd.read_csv(fp("MOVIES.csv"))
            new_id = int(mov['ID'].max()) + 1
            row = [new_id] + list(data.values())
            mov.loc[len(mov)] = row
            mov.to_csv(fp("MOVIES.csv"), index=False)
            messagebox.showinfo("Success", "Movie added successfully!")
            self.show_movies()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _update_movie(self):
        mid = simpledialog.askinteger("Update Movie", "Enter Movie ID to update:", parent=self)
        if mid is None: return
        try:
            mov = pd.read_csv(fp("MOVIES.csv"), index_col='ID')
            if mid not in mov.index:
                messagebox.showerror("Not Found", f"ID {mid} not found!"); return
            cols = list(mov.columns)
            col = simpledialog.askstring("Column", f"Columns:\n{', '.join(cols)}\n\nEnter column name:", parent=self)
            if not col: return
            val = simpledialog.askstring("Value", f"New value for '{col}':", parent=self)
            if val is None: return
            mov.loc[mid, col] = val
            mov.to_csv(fp("MOVIES.csv"))
            messagebox.showinfo("Success", "Movie updated successfully!")
            self.show_movies()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _delete_movie(self):
        mid = simpledialog.askinteger("Delete Movie", "Enter Movie ID to delete:", parent=self)
        if mid is None: return
        try:
            mov = pd.read_csv(fp("MOVIES.csv"), index_col='ID')
            if mid not in mov.index:
                messagebox.showerror("Not Found", f"ID {mid} not found!"); return
            if not messagebox.askyesno("Confirm", f"Delete movie ID {mid}?"): return
            mov = mov.drop(mid, axis=0)
            mov.to_csv(fp("MOVIES.csv"))
            messagebox.showinfo("Success", "Movie deleted successfully!")
            self.show_movies()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _search_movie(self):
        title = simpledialog.askstring("Search Movie", "Enter movie title:", parent=self)
        if not title: return
        try:
            mov = pd.read_csv(fp("MOVIES.csv"), index_col='TITLE')
            if title not in mov.index:
                messagebox.showinfo("Not Found", "Movie not found!"); return
            result = mov.loc[title]
            dlg = tk.Toplevel(self)
            dlg.title(f"Movie: {title}")
            dlg.configure(bg=PANEL)
            dlg.grab_set()
            tk.Label(dlg, text=f"🎥 {title}", bg=PANEL, fg=ACCENT,
                     font=("Segoe UI",14,"bold")).pack(pady=12, padx=20)
            if isinstance(result, pd.Series):
                for k, v in result.items():
                    row = tk.Frame(dlg, bg=PANEL)
                    row.pack(fill="x", padx=20, pady=2)
                    tk.Label(row, text=f"{k}:", bg=PANEL, fg=SUBTEXT,
                             font=FONT_LABEL, width=18, anchor="w").pack(side="left")
                    tk.Label(row, text=str(v), bg=PANEL, fg=TEXT,
                             font=FONT_ENTRY).pack(side="left")
            styled_btn(dlg, "Close", dlg.destroy, color=ACCENT, width=12).pack(pady=12)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    # ── SERIES ────────────────────────────────────────────────────────────────
    def show_series(self):
        self.clear_content()
        self.page_header("📺 Series", "Browse, add, edit and delete series records")

        btn_row = tk.Frame(self.content, bg=BG)
        btn_row.pack(padx=32, pady=(0,10), fill="x")
        styled_btn(btn_row, "⟳ Refresh",    lambda: self._load_table(tf, fp("SERIES.csv")), color=ACCENT, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "+ Add Series",  self._add_series,    color=SUCCESS, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "✎ Update",      self._update_series, color=ACCENT2, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "✖ Delete",      self._delete_series, color=DANGER,  width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "🔍 Search",     self._search_series, color=ACCENT,  width=14).pack(side="left", padx=4)

        tf = tk.Frame(self.content, bg=BG)
        tf.pack(padx=32, fill="both", expand=True)
        self._load_table(tf, fp("SERIES.csv"))

    def _add_series(self):
        fields = {"Title":"","Ratings":"","Language":"","Release Date":"",
                  "Genre":"","Runtime":"","Episodes":"","Gross":"","Seasons":""}
        data = form_dialog(self, "Add New Series", fields)
        if not data: return
        try:
            ser = pd.read_csv(fp("SERIES.csv"))
            sno = int(ser['Sr.No'].max()) + 1
            ser.loc[len(ser)] = [sno] + list(data.values())
            ser.to_csv(fp("SERIES.csv"), index=False)
            messagebox.showinfo("Success", "Series added successfully!")
            self.show_series()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _update_series(self):
        sid = simpledialog.askinteger("Update Series", "Enter Series Sr.No to update:", parent=self)
        if sid is None: return
        try:
            ser = pd.read_csv(fp("SERIES.csv"), index_col='Sr.No')
            if sid not in ser.index:
                messagebox.showerror("Not Found", f"Sr.No {sid} not found!"); return
            col = simpledialog.askstring("Column", f"Columns:\n{', '.join(ser.columns)}\n\nEnter column:", parent=self)
            if not col: return
            val = simpledialog.askstring("Value", f"New value for '{col}':", parent=self)
            if val is None: return
            ser.loc[sid, col] = val
            ser.to_csv(fp("SERIES.csv"))
            messagebox.showinfo("Success", "Series updated!")
            self.show_series()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _delete_series(self):
        sid = simpledialog.askinteger("Delete Series", "Enter Sr.No to delete:", parent=self)
        if sid is None: return
        try:
            ser = pd.read_csv(fp("SERIES.csv"), index_col='Sr.No')
            if sid not in ser.index:
                messagebox.showerror("Not Found", f"Sr.No {sid} not found!"); return
            if not messagebox.askyesno("Confirm", f"Delete series Sr.No {sid}?"): return
            ser = ser.drop(sid, axis=0)
            ser.to_csv(fp("SERIES.csv"))
            messagebox.showinfo("Success", "Series deleted!")
            self.show_series()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _search_series(self):
        title = simpledialog.askstring("Search Series", "Enter series title:", parent=self)
        if not title: return
        try:
            ser = pd.read_csv(fp("SERIES.csv"), index_col='Title')
            if title not in ser.index:
                messagebox.showinfo("Not Found", "Series not found!"); return
            result = ser.loc[title]
            dlg = tk.Toplevel(self); dlg.title(title); dlg.configure(bg=PANEL); dlg.grab_set()
            tk.Label(dlg, text=f"📺 {title}", bg=PANEL, fg=ACCENT,
                     font=("Segoe UI",14,"bold")).pack(pady=12, padx=20)
            if isinstance(result, pd.Series):
                for k, v in result.items():
                    r = tk.Frame(dlg, bg=PANEL); r.pack(fill="x", padx=20, pady=2)
                    tk.Label(r, text=f"{k}:", bg=PANEL, fg=SUBTEXT, width=18, anchor="w", font=FONT_LABEL).pack(side="left")
                    tk.Label(r, text=str(v), bg=PANEL, fg=TEXT, font=FONT_ENTRY).pack(side="left")
            styled_btn(dlg, "Close", dlg.destroy, color=ACCENT, width=12).pack(pady=12)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    # ── WORKFORCE ─────────────────────────────────────────────────────────────
    def show_workforce(self):
        self.clear_content()
        self.page_header("👥 Workforce", "Manage employees and staff records")

        btn_row = tk.Frame(self.content, bg=BG)
        btn_row.pack(padx=32, pady=(0,10), fill="x")
        styled_btn(btn_row, "⟳ Refresh",    lambda: self._load_table(tf, fp("WORKFORCE.csv")), color=ACCENT, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "+ Add Employee",self._add_employee,    color=SUCCESS, width=16).pack(side="left", padx=4)
        styled_btn(btn_row, "✎ Update",      self._update_employee, color=ACCENT2, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "✖ Delete",      self._delete_employee, color=DANGER,  width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "🔍 Search",     self._search_employee, color=ACCENT,  width=14).pack(side="left", padx=4)

        tf = tk.Frame(self.content, bg=BG)
        tf.pack(padx=32, fill="both", expand=True)
        self._load_table(tf, fp("WORKFORCE.csv"))

    def _add_employee(self):
        fields = {"Name":"","Contact Number":"","Salary":"","Gender":"","Post":""}
        data = form_dialog(self, "Add New Employee", fields)
        if not data: return
        try:
            wf = pd.read_csv(fp("WORKFORCE.csv"))
            new_id = int(wf['S-ID'].max()) + 1
            wf.loc[len(wf)] = [new_id, data["Name"], data["Contact Number"],
                                float(data["Salary"]), data["Gender"], data["Post"]]
            wf.to_csv(fp("WORKFORCE.csv"), index=False)
            messagebox.showinfo("Success", "Employee added!")
            self.show_workforce()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _update_employee(self):
        eid = simpledialog.askinteger("Update Employee", "Enter Employee S-ID:", parent=self)
        if eid is None: return
        try:
            wf = pd.read_csv(fp("WORKFORCE.csv"), index_col='S-ID')
            if eid not in wf.index:
                messagebox.showerror("Not Found", f"S-ID {eid} not found!"); return
            col = simpledialog.askstring("Column", f"Columns:\n{', '.join(wf.columns)}\n\nEnter column:", parent=self)
            if not col: return
            val = simpledialog.askstring("Value", f"New value for '{col}':", parent=self)
            if val is None: return
            wf.loc[eid, col] = val
            wf.to_csv(fp("WORKFORCE.csv"))
            messagebox.showinfo("Success", "Employee updated!")
            self.show_workforce()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _delete_employee(self):
        eid = simpledialog.askinteger("Delete Employee", "Enter Employee S-ID:", parent=self)
        if eid is None: return
        try:
            wf = pd.read_csv(fp("WORKFORCE.csv"), index_col='S-ID')
            if eid not in wf.index:
                messagebox.showerror("Not Found", f"S-ID {eid} not found!"); return
            if not messagebox.askyesno("Confirm", f"Delete employee S-ID {eid}?"): return
            wf = wf.drop(eid, axis=0)
            wf.to_csv(fp("WORKFORCE.csv"))
            messagebox.showinfo("Success", "Employee deleted!")
            self.show_workforce()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _search_employee(self):
        name = simpledialog.askstring("Search Employee", "Enter employee name:", parent=self)
        if not name: return
        try:
            wf = pd.read_csv(fp("WORKFORCE.csv"), index_col='NAME')
            if name not in wf.index:
                messagebox.showinfo("Not Found", "Employee not found!"); return
            result = wf.loc[name]
            dlg = tk.Toplevel(self); dlg.title(name); dlg.configure(bg=PANEL); dlg.grab_set()
            tk.Label(dlg, text=f"👤 {name}", bg=PANEL, fg=ACCENT,
                     font=("Segoe UI",14,"bold")).pack(pady=12, padx=20)
            if isinstance(result, pd.Series):
                for k, v in result.items():
                    r = tk.Frame(dlg, bg=PANEL); r.pack(fill="x", padx=20, pady=2)
                    tk.Label(r, text=f"{k}:", bg=PANEL, fg=SUBTEXT, width=18, anchor="w", font=FONT_LABEL).pack(side="left")
                    tk.Label(r, text=str(v), bg=PANEL, fg=TEXT, font=FONT_ENTRY).pack(side="left")
            styled_btn(dlg, "Close", dlg.destroy, color=ACCENT, width=12).pack(pady=12)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    # ── MEMBERSHIP ────────────────────────────────────────────────────────────
    def show_membership(self):
        self.clear_content()
        self.page_header("🪪 Membership", "View and manage member records")

        btn_row = tk.Frame(self.content, bg=BG)
        btn_row.pack(padx=32, pady=(0,10), fill="x")
        styled_btn(btn_row, "⟳ Refresh", lambda: self._load_table(tf, fp("MEMBERSHIP.csv")), color=ACCENT, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "✎ Update",  self._update_member, color=ACCENT2, width=14).pack(side="left", padx=4)
        styled_btn(btn_row, "🔍 Search", self._search_member, color=ACCENT,  width=14).pack(side="left", padx=4)

        tf = tk.Frame(self.content, bg=BG)
        tf.pack(padx=32, fill="both", expand=True)
        self._load_table(tf, fp("MEMBERSHIP.csv"))

    def _update_member(self):
        mid = simpledialog.askinteger("Update Member", "Enter Member M-ID:", parent=self)
        if mid is None: return
        try:
            mb = pd.read_csv(fp("MEMBERSHIP.csv"), index_col='M-ID')
            if mid not in mb.index:
                messagebox.showerror("Not Found", f"M-ID {mid} not found!"); return
            col = simpledialog.askstring("Column", f"Columns:\n{', '.join(mb.columns)}\n\nEnter column:", parent=self)
            if not col: return
            val = simpledialog.askstring("Value", f"New value for '{col}':", parent=self)
            if val is None: return
            mb.loc[mid, col] = val
            mb.to_csv(fp("MEMBERSHIP.csv"))
            messagebox.showinfo("Success", "Member updated!")
            self.show_membership()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _search_member(self):
        name = simpledialog.askstring("Search Member", "Enter member name:", parent=self)
        if not name: return
        try:
            mb = pd.read_csv(fp("MEMBERSHIP.csv"), index_col='NAME')
            if name not in mb.index:
                messagebox.showinfo("Not Found", "Member not found!"); return
            result = mb.loc[name]
            dlg = tk.Toplevel(self); dlg.title(name); dlg.configure(bg=PANEL); dlg.grab_set()
            tk.Label(dlg, text=f"🪪 {name}", bg=PANEL, fg=ACCENT,
                     font=("Segoe UI",14,"bold")).pack(pady=12, padx=20)
            if isinstance(result, pd.Series):
                for k, v in result.items():
                    r = tk.Frame(dlg, bg=PANEL); r.pack(fill="x", padx=20, pady=2)
                    tk.Label(r, text=f"{k}:", bg=PANEL, fg=SUBTEXT, width=20, anchor="w", font=FONT_LABEL).pack(side="left")
                    tk.Label(r, text=str(v), bg=PANEL, fg=TEXT, font=FONT_ENTRY).pack(side="left")
            styled_btn(dlg, "Close", dlg.destroy, color=ACCENT, width=12).pack(pady=12)
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    # ── TRANSACTIONS ──────────────────────────────────────────────────────────
    def show_transactions(self):
        self.clear_content()
        self.page_header("💳 Transactions", "Apply for or cancel membership")

        btn_row = tk.Frame(self.content, bg=BG)
        btn_row.pack(padx=32, pady=(0,10), fill="x")
        styled_btn(btn_row, "⟳ Refresh Transactions", lambda: self._load_table(tf, fp("TRANSACTIONS.csv")), color=ACCENT, width=24).pack(side="left", padx=4)
        styled_btn(btn_row, "🆕 New Member",           self._new_member,    color=SUCCESS, width=16).pack(side="left", padx=4)
        styled_btn(btn_row, "🔄 Renew Membership",     self._renew_member,  color=ACCENT2, width=18).pack(side="left", padx=4)
        styled_btn(btn_row, "❌ Cancel Membership",    self._cancel_member, color=DANGER,  width=18).pack(side="left", padx=4)

        # Plan info strip
        plan_frame = tk.Frame(self.content, bg=PANEL, bd=0,
                              highlightthickness=1, highlightbackground=ACCENT2)
        plan_frame.pack(padx=32, pady=(0,10), fill="x")
        tk.Label(plan_frame, text="  📋 Available Plans:", bg=PANEL, fg=ACCENT,
                 font=("Segoe UI",10,"bold")).pack(side="left", padx=8, pady=6)
        for _, row in plan_df.iterrows():
            tk.Label(plan_frame,
                     text=f"  {row['TYPE']}: {row['PLAN']} — ₹{row['PRICE']} / {row['PLAN PERIOD']}  ",
                     bg=PANEL, fg=TEXT, font=FONT_LABEL).pack(side="left", padx=4)

        tf = tk.Frame(self.content, bg=BG)
        tf.pack(padx=32, fill="both", expand=True)
        self._load_table(tf, fp("TRANSACTIONS.csv"))

    def _new_member(self):
        fields = {"Name":"","Membership Type (A/B/C)":"","Payment Method (CARD/NET BANKING)":""}
        data = form_dialog(self, "New Member Registration", fields)
        if not data: return
        try:
            n  = data["Name"]
            mt = data["Membership Type (A/B/C)"].upper()
            pm = data["Payment Method (CARD/NET BANKING)"].upper()

            plans = {'A':(0,30),'B':(1,180),'C':(2,365)}
            if mt not in plans:
                messagebox.showerror("Error","Invalid plan type. Use A, B or C."); return

            idx, days = plans[mt]
            mp    = plan_df.at[idx,'PLAN']
            total = plan_df.at[idx,'PRICE']
            cd    = date.today()
            nd    = cd + timedelta(days=days)

            mb    = pd.read_csv(fp("MEMBERSHIP.csv"), index_col='M-ID')
            trans = pd.read_csv(fp("TRANSACTIONS.csv"))
            new_mid = int(trans['M-ID'].max()) + 1

            mb.loc[len(mb)+1] = [n, mt]
            mb.to_csv(fp("MEMBERSHIP.csv"))

            trans.loc[len(trans)] = [new_mid, cd, n, mt, mp, cd, nd, pm, total]
            trans.to_csv(fp("TRANSACTIONS.csv"), index=False)

            receipt = (f"{'─'*40}\n"
                       f"           YOLO RECEIPT\n"
                       f"{'─'*40}\n"
                       f"Name            : {n}\n"
                       f"Membership Type : {mt}\n"
                       f"Plan            : {mp}\n"
                       f"Start Date      : {cd}\n"
                       f"End Date        : {nd}\n"
                       f"Payment Method  : {pm}\n"
                       f"Total           : ₹{total}\n"
                       f"{'─'*40}\n"
                       f"{datetime.datetime.now().strftime('%d-%m-%Y  %H:%M:%S')}")
            self._show_receipt(receipt)
            self.show_transactions()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _renew_member(self):
        fields = {"Name":"","Payment Method (CARD/NET BANKING)":""}
        data = form_dialog(self, "Renew Membership", fields)
        if not data: return
        try:
            n  = data["Name"]
            pm = data["Payment Method (CARD/NET BANKING)"].upper()
            mb = pd.read_csv(fp("MEMBERSHIP.csv"), index_col='NAME')
            if n not in mb.index:
                messagebox.showerror("Not Found","Member not found!"); return
            mt = str(mb.loc[n].iloc[0]).strip()

            plans = {'A':(0,30),'B':(1,180),'C':(2,365)}
            if mt not in plans:
                messagebox.showerror("Error",f"Invalid plan '{mt}' in record."); return

            idx, days = plans[mt]
            mp    = plan_df.at[idx,'PLAN']
            total = plan_df.at[idx,'PRICE']
            cd    = date.today()
            nd    = cd + timedelta(days=days)

            trans = pd.read_csv(fp("TRANSACTIONS.csv"))
            new_mid = int(trans['M-ID'].max()) + 1
            trans.loc[len(trans)] = [new_mid, cd, n, mt, mp, cd, nd, pm, total]
            trans.to_csv(fp("TRANSACTIONS.csv"), index=False)

            receipt = (f"{'─'*40}\n"
                       f"        YOLO RENEWAL RECEIPT\n"
                       f"{'─'*40}\n"
                       f"Name            : {n}\n"
                       f"Membership Type : {mt}\n"
                       f"Plan            : {mp}\n"
                       f"Start Date      : {cd}\n"
                       f"End Date        : {nd}\n"
                       f"Payment Method  : {pm}\n"
                       f"Total           : ₹{total}\n"
                       f"{'─'*40}\n"
                       f"{datetime.datetime.now().strftime('%d-%m-%Y  %H:%M:%S')}")
            self._show_receipt(receipt)
            self.show_transactions()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _cancel_member(self):
        name = simpledialog.askstring("Cancel Membership", "Enter member name:", parent=self)
        if not name: return
        try:
            mb = pd.read_csv(fp("MEMBERSHIP.csv"), index_col='NAME')
            if name not in mb.index:
                messagebox.showinfo("Not Found","You are not a member yet."); return
            if not messagebox.askyesno("Confirm", f"Cancel membership for '{name}'?"): return
            mb = mb.drop(name, axis=0)
            mb.to_csv(fp("MEMBERSHIP.csv"))
            messagebox.showinfo("Done","Membership cancelled successfully.")
            self.show_transactions()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _show_receipt(self, text):
        dlg = tk.Toplevel(self); dlg.title("Receipt"); dlg.configure(bg=PANEL); dlg.grab_set()
        tk.Label(dlg, text="🧾 Payment Receipt", bg=PANEL, fg=ACCENT,
                 font=("Segoe UI",14,"bold")).pack(pady=(16,8), padx=24)
        t = tk.Text(dlg, bg=ENTRY_BG, fg=SUCCESS, font=("Consolas",11),
                    width=46, height=14, relief="flat", bd=0)
        t.insert("1.0", text); t.config(state="disabled")
        t.pack(padx=24, pady=4)
        styled_btn(dlg, "Close", dlg.destroy, color=ACCENT, width=12).pack(pady=12)

    # ── ANALYTICS ─────────────────────────────────────────────────────────────
    def show_analytics(self):
        self.clear_content()
        self.page_header("📊 Analytics", "Grouped statistics across movies, series & memberships")

        nb = ttk.Notebook(self.content)
        nb.pack(padx=32, pady=8, fill="both", expand=True)

        style = ttk.Style()
        style.configure("TNotebook", background=BG, borderwidth=0)
        style.configure("TNotebook.Tab", background=PANEL, foreground=TEXT,
                        padding=[12,6], font=FONT_LABEL)
        style.map("TNotebook.Tab", background=[("selected", ACCENT2)],
                  foreground=[("selected", TEXT)])

        self._analytics_movies(nb)
        self._analytics_series(nb)
        self._analytics_plans(nb)

    def _analytics_tab(self, nb, label):
        f = tk.Frame(nb, bg=BG)
        nb.add(f, text=label)
        return f

    def _run_analytics(self, frame, func):
        for w in frame.winfo_children(): w.destroy()
        try:
            result = func()
            if isinstance(result, pd.Series):
                df = result.reset_index()
                df.columns = [str(c) for c in df.columns]
                show_table(frame, df)
            elif isinstance(result, str):
                tk.Label(frame, text=result, bg=BG, fg=SUCCESS,
                         font=("Segoe UI",14,"bold")).pack(pady=40)
            else:
                tk.Label(frame, text=str(result), bg=BG, fg=TEXT, font=FONT_SUB).pack(pady=20)
        except Exception as ex:
            tk.Label(frame, text=f"⚠ {ex}", bg=BG, fg=DANGER, font=FONT_SUB).pack(pady=20)

    def _analytics_movies(self, nb):
        tab = self._analytics_tab(nb, "🎥 Movies")
        btn_row = tk.Frame(tab, bg=BG); btn_row.pack(fill="x", padx=16, pady=10)
        result_frame = tk.Frame(tab, bg=BG); result_frame.pack(fill="both", expand=True, padx=16)

        mov_ops = [
            ("Max Runtime / Country", lambda: pd.read_csv(fp("MOVIES.csv")).groupby('COUNTRY')['RUNTIME'].max()),
            ("Min Runtime / Country", lambda: pd.read_csv(fp("MOVIES.csv")).groupby('COUNTRY')['RUNTIME'].min()),
            ("Max Gross / Genre",     lambda: pd.read_csv(fp("MOVIES.csv")).groupby('GENRE')['GROSS'].max()),
            ("Min Gross / Genre",     lambda: pd.read_csv(fp("MOVIES.csv")).groupby('GENRE')['GROSS'].min()),
            ("Max Rating / Language", lambda: pd.read_csv(fp("MOVIES.csv")).groupby('LANGUAGE')['RATING'].max()),
            ("Min Rating / Language", lambda: pd.read_csv(fp("MOVIES.csv")).groupby('LANGUAGE')['RATING'].min()),
            ("Max Rating / Year",     lambda: self._mov_by_year('RATING','max')),
            ("Min Rating / Year",     lambda: self._mov_by_year('RATING','min')),
        ]
        for lbl, fn in mov_ops:
            styled_btn(btn_row, lbl, lambda f=fn: self._run_analytics(result_frame, f),
                       color=ACCENT, width=20).pack(side="left", padx=3)

    def _mov_by_year(self, col, agg):
        mov = pd.read_csv(fp("MOVIES.csv"))
        mov['RELEASE DATE'] = pd.to_datetime(mov['RELEASE DATE'], dayfirst=True)
        mov['YEAR'] = mov['RELEASE DATE'].dt.year
        return mov.groupby('YEAR')[col].agg(agg)

    def _analytics_series(self, nb):
        tab = self._analytics_tab(nb, "📺 Series")
        btn_row = tk.Frame(tab, bg=BG); btn_row.pack(fill="x", padx=16, pady=10)
        result_frame = tk.Frame(tab, bg=BG); result_frame.pack(fill="both", expand=True, padx=16)

        ser_ops = [
            ("Max Runtime / Year",   lambda: self._ser_by_year('Runtime','max')),
            ("Min Runtime / Year",   lambda: self._ser_by_year('Runtime','min')),
            ("Max Gross / Genre",    lambda: pd.read_csv(fp("SERIES.csv")).groupby('Genre')['Gross'].max()),
            ("Min Gross / Genre",    lambda: pd.read_csv(fp("SERIES.csv")).groupby('Genre')['Gross'].min()),
            ("Max Ratings / Year",   lambda: self._ser_by_year('Ratings','max')),
            ("Min Ratings / Year",   lambda: self._ser_by_year('Ratings','min')),
            ("Max Seasons / Genre",  lambda: pd.read_csv(fp("SERIES.csv")).groupby('Genre')['Seasons'].max()),
            ("Min Seasons / Genre",  lambda: pd.read_csv(fp("SERIES.csv")).groupby('Genre')['Seasons'].min()),
        ]
        for lbl, fn in ser_ops:
            styled_btn(btn_row, lbl, lambda f=fn: self._run_analytics(result_frame, f),
                       color=ACCENT2, width=20).pack(side="left", padx=3)

    def _ser_by_year(self, col, agg):
        ser = pd.read_csv(fp("SERIES.csv"))
        ser['Release Date'] = pd.to_datetime(ser['Release Date'], dayfirst=True)
        ser['Year'] = ser['Release Date'].dt.year
        return ser.groupby('Year')[col].agg(agg)

    def _analytics_plans(self, nb):
        tab = self._analytics_tab(nb, "🪪 Plans")
        frame = tk.Frame(tab, bg=BG); frame.pack(fill="both", expand=True, padx=32, pady=20)

        def most_popular():
            mb = pd.read_csv(fp("MEMBERSHIP.csv"))
            a  = mb['MEMBERSHIP PLAN'].value_counts()
            return f"🏆 Most Popular Plan: {a.index[0]}"

        def least_popular():
            mb = pd.read_csv(fp("MEMBERSHIP.csv"))
            a  = mb['MEMBERSHIP PLAN'].value_counts()
            return f"📉 Least Popular Plan: {a.index[-1]}"

        res = tk.Frame(frame, bg=BG); res.pack(fill="both", expand=True)
        btn_row = tk.Frame(frame, bg=BG); btn_row.pack(pady=10)
        styled_btn(btn_row, "Most Popular Plan",  lambda: self._run_analytics(res, most_popular),  color=SUCCESS, width=20).pack(side="left", padx=10)
        styled_btn(btn_row, "Least Popular Plan", lambda: self._run_analytics(res, least_popular), color=DANGER,  width=20).pack(side="left", padx=10)

    # ── VISUALISATION ─────────────────────────────────────────────────────────
    def show_visualisation(self):
        self.clear_content()
        self.page_header("📈 Visualisation", "Charts and graphs for your data")

        nb = ttk.Notebook(self.content)
        nb.pack(padx=32, pady=8, fill="both", expand=True)

        self._visuals_movies(nb)
        self._visuals_series(nb)
        self._visuals_plans(nb)

    def _chart_tab(self, nb, label):
        f = tk.Frame(nb, bg=BG)
        nb.add(f, text=label)
        return f

    def _show_chart(self, parent, fig):
        for w in parent.winfo_children(): w.destroy()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def _chart_frame(self, tab):
        btn_row    = tk.Frame(tab, bg=BG); btn_row.pack(fill="x", padx=16, pady=8)
        chart_area = tk.Frame(tab, bg=BG); chart_area.pack(fill="both", expand=True, padx=16)
        return btn_row, chart_area

    def _visuals_movies(self, nb):
        tab = self._chart_tab(nb, "🎥 Movies")
        btn_row, ca = self._chart_frame(tab)

        def chart_rat_year():
            mov = pd.read_csv(fp("MOVIES.csv"))
            mov['RELEASE DATE'] = pd.to_datetime(mov['RELEASE DATE'], dayfirst=True)
            a = mov.groupby(mov['RELEASE DATE'].dt.year)['RATING'].mean()
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.plot(a.index, a.values, color=ACCENT, marker='o', linewidth=2)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Avg Ratings by Year", color=TEXT)
            ax.set_xlabel("Year", color=SUBTEXT); ax.set_ylabel("Rating", color=SUBTEXT)
            ax.tick_params(colors=TEXT); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_gross_genre():
            mov = pd.read_csv(fp("MOVIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(mov['GENRE'], mov['GROSS'], color=ACCENT2, width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Gross vs Genre", color=TEXT)
            ax.set_xlabel("Genre", color=SUBTEXT); ax.set_ylabel("Gross", color=SUBTEXT)
            ax.tick_params(colors=TEXT, axis='x', rotation=30); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_rat_lang():
            mov = pd.read_csv(fp("MOVIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(mov['LANGUAGE'], mov['RATING'], color=SUCCESS, width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Ratings vs Language", color=TEXT)
            ax.set_xlabel("Language", color=SUBTEXT); ax.set_ylabel("Rating", color=SUBTEXT)
            ax.tick_params(colors=TEXT, axis='x', rotation=30); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_gross_cert():
            mov = pd.read_csv(fp("MOVIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(mov['CERTIFICATE'], mov['GROSS'], color="#f9a825", width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Gross vs Certificate", color=TEXT)
            ax.set_xlabel("Certificate", color=SUBTEXT); ax.set_ylabel("Gross", color=SUBTEXT)
            ax.tick_params(colors=TEXT); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_dur():
            mov = pd.read_csv(fp("MOVIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.hist(mov['DURATION'], bins=10, color=ACCENT, edgecolor=PANEL)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Movie Duration Distribution", color=TEXT)
            ax.set_xlabel("Duration", color=SUBTEXT); ax.set_ylabel("Count", color=SUBTEXT)
            ax.tick_params(colors=TEXT); fig.tight_layout()
            self._show_chart(ca, fig)

        ops = [("Ratings / Year", chart_rat_year), ("Gross / Genre", chart_gross_genre),
               ("Ratings / Language", chart_rat_lang), ("Gross / Certificate", chart_gross_cert),
               ("Duration Histogram", chart_dur)]
        for lbl, fn in ops:
            styled_btn(btn_row, lbl, fn, color=ACCENT, width=18).pack(side="left", padx=3)

    def _visuals_series(self, nb):
        tab = self._chart_tab(nb, "📺 Series")
        btn_row, ca = self._chart_frame(tab)

        def chart_genre_gross():
            ser = pd.read_csv(fp("SERIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(ser['Genre'], ser['Gross'], color="olive", width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Gross vs Genre", color=TEXT)
            ax.set_xlabel("Genre", color=SUBTEXT); ax.set_ylabel("Gross", color=SUBTEXT)
            ax.tick_params(colors=TEXT, axis='x', rotation=30); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_lang_gross():
            ser = pd.read_csv(fp("SERIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(ser['Language'], ser['Gross'], color="purple", width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Language vs Gross", color=TEXT)
            ax.set_xlabel("Language", color=SUBTEXT); ax.set_ylabel("Gross", color=SUBTEXT)
            ax.tick_params(colors=TEXT, axis='x', rotation=30); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_lang_runtime():
            ser = pd.read_csv(fp("SERIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(ser['Language'], ser['Runtime'], color="pink", width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Language vs Runtime", color=TEXT)
            ax.set_xlabel("Language", color=SUBTEXT); ax.set_ylabel("Runtime", color=SUBTEXT)
            ax.tick_params(colors=TEXT, axis='x', rotation=30); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_rat_genre():
            ser = pd.read_csv(fp("SERIES.csv"))
            fig, ax = pl.subplots(figsize=(8,4), facecolor=PANEL)
            ax.bar(ser['Genre'], ser['Ratings'], color="#ff7043", width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Ratings vs Genre", color=TEXT)
            ax.set_xlabel("Genre", color=SUBTEXT); ax.set_ylabel("Ratings", color=SUBTEXT)
            ax.tick_params(colors=TEXT, axis='x', rotation=30); fig.tight_layout()
            self._show_chart(ca, fig)

        ops = [("Genre / Gross", chart_genre_gross), ("Language / Gross", chart_lang_gross),
               ("Language / Runtime", chart_lang_runtime), ("Ratings / Genre", chart_rat_genre)]
        for lbl, fn in ops:
            styled_btn(btn_row, lbl, fn, color=ACCENT2, width=18).pack(side="left", padx=3)

    def _visuals_plans(self, nb):
        tab = self._chart_tab(nb, "🪪 Plans & Members")
        btn_row, ca = self._chart_frame(tab)

        def chart_plan_freq():
            mb  = pd.read_csv(fp("MEMBERSHIP.csv"))
            sil = len(mb[mb['MEMBERSHIP PLAN']=='A'])
            gol = len(mb[mb['MEMBERSHIP PLAN']=='B'])
            pla = len(mb[mb['MEMBERSHIP PLAN']=='C'])
            fig, ax = pl.subplots(figsize=(6,4), facecolor=PANEL)
            ax.bar(['SILVER','GOLD','PLATINUM'], [sil,gol,pla],
                   color=['#e0e0e0','#ffd700','#b0bec5'], width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Plan Frequency", color=TEXT)
            ax.set_xlabel("Plan", color=SUBTEXT); ax.set_ylabel("Count", color=SUBTEXT)
            ax.tick_params(colors=TEXT); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_revenue():
            mb  = pd.read_csv(fp("MEMBERSHIP.csv"))
            sil = len(mb[mb['MEMBERSHIP PLAN']=='A']) * 199
            gol = len(mb[mb['MEMBERSHIP PLAN']=='B']) * 699
            pla = len(mb[mb['MEMBERSHIP PLAN']=='C']) * 1669
            fig, ax = pl.subplots(figsize=(6,4), facecolor=PANEL)
            ax.bar(['SILVER','GOLD','PLATINUM'], [sil,gol,pla],
                   color=['#ce93d8','#7c4dff','#e040fb'], width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Revenue per Plan", color=TEXT)
            ax.set_xlabel("Plan", color=SUBTEXT); ax.set_ylabel("Revenue (₹)", color=SUBTEXT)
            ax.tick_params(colors=TEXT); fig.tight_layout()
            self._show_chart(ca, fig)

        def chart_payment():
            trans = pd.read_csv(fp("TRANSACTIONS.csv"))
            card  = len(trans[trans['METHOD OF PAYMENT']=='CARD'])
            net   = len(trans[trans['METHOD OF PAYMENT']=='NET BANKING'])
            fig, ax = pl.subplots(figsize=(5,4), facecolor=PANEL)
            ax.bar(['CARD','NET BANKING'], [card,net], color=['olive','#00e5a0'], width=0.4)
            ax.set_facecolor(ENTRY_BG); ax.set_title("Payment Method Frequency", color=TEXT)
            ax.set_xlabel("Method", color=SUBTEXT); ax.set_ylabel("Count", color=SUBTEXT)
            ax.tick_params(colors=TEXT); fig.tight_layout()
            self._show_chart(ca, fig)

        ops = [("Plan Frequency", chart_plan_freq), ("Revenue per Plan", chart_revenue),
               ("Payment Methods", chart_payment)]
        for lbl, fn in ops:
            styled_btn(btn_row, lbl, fn, color=SUCCESS, width=18).pack(side="left", padx=3)


# ─── RUN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = OTTApp()
    app.mainloop()
