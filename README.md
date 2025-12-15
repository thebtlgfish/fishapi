# Fish API

Fish API Is A Simple Fast And Reliable Web API To Get Simple Data For Your Projects. Written In Python With Flask, Fish API Is Your Go To API 

# Available Endpoints

Currently There Are Not Many EndPoints, Here Is A list Of Them:
-  /time - Get The Current Time
- /quote - Get A Random Quote
- /girlname - Get A Random Girl Name
- /boyname - Get A Random Boy Name

# How To Self Host The API

```bash
git clone https://github.com/thebtlgfish/fishapi
cd fishapi
```

Choose The Port You Want To Run The API On (default set to port 8080)

Install Flask (skip this step if flask is already installed on your machine)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run The API
```bash
python3 main.py
```
