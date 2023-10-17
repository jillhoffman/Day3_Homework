import json
import random

null_densities_set = []
FA_densities_set = []
all_densities = []


with open("./densities/null_subnetwork_densities.json") as x:
   null_densities = json.load(x)
   for value in null_densities.values():
      null_densities_set.append(value)
      all_densities.append(value)


with open("./densities/FA_subnetwork_densities.json") as y:
   FA_densities = json.load(y)
   for value in FA_densities.values():
      FA_densities_set.append(value)
      all_densities.append(value)


def get_mean(densities):
   mean = sum(densities) / len(densities)
   return mean


actual_FA_mean = get_mean(FA_densities_set)
actual_null_mean = get_mean(null_densities_set)

actual_diff = abs(actual_FA_mean - actual_null_mean)

permutation_list = []

for i in range(10000):
   random.shuffle(all_densities)
   null = all_densities[:4999]
   alternative = all_densities[5000:]

   pnull_mean = get_mean(null)
   palternative_mean = get_mean(alternative)

   p_diff = abs(pnull_mean - palternative_mean)
   permutation_list.append(p_diff)


pvalue_values = [x for x in permutation_list if x >= actual_diff]
p_value = len(pvalue_values) / len(permutation_list)

print(p_value)







