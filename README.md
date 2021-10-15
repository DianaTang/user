A web server written in python.

- Install Python 3.8
- `python -m venv venv`
- `source venv/bin/activate` on Unix
- `pip install -r requirements.txt`
- `cd webserver
- Open `localhost:5000` to browse and generate logs

---

-Install python 3.8
Install the applications in the requirements.txt

checkout this code.  
cd webserver 
command line > python3 app.py

use terminal or any tool to do following request: 

Request:

curl -XPOST -H 'Content-Type: application/json' http://localhost:5000/user -d '{
  "first_name": "Human",
  "last_name": "Being",
  "client_name": "Company Inc."
}'
Response:

HTTP 200
{
  "id": 1,
  "first_name": "Human",
  "last_name": "Being",
  "client_name": "Company Inc."
}
Fetch user by ID
Request:

curl -XGET http://localhost:5000/user/1
Response:

HTTP 200
{
  "id": 1,
  "first_name": "Human",
  "last_name": "Being",
  "client_name": "Company Inc."
}
Delete user by ID
Request:

curl -XDELETE http://localhost:5000/user/1
Response:

HTTP 200
{}
