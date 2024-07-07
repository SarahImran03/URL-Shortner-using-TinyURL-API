import tkinter as tk
import pyshorteners as py

#GUI of the URL Shortner
GUI = tk.Tk()
GUI.title("URL Shortner")
GUI.geometry("350x170")
GUI.configure(background="light gray")

originalURL_heading = tk.Label(GUI, text="Original URL", height=2, width=10, font=("Times", 16), bg="light gray")
originalURL_heading.grid(row=0, column=0, sticky='w', padx=10)
originalURL = tk.Entry(GUI)
originalURL.grid(row=1, column=0, columnspan=3, sticky='we', padx=10)

shortenedURL_heading = tk.Label(GUI, text="Shortened URL", height=2, width=11, font=("Times", 16), bg="light gray")
shortenedURL_heading.grid(row=2, column=0, sticky='w', padx=10)
shortenedURL = tk.Entry(GUI)
shortenedURL.grid(row=3, column=0, columnspan=3, sticky='we', padx=10)

GUI.grid_columnconfigure(0, weight=1)
GUI.grid_columnconfigure(2, weight=1)

#Functionality of the URL Shortner
def shorten_url():
    shortener = py.Shortener()
    shortened_URL = shortener.tinyurl.short(originalURL.get())
    shortenedURL.insert(0, shortened_URL)

#Button
btn_process = tk.Button(GUI, text="Shorten", command=shorten_url, width=6, font=("Times"), bg="light blue")
btn_process.grid(row=0, column=2, sticky='e', padx=10)

GUI.mainloop()