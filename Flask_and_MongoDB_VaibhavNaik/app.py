from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


# -------------------------------
# Task 1: JSON API Route
# -------------------------------

@app.route("/api")
def api_data():
    try:
        # Open the backend JSON file
        with open("data.json", "r") as file:
            data = json.load(file)

        # Return the data as a JSON response
        return jsonify(data)

    except Exception as error:
        return jsonify({"error": str(error)}), 500


# -------------------------------
# MongoDB Atlas Connection
# -------------------------------

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

database = client["flask_assignment"]
collection = database["students"]


# -------------------------------
# Task 2: Frontend Form
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        try:
            # Get data submitted from the form
            name = request.form.get("name")
            email = request.form.get("email")
            course = request.form.get("course")

            # Basic validation
            if not name or not email or not course:
                return render_template(
                    "form.html",
                    error="Please fill in all the fields."
                )

            # Create document to store in MongoDB
            student_data = {
                "name": name,
                "email": email,
                "course": course
            }

            # Insert data into MongoDB Atlas
            collection.insert_one(student_data)

            # Redirect to success page
            return redirect(url_for("success"))

        except Exception as error:

            # Display error on the same page
            return render_template(
                "form.html",
                error=f"Error submitting data: {error}"
            )

    return render_template("form.html")


# -------------------------------
# Success Page
# -------------------------------

@app.route("/success")
def success():
    return render_template("success.html")


# -------------------------------
# Run Flask Application
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)