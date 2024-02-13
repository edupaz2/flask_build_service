from flask import Flask, send_file
from project import actions, create_app
import os

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
