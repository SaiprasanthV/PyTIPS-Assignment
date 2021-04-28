import threading
import tkinter
import socket
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 9090


class Client:

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # sends the connect signal
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        # message box to get the name of client
        self.nickname = simpledialog.askstring(
            "Nickname", "Please choose a nickname", parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.config(bg='lightgray')

        # title for Chat GUI
        self.chat_label = tkinter.Label(self.win, text='chat:', bg='lightgray')
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        # chat history with scrolling feature
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.config(font=("Arial", 12))
        self.text_area.pack(padx=20, pady=5)

        # displays the word -> 'Message'
        self.msg_label = tkinter.Label(
            self.win, text='Message', bg='lightgray')
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        # input text area
        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        # send button
        self.send_button = tkinter.Button(
            self.win, text='Send', command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        # stops the client if the window gets closed
        self.win.protocol("WN_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):
        # sends the message to the server and clears the input area
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        # close the client socket if the window got closed
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                # receives the message as -> 'NICK'
                message = self.sock.recv(1024).decode('utf-8')

                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        # setting the state to 'normal' to insert the new message
                        self.text_area.config(state='normal')
                        # adds the message at the end
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        # sets the state as 'disable' to prevent someone from adding text
                        self.text_area.config(state='disabled')

            except ConnectionAbortedError:
                break

            except:
                print("ERROR")
                self.sock.close()
                break


client = Client(HOST, PORT)
