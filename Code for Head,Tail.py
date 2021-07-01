import time
Motor1 = 16
Motor2 = 18
t=0;
Rpm = 1800;
const int stadard_fish_length;

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)


def Fish_detect(Detection): 
	print("Fish detected") 
	GPIO.setwarnings(False) # Ignore warning for now 
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering 
	GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off) 
	GPIO.add_event_detect(10,GPIO.RISING,Detection=fish_detected) # Setup event on pin 10 rising edge 
	while(add_event_detect != 0):
		time=0
		sleep(1)
		t=t+1

print(t)

length_of_fish = t * Rpm

head_of_fish = 0.24 * length_of_fish 
head_cut = head_of_fish / Rpm
GPIO.output(Motor1,GPIO.HIGH)

tail_of_fish = length of fish - standard fish length
tail_cut = tail_of_fish / Rpm + t
GPIO.output(Motor2,GPIO.HIGH)

GPIO.cleanup() 