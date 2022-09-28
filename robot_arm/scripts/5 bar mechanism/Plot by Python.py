import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Record_data = pd.read_csv('yoga_1Pos-2Pos.csv')

def plot_All():
    plt.figure(figsize=(10,5))
    plt.plot(Record_data['KeyNum'],np.zeros(len(Record_data.index)),color="black",linewidth=0.5,linestyle='-',label='Zero', marker='.', markersize=1)
    plt.plot(Record_data['KeyNum'],Record_data['Pos1'],             color="deeppink",linewidth=1,linestyle='-',label='Motor1_Pos(rad)', marker='o', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['Vel1'],             color="deeppink",linewidth=1,linestyle='-',label='Motor1_Vel(rad/s)', marker='v', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['T1'],               color="deeppink",linewidth=1,linestyle='-',label='Motor1_Torq(Nm)', marker='*', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['Pos2'],             color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Pos(rad)', marker='o', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['Vel2'],             color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Vel(rad/s)', marker='v', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['T2'],               color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Torq(Nm)', marker='*', markersize=3)
    plt.legend(loc = 'upper right')
    plt.xlabel("X axis --  Key_Num")
    plt.ylabel("Y axis -- Pos/Vel/Torq")
    plt.title("Pos-Torque mode: comparison of all data")
    plt.show()

def plot_Pos():
    plt.figure(figsize=(10,5))
    plt.plot(Record_data['KeyNum'],np.zeros(len(Record_data.index)),color="black",linewidth=0.5,linestyle='-',label='Zero', marker='.', markersize=1)
    plt.plot(Record_data['KeyNum'],Record_data['Pos1'],             color="deeppink",linewidth=1,linestyle='-',label='Motor1_Position', marker='o', markersize=2)
    plt.plot(Record_data['KeyNum'],Record_data['Pos2'],             color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Position', marker='o', markersize=2)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(loc = 'lower left', fontsize = 'x-large')
    plt.xlabel("X axis --  Key_Num", fontsize = 'xx-large', labelpad=5)
    plt.ylabel("Y axis -- Position(/rad)", fontsize = 'xx-large', labelpad=5)
    plt.title("Pos-Torque mode: comparison of position", fontsize = 'x-large')
    plt.show()

def plot_Vel():
    plt.figure(figsize=(10,5))
    plt.plot(Record_data['KeyNum'],np.zeros(len(Record_data.index)),color="black",linewidth=0.5,linestyle='-',label='Zero', marker='.', markersize=1)
    plt.plot(Record_data['KeyNum'],Record_data['Vel1'],             color="deeppink",linewidth=1,linestyle='-',label='Motor1_Vel', marker='v', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['Vel2'],             color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Vel', marker='v', markersize=3)
    plt.legend(loc = 'upper right')
    plt.xlabel("X axis --  Key_Num")
    plt.ylabel("Y axis -- Vel(rad/s)")
    plt.title("Pos-Torque mode: comparison of velocity")
    plt.show()

def plot_T():
    plt.figure(figsize=(10,5))
    plt.plot(Record_data['KeyNum'],np.zeros(len(Record_data.index)),color="black",linewidth=0.5,linestyle='-',label='Zero', marker='.', markersize=1)
    plt.plot(Record_data['KeyNum'],Record_data['T1'],               color="deeppink",linewidth=1,linestyle='-',label='Motor1_Torq', marker='*', markersize=3)
    plt.plot(Record_data['KeyNum'],Record_data['T2'],               color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Torq', marker='*', markersize=3)
    plt.legend(loc = 'upper right')
    plt.xlabel("X axis --  Key_Num")
    plt.ylabel("Y axis -- Torq(Nm)")
    plt.title("Pos-Torque mode: comparison of torque")
    plt.show()

def SamplingNew():
    MAXDATA=pd.DataFrame()
    yogaPPM1=[]
    yogaPPM2=[]
    yogaPTM1=[]
    yogaPTM2=[]
    bPPM1=[]
    bPPM2=[]
    bPTM1=[]
    bPTM2=[]
    yogaPPNum=[]
    yogaPTNum=[]
    bPPNum=[]
    bPTNum=[]
    Data=pd.read_csv('yn_P_P_16-108_S.csv')
    yogaPPM1.append(max(Data['T1'][16:108]))
    yogaPPM2.append(max(-Data['T2'][16:108]))
    yogaPPNum.append(108-16)
    Data=pd.read_csv('yn_P_P_16-137_S.csv')
    yogaPPM1.append(max(Data['T1'][16:137]))
    yogaPPM2.append(max(-Data['T2'][16:137]))
    yogaPPNum.append(137-16)
    Data=pd.read_csv('yn_P_P_18-128_S.csv')
    yogaPPM1.append(max(Data['T1'][18:128]))
    yogaPPM2.append(max(-Data['T2'][18:128]))
    yogaPPNum.append(128-18)
    Data=pd.read_csv('yn_P_P_20-128_S.csv')
    yogaPPM1.append(max(Data['T1'][20:128]))
    yogaPPM2.append(max(-Data['T2'][20:128]))
    yogaPPNum.append(128-20)
    Data=pd.read_csv('yn_P_P_22-124_S.csv')
    yogaPPM1.append(max(Data['T1'][22:124]))
    yogaPPM2.append(max(-Data['T2'][22:124]))
    yogaPPNum.append(124-22)
    Data=pd.read_csv('yn_P_T_15-77_S.csv')
    yogaPTM1.append(max(Data['T1'][15:77]))
    yogaPTM2.append(max(-Data['T2'][15:77]))
    yogaPTNum.append(77-15)
    Data=pd.read_csv('yn_P_T_16-85_S.csv')
    yogaPTM1.append(max(Data['T1'][16:85]))
    yogaPTM2.append(max(-Data['T2'][16:85]))
    yogaPTNum.append(85-16)
    Data=pd.read_csv('yn_P_T_17-82_S.csv')
    yogaPTM1.append(max(Data['T1'][17:82]))
    yogaPTM2.append(max(-Data['T2'][17:82]))
    yogaPTNum.append(82-17)
    Data=pd.read_csv('yn_P_T_18-87_S.csv')
    yogaPTM1.append(max(Data['T1'][18:87]))
    yogaPTM2.append(max(-Data['T2'][18:87]))
    yogaPTNum.append(87-18)
    Data=pd.read_csv('yn_P_T_20-91_S.csv')
    yogaPTM1.append(max(Data['T1'][20:91]))
    yogaPTM2.append(max(-Data['T2'][20:91]))
    yogaPTNum.append(91-20)
    Data=pd.read_csv('bn_P_P_15-122_S.csv')
    bPPM1.append(max(Data['T1'][15:122]))
    bPPM2.append(max(-Data['T2'][15:122]))
    bPPNum.append(122-15)
    Data=pd.read_csv('bn_P_P_15-142_S.csv')
    bPPM1.append(max(Data['T1'][15:142]))
    bPPM2.append(max(-Data['T2'][15:142]))
    bPPNum.append(142-15)
    Data=pd.read_csv('bn_P_P_16-130_F.csv')
    bPPM1.append(max(Data['T1'][16:130]))
    bPPM2.append(max(-Data['T2'][16:130]))
    bPPNum.append(130-16)
    Data=pd.read_csv('bn_P_P_17-145_S.csv')
    bPPM1.append(max(Data['T1'][17:145]))
    bPPM2.append(max(-Data['T2'][17:145]))
    bPPNum.append(145-17)
    Data=pd.read_csv('bn_P_P_19-145_S.csv')
    bPPM1.append(max(Data['T1'][19:145]))
    bPPM2.append(max(-Data['T2'][19:145]))
    bPPNum.append(145-19)
    Data=pd.read_csv('bn_P_T_12-99_S.csv')
    bPTM1.append(max(Data['T1'][12:99]))
    bPTM2.append(max(-Data['T2'][12:99]))
    bPTNum.append(99-12)
    Data=pd.read_csv('bn_P_T_12-102_S.csv')
    bPTM1.append(max(Data['T1'][12:102]))
    bPTM2.append(max(-Data['T2'][12:102]))
    bPTNum.append(102-12)
    Data=pd.read_csv('bn_P_T_17-104_S.csv')
    bPTM1.append(max(Data['T1'][17:104]))
    bPTM2.append(max(-Data['T2'][17:104]))
    bPTNum.append(104-17)
    Data=pd.read_csv('bn_P_T_18-105_S.csv')
    bPTM1.append(max(Data['T1'][18:105]))
    bPTM2.append(max(-Data['T2'][18:105]))
    bPTNum.append(105-18)
    Data=pd.read_csv('bn_P_T_20-105_S.csv')
    bPTM1.append(max(Data['T1'][20:105]))
    bPTM2.append(max(-Data['T2'][20:105]))
    bPTNum.append(105-20)
    MAXDATA['yogaPPM1']=yogaPPM1
    MAXDATA['yogaPPM2']=yogaPPM2
    MAXDATA['yogaPTM1']=yogaPTM1
    MAXDATA['yogaPTM2']=yogaPTM2
    MAXDATA['bPPM1']=bPPM1
    MAXDATA['bPPM2']=bPPM2
    MAXDATA['bPTM1']=bPTM1
    MAXDATA['bPTM2']=bPTM2
    MAXDATA['yogaPPNum']=yogaPPNum
    MAXDATA['yogaPTNum']=yogaPTNum
    MAXDATA['bPPNum']=bPPNum
    MAXDATA['bPTNum']=bPTNum
    MAXDATA.to_csv('MAXDATA.csv')
    MEANyogaPPM1=np.mean(yogaPPM1)
    MEANyogaPPM2=np.mean(yogaPPM2) 
    MEANyogaPTM1=np.mean(yogaPTM1) 
    MEANyogaPTM2=np.mean(yogaPTM2)
    STDyogaPPM1=np.std(yogaPPM1)
    STDyogaPPM2=np.std(yogaPPM2)
    STDyogaPTM1=np.std(yogaPTM1)
    STDyogaPTM2=np.std(yogaPTM2)
    MEANbPPM1=np.mean(bPPM1)
    MEANbPPM2=np.mean(bPPM2) 
    MEANbPTM1=np.mean(bPTM1) 
    MEANbPTM2=np.mean(bPTM2)
    STDbPPM1=np.std(bPPM1)
    STDbPPM2=np.std(bPPM2)
    STDbPTM1=np.std(bPTM1)
    STDbPTM2=np.std(bPTM2)
    MEANyogaPPNum=np.mean(yogaPPNum)
    MEANyogaPTNum=np.mean(yogaPTNum)
    MEANbPPNum=np.mean(bPPNum)
    MEANbPTNum=np.mean(bPTNum)
    STDyogaPPNum=np.std(yogaPPNum)
    STDyogaPTNum=np.std(yogaPTNum)
    STDbPPNum=np.std(bPPNum)
    STDbPTNum=np.std(bPTNum)
    print(MEANyogaPPM1,STDyogaPPM1,MEANyogaPPM2,STDyogaPPM2,MEANyogaPTM1,STDyogaPTM1,MEANyogaPTM2,STDyogaPTM2,'\n')    
    print(MEANbPPM1,STDbPPM1,MEANbPPM2,STDbPPM2,MEANbPTM1,STDbPTM1,MEANbPTM2,STDbPTM2,'\n')
    print(MEANyogaPPNum,STDyogaPPNum,MEANyogaPTNum,STDyogaPTNum,MEANbPPNum,STDbPPNum,MEANbPTNum,STDbPTNum,'\n')  

# Record_data = pd.read_csv('yn_P_T_20-91_S.csv')
def plot_TiltUp():
    [start,end]=[20,91]
    plt.figure(figsize=(10,5))
    # plt.plot(Record_data['KeyNum'][start-1:end],np.zeros(end-start+1),            color="black",linewidth=0.5,linestyle='-', marker='.', markersize=2)
    plt.plot(Record_data['KeyNum'][start-1:end],Record_data['T1'][start-1:end],   color="deeppink",linewidth=1,linestyle='-',label='Motor1_Torque', marker='*', markersize=5)
    plt.plot(Record_data['KeyNum'][start-1:end],Record_data['T2'][start-1:end],   color="goldenrod",linewidth=1,linestyle='-',label='Motor2_Torque', marker='*', markersize=5)
    plt.xticks([10,20,30,40,50,60,70,80,90,100,110], fontsize=15)
    plt.yticks([-2,-1,0,1,2,3], fontsize=15)
    plt.legend(loc = 'upper right', fontsize = 'x-large')
    plt.xlabel("X axis --  Key_Num", fontsize = 'x-large', labelpad=2)
    plt.ylabel("Y axis -- Torque (Nm)", fontsize = 'x-large', labelpad=2)
    plt.show()

# plot_All()
# plot_Pos()
# plot_Vel()
# plot_T()
# plot_TiltUp()
# SamplingNew()

Data=pd.read_csv('yoga_1Pos-2Pos_13-94.csv')
print('PP1:',max(Data['T1'][13:94]),'\n')
print('PP2:',max(-Data['T2'][13:94]),'\n')
Data=pd.read_csv('yoga_1Pos-2T_18-69.csv')
print('PT1:',max(Data['T1'][18:69]),'\n')
print('PT2:',max(-Data['T2'][18:69]),'\n')
