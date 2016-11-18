#!/usr/bin/python2

import sys, os
import optparse
import PHPParser

PATTERNS_PATH = "patterns.txt"

# -------- MAIN --------

# Check received arguments
if __name__ == '__main__':
	op = optparse.OptionParser(
		"Usage: ./analyzer.py <filePath> [-p <pattern-file> -n <pattern-number>] [-v]")
	op.add_option('-p', '--pattern-file', default=PATTERNS_PATH, action='store', dest='pattern_file',
	              help='select patterns file to read patterns from, default is \'%default\'')
	op.add_option('-n', '--pattern-number', default='0', action='store', type='int', dest='pattern_number',
	              help='select pattern to use by number of read patterns, default is %default')
	op.add_option('-v', '--verbose', action='store_true',
	              dest='verbose', help='show parsing output')
	(options, args) = op.parse_args()

	if len(args) < 1:
		op.error("incorrect number of arguments")
	if options.verbose:
		PHPParser.VERBOSE = True

	pCollection = PHPParser.PatternCollection(options.pattern_file)
	#print "Loaded patterns:\n"
	#for pattern in pCollection.patterns:
	#print "%s\n" % pattern

	# Read slice file
	files_to_parse = args
	for f in files_to_parse:
		if os.path.exists(f) == False:
			print "\nSlice file path given (\"%s\") does not exist.\n" % f
			continue

		print "\nParsing File: %s using pattern %d:\n%s\n" % (f, options.pattern_number, pCollection.patterns[options.pattern_number])
		parser = PHPParser.PHPParser(f, pCollection.patterns[options.pattern_number])

		print "\nParse Tree:\n"
		print parser.flow_graph

		print "\nProcessed File:\n"
		print parser.get_processed_file(in_line_annotations=True)
