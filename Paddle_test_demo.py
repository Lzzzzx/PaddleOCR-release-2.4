from paddleocr import PaddleOCR

#模型加载
ocr=PaddleOCR(use_angle_cls=True, lang="ch")


def detect_pic(pic_path):
    #文字识别
    result=ocr.ocr(pic_path,cls=True)
    return result
def detect_dir(dir_path):
    pass

if __name__ == '__main__':
    res=detect_pic(r'E:\毕业设计\task\PaddleOCR-release-2.4\data\1.png')

    box=list()  # 数字方框
    characters=list()  #数字信息以及其置信度
    for line in res:
        box.append(line[0])
        characters.append((line[1]))
        print(line)

    print(f'方框信息：{box}')

    print(f'数字及其置信度{characters}')