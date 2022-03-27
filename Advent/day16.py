# day16.py

with open('day16real.txt') as ipf:
    lines = ipf.readlines()

test_string  = "38006F45291200" # 0-type
test_string0 = "D2FE28" # decimal 2021
test_string1 = "EE00D40C823060" # ID 1
test_string2 = "8A004A801A8002F478"
test_string3 = "620080001611562C8802118E34"
test_string4 = "C0015000016115A2E0802F182340"
test_string5 = "A0016C880162017C3686B18A3D4780"

curr_input = test_string2

binary_rep = str(bin(int(curr_input, 16))[2:].zfill(8))

print(binary_rep)

bin_array = [int(c) for c in binary_rep]

print(bin_array)

def parse_packet(arr):
    version = 4*arr[0] + 2*arr[1] + arr[2]
    packID = 4*arr[3] + 2*arr[4] + arr[5]
    if packID == 4:
        # it's a literal value. Parse accordingly. 
        literals = arr[6:]
        bins = []

        segment_first = literals.pop(0)
        while segment_first == 1:
            for i in range(4):
                bins.append(str(literals.pop(0)))
            segment_first = literals.pop(0)
        for i in range(4):
            bins.append(str(literals.pop(0)))
        
        
        bin_string = "".join(bins)
        out_int = int(bin_string, 2)
        # return [out_int, literals]
        return [version, literals]
    
    length_type = arr[6]
    if length_type == 0:
        # 15-bit total length of sub-packets. 
        rest_array = arr[7:]
        sub_length_bin = []

        for i in range(15):
            sub_length_bin.append(str(rest_array.pop(0)))
        bin_string = "".join(sub_length_bin)
        sub_length = int(bin_string, 2)

        data_arr = rest_array[:sub_length]

        while not data_arr == []:
            [version, rest] = parse_packet(data_arr)
            print("version", version)
            data_arr = rest

        return [version, rest_array[sub_length:]]

    else:
        # 11-bit number of sub-packets contained. 
        rest_array = arr[7:]
        sub_length_bin = []

        for i in range(11):
            sub_length_bin.append(str(rest_array.pop(0)))
        bin_string = "".join(sub_length_bin)
        num_subs = int(bin_string, 2)

        for i in range(num_subs):
            [new_version, unparsed] = parse_packet(rest_array)
            print("version", new_version)
            rest_array = unparsed
        return [version, rest_array]

# print(parse_packet(bin_array))

def get_packet_versions(arr):
    # Returns list containing: 
    # [unparsed, versions, ....]
    # versions are in any order. 
    version = 4*arr[0] + 2*arr[1] + arr[2]
    packID = 4*arr[3] + 2*arr[4] + arr[5]

    print("packet with version =", version, "packID =", packID)
    if packID == 4:
        # it's a literal value. Parse accordingly. 
        print("type is literal")
        literals = arr[6:]

        is_last_segment = False
        while(not is_last_segment):
            is_last_segment = (literals.pop(0) == 0)
            literals = literals[4:]
        literals = literals[4:]

        # return [out_int, literals]
        return [literals, version]
    
    length_type = arr[6]
    if length_type == 0:
        # 15-bit total length of sub-packets. 
        print("type is 15-bit len")
        rest_array = arr[7:]
        sub_length_bin = [str(x) for x in rest_array[:15]]
        bin_string = "".join(sub_length_bin)
        sub_length = int(bin_string, 2)

        data_arr = rest_array[15:sub_length + 15]

        version_nums = []

        while not data_arr == []:
            results = get_packet_versions(data_arr)
            print("results 15", results)
            rest = results[0]
            version_nums = version_nums + results[1:]
            data_arr = rest

        return [rest_array[sub_length + 15:], version] + version_nums

    else:
        # 11-bit number of sub-packets contained. 
        
        rest_array = arr[7:]
        sub_length_bin = [str(x) for x in rest_array[:11]]
        bin_string = "".join(sub_length_bin)
        num_subs = int(bin_string, 2)

        print("type is 11-bit num with", num_subs, "subpackets")

        list_versions = []

        for i in range(num_subs):
            results = get_packet_versions(rest_array)
            rest_array = results[0]
            print("results 11", results)
            list_versions = list_versions + results[1:]
        return [rest_array, version] + list_versions

print(get_packet_versions(bin_array))

print(binary_rep)
print("VVVTTTILLLLLLLLLLL")