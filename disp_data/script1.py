import json

#f = open('data.json')
#data = json.loads(f.read())
f = '{"resource":[{"FirstName":"Nikhil","StartTime":"2019-11-10 19:07:01","Phoneno":"444","ReservationId":112},{"FirstName":"Nikhil","StartTime":"2019-11-20 09:17:01","Phoneno":"444555","ReservationId":113},{"FirstName":"Nikhil","StartTime":"2019-11-20 09:17:01","Phoneno":"444555","ReservationId":114},{"FirstName":"Nikhil","StartTime":"2019-11-21 10:28:01","Phoneno":"3333","ReservationId":120},{"FirstName":"Nikhil","StartTime":"2019-11-21 19:28:01","Phoneno":"22","ReservationId":119},{"FirstName":"Nik","StartTime":"2019-11-28 19:07:01","Phoneno":"6644","ReservationId":122},{"FirstName":"Nikhil","StartTime":"2019-12-01 19:25:01","Phoneno":"222","ReservationId":116},{"FirstName":"Nikhil","StartTime":"2020-01-01 19:25:01","Phoneno":"55","ReservationId":117},{"FirstName":"Nikhil","StartTime":"2020-01-03 09:00:00","Phoneno":"4125196270","ReservationId":123},{"FirstName":"Nikhil","StartTime":"2020-01-03 09:00:00","Phoneno":"4125196270","ReservationId":128},{"FirstName":"Nikhil","StartTime":"2020-01-03 09:00:00","Phoneno":"4125196270","ReservationId":129},{"FirstName":"Nikhil","StartTime":"2020-01-22 11:00:00","Phoneno":"4125196270","ReservationId":125},{"FirstName":"Nikhil","StartTime":"2020-01-23 11:00:00","Phoneno":"4125196270","ReservationId":124},{"FirstName":"Nikhil","StartTime":"2020-01-23 14:00:00","Phoneno":"4125196270","ReservationId":126},{"FirstName":"Nikhil","StartTime":"2020-01-23 15:00:00","Phoneno":"4125196270","ReservationId":127},{"FirstName":"Nikhil","StartTime":"2020-01-24 09:00:00","Phoneno":"4125196270","ReservationId":130},{"FirstName":"Nikhil","StartTime":"2020-01-25 09:00:00","Phoneno":"4125196270","ReservationId":131},{"FirstName":"Nikhil","StartTime":"2020-01-25 09:00:00","Phoneno":"4125196270","ReservationId":132},{"FirstName":"Nikhil","StartTime":"2020-01-25 10:30:00","Phoneno":"4125196270","ReservationId":134},{"FirstName":"Nikhil","StartTime":"2020-01-25 11:00:00","Phoneno":"4125196270","ReservationId":133},{"FirstName":"Nikhil","StartTime":"2020-01-25 15:00:00","Phoneno":"4125196270","ReservationId":135},{"FirstName":"Nikhil","StartTime":"2020-01-26 15:00:00","Phoneno":"4125196270","ReservationId":136},{"FirstName":"s","StartTime":"2020-01-27 09:00:00","Phoneno":"12345678","ReservationId":137},{"FirstName":"s","StartTime":"2020-01-27 09:00:00","Phoneno":"12345678","ReservationId":138},{"FirstName":"Nikhil","StartTime":"2020-01-27 10:30:00","Phoneno":"4125196270","ReservationId":139},{"FirstName":"Nikhil","StartTime":"2020-01-27 10:30:00","Phoneno":"4125196270","ReservationId":140},{"FirstName":"Nikhil","StartTime":"2020-01-27 10:30:00","Phoneno":"4125196270","ReservationId":142},{"FirstName":"sid","StartTime":"2020-01-27 10:30:00","Phoneno":"4125196270","ReservationId":143},{"FirstName":"Nikhil","StartTime":"2020-01-28 10:30:00","Phoneno":"4125196270","ReservationId":141},{"FirstName":"Nikhil","StartTime":"2020-01-28 10:30:00","Phoneno":"4125196270","ReservationId":173},{"FirstName":"Nikhil","StartTime":"2020-01-28 10:30:00","Phoneno":"4125196270","ReservationId":174},{"FirstName":"Nikhil","StartTime":"2020-01-28 10:30:00","Phoneno":"4125196270","ReservationId":175},{"FirstName":"","StartTime":"2020-02-15 09:00:00","Phoneno":"7356780820","ReservationId":144},{"FirstName":"Sidharth","StartTime":"2020-02-15 09:00:00","Phoneno":"7356780820","ReservationId":145},{"FirstName":"John","StartTime":"2020-02-16 09:00:00","Phoneno":"123456789","ReservationId":146},{"FirstName":"Sidharth","StartTime":"2020-02-16 09:00:00","Phoneno":"23456789","ReservationId":147},{"FirstName":"s","StartTime":"2020-02-16 09:00:00","Phoneno":"12345678","ReservationId":148},{"FirstName":"ss","StartTime":"2020-02-16 09:00:00","Phoneno":"12345678","ReservationId":149},{"FirstName":"John","StartTime":"2020-02-20 09:00:00","Phoneno":"6007842551","ReservationId":150},{"FirstName":"john","StartTime":"2020-02-26 10:00:00","Phoneno":"700125648","ReservationId":151},{"FirstName":"john","StartTime":"2020-02-26 10:00:00","Phoneno":"700125648","ReservationId":152},{"FirstName":"Sid","StartTime":"2020-02-27 09:00:00","Phoneno":"5654667666755","ReservationId":154},{"FirstName":"S","StartTime":"2020-02-27 09:00:00","Phoneno":"12345678","ReservationId":155},{"FirstName":"Sidharth","StartTime":"2020-02-27 09:30:00","Phoneno":"7356780820","ReservationId":153},{"FirstName":"Sid","StartTime":"2020-02-28 13:00:00","Phoneno":"786544732","ReservationId":156},{"FirstName":"Nikhil","StartTime":"2020-03-01 11:00:00","Phoneno":"4125196270","ReservationId":157},{"FirstName":"jose","StartTime":"2020-03-02 09:00:00","Phoneno":"8921235857","ReservationId":160},{"FirstName":"","StartTime":"2020-03-02 09:30:00","Phoneno":"","ReservationId":167},{"FirstName":"Nikhil","StartTime":"2020-03-02 12:30:00","Phoneno":"4125196270","ReservationId":158},{"FirstName":"Nikhil","StartTime":"2020-03-02 14:00:00","Phoneno":"4125196270","ReservationId":159},{"FirstName":"john","StartTime":"2020-03-03 09:00:00","Phoneno":"1234567889","ReservationId":169},{"FirstName":"hasdjkh","StartTime":"2020-03-03 09:30:00","Phoneno":"","ReservationId":162},{"FirstName":"3232323","StartTime":"2020-03-03 09:30:00","Phoneno":"","ReservationId":165},{"FirstName":"vcvcv","StartTime":"2020-03-03 16:00:00","Phoneno":"1223344445","ReservationId":164},{"FirstName":"Nikhil","StartTime":"2020-03-04 09:00:00","Phoneno":"5167786479","ReservationId":172},{"FirstName":"","StartTime":"2020-03-04 09:30:00","Phoneno":"","ReservationId":168},{"FirstName":"john","StartTime":"2020-03-04 10:30:00","Phoneno":"8394534895","ReservationId":161},{"FirstName":"","StartTime":"2020-03-04 10:30:00","Phoneno":"","ReservationId":163},{"FirstName":"Nikhil","StartTime":"2020-03-04 10:30:00","Phoneno":"5167786479","ReservationId":171},{"FirstName":"","StartTime":"2020-03-04 13:00:00","Phoneno":"33333","ReservationId":166},{"FirstName":"sidharth","StartTime":"2020-03-04 16:00:00","Phoneno":"123456789","ReservationId":170},{"FirstName":"Nikhil","StartTime":"2020-03-06 10:30:00","Phoneno":"4125196270","ReservationId":176},{"FirstName":"Nikhil","StartTime":"2020-03-06 10:30:00","Phoneno":"5167786479","ReservationId":177},{"FirstName":"john","StartTime":"2020-03-08 09:30:00","Phoneno":"4125196270","ReservationId":178},{"FirstName":"john","StartTime":"2020-03-09 09:00:00","Phoneno":"4125196270","ReservationId":182},{"FirstName":"Jose","StartTime":"2020-03-09 09:00:00","Phoneno":"08921235859","ReservationId":184},{"FirstName":"Jose","StartTime":"2020-03-09 09:00:00","Phoneno":"1245845","ReservationId":190},{"FirstName":"john","StartTime":"2020-03-09 09:30:00","Phoneno":"4125196270","ReservationId":181},{"FirstName":"Jose","StartTime":"2020-03-09 10:00:00","Phoneno":"08921235859","ReservationId":191},{"FirstName":"Nikhil","StartTime":"2020-03-09 10:30:00","Phoneno":"4125196270","ReservationId":179},{"FirstName":"Nikhil","StartTime":"2020-03-09 10:30:00","Phoneno":"4125196270","ReservationId":180},{"FirstName":"Jose","StartTime":"2020-03-09 10:30:00","Phoneno":"08921235859","ReservationId":187},{"FirstName":"Jose","StartTime":"2020-03-09 11:00:00","Phoneno":"08921235859","ReservationId":188},{"FirstName":"Jose","StartTime":"2020-03-09 11:30:00","Phoneno":"08921235859","ReservationId":189},{"FirstName":"Jose","StartTime":"2020-03-10 09:00:00","Phoneno":"08921235859","ReservationId":183},{"FirstName":"Jose","StartTime":"2020-03-10 09:30:00","Phoneno":"08921235859","ReservationId":192},{"FirstName":"Jose","StartTime":"2020-03-10 09:30:00","Phoneno":"08921235859","ReservationId":193},{"FirstName":"Jose","StartTime":"2020-03-10 10:00:00","Phoneno":"08921235859","ReservationId":185},{"FirstName":"Jose","StartTime":"2020-03-10 11:00:00","Phoneno":"08921235859","ReservationId":194},{"FirstName":"Jose","StartTime":"2020-03-10 14:30:00","Phoneno":"08921235859","ReservationId":186},{"FirstName":"jose","StartTime":"2020-03-11 09:00:00","Phoneno":"23444","ReservationId":197},{"FirstName":"rr","StartTime":"2020-03-11 09:00:00","Phoneno":"334344","ReservationId":199},{"FirstName":"ss","StartTime":"2020-03-11 09:30:00","Phoneno":"325345","ReservationId":198},{"FirstName":"ghh","StartTime":"2020-03-11 09:30:00","Phoneno":"5785","ReservationId":201},{"FirstName":"john","StartTime":"2020-03-11 10:00:00","Phoneno":"6565665","ReservationId":195},{"FirstName":"dasd","StartTime":"2020-03-11 10:00:00","Phoneno":"234235","ReservationId":204},{"FirstName":"Jose","StartTime":"2020-03-11 10:30:00","Phoneno":"08921235859","ReservationId":196},{"FirstName":"John","StartTime":"2020-03-11 10:30:00","Phoneno":"12345678","ReservationId":200},{"FirstName":"rr","StartTime":"2020-03-11 11:00:00","Phoneno":"345634","ReservationId":203},{"FirstName":"ghgh","StartTime":"2020-03-11 13:00:00","Phoneno":"666","ReservationId":202},{"FirstName":"john","StartTime":"2020-03-11 15:00:00","Phoneno":"12345678","ReservationId":205},{"FirstName":"Jose","StartTime":"2020-03-12 09:00:00","Phoneno":"08921235859","ReservationId":206},{"FirstName":"Nikhil","StartTime":"2020-03-12 09:30:00","Phoneno":"5167786479","ReservationId":210},{"FirstName":"jj","StartTime":"2020-03-12 10:00:00","Phoneno":"243","ReservationId":207},{"FirstName":"Nikhil","StartTime":"2020-03-12 10:30:00","Phoneno":"5167786479","ReservationId":211},{"FirstName":"Jose","StartTime":"2020-03-12 16:00:00","Phoneno":"08921235859","ReservationId":209},{"FirstName":"Jose","StartTime":"2020-03-12 16:30:00","Phoneno":"08921235859","ReservationId":208},{"FirstName":"Jose","StartTime":"2020-03-13 09:00:00","Phoneno":"08921235859","ReservationId":219},{"FirstName":"Jose","StartTime":"2020-03-13 09:00:00","Phoneno":"08921235859","ReservationId":222},{"FirstName":"Jose","StartTime":"2020-03-13 09:00:00","Phoneno":"08921235859","ReservationId":224},{"FirstName":"Jose","StartTime":"2020-03-13 09:00:00","Phoneno":"08921235859","ReservationId":225},{"FirstName":"Jose","StartTime":"2020-03-13 09:00:00","Phoneno":"08921235859","ReservationId":228},{"FirstName":"Sidharth","StartTime":"2020-03-13 09:00:00","Phoneno":"4125196270","ReservationId":237},{"FirstName":"Nikhil","StartTime":"2020-03-13 09:30:00","Phoneno":"5167786479","ReservationId":212},{"FirstName":"Jose","StartTime":"2020-03-13 09:30:00","Phoneno":"08921235859","ReservationId":226},{"FirstName":"gg","StartTime":"2020-03-13 09:30:00","Phoneno":"08921235859","ReservationId":227},{"FirstName":"Jose","StartTime":"2020-03-13 09:30:00","Phoneno":"08921235859","ReservationId":231},{"FirstName":"John","StartTime":"2020-03-13 09:30:00","Phoneno":"123456789","ReservationId":236},{"FirstName":"Jose","StartTime":"2020-03-13 10:00:00","Phoneno":"08921235859","ReservationId":235},{"FirstName":"Nikhil","StartTime":"2020-03-13 10:00:00","Phoneno":"5167786479","ReservationId":239},{"FirstName":"Jose","StartTime":"2020-03-13 10:30:00","Phoneno":"08921235859","ReservationId":233},{"FirstName":"Jose","StartTime":"2020-03-13 10:30:00","Phoneno":"08921235859","ReservationId":234},{"FirstName":"Jose","StartTime":"2020-03-13 15:00:00","Phoneno":"08921235859","ReservationId":232},{"FirstName":"Sid","StartTime":"2020-03-13 15:30:00","Phoneno":"4125196270","ReservationId":238},{"FirstName":"Jose","StartTime":"2020-03-13 16:30:00","Phoneno":"08921235859","ReservationId":220},{"FirstName":"Jose","StartTime":"2020-03-13 16:30:00","Phoneno":"08921235859","ReservationId":223},{"FirstName":"Jose","StartTime":"2020-03-13 16:30:00","Phoneno":"08921235859","ReservationId":230},{"FirstName":"john","StartTime":"2020-03-14 09:00:00","Phoneno":"12345678","ReservationId":240},{"FirstName":"Jose","StartTime":"2020-03-14 09:00:00","Phoneno":"08921235859","ReservationId":246},{"FirstName":"Nikhil","StartTime":"2020-03-14 09:30:00","Phoneno":"4125196270","ReservationId":244},{"FirstName":"sid","StartTime":"2020-03-14 10:00:00","Phoneno":"12345678","ReservationId":242},{"FirstName":"sid","StartTime":"2020-03-14 10:30:00","Phoneno":"4125196270","ReservationId":243},{"FirstName":"Nikhil","StartTime":"2020-03-14 11:00:00","Phoneno":"4125196270","ReservationId":245},{"FirstName":"Sidharth","StartTime":"2020-03-14 14:30:00","Phoneno":"12345678","ReservationId":241},{"FirstName":"Jose","StartTime":"2020-03-15 09:00:00","Phoneno":"08921235859","ReservationId":229},{"FirstName":"Jose","StartTime":"2020-03-15 12:00:00","Phoneno":"08921235859","ReservationId":216},{"FirstName":"Jose","StartTime":"2020-03-15 14:00:00","Phoneno":"08921235859","ReservationId":215},{"FirstName":"Jose","StartTime":"2020-03-16 09:00:00","Phoneno":"08921235859","ReservationId":221},{"FirstName":"Jose","StartTime":"2020-03-16 10:00:00","Phoneno":"08921235859","ReservationId":217},{"FirstName":"Jose","StartTime":"2020-03-16 10:30:00","Phoneno":"08921235859","ReservationId":218},{"FirstName":"Jose","StartTime":"2020-03-19 09:00:00","Phoneno":"08921235859","ReservationId":213},{"FirstName":"Jose","StartTime":"2020-03-19 16:30:00","Phoneno":"08921235859","ReservationId":214},{"FirstName":"Nikhil","StartTime":"2020-05-01 19:26:01","Phoneno":"22","ReservationId":118}]}'
data = json.loads(f)


first_name =[]
start_time = []
phone_no = []
res_id = []

# Python program to convert time from 24 hour 
# to 12 hour format 
  
# Convert Function which takes in 
# 24hour time and convert it to 
# 12 hour format 
def convert12(string): 
  
    # Get Hours 
    h1 = ord(string[0]) - ord('0'); 
    h2 = ord(string[1]) - ord('0'); 
  
    hh = h1 * 10 + h2; 
  
    # Finding out the Meridien of time 
    # ie. AM or PM 
    Meridien=""; 
    if (hh < 12): 
        Meridien = "AM"; 
    else: 
        Meridien = "PM"; 
  
    hh %= 12; 
    my_str = '';
  
    # Handle 00 and 12 case separately 
    if (hh == 0): 
        my_str = my_str + '12';
        #print("12", end = ""); 
  
        # Printing minutes and seconds 
        for i in range(2, 8):
            my_str = my_str + string[i];
            #print(string[i], end = ""); 
  
    else:
        my_str = my_str + str(hh) ;
        #req_Time = hh
        #print(hh,end=""); 
          
        # Printing minutes and seconds 
        for i in range(2, 8): 
            my_str = my_str + string[i];
            #req_Time = req_Time + str[i];
            #print(string[i], end = ""); 
  
    # After time is printed 
    # cout Meridien 
    my_str = my_str + ' ' + Meridien;
    return(my_str);
    #print(" " + Meridien); 


if len(first_name)==0:
    for i in data['resource']:
        for j in i:
            if j=='FirstName':
                first_name.append(i[j])
            elif j == 'StartTime':
                datetime = i[j].split()
                date = datetime[0]
                time = datetime[1]
                req_time = convert12(time);
                req_datetime = date + ' ' + req_time
                start_time.append(req_datetime)

            elif j == 'Phoneno':
                phone_no.append(i[j])
            elif j == 'ReservationId':
                res_id.append(i[j])

        

