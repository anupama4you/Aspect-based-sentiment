import xml.etree.ElementTree as ET
from src.analyze import asa
from src.polarity import polarity1, polarity2

def process():
    tree = ET.parse('./resources/dataset.xml')
    root = tree.getroot()

    i = 0
    ds_positive = 0
    ds_negative = 0
    ds_neutral = 0
    absa1_positive = 0
    absa1_negative = 0
    absa1_neutral = 0
    absa2_positive = 0
    absa2_negative = 0
    absa2_neutral = 0

    truepositive1 = 0
    truenegative1 = 0
    falsepositive1 = 0
    falsenegative1 = 0
    truepositive2 = 0
    truenegative2 = 0
    falsepositive2 = 0
    falsenegative2 = 0

    for child in root:
        sent = ""
        for child1 in child:
            if child1.tag == "text":
                sent = child1.text
            if child1.tag == "aspectTerms":
                #print("Sent: "+sent)
                data = asa(sent)
                #print(data)
                if(data != ""):
                    for child2 in child1:
                        print("-------------------------------------------------")
                        ds1 = child2.attrib['polarity']
                        print(child2.attrib['term'] + " : " + ds1)
                        if ds1 == "positive":
                            ds_positive += 1
                        elif ds1 == "negative":
                            ds_negative += 1
                        elif ds1 == "neutral":
                            ds_neutral += 1
                        for data1 in data:
                            if child2.attrib['term'] == data1[0]:
                                try:
                                    absa1 = polarity1(data1[1][0])
                                    absa2 = polarity2(data1[1][0])
                                    print(data1[0]+" : "+data1[1][0]+" : "+absa1+" : "+absa2)
                                    if absa1 == "positive":
                                        absa1_positive += 1
                                        if absa1 == ds1:
                                            truepositive1 += 1
                                        else:
                                            falsepositive1 += 1
                                    elif absa1 == "negative":
                                        absa1_negative += 1
                                        if absa1 == ds1:
                                            truenegative1 += 1
                                        else:
                                            falsenegative1 += 1
                                    elif absa1 == "neutral":
                                        absa1_neutral += 1
                                        if absa1 == ds1:
                                            truepositive1 += 1
                                        else:
                                            falsepositive1 += 1
                                    if absa2 == "positive":
                                        absa2_positive += 1
                                        if absa2 == ds1:
                                            truepositive2 += 1
                                        else:
                                            falsepositive2 += 1
                                    elif absa2 == "negative":
                                        absa2_negative += 1
                                        if absa2 == ds1:
                                            truenegative2 += 1
                                        else:
                                            falsenegative2 += 1
                                    elif absa2 == "neutral":
                                        absa2_neutral += 1
                                        if absa2 == ds1:
                                            truepositive2 += 1
                                        else:
                                            falsepositive2 += 1
                                except:
                                    pass
                print("********************************************************************************************")
                i += 1
        if i == -1:
            break

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Count: "+str(i))
    print("-------------------------------------------------")
    print("ds_positive: "+str(ds_positive))
    print("ds_negative: "+str(ds_negative))
    print("ds_neutral: "+str(ds_neutral))
    print("-------------------------------------------------")
    print("absa1_positive: "+str(absa1_positive))
    print("absa1_negative: "+str(absa1_negative))
    print("absa1_neutral: "+str(absa1_neutral))
    print("-------------------------------------------------")
    print("absa2_positive: "+str(absa2_positive))
    print("absa2_negative: "+str(absa2_negative))
    print("absa2_neutral: "+str(absa2_neutral))
    print("-------------------------------------------------")
    print("truepositive1: "+str(truepositive1))
    print("falsepositive1: "+str(falsepositive1))
    print("truenegative1: "+str(truenegative1))
    print("falsenegative1: "+str(falsenegative1))
    print("-------------------------------------------------")
    print("truepositive2: "+str(truepositive2))
    print("falsepositive2: "+str(falsepositive2))
    print("truenegative2: "+str(truenegative2))
    print("falsenegative2: "+str(falsenegative2))
    print("-------------------------------------------------")