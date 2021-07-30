from flask import Blueprint, jsonify
from pynvml import *

gpu_metrics = Blueprint('gpu_metrics', __name__)


@gpu_metrics.route('/usage')
def list():
    gpu_usage = []
    # nvmlInit()
    # handle = nvmlDeviceGetHandleByIndex(0)
    # info = nvmlDeviceGetMemoryInfo(handle)
    #
    # for x in range(10):
    #     gpu_usage.append(info.used)
    return jsonify([])
