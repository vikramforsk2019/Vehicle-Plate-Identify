# Vehicle-Plate-Identify
Number plate detection/recognization using yolo and Flask api. 
# Perform Plate Detection Using Yolov3 and Tensorflow 
1.Data Preprocessing
* The structure of the `Plate_dataset`
```
├── Plate_data
│   ├── Annotations
│   │       └── 0.xml (315 items)
│   ├── ImageSets  #contains the all images     
│   └── JPEGImages
│   |   └── 0.txt (315 items)
    |
    |____xml_to_text.py #yolo format text file



* The JPEGImages:

    Image Type : jpg(JPG)
    Width x Height : 640 x 480

 The Annotations : The VOC format .xml for Object Detection, automatically generate by the label tools. Below is an example of .xml file.

 <annotation>
<filename>0.jpg</filename>
  <size>
   <width>806</width>
    <height>466</height>
 </size>
  <object>
  <name>number_plate</name>
  <bndbox>
    <xmin>581</xmin>
    <ymin>273</ymin>
    <xmax>700</xmax>
    <ymax>320</ymax>
   </bndbox>
  </object>
</annotation>


* my google drive folder format is:

Yolov3
|
|
├── Yolo-files
│            |
|            |_____.darknet53.conv.74 
|            |
|            |_____yolov3.weights 
|
|____Backup/
|
|____generate_train.py
|
|____obj.data
|
|____obj.names
|
|____obj.zip


# Trained Model
First extract the images from various sources like github,medium etc.
almost 300+ images which are possible to trained the model on google colaboratery using yolo.
   1. Clone Darknet yolov3 
   2.Data Annotation. 
   3. Data preparation as needed by YOLO. 
   4. Configuration files preparation. 
   5. Training. 
   6. Result weights. 

# Flask Api Structure
```bash
|-- Procfile
|-- __pycache__
|   |-- app.cpython-37.pyc
|   `-- yolo_detection.cpython-37.pyc
|-- app.py
|-- classes.names
|-- darknet-yolov3.cfg
|-- lapi.weights
|-- requirements.txt
|-- static
|   |-- detect_cut
|   |   |-- 8.jpg
|   |   `-- babu.png
|   |-- index.js
|   |-- style.css
|   `-- uploads
|       |-- 8.jpg
|       |-- 8_yolo_out_py.jpg
|       |-- babu.png
|       `-- babu_yolo_out_py.jpg
|-- templates
|   `-- upload.html
`-- yolo_detection.py
```
5 directories, 18 files
   
# All are describe on google drive 
https://drive.google.com/drive/u/0/folders/1xj-a9WmIdEcOhgU42ZBs4FpBDHPN4LFT

![Screenshot_2020-10-19 Upload Image](https://user-images.githubusercontent.com/51817568/96476670-28bd1d00-1253-11eb-94fc-46dbf2f26ffb.png)
![Screenshot_2020-10-19 Upload Image(1)](https://user-images.githubusercontent.com/51817568/96476775-47231880-1253-11eb-9342-e0e24d6d5b7c.png)
![Screenshot_2020-10-19 Upload Image(2)](https://user-images.githubusercontent.com/51817568/96476846-6621aa80-1253-11eb-8df9-e443b41078c5.png)

