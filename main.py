import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

# Mock data for ETL sources
mock_data = {
    "source1": [
        {"id": 1, "name": "John Doe", "city": "New York"},
        {"id": 2, "name": "Jane Smith", "city": "Los Angeles"},
    ],
    "source2": [
        {"id": 1, "product": "Laptop", "price": 999.99},
        {"id": 2, "product": "Mouse", "price": 29.99},
    ],
}

@app.route("/api/health")
def health_check():
    """
    Health check endpoint to verify that the service is running.
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/data")
def get_data():
    """
    Returns sample ETL data from mock sources.
    """
    return jsonify({
        "status": "success",
        "data": mock_data,
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/stats")
def get_stats():
    """
    Returns statistics about the data.
    """
    stats = {
        "total_records": sum(len(v) for v in mock_data.values()),
        "sources": len(mock_data),
        "source_breakdown": {k: len(v) for k, v in mock_data.items()},
        "timestamp": datetime.now().isoformat()
    }
    return jsonify(stats)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
