import psutil
from flask import Blueprint, jsonify

ram_metrics = Blueprint('ram_metrics', __name__)


@ram_metrics.route('/usage')
def list():
    return jsonify(psutil.virtual_memory()[2])
