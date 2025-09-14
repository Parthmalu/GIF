from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExank3aGtxaGVpM2RwYXp3N29icG5kd3R4bnE5bnI1bmlwcHM3M3NpcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ZBQhoZC0nqknSviPqT/giphy.gif"  # Replace this URL with your desired GIF URL
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Sorry Message with GIF</title>
        <style>
          body {{
            background-color: #f0e6f7;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #4b2c83;
            text-align: center;
          }}
          h1 {{
            font-size: 3rem;
            margin-bottom: 20px;
          }}
          img {{
            width: 320px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
          }}
        </style>
    </head>
    <body>
        <h1>I'm sorry 😔🙏</h1>
        <img src="{gif_url}" alt="Sorry GIF" />
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run()

