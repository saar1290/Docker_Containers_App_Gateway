from fastapi import FastAPI
from pydantic import BaseModel
import docker
import uvicorn

docker_api = docker.DockerClient(base_url='unix://var/run/docker.sock')

<<<<<<< HEAD
class Start(BaseModel):
=======
class msg(BaseModel):
>>>>>>> ee056f8 (Update content)
    instance_num: str
    PX4_SIM_HOST_ADDR: str
    user: str
    drone_role: str

app = FastAPI()

@app.post("/start")
<<<<<<< HEAD
def start_instance(item: Start):
    ip = item.PX4_SIM_HOST_ADDR.split('.')[-1]
    port = "4{}{}".format(ip, item.instance_num)
    container = docker_api.containers.run('registry:5000/px4:latest', detach=True, tty=True,
    environment=["PX4_SIM_HOST_ADDR={}".format(item.PX4_SIM_HOST_ADDR), "instance_num={}".format(item.instance_num)],
    ports={'4560/tcp':'{}'.format(port)}, name='px4-{}-{}-{}'.format(item.drone_role, item.user, item.instance_num))
    return "The instance {} is created, and listening on host workstation:{}".format(item.instance_num, port)

@app.post("/stop")
def stop_instance(item: Start):
=======
def start_instance(item: msg):
    port = "4{}{}".format(item.PX4_SIM_HOST_ADDR[-1], item.instance_num)
    container = docker_api.containers.run('registry:5000/px4:latest', detach=True, tty=True,
    environment=["PX4_SIM_HOST_ADDR={}".format(item.PX4_SIM_HOST_ADDR), "instance_num={}".format(item.instance_num)],
    ports={'4560/tcp':'{}'.format(port)}, name='px4-{}-{}-{}'.format(item.drone_role, item.user, item.instance_num))
    logs = container.logs()
    return "The instance {} is created, and listening with host workstation:{}".format(item.instance_num, port), logs

@app.post("/stop")
def stop_instance(item: msg):
>>>>>>> ee056f8 (Update content)
    con_name = 'px4-{}-{}-{}'.format(item.drone_role, item.user, item.instance_num)
    docker_api.api.kill(con_name)
    docker_api.api.remove_container(con_name, force=True)
    return "### Container {} killed ###".format(con_name)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)