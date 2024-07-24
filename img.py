from PIL import Image # 可以大量處理圖檔
import os 

for file in os.listdir('origin'): # 打開資料夾origin 
    if file.endswith('.jpg'): # 若是字尾是.jpg，
        image_file = Image.open(os.path.join('origin', file))
        image_file = image_file.convert('L')
        image_file.save(os.path.join('result', file[:-4] + '_宮崎駿.png')) 
        # file[:-4] 是去除 .jpg
# 程式邏輯是：使用os.listdir()找到指定的文件夾，用if file.endswith('.jpg')
# 篩選出附檔名為.jpg的檔案。使用.open() 打開指定位置的檔案夾以及讀取裡面的檔案
# 語法是 Image.open(os.path.join('檔案名稱', file))
# .convert() 轉換的語法，代號為'L'
# .save 存取檔案。存到(os.path.join('result', flie[:-4] + '_宮崎駿.png)')
# 存到result 檔案夾裡面，file 檔案名稱只擷取到 .jpg 前，外加 _宮崎駿.png成為
# 新檔名。 