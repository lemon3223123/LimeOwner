from flask import Flask, request, jsonify
import time
import threading

app = Flask(__name__)

# Global variable to store the status
current_status = "Idle"

@app.route('/trigger', methods=['POST'])
def trigger_action():
    global current_status
    action = request.json.get('action')
    
    if action == "Injected":
        current_status = "Injected"
        print("Action: Injected")
        
        # After 1 second, revert to "Idle"
        threading.Timer(1.0, reset_to_idle).start()
        return jsonify({"status": "success", "message": "Injected!"}), 200
    elif action == "Unloaded":
        current_status = "Unloaded"
        print("Action: Unloaded")
        
        # After 1 second, revert to "Idle"
        threading.Timer(1.0, reset_to_idle).start()
        return jsonify({"status": "success", "message": "Unloaded!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid action!"}), 400

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": current_status})

# Helper function to reset the status to Idle
def reset_to_idle():
    global current_status
    current_status = "Idle"
    print("Status reset to Idle")

if __name__ == '__main__':
    app.run()
