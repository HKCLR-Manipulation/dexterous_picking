from os import closerange
import motormodule as mm
import time
import matplotlib.pyplot as plt
import keyboard
import pandas as pd
import numpy as np

class TestModule:
    def __init__(self,COM):
        self.mmc = mm.MotorModuleController(COM)
        self.Step_Pos = 0.04
        self.Goal_T=0
        self.Step_T =0.1
        self.Key_Num =0
        self.Mode='POS-T'

        self.Record=pd.DataFrame()
        self.Record_Pos1=[]
        self.Record_Vel1=[]
        self.Record_T1=[]
        self.Record_Pos2=[]
        self.Record_Vel2=[]
        self.Record_T2=[]
        self.Record_KeyNum=[]
    
    def Hold_1POS(self):
        self.mmc.disable_motor(1)
        self.mmc.enable_motor(1)
        self.mmc.send_command(1,0,0,0,0,0)
        self.mmc.send_command(1, self.mmc.rx_values_1[1][0], 0, 100, 2.4, 0)
    def Hold_2POS(self):
        self.mmc.disable_motor(2)
        self.mmc.enable_motor(2)
        self.mmc.send_command(2,0,0,0,0,0)
        self.mmc.send_command(2, self.mmc.rx_values_2[1][0], 0, 100, 2.4, 0)
    def SendCommand(self,can_id,G_Pos,G_Vel,Kp,Kv,G_T):
        self.mmc.disable_motor(can_id)
        self.mmc.enable_motor(can_id)
        self.mmc.send_command(can_id,G_Pos,G_Vel,Kp,Kv,G_T)
    def SingleRecord(self,):
        self.Key_Num=self.Key_Num+1
        self.Record_KeyNum.append(self.Key_Num)
        self.Record_Pos1.append(self.mmc.rx_values_1[1][0])
        self.Record_Vel1.append(self.mmc.rx_values_1[2][0])
        self.Record_T1.append(self.mmc.rx_values_1[3][0])
        self.Record_Pos2.append(self.mmc.rx_values_2[1][0])
        self.Record_Vel2.append(self.mmc.rx_values_2[2][0])
        self.Record_T2.append(self.mmc.rx_values_2[3][0])

    def Collect(self):
        self.Record['KeyNum']=self.Record_KeyNum
        self.Record['Pos1']=self.Record_Pos1
        self.Record['Vel1']=self.Record_Vel1
        self.Record['T1']=self.Record_T1
        self.Record['Pos2']=self.Record_Pos2
        self.Record['Vel2']=self.Record_Vel2
        self.Record['T2']=self.Record_T2
        self.Record.to_csv('Record_Data.csv') 

    def plotPose(self):
        plt.figure(figsize=(10,5))
        plt.plot(self.Record_KeyNum,np.zeros(len(self.Record_KeyNum)),color="black",linewidth=0.5,linestyle='-',label='Zero', marker='.', markersize=5)
        plt.plot(self.Record_KeyNum,self.Record_Pos1,color="deeppink",linewidth=2,linestyle=':',label='M1_Pos(rad)', marker='o')
        plt.plot(self.Record_KeyNum,self.Record_Vel1,color="deeppink",linewidth=2,linestyle=':',label='M1_Vel(rad/s)', marker='v', markersize=10)
        plt.plot(self.Record_KeyNum,self.Record_T1,color="deeppink",linewidth=2,linestyle='-',label='M1_Torq(nm)', marker='*', markersize=15)
        plt.plot(self.Record_KeyNum,self.Record_Pos2,color="goldenrod",linewidth=2,linestyle=':',label='M2_Pos(rad)', marker='o')
        plt.plot(self.Record_KeyNum,self.Record_Vel2,color="goldenrod",linewidth=2,linestyle=':',label='M2_Vel(rad/s)', marker='v', markersize=10)
        plt.plot(self.Record_KeyNum,self.Record_T2,color="goldenrod",linewidth=2,linestyle='-',label='M2_Torq(nm)', marker='*', markersize=15)
        plt.legend(loc = 'upper right')
        plt.xlabel("X axis -- Key_Num")
        plt.ylabel("Y axis -- Pos/Vel/Torq")
        plt.title("Data record of two motors")
        plt.show()

def main():
    tm=TestModule("COM3")
    try:
        while True:
            keyname=keyboard.read_key()
            if keyname == "up":
                if tm.Mode=='POS-T':
                    tm.SendCommand(2, 0, 0, 0, 0, tm.Goal_T)
                else:
                    tm.Hold_2POS()
                tm.Hold_1POS()
                tm.SendCommand(1, tm.mmc.rx_values_1[1][0]+tm.Step_Pos, 0, 100, 2.4, 0)
                print("M1_Pos:",tm.mmc.rx_values_1[1][0])
                tm.SingleRecord()
            elif keyname == "down":
                if tm.Mode=='POS-T':
                    tm.SendCommand(2, 0, 0, 0, 0, tm.Goal_T)
                else:
                    tm.Hold_2POS()
                tm.Hold_1POS()
                tm.SendCommand(1, tm.mmc.rx_values_1[1][0]-tm.Step_Pos, 0, 100, 2.4, 0)
                print("M1_Pos:",tm.mmc.rx_values_1[1][0])
                tm.SingleRecord()
            elif keyname == "w":
                tm.Hold_1POS()
                if tm.Mode=='POS-T':
                    tm.Goal_T=tm.Goal_T-tm.Step_T
                    tm.SendCommand(2, 0, 0, 0, 0, tm.Goal_T)
                    print("M2_T:",tm.mmc.rx_values_2[3][0])
                else:
                    tm.Hold_2POS()
                    tm.SendCommand(2, tm.mmc.rx_values_2[1][0]-tm.Step_Pos, 0, 100, 2.4, 0)
                    print("M2_Pos:",tm.mmc.rx_values_2[1][0])
                tm.SingleRecord()
            elif keyname == "s":
                tm.Hold_1POS()
                if tm.Mode=='POS-T':
                    tm.Goal_T=tm.Goal_T+tm.Step_T
                    tm.SendCommand(2, 0, 0, 0, 0, tm.Goal_T)
                    print("M2_T:",tm.mmc.rx_values_2[3][0])
                else:
                    tm.Hold_2POS()
                    tm.SendCommand(2, tm.mmc.rx_values_2[1][0]+tm.Step_Pos, 0, 100, 2.4, 0)
                    print("M2_Pos:",tm.mmc.rx_values_2[1][0])
                tm.SingleRecord()
            elif keyname == "space":
                tm.Mode='POS-POS'
                print ('Mode is changed to POS-POS after:',tm.Key_Num)
            else:
                print(keyname,tm.Key_Num)
            time.sleep(0.2)
    except KeyboardInterrupt: 
        tm.mmc.disable_motor(1)
        tm.mmc.disable_motor(2)
        tm.Record_Pos1=[i-tm.Record_Pos1[0] for i in tm.Record_Pos1]
        tm.Record_Pos2=[i-tm.Record_Pos2[0] for i in tm.Record_Pos2]
        tm.Collect()
        tm.plotPose() 

if __name__=='__main__':
	main()
    
	
