from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Sistema de Controle de Visitas</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0;
                }
                .container {
                    background: white;
                    border-radius: 20px;
                    padding: 40px;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                    text-align: center;
                }
                h1 {
                    color: #667eea;
                    margin-bottom: 30px;
                }
                .buttons {
                    display: flex;
                    gap: 20px;
                    flex-wrap: wrap;
                    justify-content: center;
                }
                a {
                    display: inline-block;
                    padding: 15px 30px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-decoration: none;
                    border-radius: 10px;
                    font-weight: bold;
                    transition: transform 0.2s;
                }
                a:hover {
                    transform: translateY(-3px);
                }
                a.admin {
                    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🔐 Sistema de Controle de Taxas</h1>
                <div class="buttons">
                    <a href="/checkin">✅ Check-in</a>
                    <a href="/checkout">🚪 Check-out</a>
                </div>
            </div>
        </body>
    </html>
    """

# Página de Check-in
@app.route('/checkin')
def pagina_checkin():
    return render_template('checkin.html')

# Página de Check-out
@app.route('/checkout')
def pagina_checkout():
    return render_template('checkout.html')

# Página de Admin (CORRIGIDA)
@app.route('/admin')
def pagina_admin(): # <-- Função renomeada
    return render_template('admin.html')

@app.route('/confirmacao')
def pagina_confirmacao(): # <-- Função renomeada
    return render_template('confirmacao.html')
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5001)




