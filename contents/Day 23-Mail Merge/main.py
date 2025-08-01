with open(r"100-days-of-coding--Python-\contents\Day 23-Mail Merge\Input\Names\invited_names.txt") as names:
    names_as_list = []
    for line in names:
        for each_name in line.split():
            names_as_list.append(each_name)

            
with open(r"100-days-of-coding--Python-/contents/Day 23-Mail Merge/Input/Letters/starting_letter.txt") as letter:
    for names in names_as_list:
        with open("100-days-of-coding--Python-\contents\Day 23-Mail Merge\Input\Letters\starting_letter.txt", "r") as template_file:
            letter_template = template_file.read()
            base_dir = "100-days-of-coding--Python-/contents/Day 23-Mail Merge/Output/ReadyToSend"
            filename = f"letter_for_{names}.txt"  
            personalized_letter = letter_template.replace("[name]", names)
            with open(f"{base_dir}/{filename}", "w") as file:  # Note the "w" mode
                file.write(personalized_letter)
                