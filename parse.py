import argparse
parser = argparse.ArgumentParser(description='String for parsing')
parser.add_argument('-s','--st',help='string', required=True)
args = parser.parse_args( )
for item in args.st.split("|"):
	for final in item.split(" "):
		if "vivek-lambda-test" in final:
			print ("Final output")
			print(final)
