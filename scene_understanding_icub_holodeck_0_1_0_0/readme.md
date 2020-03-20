
# NRP Settings

The default settings spawns objects obtained from http://data.nvision2.eecs.yorku.ca/3DGEMS/. The objects are spawed with random orientation along the vertical axis. Icub's left eye is used as the camera to capture the images. The default camera resolution is 2046x2046 pixels. The resolution can be changed by modifying this line in icub/model.sdf. 

"<sensor type="camera" name="camera_left">"
  
# Usage

The images can be capured and saved by executing 'run_experiment.py'. The default setting capures 800 images per object and saves the labels as well. 
