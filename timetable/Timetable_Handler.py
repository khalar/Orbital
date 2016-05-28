import json
import Timetable_Extraction

additive_table = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}

timetable = ['0']*672

#process timetable
def table_generation(week,starttime,endtime):
	if len(starttime)<4:
		starttime = '0'+starttime
	if len(endtime)<4:
		endtime = '0'+endtime
	startnum = (int(starttime[0])*10+int(starttime[1]))*60+int(starttime[2])*10+int(starttime[3])
	endnum = (int(endtime[0])*10+int(endtime[1]))*60+int(endtime[2])*10+int(endtime[3])
	start = int((startnum + additive_table[week]*1440)/15)
	end = int((endnum + additive_table[week]*1440)/15)
	#print start,end
	for i in range(start,end):
		timetable[i] = '1'

#obtain timetable as a string of length 672
def timetable_string(userid,password):
	raw_json = Timetable_Extraction.retrieve_timetable(userid,password)
	json_timetable = json.loads(raw_json)['Results']
	for i in range(len(json_timetable)):
		table_generation(json_timetable[i]['DayText'],json_timetable[i]['StartTime'],json_timetable[i]['EndTime'])
	return ''.join(timetable)
