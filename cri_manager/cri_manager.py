from .cri_manager_config import CriManagerConfiguration

import json
import docker
import random
import logging
import functools
import docker

LOGGER = logging.getLogger(__name__)


class CriManager(object):

    def __init__(self, config=CriManagerConfiguration(), **kvargs):
        super(CriManager, self).__init__(**kvargs)
        self.client = None
        self.config = config if config != None else CriManagerConfiguration()
        self.config.load_configuration()

    def start(self):
        LOGGER.info('Starting manager')
        try:
            base_url = self.config.settings['host']['base_url']
            self.client = docker.DockerClient(base_url=base_url)
        except:
            self.client = docker.DockerClient.from_env()

    def swarm_info(self):
        pass

    def swarm_init(self, advertise='0.0.0.0:2377', listen='0.0.0.0:5001', force_cluster=False):
        if self.client != None:
            self.client.swarm.init(advertise_addr=advertise, listen_addr=listen,force_new_cluster=force_cluster)
    
    def swarm_leave(self):
        if self.client != None:
            self.client.swarm.leave(force=True)

    def api_create_service(self, name, image='busybox', command=['echo', 'hello world']):
        container_spec = docker.types.ContainerSpec(image=image, command=command)
        task_tmpl = docker.types.TaskTemplate(container_spec)
        return self.client.api.create_service(task_tmpl, name=name)

    def api_select_service(self, name):
        return self.client.api.inspect_service(service=name)

    def api_update_service(self, name, **kwargs):
        service = self.client.api.inspect_service(service=name)
        return service.update(**kwargs)

    def api_delete_service(self, name):
        return self.client.api.remove_service(name)

    def api_scale_service(self, name, replicas):
        service = self.client.api.inspect_service(service=name)
        return service.update(mode=docker.types.ServiceMode("replicated", replicas=replicas))

    def create_service(self, name, image='busybox', command=['echo', 'hello world'], **kwargs):
        return self.client.services.create(image, command=command, **kwargs)

    def select_service(self, name):
        return self.client.services.list(filters=dict(name=name))[0]

    def update_service(self, name, **kwargs):
        service = self.select_service(name)
        return service.update(**kwargs)

    def delete_service(self, name):
        service = self.select_service(name)
        return service.remove()

    def scale_service(self, name, replicas):
        service = self.select_service(name)
        return service.scale(replicas)
