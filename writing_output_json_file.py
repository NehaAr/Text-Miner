def solution_dump(solution_file_path):
  solution_data = []
  #print(input_data1)
  for input_sentence in input_data1:
    print(input_sentence)
    solution_sid = int(input_sentence['sid'])
    print(solution_sid)
    solution_tokens = solution(input_sentence['output_tokens'])
    solution_data.append({'sid':solution_sid,
                          'output_tokens':solution_tokens})
