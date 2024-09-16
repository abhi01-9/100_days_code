# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
# print(contents)

# Alternate way to open file so no need to close the file manually
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing to the file
# r = read , w = write (add new info and remove older info) , a = append (add the info and keep older info as well)
with open("my_file.txt", mode="a") as file: # if try to open a file that doesn't exist it will create that file from scratch and open that.
    file.write("\nNew text.")
