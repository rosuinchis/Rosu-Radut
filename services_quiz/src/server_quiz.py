#! /usr/bin/env python
import rospy

from services_quiz.srv import QuizServMess, QuizServMessResponse
from datetime import datetime
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My callback has been called")
    start_time = datetime.now()
    turn = Twist()
    while start_time - current_time < request.duration:
        turn.angular.x = 0.5
        pub.publish(turn)
        current_time = datetime.now()
    turn.linear.x = 0.0
    turn.angular.z = 0.0
    pub.publish(turn)
    response = QuizServMessResponse()
    response.success = True

    return response

rospy.init_node('service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size =1)
my_service = rospy.Service('/my_service', QuizServMess, my_callback)
rospy.spin()
