from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route("/")
def home():    
    info = None

    with open("info.json", "r") as read_file:
        info = json.load(read_file)
    
    about = info['about']
    interests = info['interests']
    education = info['education']
    certifications = info['certifications']
    experiences = info['experience']
    projects = info['projects']

    data=render_template("/index.html" ,
                            about = about,
                            interests = interests,
                            education = education,
                            certifications = certifications,
                            experiences = experiences,
                            projects = projects,
                            # context = context
                        )
    return data

if __name__ =='__main__':
    app.run(debug=True)
