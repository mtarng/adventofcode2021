import os
import numpy as np

# file1 = open(os.path.join(os.path.dirname(__file__), 'testinput.txt'), 'r')
file1 = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file1.readlines()


all_outputs_total = 0
for line in lines:
    segments, output = line.strip().split("|")

    print("segments:", segments)
    print("output:", output)

    # Find known digit segment components
    for segment in segments.strip().split(" "):
        # print(segment)
        segment_length = len(segment)
        if segment_length == 2:
            print("1:", segment)
            one_set = set(segment)

        elif segment_length == 3:
            print("7:", segment)
            seven_set = set(segment)

        elif segment_length == 4:
            print("4:", segment)
            four_set = set(segment)

        elif segment_length == 7:
            print("8:", segment)
            eight_set = set(segment)

    print("one_set:",one_set)
    print("four_set:",four_set)
    print("seven_set:",seven_set)
    print("eight_set:",eight_set)
        
        
    # Calculate remaining segments based on set knowledge
    segments = segments.strip().split(" ")
    segments_sorted = sorted(segments, key=len)
    for segment in segments_sorted:
        print("segment:",segment)
        segment_length = len(segment)
        # 5 length - 2, 3, 5
        segment_set = set(segment)
        if segment_length == 5:
            if one_set.issubset(segment_set):
                three_set = segment_set
                print("three_set:",three_set)
            elif len(segment_set.difference(four_set)) == 3:
                two_set = segment_set
                print("two_set:",two_set)
            else:
                five_set = segment_set
                print("five_set:",five_set)
        # 6 length - 0, 6, 9,
        elif segment_length == 6:
            if len(segment_set.difference(four_set)) == 2:
                nine_set = segment_set
                print("nine_set:",nine_set)
            elif len(segment_set.difference(five_set)) == 1:
                six_set = segment_set
                print("six_set:",six_set)
            else:
                zero_set = segment_set
                print("zero_set:",zero_set)


    print("zero_set:",zero_set)
    print("one_set:",one_set)
    print("two_set:",two_set)
    print("three_set:",three_set)
    print("four_set:",four_set)
    print("five_set:",five_set)
    print("six_set:",six_set)
    print("seven_set:",seven_set)
    print("eight_set:",eight_set)
    print("nine_set:",nine_set)
    

    



    
    # Calculate output digits based by components
    output_total_str = ""
    for output_num in output.strip().split(" "):
        print(output_num)
        output_set = set(output_num)
        if output_set == zero_set:
            output_total_str += "0"
        elif output_set == one_set:
            output_total_str += "1"
        elif output_set == two_set:
            output_total_str += "2"
        elif output_set == three_set:
            output_total_str += "3"
        elif output_set == four_set:
            output_total_str += "4"
        elif output_set == five_set:
            output_total_str += "5"
        elif output_set == six_set:
            output_total_str += "6"
        elif output_set == seven_set:
            output_total_str += "7"
        elif output_set == eight_set:
            output_total_str += "8"
        elif output_set == nine_set:
            output_total_str += "9"
        else:
            print("ERROR!")

    print("output_total_str", output_total_str)
    all_outputs_total += int(output_total_str)

print(all_outputs_total)

# positions = list( map( int, lines[0].strip().split(",")))
