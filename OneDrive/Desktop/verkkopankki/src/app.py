from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data
accounts = {
    "12345": {"pin": "1122", "balance": 2300},
}

# Reitti saldon tarkistamiseen
@app.route("/api/balance", methods=["POST"])
def check_balance():
    data = request.get_json()
    account = data.get("account")
    pin = data.get("pin")
    
    if account in accounts and accounts[account]["pin"] == pin:
        return jsonify({"balance": accounts[account]["balance"]}), 200
    return jsonify({"error": "Invalid account or PIN"}), 400

# Reitti rahan nostamiseen
@app.route("/api/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    account = data.get("account")
    pin = data.get("pin")
    amount = data.get("amount")
    
    if account in accounts and accounts[account]["pin"] == pin:
        if amount <= accounts[account]["balance"] and amount > 0:
            accounts[account]["balance"] -= amount
            return jsonify({"withdrawn": amount, "new_balance": accounts[account]["balance"]}), 200
        return jsonify({"error": "Insufficient balance or invalid amount"}), 400
    return jsonify({"error": "Invalid account or PIN"}), 400

# Reitti rahan tallettamiseen
@app.route("/api/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    account = data.get("account")
    pin = data.get("pin")
    amount = data.get("amount")
    
    if account in accounts and accounts[account]["pin"] == pin:
        if amount > 0:
            accounts[account]["balance"] += amount
            return jsonify({"deposited": amount, "new_balance": accounts[account]["balance"]}), 200
        return jsonify({"error": "Invalid deposit amount"}), 400
    return jsonify({"error": "Invalid account or PIN"}), 400

# Flask-palvelimen käynnistäminen
if __name__ == "__main__":
    app.run(debug=True)
