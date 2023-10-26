from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

# Set the template folder explicitly
app.template_folder = 'templates'

# # Configure MongoDB
# client = MongoClient('mongodb://localhost:27017')  # Update with your MongoDB URI
# # db = client['FullStackProject']  # Replace with your database name
# student = client.db.FullStackProject

# Configure the MongoDB connection
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/'
# mongo = MongoClient(app.config['MONGO_URI'])
# db =  db.mongo["FullStackProject"]


client = MongoClient('mongodb://localhost:27017/')
db = client['FullStackProject']  # Replace 'your_db_name' with your actual database name
student = db['Student'] 



from app import routes