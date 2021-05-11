# Messager
Skillbox intensive Demo Messager for 3 days by Nikita Levashov 
The messager to be work in local and remove mode in terminal or qt widget
- Design of UI developed via https://www.qt.io/
- Public URL can be configured via https://ngrok.com
- Default endpoint set on the local machine http://127.0.0.1:5000
## Prerequisites:
- install python version = 3.9.2 on local machine
- install via Terminal run: pip Flask 
- install via Terminal run: pip PyQt6
- publish local/server.py on https://ngrok.com (if needed public URL)
## Local run via Terminal
- run: python local/server.py
- Change endpoint into source code http://127.0.0.1:5000 (if needed)
- run: python local/receiver.py
- run: python local/sender.py
## Remote run with public URL
- configure server_url in remote/messenger.py i.e "http://c6ff98effef0.ngrok.io"
- run: python local/messenger.py
Feature:
## Bot
- implement boot into local/server.py
## Hints: 
- see remote/hint.py for instruction how to generate messenger.ui by www.qt.io
## Improvements needed (TODO) 
- a global config with server_url
- bot with CHF rate