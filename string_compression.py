def string_compression():
    d_str = input("Enter the string character: ")
    count_str = 1  # set count as 0
    new_str = ""  # initialise new blank string
    for i in range(len(d_str)-1):
        if(d_str[i] == d_str[i+1]):
            count_str += 1
        else:
            if(count_str > 1):
                new_str = new_str + str(count_str) + d_str[i]
            else:
                new_str += d_str[i]
            count_str = 1
    # print the last character
    if(count_str > 1):
        new_str += str(count_str)
        new_str += d_str[-1]
    else:
        new_str += d_str[-1]
    print(new_str.upper())


if __name__ == "__main__":
    string_compression()
