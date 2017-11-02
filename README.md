# FindHeaderPath

## 1.备注

寻找头文件相对路径，添加到S32 IDE头文件包含中

2017年11月1日17:25:23 
增加头文件修改直接到.cproject，不用手工复制粘贴
增加FindHeader.bat 批处理直接运行此脚本，实现真*一键导入头文件

## 2.使用方法
### 1.用文本编辑器打开FindHeaderPath.py

```python
#是否将配置一键写入到工程中 True 一键修改到cproject 刷新下项目相对头文件路径就出现了
IsNeedTowriteCproject=True
```
### 2.如果 IsNeedTowriteCproject 选择 false,会生成 *HeaderPath.txt*，再手动选择更新到 .*.cproject*,如果选择 IsNeedTowriteCproject=True,则会一键修改到 *.cproject*