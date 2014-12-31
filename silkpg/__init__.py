from multicorn import ForeignDataWrapper,utils
import logging
import operator
import datetime
import silk
import sys


class SilkDataWrapper(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(SilkDataWrapper, self).__init__(options, columns)
        self.columns = columns
	self.debug = options.get('debug',False)
	silk.site.init_site(siteconf=options['siteconf'], rootdir=options['rootdir'])

    def execute(self, quals, columns):
	# Dict of postgres operators to python functions
	operators={'=': 'eq', '<':'lt', '>':'gt', '<=': 'le', '>=': 'ge', '!=': 'ne', '<<=': 'within', '>>=': 'contains'}
	# Define our own reversed "contains"
	operator.within=lambda a,b: a in b

	stime=datetime.datetime(2000,1,1)
	etime=datetime.datetime(2032,1,1)
        sensor=None

	if self.debug:
		utils.log_to_postgres((quals),logging.INFO)

	# Time bound the query for restricting files from repository
	for qual in quals:
		if qual.field_name == 'stime' and qual.operator in ['>','>='] and qual.value > stime:
			stime=qual.value
		elif qual.field_name == 'etime' and qual.operator in ['<','<='] and qual.value < etime:
			etime=qual.value
		elif qual.field_name == 'sensor' and qual.operator == '=':
			sensor=qual.value
 
	if self.debug:
		utils.log_to_postgres("Searching for data between %s and %s" % (stime,etime),logging.INFO)

	for file in silk.site.repository_silkfile_iter(start=stime, end=etime, sensors=sensor):
		# Examine each record in the file
		for rec in file:
 			# Check each qualifier (AND)
			for qual in quals:
				# If qualifier is an IP convert to silk Wildcard IP
				if qual.field_name in ['nhip','sip','dip']:
					value=silk.IPWildcard(qual.value)
				else:
					value=qual.value
	
			        if not getattr(operator,operators[qual.operator])(getattr(rec,qual.field_name), value):
					break
			else: 
				# All qualifiers matched
				# Return the data
				line={}	
				for column_name in self.columns:
		       			line[column_name] = '%s' % (getattr(rec,column_name))
            			yield line
