import paramiko
import api.models.connect_ev3_dev as connect

class getMotersList():
     CMD = 'for f in /sys/class/tacho-motor/*; do echo $f; done'
     def command(self, connection: connect.connectEv3Dev):
          motors = []
          motors = connection.sendForList(self.CMD)
          return motors
     
