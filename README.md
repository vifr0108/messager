# messager
Skillbox Demo Messager for 3 days. 
The server.py messger can work as local mode via terminal of PyCharm or https://ngrok.com as remote public server
Design of UI developed via https://www.qt.io/

Prereqisites:
# install python version = 3.9.2
# install via Terminal: pip Flask 
# install via Terminal: pip PyQt6

# Local run via Terminal
- python local/server.py
- python local/receiver.py
- python local/sender.py

# Remote run with public URL
- publish local/server.py on https://ngrok.com
- configure server_url in remote/messenger.py i.e "http://c6ff98effef0.ngrok.io"
- python local/messenger.py


Feature:
# Bot
- implement boot into local/server.py i.e. local/server.py:68
