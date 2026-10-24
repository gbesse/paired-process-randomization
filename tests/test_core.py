import unittest
from paired_process_randomization import run
class Tests(unittest.TestCase):
 def pairs(self):return [{'id':str(i),'baseline':0,'candidate':1}for i in range(3)]
 def test_known_exact_three_pair_tail(self):
  r=run({'pairs':self.pairs(),'alternative':'greater'});self.assertEqual(r['exact_p_value'],1/8);self.assertEqual(r['total_sign_assignments'],8)
 def test_two_sided_and_swap_symmetry(self):
  d={'pairs':self.pairs()};self.assertEqual(run(d)['exact_p_value'],.25);d['pairs']=[{**r,'candidate':-1}for r in d['pairs']];self.assertEqual(run(d)['exact_p_value'],.25)
 def test_zero_differences_keep_probability_mass(self):
  r=run({'pairs':[{'id':str(i),'baseline':7,'candidate':7}for i in range(5)]});self.assertEqual(r['exact_p_value'],1);self.assertEqual(r['extreme_assignments'],32)
 def test_direction_is_explicit(self):self.assertEqual(run({'pairs':self.pairs(),'alternative':'less'})['exact_p_value'],1)
 def test_duplicate_pairs_rejected(self):
  with self.assertRaises(ValueError):run({'pairs':[self.pairs()[0],self.pairs()[0]]})
