from flask import Flask

from cpu.api import cpu_metrics
from gpu.api import gpu_metrics
from ram.api import ram_metrics
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.register_blueprint(cpu_metrics, url_prefix='/cpu')
app.register_blueprint(gpu_metrics, url_prefix='/gpu')
app.register_blueprint(ram_metrics, url_prefix='/ram')
