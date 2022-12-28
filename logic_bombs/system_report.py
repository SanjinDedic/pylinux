#print out temperature / disk usage / cool stuff every 30 seconds

#print(t)
import platform
import schedule
import time
import psutil as pt
#check for wifi

def job():
    

    print("Computer Operating System: {user}".format(user=platform.node()))
    print("Computer User: {user}".format(user=pt.users()[0][0]))
    print("Processor cores: {cores}".format(cores=pt.cpu_count()))
    print("Processor Load:  {load}%".format(load=pt.cpu_percent()))
    print("Computer RAM: {ram1:.2f} GB".format(ram1=(pt.virtual_memory()[0]/(1024**3))))
    print("Computer RAM used: {ram2:.2f} GB".format(ram2=(pt.virtual_memory()[1]/(1024**3))))
    print("Computer Total Storage: {disk1:.2f} GB".format(disk1=(pt.disk_usage('C:\\')[0]/(1024**3))))
    print("Computer Storage used: {disk2:.2f} GB".format(disk2=(pt.disk_usage('C:\\')[1]/(1024**3))))
    print("Computer local network IP: {net} C".format(net=pt.net_if_addrs()["Wi-Fi"]))
    
    
schedule.every(1).seconds.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)