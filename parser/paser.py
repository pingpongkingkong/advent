import pandas as pd
import json

b = json.loads(open('advent.txt').read())

t = []
for member_id in b['members']:
    md = b['members'][member_id]
    name = md.get('name', 'User %s' % member_id)
    for cdl_id in md['completion_day_level']:
            cdl =  md['completion_day_level'][cdl_id]
            star_one = cdl.get('1', {'get_star_ts':0})['get_star_ts']
            star_two = cdl.get('2', {'get_star_ts':0})['get_star_ts']
            t.append( (member_id, name, cdl_id, star_one, star_two) )            

df = pd.DataFrame(t)
df.columns = ['member_id', 'name', 'day', 'star_one', 'star_two']

df['star_one'] = df.star_one.apply(pd.to_datetime)
df['star_two'] = df.star_two.apply(pd.to_datetime)

df['diff'] = df.star_two - df.star_one

df['diff_sec'] = df['diff'].dt.total_seconds().astype(int)
