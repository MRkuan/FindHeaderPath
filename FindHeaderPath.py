#本脚本目的搜索头文件所在的路径加到set里面，再遍历打出符合S32K144添加头文件相对路径格式 
#如果要编译文件，请把注释删除再编译运行  
  
#如果字符格式出错，请在程序第一行加上“#coding=utf-8” ps：等号左右两边不要留空格(或者直接把程序中的中文用英文代替)  
  
import os  
  
MySelectPath = os.path.abspath('.')  

#空set
file_list  = set([])
def FindHeader(MyPath):  
    for i in os.listdir(MyPath):  
        FilePath = os.path.abspath(os.path.join(MyPath, i)) 
        myFileList = []
        myFileList=os.path.splitext(i)          
#       输出找到的.h格式的文件  
        if myFileList[1]=='.h':  
            print ('找到头文件 ：', i) 
            tmp=FilePath[len(MySelectPath):len(FilePath)-len(i)-1]
            print ('文件相对路径是 ：',tmp)
            file_list.add(tmp)  
        elif os.path.isdir(FilePath):  
#           print FilePath  
#           print '进入文件夹 ：', i  
            FindHeader(FilePath)  
          
#       else:  
#           print i, '———— No dir and No txtFile'     

print('-----------------[start]------------------') 
FindHeader(MySelectPath)  

print('------------------------------------------')
# print(file_list)

f = open('HeaderPath.txt', 'w')

for tmp in file_list:
    tmp = tmp.replace('\\','/')	# 将字符串里的\\替换成/
    tmp='<listOptionValue builtIn="false" value="&quot;${workspace_loc:/${ProjName}'+tmp+'}&quot;"/>'
    print(tmp)
    f.write(tmp+'\n')


f.close()
print('-----------------[end]------------------') 

    
