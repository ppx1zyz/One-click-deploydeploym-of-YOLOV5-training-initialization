#run this code to creat basic file and init
#Before running check train.py yolov5x.py ......
#run anaconda and input to train
"""
conda activate machineLearn
cd D:\Document\Project\Python\Jupyter\Select_cv\AutoBuild\yolov5-master
d:
python train.py

"""
#run to detect(source 0 means using cam......)
""" 
python detect.py --weights runs/train/exp3/weights/best.pt --source data/Samples/ --device 0 --save-txt
python detect.py --weights runs/train/exp25/weights/best.pt --source 0 --device 0 --save-txt
"""
import start_lib as st
import os
yoloPath ='yolov5-master'
trClass  =['kiwi']
yoloModel='yolov5m'
st.creatFile(yoloPath+"/data/Annotations")
st.creatFile(yoloPath+"/data/images")
st.creatFile(yoloPath+"/data/ImageSets")
st.creatFile(yoloPath+"/data/JPEGImages")
st.creatFile(yoloPath+"/data/labels")
st.moveFile('image',yoloPath+'/data/images')
st.moveFile('image',yoloPath+'/data/JPEGImages')
st.moveFile('Annotations',yoloPath+'/data/Annotations')
print('successfully init all data!Now start to creat txt')

m2=[]
count=0
for c in trClass:
    m2.append('  '+str(count)+': '+str(c))
    count+=1
st.rewriteBlock(yoloPath+'/data/my.yaml','#start','#end',m2)

m2=['nc: '+str(count)]
st.rewriteBlock(yoloPath+'/models/'+yoloModel+'.yaml','#start','#end',m2)

m2=["    parser.add_argument('--weights', type=str, default='models/"+yoloModel+".pt', help='initial weights path')",
    "    parser.add_argument('--cfg', type=str, default='models/"+yoloModel+".yaml', help='model.yaml path')"]
st.rewriteBlock(yoloPath+'/train.py','#start','#end',m2)

m2=['classes = [']
for c in trClass:
    m2.append("'"+str(c)+"',")
m2.append(']')
st.rewriteBlock(yoloPath+'/myVocLabel.py','#start','#end',m2)

os.system('cd '+str(yoloPath)+' && python myMakeTxt.py && python myVocLabel.py')
print('All the initializations has been made!\nRun train.py to start training')