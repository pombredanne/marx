import os
import docker

client = docker.Client(base_url='unix://var/run/docker.sock', version="1.4")
