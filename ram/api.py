import psutil
from flask import Blueprint, jsonify

ram_metrics = Blueprint('ram_metrics', __name__)


@ram_metrics.route('/usage')
def list():
    cpu_usage = []
    for x in range(10):
        cpu_usage.append(psutil.virtual_memory()[2])
    return jsonify(cpu_usage)
