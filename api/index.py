from flask import Flask

app = Flask(__name__)
 
@app.route("/api/python")
def hello_world():
    # Open the pseudoindex.txt file for reading
    with open("pseudoindex.txt", "r") as file:
        # Read the contents of the file
        file_contents = file.read()

    # Return the contents of the file as the response
    return file_contents

if __name__ == "__main__":
    app.run()
