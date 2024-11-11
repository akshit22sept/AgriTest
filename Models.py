import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras.models import load_model
import numpy as np
from numpy.random import randint,choice
import pandas as pd
import matplotlib.pyplot as plt
from skimage.io import imread
import seaborn as sns
from skimage.transform import rescale, resize, downscale_local_mean

AllLeavesClasses=['Apple', 'Blueberry', 'Cherry', 'Corn', 'Grape', 'Mango', 'Orange', 'Peach', 'Pepper,', 'Potato', 'Raspberry', 'Soybean', 'Squash', 'Strawberry', 'Sugarcane', 'Tea', 'Tomato', 'Wheat']
WheatClasses=["Aphid",'Black_Rust','Blast','Brown_Rust','Common_Root_Rot','Fusarium_Head_Blight','Healthy','Leaf_Blight','Mildew','Mite','Septoria','Smut','Stem_fly','Tan_spot','Yellow_Rust']
AppleClasses=['Apple_scab', 'Black_rot', 'Cedar_apple_rust', 'healthy']
TomatoClasses=['Bacterial_spot','Early_blight','healthy','Late_blight','Leaf_Mold','Septoria_leaf_spot','Spider_mites Two-spotted_spider_mite','Target_Spot','Tomato_mosaic_virus','Tomato_Yellow_Leaf_Curl_Virus']
PotatoClasses=["Early Blight","Healthy","Late Blight"]
SPotato=['Soybean',"Pepper,"]
SApple=["Cherry","Blueberry"]
SWheat=["Corn"]
SSugarcane=["Peach"]
SMango=['Tea']

AllClasses=[AllLeavesClasses,AppleClasses,PotatoClasses,TomatoClasses,WheatClasses]
def GetInfo(Name,NameList,ModelList):
    return ModelList[NameList.index(Name)]

ModelName=[]
Model=[]
m=load_model("Models\\AllLeavesTesting.h5")
for i in os.listdir("Models"):
    if not "testing" in i.lower():
        ModelName.append(i.split("Model")[0])
        Model.append(load_model(f"Models\\{i}"))
'''
f=AllLeavesClasses[randint(0,18)]
c=f.lower()
i=randint(0,5)
a=imread(f"Valid\\{c}\\{choice(os.listdir(f"Valid\\{c}\\"))}")
print(c)
'''

a=imread(f"TESTING\\WheatHealthy1.png")
print(ModelName)


def Predict(image):
    a = resize(image, [255, 255], anti_aliasing=True)
    a1 = np.expand_dims(a, axis=0)
    predict=GetInfo("AllLeaves",ModelName,Model).predict(a1)
    predict2=m.predict(a1)

    Pred=predict+predict2
    classes_x=np.argmax(Pred,axis=1)
    LeafType=GetInfo("AllLeaves",ModelName,AllClasses)[int(classes_x)]
    e=predict[0]*100
    if LeafType in SApple:
        LeafType = "Apple"
    if LeafType in SPotato:
        LeafType = "Potato"
    if LeafType in SWheat:
        LeafType = "Wheat"
    if LeafType in SSugarcane:
        LeafType = "Sugarcane"
    if LeafType in SMango:
        LeafType="Mango"


    if [i for i in ModelName if LeafType in ModelName]:
        predictDis=GetInfo(LeafType,ModelName,Model).predict(a1)
        ClassDis = np.argmax(predictDis, axis=1)
        Dis = GetInfo(LeafType,ModelName,AllClasses)[int(ClassDis)]
        return f"  Leaf Type = {LeafType}",f"  Condition = {Dis}"
    else:
        return f"  Leaf Type = {LeafType}","  Not enough information about this plant"



Pred,Dis=Predict(a)

print(Pred,Dis)