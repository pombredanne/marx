import os
import docker
from .lib import Lib


lib = Lib(os.path.expanduser("~/.marx"))
client = docker.Client(base_url='unix://var/run/docker.sock', version="1.4")
