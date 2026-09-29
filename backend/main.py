from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Music Analytic App is running"}

@app.get("/about")
def about():
    return {
        "name": "Music Analytic App",
        "description": "An app to analyze personal music data"
    }