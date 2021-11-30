from os import path

max_num_imgs=10
min_num_keypoints=1
max_num_people=10
IMG_SIZE = 256
BATCH_SIZE = 16
NUM_KEYPOINTS = 17   # 17 pairs each having x, y coordinates 
HEATMAP_SIZE=64
EPOCHS=100
root_data_folder='/content/dataset_coco/'
#root_data_folder='..'
folder_ann=path.join(root_data_folder,'annotations')
#train folders
train_annot_path=path.join(folder_ann,'person_keypoints_train2017.json')
train_folder_img=path.join(root_data_folder,'train2017')
#validate folders
val_annot_path=path.join(folder_ann,'person_keypoints_val2017.json')
val_folder_img=path.join(root_data_folder,'val2017')
#flag_debug=True
flag_debug=False
