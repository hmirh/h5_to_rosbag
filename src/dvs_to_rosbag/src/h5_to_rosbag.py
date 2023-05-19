#!/usr/bin/env python3

import rospy
import rosbag
from dvs_msgs.msg import Event
from dvs_msgs.msg import EventArray
import h5py



# Open the H5 file for reading
#h5_file = h5py.File('/home/hengam2/h5torobag/catkin_ws/src/dvs_to_rosbag/events.h5', 'r')

# Get the events dataset
#events = h5_file['events']

# Read the first line
#first_line = events[0][0]

# Close the H5 file
#h5_file.close()

# Do something with the first line
#print(first_line)



def convert_h5_to_rosbag(h5_file_path, bag_file_path, topic_name):

    # Open the H5 file for reading
    h5_file = h5py.File(h5_file_path, 'r')

    # Create a ROS bag for writing
    bag = rosbag.Bag(bag_file_path, 'w')

    # Get the event data from the H5 file
    events = h5_file['events']

    # Create a ROS EventArray message
    event_array = EventArray()

    # Iterate over the events and populate the EventArray message
    for event in events:
        # Create an Event message for each event
        ros_event = Event()
        ros_event.ts = rospy.Time.from_sec(event[0])
        print(ros_event.ts)
        ros_event.x = event[1]
        ros_event.y = event[2]
        ros_event.polarity = event[3]
        
        # Append the Event to the EventArray
        event_array.events.append(ros_event)
        
        # Write the Event message to the ROS bag
        bag.write(topic_name, ros_event)
        
    # Write the EventArray message to the ROS bag
    #bag.write(topic_name, event_array)

    # Close the H5 file and the ROS bag
    h5_file.close()
    bag.close()
    
if __name__ == '__main__':
    rospy.init_node('h5_to_rosbag')

    # Set the paths and topic name according to your requirements
    h5_file_path = '/home/hengam2/h5torobag/catkin_ws/src/dvs_to_rosbag/events.h5'
    bag_file_path = '/home/hengam2/h5torobag/catkin_ws/src/dvs_to_rosbag/output.bag'
    topic_name = '/dvs/events'

    convert_h5_to_rosbag(h5_file_path, bag_file_path, topic_name)
    
    

