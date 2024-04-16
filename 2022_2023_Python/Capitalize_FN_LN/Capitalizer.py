#functions with output

def format_name(f_name, l_name):
  """Take a first and last name and format it to return the title case version of the name AKA capitalize each word."""
  if f_name == "" or l_name == "":
    return "Invalid input. Program terminated."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?: "), input("What is your lastname?: ")))
#.title() = to capitalized each word in a sentence or a word.

