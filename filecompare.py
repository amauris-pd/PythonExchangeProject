def read_file(filename):
    with open(filename) as file:
        content = file.read()
    splitted_content = content.split("\n")
    return splitted_content


def get_difference(list1, list2, list1_name, list2_name):
    for question in list1:
        if question not in list2:
            print(f"This question is in {list1_name} but not in {list2_name}: {question}")


# Open the first file
survey1 = read_file("first_file.txt")

# Open the second file
survey2 = read_file("second_file.txt")

get_difference(survey1, survey2, "Survey 1", "Survey 2")
get_difference(survey2, survey1, "Survey 2", "Survey 1")
