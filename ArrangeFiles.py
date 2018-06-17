import os
import re
import shutil

# 压缩文件 正则
zip = '.*?(\.0|\.000|\.001|\.7z|\.ace|\.ain|\.alz|\.apz|\.ar|\.arc|\.ari|\.arj|\.axx|\.bh|\.bhx|\.boo|\.bz|\.bza|\.bz2|\.bzip2|\.c00|\.c01|\.c02|\.cab|\.car|\.cbr|\.cbz|\.cp9|\.cpgz|\.cpt|\.dar|\.dd|\.deb|\.dgc|\.dist|\.ecs|\.efw|\.f|\.fdp|\.gca|\.gz|\.gzi|\.gzip|\.ha|\.hbc|\.hbc2|\.hbe|\.hki|\.hki1|\.hki2|\.hki3|\.hpk|\.ice|\.imp|\.ipg|\.ipk|\.ish|\.j|\.jar|\.jgz|\.jic|\.kgb|\.kz|\.lbr|\.lha|\.lnx|\.lqr|\.lzh|\.lzm|\.lzma|\.lzo|\.lzx|\.md|\.mint|\.mou|\.mpkg|\.mzp|\.nz|\.p7m|\.package|\.pae|\.paq6|\.paq7|\.paq8|\.par|\.par2|\.pbi|\.pcv|\.pea|\.pf|\.pim|\.pit|\.piz|\.pkg|\.pup|\.pup|\.puz|\.pwa|\.qda|\.r00|\.r01|\.r02|\.r03|\.rar|\.rk|\.rnc|\.rpm|\.rte|\.rz|\.rzs|\.s00|\.s01|\.s02|\.s7z|\.sar|\.sdn|\.sea|\.sfx|\.sh|\.shar|\.shk|\.shr|\.sit|\.sitx|\.spt|\.sqx|\.sqz|\.tar|\.tbz2|\.tgz|\.tlz|\.uc2|\.uha|\.uue|\.wad|\.war|\.wot|\.xef|\.xez|\.xpi|\.xx|\.xxe|\.y|\.yz|\.z|\.zap|\.zfsendtotarget|\.zip|\.zix|\.zoo|\.zz)$'
# word文档 正则
doc = '.*?(\.doc|\.docx|\.wps|\.wpt)$'
# excel文档 正则
exl = '.*?(\.xls|\.xlsx|\.et|\.ett)$'
# ppt文档 正则
ppt = '.*?(\.ppt|\.pptx|\.dps|\.dpt)$'
# ps文件 正则
ps = '.*?(\.psd)$'
# ai文件 正则
ai = '.*?(\.ai)$'
# cad文件 正则
cad = '.*?(\.dwt)$'
# txt文档 正则
txt = '.*?(\.txt)$'
# pdf文档 正则
pdf = '.*?(\.pdf)$'
# 视频文件 正则
vedio = '.*?(\.wmv|\.asf|\.asx|\.rm|\.rmvb|\.mp4|\.3gp|\.mov|\.m4v|\.avi|\.dat|\.mkv|\.flv|\.vob)$'
# .exe 正则
exe = '.*?(\.exe)$'
# 图片文件 正则
img = '.*?(\.bmp|\.jpeg|\.jpg|\.png|\.tiff|\.gif|\.pcx|\.tga|\.exif|\.fpx|\.svg|\.psd|\.cdr|\.pcd|\.dxf|\.ufo|\.eps|\.ai|\.raw|\.WMF|\.webp)$'
# 音频文件 正则
audio = '.*?(\.cda|\.WAV|\.aiff|\.mp3|\.mid|\.wma|\.ra|\.rm|\.rmx|\.vqf|\.ogg|\.amr|\.ape|\.flac|\.acc)$'
# 种子文件 正则
torrent = '.*?(\.torrent)$'
# 电子书文件 正则
book = '.*?(\.mobi|\.epub|\.azw)$'
# 网页文件 正则
html = '.*?(\.css|\.js|\.html|\.php|\.jsp|\.aps)$'

filePathGlobal = ''


def handleFile(fileName, toPathName, nowPath):
    if (os.path.exists(toPathName)):
        # nowPath为Z:\download，fileName为a.txt,toPathName为Z:\download\txt\
        shutil.move(nowPath + '\\' + fileName, toPathName)
    else:
        os.makedirs(toPathName)
        shutil.move(nowPath + '\\' + fileName, toPathName)


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    allPathDir = os.listdir(filepath)
    # print('文件数：' + len(allPathDir))
    i = 0

    for fileName in allPathDir:
        # print(str(i) + " " + allDir)# .decode('gbk')是解决中文显示乱码问题
        if (re.match(zip, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + '压缩文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(doc, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'word文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(exl, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'excel文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(ppt, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'ppt文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(ps, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'ps文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(ai, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'ai文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(cad, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'cad文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(txt, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'txt文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(pdf, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'pdf'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(vedio, fileName)):
            # print(fileName)
            fileRealName = os.path.splitext(fileName)[0]
            fileSuffixName = os.path.splitext(fileName)[1]
            # print("文件名：" + fileRealName)
            # print("后缀名：" + fileSuffixName)
            fileRealName = re.sub(
                '1024P|720P|1024p|720p|720|1024|-|国语|高清|超清|\[|]|[\u4e00-\u9fa5]{2}(下载|影视|天堂)|www\..*?\.(cc|me|com|cn|org|tv|us)',
                "", fileRealName)
            # print(fileRealName + fileSuffixName)
            fileRealName = fileRealName.rstrip('.')
            os.rename(filepath + '\\' + fileName, filepath + '\\' + fileRealName + fileSuffixName)
            toPathName = filepath + '\\' + '视频文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(exe, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'exe文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(img, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + '图片'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(audio, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + '音频文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(torrent, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + '种子文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(book, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + '电子书'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match(html, fileName)):
            # print(fileName)
            toPathName = filepath + '\\' + 'html相关文件'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        elif (re.match('压缩文件|html相关文件|电子书|种子文件'
                       '|音频文件|图片|exe文件|视频文件|pdf'
                       '|txt文件|cad文件|ai文件|ps文件|ppt文件'
                       '|word文件|excel文件', fileName) == None):
            toPathName = filepath + '\\' + '其他'
            handleFile(fileName, toPathName, filepath)
            print('将 ' + fileName + ' 转移到：' + toPathName)
        i = i + 1
    print('整理完成')


if __name__ == '__main__':
    print('请输入想要整理的目录：（如Z:\download）')
    filePathC = input()
    if (filePathC[len(filePathC) - 1] == '\\'):
        filePathC = filePathC.rstrip('\\')
        print(filePathC)
    eachFile(filePathC)
