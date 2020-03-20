import numpy as np
import rospy
from PIL import Image
from geometry_msgs.msg import Pose
from hbp_nrp_virtual_coach.virtual_coach import VirtualCoach 
from cdp4_data_collection import CDP4DataCollection as data_collection 


objects = list(['table_conference_1','vase_large_2','bookshelf_large','laptop_pc_1','sofa_set_1','toolbox_metal_blue','mug_beer','coffee_machine','coffee_table_set_1','file_cabinet_large'])
shift = [0.3490,0.5950,0.936,0.128,0.3830,0.108,0.123,0.213,0.241,0.352]
large_obj = [0,1,0,1,0,1,1,1,0,0]
vc = VirtualCoach(environment='local', storage_username='nrpuser')
sim = vc.launch_experiment('scene_understanding_icub_holodeck_0_1_0_0')
sim.start()

dc = data_collection()
path = 'train_data'


orig_pose = Pose()
orig_pose.position.z = 10
for i in range(10):
    dc.add_object(objects[i], orig_pose)


counter = 0
for i in range(10):
    
    for j in range(800):
        print(objects[i],j)
        pose = dc.generate_random_pose(large_obj[i])
        dc.set_object_pose(objects[i], pose, True)
        dc.move_eyes(pose.position,shift[i])
        rospy.sleep(0.2)
        image = dc.capture_image().astype(np.uint8)
        image = Image.fromarray(image)
        file_name = '%s/images/snapshot_%.3d.jpg' % (path, counter)
        counter = counter +1
        image.save(file_name)
        dc.set_object_pose(objects[i], orig_pose, False)
        rospy.sleep(0.1)
sim.stop()

file_name = '%s/labels.txt' % path
with open(file_name, 'w+') as f:
    for item in dc.spawned_objects:
        f.write('%s\n' % item)

