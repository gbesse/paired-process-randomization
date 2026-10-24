import itertools,math
from .common import number,unique_ids

def run(data):
 pairs=data['pairs'];unique_ids(pairs)
 if not 1<=len(pairs)<=16:raise ValueError('pair_count')
 diffs=[number(r['candidate'],-1e12,1e12)-number(r['baseline'],-1e12,1e12)for r in pairs];n=len(diffs);observed=math.fsum(diffs)/n;alternative=data.get('alternative','two_sided')
 if alternative not in ('two_sided','greater','less'):raise ValueError('alternative')
 tolerance=1e-12*max(1,max(abs(x)for x in diffs));extreme=0
 for signs in itertools.product((-1,1),repeat=n):
  value=math.fsum(s*x for s,x in zip(signs,diffs))/n
  extreme+=abs(value)>=abs(observed)-tolerance if alternative=='two_sided' else value>=observed-tolerance if alternative=='greater' else value<=observed+tolerance
 return {'mean_candidate_minus_baseline':observed,'exact_p_value':extreme/(2**n),'extreme_assignments':extreme,'total_sign_assignments':2**n,'alternative':alternative,'tie_tolerance':tolerance,'null_model':'independent_exchangeable_signs_within_prespecified_pairs','causality_proven':False}
