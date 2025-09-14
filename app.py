from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    gif_url = "https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif"  # Replace with your GIF URL
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>GIF Display</title>
        <style>
          body {{
            background-color: #f0e6f7;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
          }}
          img {{
            width: 320px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
          }}
        </style>
    </head>
    <body>
        <img src="{gif_url}" alt="GIF" />
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run()
