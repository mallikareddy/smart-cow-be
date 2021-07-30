from flask import Blueprint, jsonify
from pynvml import *

gpu_metrics = Blueprint('gpu_metrics', __name__)


@gpu_metrics.route('/usage')
def list():
    # nvmlInit()
    # handle = nvmlDeviceGetHandleByIndex(0)
    # info = nvmlDeviceGetMemoryInfo(handle)
    #
    # info.used
    return jsonify([])
