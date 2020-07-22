import csv

def data_writer(time, consigne, temperature, temperature_max, puissance, coeff_proportionnel, coeff_integral, coeff_derive, proportionnel, integral, derive, file_name='eggsss.csv'):
    with open(file_name, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL) #
        spamwriter.writerow([time, consigne, temperature, temperature_max, puissance, coeff_proportionnel, coeff_integral, coeff_derive, proportionnel, integral, derive])
    csvfile.close()
    
def getValues(ser, puissance=0):
    
    if puissance > 124:
        puissance = 125
    if puissance <0 :                
        puissance = 0
    puissance = int(puissance //1)
    tkt =chr(puissance)
    ser.write(tkt.encode('ascii'))
    arduinoData = ser.readline().decode('ascii')
   
    return arduinoData

