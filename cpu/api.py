import psutil
from flask import Blueprint, jsonify

cpu_metrics = Blueprint('cpu_metrics', __name__)


@cpu_metrics.route('/usage')
def list():
    return jsonify(psutil.cpu_percent(interval=1))
