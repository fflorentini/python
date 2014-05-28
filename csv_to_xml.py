import csv
import sys

if len(sys.argv) == 1:
  sys.exit("usage: python csv_to_xml.py <path to csv file>");
csv_file = sys.argv[1]

csv.register_dialect('custom',
                     delimiter=',',
                     doublequote=True,
                     escapechar=None,
                     quotechar='"',
                    quoting=csv.QUOTE_MINIMAL,
                    skipinitialspace=False)

with open(csv_file) as ifile:
   data = csv.reader(ifile, dialect='custom')
   print "<document>"
   for record in data:
       print "   <record>"
       for i, field in enumerate(record):
           print "      <field%s>" % i + field + "</field%s>" % i
       print "   <record>"
   print "</document>"
