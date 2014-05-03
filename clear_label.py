in_file = open('data_twitter_tokenized.txt', 'r')
in_lines = in_file.readlines()
out_lines = []
for in_line in in_lines:
    out_lines.append(' '.join(in_line.split()[1:]) + ' . @@@@@.\r\n')
in_file.close()
out_file = open('twitter_no_label.txt', 'w')
out_file.writelines(out_lines)
out_file.close()

