import tkinter as tk
from tkinter import messagebox
from threading import Thread
root = tk.Tk()
root.title("Numeral Base Converter")

def decBin(dec):
  if dec == 0:
    fBin = "00000000"
  else:
    bin = []
    while dec >= 1:
      bin.append(str(dec % 2))
      dec = int(dec / 2)
    while len(bin) % 8 != 0:
      bin.append("0")
    bin.reverse()
    fBin = "".join(bin)
  return(fBin)

def binDec(bin):
  fBin = list(bin)
  fBin.reverse()
  i = 0
  dec = 0
  while i < len(bin):
    dec = dec + (int(fBin[i]) * (2**i))
    i += 1
  return(dec)

def decHex(dec):
  hexDict = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F"
  }
  hex = []
  i = 0
  while i < 1:
    if (dec % 16) >= 10:
      hex.append(hexDict[str(dec % 16)])
    else:
      hex.append(str(dec % 16))
    dec = int(dec / 16)
    if dec / 16 == int(dec / 16) == 0:
      i += 1
  hex.reverse()
  fHex = "".join(hex)
  return(fHex)

def hexDec(hex):
  hexDict = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F"
  }
  fHex = list(hex)
  j = 0
  while j < len(fHex):
    k = 10
    while k < 16:
      if fHex[j] == hexDict[str(k)]:
        fHex[j] = str(k)
      k += 1
    j += 1
  try:
    hexCheck = "".join(fHex)
    hexAlpha = int(hexCheck)
    hexAlpha += 1
  except(ValueError):
    tk.messagebox.showinfo("Hexadecimal", "Please only enter hex digits into the hex field.")
    return(False, 0)
  fHex.reverse()
  i = 0
  dec = 0
  while i < len(hex):
    dec = dec + (int(fHex[i]) * (16**i))
    i += 1
  return(True, dec)

def binHex(convert):
  convert = binDec(convert)
  hex = decHex(convert)
  return(hex)

def hexBin(convert):
  hc = hexDec(convert)
  convert = hc[1]
  bin = decBin(convert)
  return(bin)

def decimal(self):
  try:
    c1 = int(de.get())
    bin = decBin(c1)
    hex = decHex(c1)
    bet.set(bin)
    het.set(hex)
  except(ValueError):
    tk.messagebox.showinfo("Decimal", "Please only enter decimal digits into the decimal field.")

def binary(self):
  c2 = be.get()
  i = 0
  while i < len(c2):
    if c2[i] != "0" and c2[i] != "1":
      tk.messagebox.showinfo("Binary", "Please only enter binary digits into the binary field.")
      bitCheck = False
      break
    else:
      bitCheck = True
    i += 1
  if bitCheck == True:
    dec = binDec(c2)
    hex = binHex(c2)
    det.set(dec)
    het.set(hex)

def hex(self):
  c3 = he.get().upper()
  hd = hexDec(c3)
  hexCheck = hd[0]
  if hexCheck == True:
    dec = hd[1]
    bin = hexBin(c3)
    det.set(dec)
    bet.set(bin)

def dcopy(self):
  copy = de.get()
  root.clipboard_clear()
  root.clipboard_append(copy)
  root.update()

def bcopy(self):
  copy = be.get()
  root.clipboard_clear()
  root.clipboard_append(copy)
  root.update()

def hcopy(self):
  copy = he.get()
  root.clipboard_clear()
  root.clipboard_append(copy)
  root.update()

inst = tk.Label(
  text = "Type in value and press enter to convert.\nDouble-click one of the boxes to copy the contents."
)
inst.pack()

d = tk.Label(
  text = "Decimal: "
)
b = tk.Label(
  text = "Binary: "
)
h = tk.Label(
  text = "Hexadecimal: "
)

det = tk.StringVar()
bet = tk.StringVar()
het = tk.StringVar()
de = tk.Entry(width = 1000, textvariable = det)
be = tk.Entry(width = 1000, textvariable = bet)
he = tk.Entry(width = 1000, textvariable = het)

q = tk.Button(
  text = "Quit",
  width = 20,
  activeforeground = "white",
  command = root.destroy
)

d.pack()
de.insert(0, "0")
de.bind("<Return>", decimal)
de.bind("<Double-Button-1>", dcopy)
de.pack()

b.pack()
be.insert(0, "00000000")
be.bind("<Return>", binary)
be.bind("<Double-Button-1>", bcopy)
be.pack()

h.pack()
he.insert(0, "0")
he.bind("<Return>", hex)
he.bind("<Double-Button-1>", hcopy)
he.pack()

q.pack()
root.mainloop()