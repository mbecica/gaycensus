import csv
import json

splintered = {
    'Same-sex Couples':[{'p':'data/ss-couple-percent.csv'}, {'d':'data/ss-couple-total.csv'}],
    'Same-sex Spouses':[{'p':'data/ss-spouse-percent.csv'},{'d':'data/ss-spouse-total.csv'}],
    'Same-sex Unmarried':[{'p':'data/ss-unmarried-percent.csv'},{'d':'data/ss-unmarried-total.csv'}],
}
whole = {
    'inconsistent-percent':'data/inconsistent-percent.csv',
    'summary-percent':'data/summary-percent.csv',
    'summary-total':'data/summary-total.csv',
}

data = {} 
ss = {}
inconsistent = {}

source = csv.reader(open(whole['inconsistent-percent'], 'rb'), delimiter=',')
data['inconsistent-percent'] = []
for i in source:
  data['inconsistent-percent'].append(i)

#Restructure the inconsistent-percent data
for s in data['inconsistent-percent']:
  if (s[0] in inconsistent):
    print ''
  else:
    inconsistent[s[0]] = {
      'Same-sex Couples': {
        'All forms':s[1],
        'Mail':s[2],
        'NRFU':s[3]
      },
      'Same-sex Unmarried': {
        'All forms':s[4],
        'Mail':s[5],
        'NRFU':s[6]
      },
      'Same-sex Spouses': {
        'All forms':s[7],
        'Mail':s[8],
        'NRFU':s[9]
      }
    }

#Combining sources
"""
for k, v in splintered.iteritems():
  ss[k] = {}
  for l in v:
    for s in l:
      ss[k][s] = []
      source = csv.reader(open(l[s], 'rb'), delimiter=',')
      for i in source:
        ss[k][s].append(i)

for b in ss:
  for t in ss[b]:
      for s in ss[b][t]:
          state = s[0]
          if (state in data):
            if (b in data[state]):
              if (t == 'd'):
                data[state][b]['Census 2000']['total'] = s[1]
                data[state][b]['Census 2010']['total'] = s[2]
                data[state][b]['ACS 2010']['total'] = s[3]
                data[state][b]['ACS 2010']['total std err'] = s[4]
                data[state][b]['Percent Change'] = s[5]
              else:
                data[state][b]['Census 2000']['percent'] = s[1]
                data[state][b]['Census 2010']['percent'] = s[2]
                data[state][b]['ACS 2010']['percent'] = s[3]
                data[state][b]['ACS 2010']['percent std err'] = s[4]
            else:
              data[state][b] = {
                'Census 2000': {},
                'Census 2010': {},
                'ACS 2010':{},
                'Percent Change':{},
              }
              if (t == 'd'):
                data[state][b]['Census 2000']['total'] = s[1]
                data[state][b]['Census 2010']['total'] = s[2]
                data[state][b]['ACS 2010']['total'] = s[3]
                data[state][b]['ACS 2010']['total std err'] = s[4]
                data[state][b]['Percent Change'] = s[5]
              else:
                data[state][b]['Census 2000']['percent'] = s[1]
                data[state][b]['Census 2010']['percent'] = s[2]
                data[state][b]['ACS 2010']['percent'] = s[3]
                data[state][b]['ACS 2010']['percent std err'] = s[4]
          else:
            data[state] = {}
            data[state][b] = {
              'Census 2000': {},
              'Census 2010': {},
              'ACS 2010':{},
              'Percent Change':{},
            }
            if (t == 'd'):
                data[state][b]['Census 2000']['total'] = s[1]
                data[state][b]['Census 2010']['total'] = s[2]
                data[state][b]['ACS 2010']['total'] = s[3]
                data[state][b]['ACS 2010']['total std err'] = s[4]
                data[state][b]['Percent Change'] = s[5]
            else:
              data[state][b]['Census 2000']['percent'] = s[1]
              data[state][b]['Census 2010']['percent'] = s[2]
              data[state][b]['ACS 2010']['percent'] = s[3]
              data[state][b]['ACS 2010']['percent std err'] = s[4]

"""
f = open('inconsistent-percent.json', 'w')
f.write(json.dumps(inconsistent, separators = (',', ':'), sort_keys=True, indent=2) + ';')
f.close();
