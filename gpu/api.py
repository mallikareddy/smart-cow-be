from GPUtil import GPUtil
from flask import Blueprint, jsonify

gpu_metrics = Blueprint('gpu_metrics', __name__)


@gpu_metrics.route('/usage')
def list():
    device_ids = GPUtil.getAvailable(
        order='first', limit=1, includeNan=False
    )
    return jsonify(device_ids[0].memoryUsed if len(device_ids) > 0 else 0)
