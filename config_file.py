################################################################################
#                              Configuration parameters
################################################################################

# class labels
CATEGORY_INDEX = {1: {'id': 1, 'name': 'pedestrian'},
                  2: {'id': 2, 'name': 'cyclist'},
                  3: {'id': 3, 'name': 'partially-visible person'},
                  4: {'id': 4, 'name': 'ignore region'},
                  5: {'id': 5, 'name': 'crowd'}}

#PATH_TO_SAVE_VIDEOS = '/home/lserra/Work/Serving/output_folder/video/'
OUTPUT_FOLDER = '/home/datasci/video_analytics/output_folder/'

# PATH to existent database
PATH_DB = OUTPUT_FOLDER + 'video.db'

# orientation of crossing line
HORIZONTAL = True

# position of crossing line
#POS = 2.8

# flush data to database
FLUSH_TRIGGER=1150

# detection threshold
THRESHOLD = 0.5

# object detection model to make use of
MODEL_NAME = 'widerperson'

#IP address of the model server
HOST = 'localhost'
################################################################################
