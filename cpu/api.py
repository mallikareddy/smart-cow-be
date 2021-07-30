import psutil
from flask import Blueprint, jsonify

cpu_metrics = Blueprint('cpu_metrics', __name__)


@cpu_metrics.route('/usage')
def list():
    cpu_usage = []
    for x in range(10):
        cpu_usage.append(psutil.cpu_percent(interval=1))
    return jsonify(cpu_usage)
