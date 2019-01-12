#!/usr/bin/env python

from time import sleep

# standard import
import rospy
import imutils

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from detectStopSigns import Stop_sign_detection
# RightHook simulation control service defs
from rh_msgs.srv import SimControl, SimControlRequest

# RightHook actuation message
from rh_msgs.msg import VehicleActuation

class Stop_Flag:

	def __init__(self, init_flag= False):
		self.init_flag = init_flag
		self.bridge = CvBridge()

	def callback(self, image):
		output_flag = False
		try:
			cv_image = self.bridge.imgmsg_to_cv2(image, "rgb8")
		except CvBridgeError, e:
			print e
		cv_image = imutils.resize(cv_image, width=500)
		output_flag = Stop_sign_detection(cv_image)

		print (output_flag)

		self.init_flag = self.init_flag|output_flag




# main function
if __name__ == "__main__":

	# start the actuation and control node
	rospy.init_node('vehicle_controller', anonymous=True)

	# wait until service is advertised
	rospy.wait_for_service('sim_control')

	# create actuation publisher
	actuation_publisher = rospy.Publisher(
		'/vehicle_ZDQ4cW5k/actuation/cmd',
		VehicleActuation,
		queue_size=0)
	stop_sign = Stop_Flag()
	stop_sign_detector = rospy.Subscriber("/vehicle_ZDQ4cW5k/camera/image_raw",Image,stop_sign.callback, queue_size = 1)


	# wait for actuator to connect
	while actuation_publisher.get_num_connections() == 0:
		print "Waiting for actuation connection....."
		sleep(1.0)

	try:
		# get handle to service
		print "connection established....."
		control = rospy.ServiceProxy('sim_control', SimControl)
		while True:
			# new request object
			srv_req = SimControlRequest()
			# fill it out with enum
			srv_req.code = SimControlRequest.ADVANCE
			# send request and get handle to response
			srv_resp = control(srv_req)
			# print response
			print srv_resp.response_msg

			'''
				this is ordinarily where logic would go, but we will
				just stand on the brake
			'''
			throttle = 0.0
			brake = 0.0
			steering = 0.0

			print ("check_flag:",stop_sign.init_flag)

			if stop_sign.init_flag:
				throttle = 0.0
				brake = 0.1


			# create actuation message
			actuation_msg = VehicleActuation()
			actuation_msg.normalized_throttle = throttle
			actuation_msg.normalized_brake = brake
			actuation_msg.steering_degrees = steering

			# send actuation
			actuation_publisher.publish(actuation_msg)

	# handle exception
	except rospy.ServiceException, e:
		print "service call failed: %s"%e
