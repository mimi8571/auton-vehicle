#!usr/bin/env python
import rospy
import tf
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion Twist Point 
from sensor_msgs.msg import Imu 

# gmapping; traditional EKF filter; exact point mapping
# For gmapping, need odometry; must set up beforehand. None needed for hector mapping.
# gmap has odometry through transform. Set up tf_listener, buffer, etc.
# stabilize rolling shutter effect and other sources of noise

class Map(object):
	def __init__(self):
		self.pubGrid = rospy.Publisher('map', OccupancyGrid, queue_size = 100) # ('ser_wrt',String, queue_size=100)
		self.pubPosition = rospy.Publisher('pose', PoseStamped, queue_size=10)
		rospy.Subscriber('scan', LaserScan, scanCallback)
		rospy.Subscriber('odom', Odometry, positionCallback)
		rospy.Subscriber('syscommand', String, system)
		self.tf_odom_listener = tf.TransformListener()
	 	try:
	 		(self.surr, self.position) = listener.lookupTransform('/map', '/odom', rospy.Time(0))
	 	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
	 		continue

	def scanCallback(self, laser): # check if robot is centered in circle
		map.map_update_interval = 1
		min = laser.range_min
		max = laser.range_max
		x = laser.ranges
		N = len(x)
		cumsum = np.cumsum(np.insert(x, 0, 0))  # moving average
	    avg = (cumsum[N:] - cumsum[:-N]) / float(N) 
	    for i in (0, N):  
	    	if x[i] > avg :
	    		radius = avg
	    	else
	    		radius = x[i]
	    return(avg)

	def positionCallback(self, data):
		pos_x = data.x;
		pos_y = data.y;


	def mapEstimation():
		# estimate coordinates of surrounding circle
	    angle_range = laser.angle_max - laser.angle_min
	    for j in (0, int(N/angle_range*2*pi)):
	    	circle[j] = map_position + avg

	    pubGrid.publish(circle)
	    pubPosition.publish(wrt_position)
		
	if __name__ == "__main__":
		rospy.init_node('spatial')
		n = Map()
		rospy.spin()


