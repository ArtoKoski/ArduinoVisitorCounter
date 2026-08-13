from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {
    "entered": 0,
    "exited": 0,
    "current": 0
}

@app.route('/data', methods=['POST'])
def data():

    global data_store

    data_store = request.json

    print("NEW DATA:")
    print(data_store)

    return "OK"


@app.route('/get')
def get_data():

    return jsonify(data_store)


def home():

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>People Counter</title>

        <style>

            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                background: #1e293b;
                padding: 40px;
                border-radius: 20px;
                width: 350px;
                text-align: center;
                box-shadow: 0 0 25px rgba(0,0,0,0.4);
            }

            h1 {
                margin-bottom: 30px;
                font-size: 32px;
            }

            .card {
                background: #334155;
                margin: 15px 0;
                padding: 20px;
                border-radius: 15px;
            }

            .number {
                font-size: 42px;
                font-weight: bold;
                margin-top: 10px;
            }

            .in {
                border-left: 6px solid #22c55e;
            }

            .out {
                border-left: 6px solid #ef4444;
            }

            .now {
                border-left: 6px solid #3b82f6;
            }

        </style>
    </head>

    <body>

        <div class="container">

            <h1>People Counter</h1>

            <div class="card in">
                IN
                <div class="number" id="entered">0</div>
            </div>

            <div class="card out">
                OUT
                <div class="number" id="exited">0</div>
            </div>

            <div class="card now">
                NOW
                <div class="number" id="current">0</div>
            </div>

        </div>

        <script>

            async function updateData() {

                const response = await fetch('http://10.6.128.97:5000/get');
                const data = await response.json();

                document.getElementById('entered').innerText = data.entered;
                document.getElementById('exited').innerText = data.exited;
                document.getElementById('current').innerText = data.current;
            }

            updateData();

            setInterval(updateData, 1000);

        </script>

    </body>
    </html>
    """

@app.route('/Foxtrot')
def foxtrot_page():
    return home()


app.run(host="0.0.0.0", port=5000)