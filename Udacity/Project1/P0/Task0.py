"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def get_time_from_date_time(text_date_time):
    _, time = text_date_time.split(' ')
    return time

def get_data_from_item(text , is_call=False):
    incoming_number = text[0]
    answering_nuber = text[1]
    text_date_time = text[2]
    time = get_time_from_date_time(text_date_time)
    if is_call:
        duration = text[3]
        return incoming_number, answering_nuber, time, duration
    else:  # is text
        return incoming_number, answering_nuber, time


first_text_content, last_call = texts[0],  calls[-1]

inc_num_txt, ans_num_txt, time_txt = get_data_from_item(first_text_content)

print(f'First record of texts, {inc_num_txt} texts {ans_num_txt} at time {time_txt}' )

inc_num_call, ans_num_call, time_call, drtn_call = get_data_from_item(last_call, True)
print(f'Last record of calls, {inc_num_call} calls {ans_num_call} at time {time_call}, lasting {drtn_call} seconds')