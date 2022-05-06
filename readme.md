## _Travel Site Flask Simple Web App_

I attached required dependencies to run the app locally on your machine
you can find it in the requirements.txt file.

To install dependencies run this command on your terminal:

`pip install -r requirements.txt`

Now you need to initialize the database using the predefined model:

Open python console or on your terminal run command:

`python`

Then run the following code:

`from app import db`

`db.create_all()`

Now flask app database is ready.

You need to set `FLASK_APP` environment variable to load the application:

Run CMD command:

`set FLASK_APP=app`

Or run Powershell command:

`$env:FLASK_APP = "app"`

You can run flask app on your local host by executing this command on your terminal:

`flask run`

It will run on  `http://127.0.0.1:5000`

This simple flask app is a travel planning site 

The main functionalities of this app:
* Register to the app with account.
* Login to the app.
* Authenticate only registered users to the profile page.
* View user travel destination sites.
* Add new travel destination site.
* Logout from user account.


**Made with ❤ by Mohamad Oghli**

Email:
`mhd.sh.oghli@gmail.com`