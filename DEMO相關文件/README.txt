單張圖的辨識執行:
執行generate_caption.py並指定要辨識圖片的路徑(default:target/test.jpg)

若要更換圖片的路徑:
於generate_caption.py修改內部參數img_path_default = <PATH_TO_IMG>

或是執行以下:
python generate_caption.py --img-path <PATH_TO_IMG>

將會呈現辨識結果，並將其儲存於target底下
<image_name>_resule.jpg:test結果
<image_name>_detail.jpg:test細節


目前使用的模型存放於model，路徑為model/model_10.pth
若要使用不同模型辨識圖片:
於generate_caption.py修改內部參數model_path_default = <PATH_TO_MODEL>

或是執行以下:
python generate_caption.py --img-path <PATH_TO_IMG> --model <PATH_TO_MODEL>



若要查看(查詢)目前有存取到的單字:
執行look_json.py的check函式
若存在，顯示match和id；若否，顯示not match