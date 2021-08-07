from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Your bot is alive!"

if __name__ == '__main__':
    app.run(debug=True)
