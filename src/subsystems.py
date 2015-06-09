import wpilib
from utils import MultiMotor
from nutrons import Robot
from commands import DriveCmd

class DriveTrain(wpilib.command.Subsystem):
    def initDefaultCommand(self):
        self.setDefaultCommand(DriveCmd())
        #self.logger.info("Setting default")
    def driveTWH(self,throttle,wheel,h):
        (left,right,h) = self.h_drive(throttle,wheel,h)        
        Robot.left_drive.set(-left)
        Robot.right_drive.set(right)
        Robot.h_motor.set(h)
    def driveLRH(self,left,right,h):
        Robot.left_drive.set(-left)
        Robot.right_drive.set(right)
        Robot.h_motor.set(h)
    def h_drive(self,throttle,wheel,y):
        ''' Return a left , right, h tripple '''
        left = throttle - wheel
        right = throttle + wheel
        h = y
        return (left,right,h)