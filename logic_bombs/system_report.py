#print out temperature / disk usage / cool stuff every 30 seconds
#import psutil
#v =psutil.cpu_percent(interval=1)
#psutil.cpu_count()
#psutil.disk_usage('/')
#t=psutil.sensors_temperatures()
#print(t)

import schedule
import time
from pyspectator.computer import Computer
from pyspectator.processor import Cpu
from pyspectator.network import NetworkInterface
from pyspectator.memory import AbsMemory


def job():
    computer = Computer()
    cpu = Cpu(monitoring_latency=1)
    network = NetworkInterface(monitoring_latency=1)
    #memory = AbsMemory()

    print(computer.os)
    print(computer.hostname)
    print(cpu.name)
    print(cpu.count)
    print(cpu.load)
    #print(cpu.temperature)
    
    print(network.ip_address)
    #print(memory.available)
    #print(memory.used)
    

#schedule.every(1).minutes.do(job)
schedule.every(1).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)