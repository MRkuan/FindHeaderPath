'''
本脚本目的搜索头文件所在的路径加到set里面，再遍历打出符合S32K144添加头文件相对路径格式 
如果要编译文件，请把注释删除再编译运行  
  
如果字符格式出错，请在程序第一行加上“#coding=utf-8” ps：等号左右两边不要留空格(或者直接把程序中的中文用英文代替)  
github 地址 https://github.com/MRkuan/FindHeaderPath 

 2017年11月1日17:25:23 增加 是否生成的头文件相对路径是否一键加入到 .cproject 
'''
import os  

#是否将配置一键写入到工程中 True 一键修改到cproject 刷新下项目相对头文件路径就出现了
IsNeedTowriteCproject=True


MySelectPath = os.path.abspath('.') 
keyWordStart='<option id="gnu.c.compiler.option.include.paths.1655801871" name="Include paths (-I)" superClass="gnu.c.compiler.option.include.paths" useByScannerDiscovery="false" valueType="includePath">\n'
keyWordEnd='</option>\n'
#这个是用户相对路径头文件前缀
KeyWordUser='<listOptionValue builtIn="false" value="&quot;${workspace_loc:/${ProjName}'
#空set
file_list  = set([])

def FindHeader(MyPath):  
    for i in os.listdir(MyPath):  
        FilePath = os.path.abspath(os.path.join(MyPath, i)) 
        myFileList = []
        myFileList=os.path.splitext(i)          
        if myFileList[1]=='.h':  #输出找到的.h格式的文件  
            print ('找到头文件 ：', i) 
            tmp=FilePath[len(MySelectPath):len(FilePath)-len(i)-1]
            print ('文件相对路径是 ：',tmp)
            file_list.add(tmp)  
        elif os.path.isdir(FilePath):  
            FindHeader(FilePath)  

FindHeader(MySelectPath)  


#寻找的头文件组合成写入字符
writeLines=[]
for tmp in file_list:
    tmp = tmp.replace('\\','/')	# 将字符串里的\\替换成/
    tmp='<listOptionValue builtIn="false" value="&quot;${workspace_loc:/${ProjName}'+tmp+'}&quot;"/>'
    print(tmp)
    writeLines.append(tmp)


#判断是读出文本还是直接一键修改到.cproject
if IsNeedTowriteCproject == False:
    f = open('HeaderPath.txt', 'w')
    for tmp in writeLines: 
        f.write(tmp+'\n')
    f.close()
    print('成功将头文件相对路径写入文本到HeaderPath.txt') 
else:
    lines=[]

    f=open('.cproject','r')  #your path!
    for line in f:
        lines.append(line)
    f.close()
    print(lines)

#搜索开始和结束索引
    satrtLines=0
    endLines=0
    LinesCount=0;
    CprojectLine=[]
#用下简单状态机处理下
    status=0   # 0 未找到开始 1 找到 开始 
    for tmp in lines: 
        LinesCount=LinesCount+1 
        if 0==status:
            if tmp.replace('\t', '')==keyWordStart:          
                satrtLines=LinesCount 
                status=1
        elif 1==status:
            if tmp.replace('\t', '')==keyWordEnd: 
                endLines=LinesCount
                for i in range(satrtLines,endLines-1) :
                    lines.pop(satrtLines)

                CprojectLine.reverse()

                for i in CprojectLine:
                     lines.insert(satrtLines,i)

                for i in writeLines:
                     lines.insert(satrtLines,'\t'*9+i+'\n')
                CprojectLine.clear()
                status=0
            else:  
                if KeyWordUser in tmp:
                     status=1
                    #lines.pop[linesCount]  #把旧的 给和谐
                else:
                    CprojectLine.append(tmp)

    file=open('.cproject','w')  
    for tmp in lines:
        file.write(tmp)
    file.close()  
    print('成功将头文件相对路径写入文本到.cproject') 

    

    
