import api.service.connection.connect_motors as connect

class getAngle():
     def command(self, connection: connect.connectEv3Dev, sensor_id: str):
          angle = connection.sendForGet('cat /sys/class/lego-sensor/' + sensor_id + '/value0')
          return angle