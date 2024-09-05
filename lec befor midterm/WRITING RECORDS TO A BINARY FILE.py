import struct

#define a record as a tuple
record = (1, "John Doe", 20, 3.75)

#open a binary file for writing
with open("record.bid","wb") as file:

    #pack the record into binary format
    data = struct.pack("i20sid", record[0], record[1].encode(),record[2], record[3])

    #Write the packed data to the file
    file.write(data)