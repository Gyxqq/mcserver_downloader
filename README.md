# mcserver_downloader
a downloader for mc server  
[点击这里下载](https://github.com/Gyxqq/mcserver_downloader/releases/tag/v1)  
运行downloader.exe或者downloader.py生成download.txt  
将download.txt复制到aria2目录下  
终端进入到aria2目录，执行
```shell
.\aria2c --input-file=download.txt
```
# 如果电脑上没有python请下载with_exe版的
fork到自己帐号->点击自己仓库的action-> main.yml -> run workflow->选择版本->构建forge服务端-> all workflows -> 选择刚刚运行的那个->summary->Artifacts->下载release
